import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from check_text import check


def test_dash_in_prose():
    assert any("dash" in p for p in check("Radar non-kontak dipakai."))


def test_en_em_dash():
    assert check("A – B") and check("A — B")


def test_citation_range():
    assert any("citation" in p for p in check("Bukti [42]."))


def test_citation_ok():
    assert check("Bukti [1][41].") == []


def test_new_marker():
    assert check("Bukti [new].")


def test_banned_word():
    assert any("banned" in p for p in check("Sistem ini memberi diagnosa."))


def test_banned_negated():
    assert check("Keluaran bukan diagnosa.") == []


def test_bibliography_skipped():
    assert check("## DAFTAR PUSTAKA\n[50] A-B, doi: 10.1-2") == []


def test_heading_and_image_skipped():
    assert check("![Gambar 3.1 Alur](figures/a-b.png)") == []


def test_inline_code_skipped():
    assert check("Kode `raw-capture` dipakai.") == []
