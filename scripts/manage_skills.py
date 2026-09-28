"""Install committed skill snapshots with provenance, local-edit protection and rollback."""
import argparse
import hashlib
import io
import json
import os
import shutil
import subprocess
import tarfile
import tempfile
import uuid
from datetime import datetime, timezone
from pathlib import Path

from check_skills import validate, within

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://github.com/ChoKyungHwan98/Ai_Skills"
RECEIPT = ".codex-skill-install.json"
DEFAULT_SKILL = "game-tool-visual-director"


def git(repo, *args):
    result = subprocess.run(["git", "-C", str(repo), *args], capture_output=True)
    if result.returncode:
        # Do not echo remote URL/credential-bearing stderr from Git.
        raise ValueError(f"Git operation failed ({args[0]}). Check repository/ref and Git authentication.")
    return result.stdout


def hashes(folder, ignore_receipt=True):
    found = {}
    if folder.is_symlink() or (hasattr(folder, "is_junction") and folder.is_junction()):
        raise ValueError(f"Linked installation/backup is not supported: {folder}")
    for path in sorted(folder.rglob("*")):
        if path.is_symlink() or (hasattr(path, "is_junction") and path.is_junction()):
            raise ValueError(f"Linked file is not supported: {path}")
        if path.is_file():
            key = path.relative_to(folder).as_posix()
            if ignore_receipt and key == RECEIPT:
                continue
            found[key] = hashlib.sha256(path.read_bytes()).hexdigest()
    return found


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path, value):
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def installation_receipt(folder):
    path = folder / RECEIPT
    if not path.exists():
        return None
    receipt = read_json(path)
    if receipt.get("repository") != SOURCE or receipt.get("skill") != folder.name:
        raise ValueError("Installation receipt belongs to another repository or skill")
    return receipt


def ensure_unmodified(folder, adopt=False):
    if not folder.exists():
        return
    if not folder.is_dir():
        raise ValueError(f"Destination is not a directory: {folder}")
    actual = hashes(folder)
    receipt = installation_receipt(folder)
    if receipt is None:
        if not adopt:
            raise ValueError("Unmanaged installation: use --adopt once to back up and transition it.")
        return
    expected = receipt["files"]
    changed = [name for name in sorted(actual.keys() | expected.keys()) if actual.get(name) != expected.get(name)]
    if changed:
        raise ValueError("Local installation edits detected; preserve/port them before syncing: " + ", ".join(changed))


def extract_snapshot(repo, ref, target):
    commit = git(repo, "rev-parse", "--verify", ref + "^{commit}").decode().strip()
    archive = git(repo, "archive", "--format=tar", commit)
    with tarfile.open(fileobj=io.BytesIO(archive)) as tar:
        for member in tar.getmembers():
            path = within(target / member.name, target)
            if member.isdir():
                path.mkdir(parents=True, exist_ok=True)
            elif member.isfile():
                path.parent.mkdir(parents=True, exist_ok=True)
                with tar.extractfile(member) as stream, path.open("wb") as output:
                    shutil.copyfileobj(stream, output)
            else:
                raise ValueError("Archive links or special files are not supported")
    return commit


def replace_installation(stage, destination, backup_root):
    # Resolve and verify all recursive cleanup/move targets within explicit roots.
    destination = within(destination, destination.parent)
    stage = within(stage, destination.parent)
    if not stage.name.startswith(".skill-stage-") or stage.is_symlink():
        raise ValueError("Unexpected staging directory")
    backup_root = backup_root.resolve()
    if destination.is_relative_to(backup_root) or backup_root.is_relative_to(destination):
        raise ValueError("Backup and installation directories must be separate")
    bundle = None
    if destination.exists():
        original_hashes = hashes(destination, ignore_receipt=False)
        timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
        bundle = within(backup_root / destination.name / (timestamp + "-" + uuid.uuid4().hex[:6]), backup_root)
        bundle.mkdir(parents=True)
        payload = within(bundle / "payload", bundle)
        write_json(bundle / "receipt.json", {"skill": destination.name, "destination": str(destination), "files": original_hashes})
        shutil.move(str(destination), str(payload))
    try:
        stage.rename(destination)
    except Exception:
        if bundle and not destination.exists():
            shutil.move(str(within(bundle / "payload", bundle)), str(destination))
        raise
    return bundle


