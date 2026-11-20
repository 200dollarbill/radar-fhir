"""Validate the hand-authored views in docs/reference/{claude,human}."""
import re
import sys
from pathlib import Path

MAX_LINES = 400
_SOURCE_LINE = re.compile(r"^- (raw/[^\s]+\.md)\s*$")
_CLAUDE_EXEMPT = {"INDEX.md", "VALIDITY-REVIEW.md"}


def _sources_of(text: str) -> list[str] | None:
    if "## Sources" not in text:
        return None
    tail = text.split("## Sources", 1)[1]
    return [m.group(1) for m in (_SOURCE_LINE.match(l) for l in tail.splitlines()) if m]


def _mentioned(name: str, text: str) -> bool:
    """Check if name is mentioned in text with word boundaries (not just substring)."""
    return re.search(r"(?<![\w.-])" + re.escape(name) + r"(?![\w.-])", text) is not None


def lint(reference_root: Path) -> list[str]:
    root = Path(reference_root)
    problems: list[str] = []
    claude, human = root / "claude", root / "human"

    index_text = (claude / "INDEX.md").read_text(encoding="utf-8") if (claude / "INDEX.md").exists() else ""
    for f in sorted(claude.glob("*.md")):
        text = f.read_text(encoding="utf-8")
        n = text.count("\n")
        if n > MAX_LINES:
            problems.append(f"claude/{f.name}: {n} lines exceeds {MAX_LINES}")
        if f.name == "INDEX.md":
            continue
        if not _mentioned(f.name, index_text):
            problems.append(f"claude/INDEX.md does not mention {f.name}")
        if f.name in _CLAUDE_EXEMPT:
            continue
        srcs = _sources_of(text)
        if not srcs:
            problems.append(f"claude/{f.name}: missing '## Sources' section with '- raw/...' lines")
            continue
        for s in srcs:
            if not (root / s).exists():
                problems.append(f"claude/{f.name}: source {s} does not exist")

    readme = (human / "README.md").read_text(encoding="utf-8") if (human / "README.md").exists() else ""
    for f in sorted(human.glob("*.md")):
        if f.name != "README.md" and not _mentioned(f.name, readme):
            problems.append(f"human/README.md does not mention {f.name}")
    return problems


def main() -> int:
    root = Path(__file__).resolve().parents[2] / "docs" / "reference"
    problems = lint(root)
    for p in problems:
        print(p)
    print(f"{len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
