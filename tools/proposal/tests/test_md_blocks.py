import sys, pathlib
import pytest

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from md_blocks import parse  # noqa: E402

HEAD = "## Judul:\nT\n\n## BAB I PENDAHULUAN\n\n"
TAIL = "\n\n## DAFTAR PUSTAKA\n[1] A.\n"


def body(md, base=ROOT / "docs/proposal_md"):
    return parse(HEAD + md + TAIL, base).body


def test_heading_levels():
    b = parse("## Judul:\nT\n\n## BAB I PENDAHULUAN\n\n### 1.1 X\n\n#### 3.4.1 Y" + TAIL,
              ROOT).body
    assert [(x.kind, x.text) for x in b] == [
        ("h1", "BAB I PENDAHULUAN"), ("h2", "1.1 X"), ("h3", "3.4.1 Y")]


def test_table_caption_attached():
    b = body("Tabel 3.1 Cap\n\n| a | b |\n|---|---|\n| 1 | 2 |")
    t = [x for x in b if x.kind == "table"]
    assert len(t) == 1 and t[0].text == "Tabel 3.1 Cap"
    assert t[0].rows == [["a", "b"], ["1", "2"]]
    assert not any(x.kind == "p" and x.text.startswith("Tabel") for x in b)


def test_listing_caption_after_fence():
    b = body("```json\n{}\n```\n\nListing 3.1 Cap")
    l = [x for x in b if x.kind == "listing"]
    assert l[0].lines == ["{}"] and l[0].text == "Listing 3.1 Cap"
    assert not any(x.kind == "p" for x in b)


def test_formula_block():
    f = [x for x in body("```rumus\nA = B (3.1)\n```") if x.kind == "formula"]
    assert f[0].lines == ["A = B (3.1)"]


def test_placeholders_verbatim():
    p = [x for x in body("Isi [insert data: x] dan [cite: y].") if x.kind == "p"][0]
    assert "".join(t for t, _ in p.runs) == "Isi [insert data: x] dan [cite: y]."


def test_code_and_comment_stripped():
    p = [x for x in body("a `b` c <!-- check:ok x -->") if x.kind == "p"][0]
    assert p.text == "a b c"


def test_bold_runs():
    p = [x for x in body("a **b** c") if x.kind == "p"][0]
    assert p.runs == [("a ", False), ("b", True), (" c", False)]


def test_missing_image_raises(tmp_path):
    with pytest.raises(FileNotFoundError, match="nope.png"):
        body("![Gambar 1.1 X](figures/nope.png)", tmp_path)


def test_image_block():
    i = [x for x in body("![Gambar 3.1 Alur penelitian](figures/alur.png)") if x.kind == "img"][0]
    assert i.text == "Gambar 3.1 Alur penelitian" and i.path.name == "alur.png"


def test_real_proposal():
    d = parse((ROOT / "docs/proposal_md/proposal.md").read_text(encoding="utf-8"),
              ROOT / "docs/proposal_md")
    assert len(d.references) == 41 and d.references[0].startswith("[1] ")
    assert d.title_id.startswith("Pengembangan Sistem Pendukung")
    assert d.title_en.startswith("Development of a Clinical")
    assert d.kata_kunci.startswith("Kata kunci:") and d.keywords.startswith("Keywords:")
    assert len(d.abstrak) == 1 and len(d.abstract) == 1
    h2 = [x.text for x in d.body if x.kind == "h2"]
    assert "3.1 Pendekatan dan Alur Penelitian" in h2 and "3.12 Rencana Kerja" in h2
