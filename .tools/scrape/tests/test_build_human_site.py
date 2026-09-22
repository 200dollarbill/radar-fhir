"""Tests for tools/scrape/build_human_site.py."""
from pathlib import Path

from tools.scrape.build_human_site import build


def _write(dir_: Path, name: str, text: str) -> None:
    (dir_ / name).write_text(text, encoding="utf-8")


def test_order_readme_first_review_last_one_section_per_file(tmp_path: Path) -> None:
    _write(tmp_path, "README.md", "# Overview\n\nIntro text.\n")
    _write(tmp_path, "01-a.md", "# Section A\n\nSome content.\n")
    _write(tmp_path, "validity-review.md", "# Validity Review\n\nReview text.\n")

    result = build(tmp_path)

    readme_pos = result.index('<section id="README"')
    a_pos = result.index('<section id="01-a"')
    review_pos = result.index('<section id="validity-review"')
    assert readme_pos < a_pos < review_pos
    assert result.count("<section id=") == 3


def test_mermaid_fence_becomes_escaped_pre(tmp_path: Path) -> None:
    _write(tmp_path, "README.md", "# Overview\n\nIntro.\n")
    _write(
        tmp_path,
        "01-diagram.md",
        "# Diagram\n\n```mermaid\ngraph TD\n  A --> B\n```\n",
    )

    result = build(tmp_path)

    assert '<pre class="mermaid">' in result
    assert "--&gt;" in result
    assert '<p><pre class="mermaid">' not in result


def test_markdown_table_becomes_html_table(tmp_path: Path) -> None:
    _write(tmp_path, "README.md", "# Overview\n\nIntro.\n")
    _write(
        tmp_path,
        "01-table.md",
        "# Table\n\n| A | B |\n| - | - |\n| 1 | 2 |\n",
    )

    result = build(tmp_path)

    assert "<table>" in result
