from pathlib import Path
from tools.scrape import lint_views


def _make(root: Path):
    (root / "raw" / "fhir-r4").mkdir(parents=True)
    (root / "raw" / "fhir-r4" / "patient.md").write_text("---\nid: patient\n---\nx\n")
    (root / "claude").mkdir()
    (root / "human").mkdir()
    (root / "claude" / "INDEX.md").write_text("- fhir-patient.md — Patient\n")
    (root / "claude" / "fhir-patient.md").write_text("# Patient\n\n## Sources\n- raw/fhir-r4/patient.md\n")
    (root / "human" / "README.md").write_text("1. 01-patient.md\n")
    (root / "human" / "01-patient.md").write_text("# Patient\n")


def test_clean_tree_has_no_problems(tmp_path):
    _make(tmp_path)
    assert lint_views.lint(tmp_path) == []


def test_missing_sources_section(tmp_path):
    _make(tmp_path)
    (tmp_path / "claude" / "fhir-patient.md").write_text("# Patient\n")
    problems = lint_views.lint(tmp_path)
    assert any("fhir-patient.md" in p and "Sources" in p for p in problems)


def test_nonexistent_raw_path(tmp_path):
    _make(tmp_path)
    (tmp_path / "claude" / "fhir-patient.md").write_text("# P\n\n## Sources\n- raw/fhir-r4/nope.md\n")
    assert any("nope.md" in p for p in lint_views.lint(tmp_path))


def test_too_long(tmp_path):
    _make(tmp_path)
    (tmp_path / "claude" / "fhir-patient.md").write_text(
        "# P\n" + "line\n" * 400 + "## Sources\n- raw/fhir-r4/patient.md\n")
    assert any("400" in p for p in lint_views.lint(tmp_path))


def test_not_in_index(tmp_path):
    _make(tmp_path)
    (tmp_path / "claude" / "INDEX.md").write_text("nothing here\n")
    assert any("INDEX.md" in p for p in lint_views.lint(tmp_path))


def test_human_not_in_readme(tmp_path):
    _make(tmp_path)
    (tmp_path / "human" / "README.md").write_text("nothing\n")
    assert any("README.md" in p for p in lint_views.lint(tmp_path))
