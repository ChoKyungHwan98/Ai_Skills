"""Repository packaging checks. These do not grade visual or behavioral quality."""
import json
import re
import struct
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def within(path, parent):
    path = path.resolve()
    if not path.is_relative_to(parent.resolve()) or path == parent.resolve():
        raise ValueError(f"Path must be inside {parent}: {path}")
    return path


def skill_metadata(folder):
    content = (folder / "SKILL.md").read_text(encoding="utf-8-sig")
    front = re.match(r"^---\r?\n(.*?)\r?\n---(?:\r?\n|$)", content, re.S)
    if not front:
        raise ValueError(f"Missing frontmatter: {folder}")
    name = re.search(r"^name:\s*([a-z0-9-]+)\s*$", front[1], re.M)
    description = re.search(r"^description:\s*\S.+$", front[1], re.M)
    version = re.search(r'^\s+version:\s*[\"\']?(\d+\.\d+\.\d+)[\"\']?\s*$', front[1], re.M)
    if not name or not description or not version or name[1] != folder.name or len(name[1]) > 64:
        raise ValueError(f"Invalid name, description, or metadata.version: {folder}")
    return {"name": name[1], "version": version[1]}


def image_size(path):
    data = path.read_bytes()
    if data[:8] == b"\x89PNG\r\n\x1a\n" and path.suffix.lower() == ".png":
        return list(struct.unpack(">II", data[16:24]))
    if data[:2] == b"\xff\xd8" and path.suffix.lower() in {".jpg", ".jpeg"}:
        pos = 2
        while pos < len(data):
            if data[pos] != 0xFF:
                raise ValueError(f"Invalid JPEG marker: {path}")
            while pos < len(data) and data[pos] == 0xFF:
                pos += 1
            marker = data[pos]
            pos += 1
            length = int.from_bytes(data[pos:pos + 2], "big")
            if marker in {0xC0, 0xC1, 0xC2}:
                height, width = struct.unpack(">HH", data[pos + 3:pos + 7])
                return [width, height]
            if length < 2:
                break
            pos += length
    raise ValueError(f"Unsupported/mislabeled capture: {path}")


def validate(root):
    manifest = json.loads((root / "releases.json").read_text(encoding="utf-8"))
    if manifest.get("schema_version") != 1 or manifest.get("repository") != "https://github.com/ChoKyungHwan98/Ai_Skills":
        raise ValueError("Unsupported release manifest")
    if not manifest.get("skills"):
        raise ValueError("No skills in release manifest")
    for name, release in manifest["skills"].items():
        folder = within(root / release["path"], root / "skills")
        metadata = skill_metadata(folder)
        if metadata != {"name": name, "version": release["version"]}:
            raise ValueError(f"Version/name mismatch: {name}")
        if release["channel"] not in {"stable", "candidate"}:
            raise ValueError(f"Invalid release channel: {name}")
        for md in folder.rglob("*.md"):
            for href in re.findall(r"\[[^\]]*\]\(([^)]+)\)", md.read_text(encoding="utf-8-sig")):
                if re.match(r"^[a-zA-Z]+:", href) or href.startswith("#"):
                    continue
                target = within(md.parent / href.split("#")[0], folder)
                if not target.exists():
                    raise ValueError(f"Broken reference in {md}: {href}")
        cases = json.loads((folder / "evals/evals.json").read_text(encoding="utf-8"))
        if cases["skill_name"] != name or not cases["evals"]:
            raise ValueError(f"Invalid eval list: {name}")
        ids, names = set(), set()
        for case in cases["evals"]:
            if case["id"] in ids or case["name"] in names or not case["prompt"] or not case["expected_behavior"]:
                raise ValueError(f"Invalid/duplicate eval: {case}")
            ids.add(case["id"])
            names.add(case["name"])
    for case_file in (root / "evals/cases").glob("*/case.json"):
        case = json.loads(case_file.read_text(encoding="utf-8"))
        if case.get("evaluation_status") not in {"reference_only", "not_evaluated", "evaluated"}:
            raise ValueError(f"Missing evaluation status: {case_file}")
        for capture in case["captures"]:
            image = within(case_file.parent / capture["file"], case_file.parent)
            if image_size(image) != capture["image_size"]:
                raise ValueError(f"Wrong image dimensions: {image}")
            if not capture.get("provenance"):
                raise ValueError(f"Missing capture provenance: {image}")
    return manifest


if __name__ == "__main__":
    try:
        result = validate(ROOT)
        for name, item in result["skills"].items():
            print(f"PASS packaging: {name} {item['version']} ({item['channel']})")
        print("Behavioral and visual verdicts: NOT assessed by this command.")
    except (ValueError, OSError, KeyError) as exc:
        raise SystemExit(f"FAIL: {exc}")