def install(repo, ref, skill, dest_parent, backup_root, *, allow_candidate=False, adopt=False):
    if not skill or any(c not in "abcdefghijklmnopqrstuvwxyz0123456789-" for c in skill):
        raise ValueError("Invalid skill name")
    destination = dest_parent.resolve() / skill
    # Reject a linked destination before resolving it through within().
    hashes(destination) if destination.exists() else None
    ensure_unmodified(destination, adopt=adopt)
    original = hashes(destination, ignore_receipt=False) if destination.exists() else None
    with tempfile.TemporaryDirectory(prefix="skill-snapshot-") as temporary:
        snapshot = Path(temporary)
        commit = extract_snapshot(repo, ref, snapshot)
        manifest = validate(snapshot)
        release = manifest["skills"][skill]
        if release["channel"] != "stable" and not allow_candidate:
            raise ValueError("Candidate release; use --allow-candidate explicitly to trial it.")
        source = within(snapshot / release["path"], snapshot / "skills")
        hashes(source)
        current = installation_receipt(destination) if destination.exists() else None
        content_hashes = hashes(source)
        if current and current["commit"] == commit and current["files"] == content_hashes:
            return {"status": "up_to_date", "destination": str(destination), "commit": commit, "version": release["version"]}
        destination.parent.mkdir(parents=True, exist_ok=True)
        stage = Path(tempfile.mkdtemp(prefix=".skill-stage-", dir=destination.parent))
        try:
            shutil.copytree(source, stage, dirs_exist_ok=True)
            receipt = {"schema_version": 1, "repository": SOURCE, "skill": skill,
                       "version": release["version"], "channel": release["channel"], "commit": commit,
                       "installed_at": datetime.now(timezone.utc).isoformat(), "files": content_hashes}
            write_json(stage / RECEIPT, receipt)
            # Recheck after staging to protect edits made during validation/extraction.
            ensure_unmodified(destination, adopt=adopt)
            if (hashes(destination, ignore_receipt=False) if destination.exists() else None) != original:
                raise ValueError("Installation changed during staging; sync refused")
            bundle = replace_installation(stage, destination, backup_root)
        finally:
            if stage.exists():
                shutil.rmtree(within(stage, destination.parent))
    return {"status": "installed", "version": release["version"], "channel": release["channel"],
            "commit": commit, "destination": str(destination), "backup": str(bundle) if bundle else None}


def rollback(bundle, backup_root):
    backup_root = backup_root.resolve()
    bundle = within(bundle, backup_root)
    record = read_json(bundle / "receipt.json")
    payload = within(bundle / "payload", bundle)
    if hashes(payload, ignore_receipt=False) != record["files"]:
        raise ValueError("Backup has changed; rollback refused")
    destination = Path(record["destination"])
    if not destination.is_absolute() or destination.name != record["skill"]:
        raise ValueError("Invalid backup destination")
    if not destination.exists():
        raise ValueError("Current installation missing; inspect before restoring")
    ensure_unmodified(destination)
    stage = Path(tempfile.mkdtemp(prefix=".skill-stage-", dir=destination.parent))
    try:
        shutil.copytree(payload, stage, dirs_exist_ok=True)
        ensure_unmodified(destination)
        new_backup = replace_installation(stage, destination, backup_root)
    finally:
        if stage.exists():
            shutil.rmtree(within(stage, destination.parent))
    return {"status": "restored", "destination": str(destination), "backup": str(new_backup)}


def default_destination(skill):
    codex = Path(os.environ.get("CODEX_HOME", str(Path.home() / ".codex"))) / "skills"
    agents = Path.home() / ".agents/skills"
    if (codex / skill).exists() and (agents / skill).exists():
        raise ValueError("Duplicate installations; choose --dest and resolve the duplicate")
    return codex if (codex / skill).exists() else agents


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["status", "sync", "rollback"])
    parser.add_argument("--skill", default=DEFAULT_SKILL)
    parser.add_argument("--ref", default="origin/main")
    parser.add_argument("--dest", type=Path, help="Parent directory containing installed skills")
    parser.add_argument("--backup-root", type=Path, default=Path.home() / ".codex/skill-backups")
    parser.add_argument("--backup", type=Path)
    parser.add_argument("--fetch", action="store_true")
    parser.add_argument("--adopt", action="store_true")
    parser.add_argument("--allow-candidate", action="store_true")
    args = parser.parse_args()
    if args.command == "rollback":
        if not args.backup:
            parser.error("rollback requires --backup")
        result = rollback(args.backup, args.backup_root)
    else:
        parent = args.dest or default_destination(args.skill)
        destination = parent.resolve() / args.skill
        if args.command == "status":
            if not destination.exists():
                result = {"status": "not_installed", "destination": str(destination)}
            else:
                hashes(destination)
                receipt = installation_receipt(destination)
                if receipt:
                    ensure_unmodified(destination)
                    result = {"status": "managed_clean", "destination": str(destination),
                              "version": receipt["version"], "channel": receipt["channel"], "commit": receipt["commit"]}
                else:
                    result = {"status": "unmanaged", "destination": str(destination)}
        else:
            if args.fetch:
                remote = git(ROOT, "remote", "get-url", "origin").decode().strip().rstrip("/")
                if remote not in {SOURCE, SOURCE + ".git", "git@github.com:ChoKyungHwan98/Ai_Skills.git"}:
                    raise ValueError("Origin is not the canonical Ai_Skills repository")
                git(ROOT, "fetch", "origin", "refs/heads/main:refs/remotes/origin/main")
            result = install(ROOT, args.ref, args.skill, parent, args.backup_root,
                             allow_candidate=args.allow_candidate, adopt=args.adopt)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, KeyError) as exc:
        raise SystemExit(f"Stopped: {exc}")
