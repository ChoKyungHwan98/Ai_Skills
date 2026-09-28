"""Meaningful deployment invariants; no design-quality claims."""
import io
import json
import py_compile
import subprocess
import sys
import tarfile
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from check_skills import validate
from manage_skills import RECEIPT, extract_snapshot, hashes, install, rollback


class ManagementTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="skill-management-test-")
        self.root = Path(self.temp.name)
        self.repo = self.root / "repo"
        self.repo.mkdir()
        self.name = "example-skill"
        self.skill = self.repo / "skills" / self.name
        (self.skill / "references").mkdir(parents=True)
        (self.skill / "evals").mkdir()
        self.dest = self.root / "installed"
        self.backups = self.root / "backups"
        self.git("init")
        self.git("config", "user.name", "Skill management test")
        self.git("config", "user.email", "test@example.invalid")
        self.write_version("1.0.0")
        self.commit()

    def tearDown(self):
        self.temp.cleanup()

    def git(self, *args):
        result = subprocess.run(["git", "-C", str(self.repo), *args], capture_output=True)
        if result.returncode:
            raise AssertionError(result.stderr.decode(errors="replace"))
        return result.stdout.decode().strip()

    def write_version(self, version, channel="stable"):
        (self.skill / "SKILL.md").write_text(
            f'---\nname: {self.name}\ndescription: Exercise deployment invariants.\nmetadata:\n  version: "{version}"\n---\n[Details](references/details.md)\n', encoding="utf-8")
        (self.skill / "references/details.md").write_text("Details " + version, encoding="utf-8")
        (self.skill / "evals/evals.json").write_text(json.dumps({"skill_name": self.name, "evals": [
            {"id": 1, "name": "case", "prompt": "A realistic request", "expected_behavior": ["An observable invariant"]}]}), encoding="utf-8")
        (self.repo / "releases.json").write_text(json.dumps({"schema_version": 1,
            "repository": "https://github.com/ChoKyungHwan98/Ai_Skills", "skills": {self.name: {
                "path": f"skills/{self.name}", "version": version, "channel": channel}}}), encoding="utf-8")

    def commit(self):
        self.git("add", ".")
        self.git("commit", "-m", "Fixture version")
        return self.git("rev-parse", "HEAD")

    def sync(self, **options):
        return install(self.repo, "HEAD", self.name, self.dest, self.backups, **options)

    def test_committed_snapshot_not_dirty_checkout(self):
        sha = self.git("rev-parse", "HEAD")
        self.write_version("2.0.0")
        result = self.sync()
        self.assertEqual(result["commit"], sha)
        self.assertEqual(result["version"], "1.0.0")
        self.assertEqual((self.dest / self.name / "references/details.md").read_text(), "Details 1.0.0")

    def test_adoption_requires_opt_in_and_backups_every_file(self):
        current = self.dest / self.name
        current.mkdir(parents=True)
        (current / "custom.txt").write_text("Keep this local note")
        with self.assertRaisesRegex(ValueError, "Unmanaged"):
            self.sync()
        result = self.sync(adopt=True)
        self.assertEqual((Path(result["backup"]) / "payload/custom.txt").read_text(), "Keep this local note")

    def test_modified_added_and_deleted_files_cannot_be_overwritten(self):
        self.sync()
        current = self.dest / self.name
        detail = current / "references/details.md"
        original = detail.read_bytes()
        detail.write_text("A local edit")
        with self.assertRaisesRegex(ValueError, "Local installation edits"):
            self.sync(adopt=True)
        detail.write_bytes(original)
        added = current / "extra.txt"
        added.write_text("New local content")
        with self.assertRaisesRegex(ValueError, "Local installation edits"):
            self.sync()
        added.unlink()
        detail.unlink()
        with self.assertRaisesRegex(ValueError, "Local installation edits"):
            self.sync()

    def test_generated_bytecode_allows_sync_and_survives_backup(self):
        helper = self.skill / "scripts/helper.py"
        helper.parent.mkdir()
        helper.write_text("answer = 42\n", encoding="utf-8")
        self.commit()
        self.sync()
        current = self.dest / self.name
        cache = Path(py_compile.compile(str(current / "scripts/helper.py"), doraise=True))
        cache_key = cache.relative_to(current).as_posix()
        self.assertTrue(cache.exists())
        self.assertNotIn(cache_key, hashes(current))
        self.assertIn(cache_key, hashes(current, ignore_receipt=False))
        self.assertEqual(self.sync()["status"], "up_to_date")

        note = cache.parent / "local-note.txt"
        note.write_text("Keep this user file", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Local installation edits"):
            self.sync()
        note.unlink()

        before = hashes(current, ignore_receipt=False)
        self.write_version("1.1.0")
        self.commit()
        updated = self.sync()
        payload = Path(updated["backup"]) / "payload"
        self.assertEqual(hashes(payload, ignore_receipt=False), before)
        rollback(Path(updated["backup"]), self.backups)
        self.assertEqual(hashes(current, ignore_receipt=False), before)

    def test_update_and_rollback_preserve_complete_versions(self):
        self.sync()
        first = hashes(self.dest / self.name, ignore_receipt=False)
        self.write_version("1.1.0")
        self.commit()
        updated = self.sync()
        second = hashes(self.dest / self.name, ignore_receipt=False)
        result = rollback(Path(updated["backup"]), self.backups)
        self.assertEqual(hashes(self.dest / self.name, ignore_receipt=False), first)
        self.assertEqual(hashes(Path(result["backup"]) / "payload", ignore_receipt=False), second)

    def test_corrupt_backup_and_modified_current_block_rollback(self):
        self.sync()
        self.write_version("1.1.0")
        self.commit()
        bundle = Path(self.sync()["backup"])
        old = bundle / "payload/references/details.md"
        saved = old.read_bytes()
        old.write_text("Corrupt backup")
        with self.assertRaisesRegex(ValueError, "Backup has changed"):
            rollback(bundle, self.backups)
        old.write_bytes(saved)
        (self.dest / self.name / "references/details.md").write_text("Local changes")
        with self.assertRaisesRegex(ValueError, "Local installation edits"):
            rollback(bundle, self.backups)

    def test_candidate_needs_explicit_trial(self):
        self.write_version("1.1.0", channel="candidate")
        self.commit()
        with self.assertRaisesRegex(ValueError, "Candidate release"):
            self.sync()
        self.assertFalse((self.dest / self.name).exists())
        self.assertEqual(self.sync(allow_candidate=True)["channel"], "candidate")

    def test_failed_swap_restores_original_installation(self):
        self.sync()
        before = hashes(self.dest / self.name, ignore_receipt=False)
        self.write_version("1.1.0")
        self.commit()
        with patch.object(Path, "rename", side_effect=OSError("Simulated staging swap failure")):
            with self.assertRaisesRegex(OSError, "swap failure"):
                self.sync()
        self.assertEqual(hashes(self.dest / self.name, ignore_receipt=False), before)

    def test_idempotent_update_does_not_create_backup(self):
        self.sync()
        self.assertEqual(self.sync()["status"], "up_to_date")
        self.assertFalse(self.backups.exists())

    def test_broken_reference_blocks_install_before_mutation(self):
        self.sync()
        before = hashes(self.dest / self.name, ignore_receipt=False)
        (self.skill / "references/details.md").unlink()
        self.commit()
        with self.assertRaisesRegex(ValueError, "Broken reference"):
            self.sync()
        self.assertEqual(hashes(self.dest / self.name, ignore_receipt=False), before)

    def test_version_mismatch_is_detected(self):
        self.write_version("1.1.0")
        manifest = json.loads((self.repo / "releases.json").read_text())
        manifest["skills"][self.name]["version"] = "9.9.9"
        (self.repo / "releases.json").write_text(json.dumps(manifest))
        with self.assertRaisesRegex(ValueError, "Version/name mismatch"):
            validate(self.repo)

    def test_archive_traversal_and_links_are_rejected(self):
        for kind in ("traversal", "symlink"):
            archive = io.BytesIO()
            with tarfile.open(fileobj=archive, mode="w") as tar:
                item = tarfile.TarInfo("../escape.txt" if kind == "traversal" else "link")
                if kind == "symlink":
                    item.type = tarfile.SYMTYPE
                    item.linkname = "../escape.txt"
                else:
                    item.size = 1
                tar.addfile(item, io.BytesIO(b"x") if kind == "traversal" else None)
            with patch("manage_skills.git", side_effect=[b"a" * 40, archive.getvalue()]):
                with self.assertRaises(ValueError):
                    extract_snapshot(self.repo, "HEAD", self.root / "extract")
            self.assertFalse((self.root / "escape.txt").exists())


if __name__ == "__main__":
    unittest.main()
