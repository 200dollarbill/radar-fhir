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
    assert check("Bukti [1], [41].") == []


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


def test_allow_marker():
    assert check("Variabel RME: tanda vital, diagnosis, prosedur. <!-- check:ok diagnosis -->") == []


def test_allow_marker_only_named_word():
    assert check("Diagnosis dan prediksi. <!-- check:ok diagnosis -->")


def test_adjacent_citations():
    assert any("citation" in p for p in check("Bukti [5][6]."))


def test_spaced_dash():
    assert any("dash" in p for p in check("Antara 1,2 - 1,4 juta."))


def test_digit_hyphen():
    assert any("dash" in p for p in check("Periode 2020-2026."))


def test_inflected_banned():
    for w in ("memprediksi", "memantau", "mendiagnosis"):
        assert any("banned" in p for p in check(f"Sistem ini {w} pasien.")), w


def test_tidak_hanya_is_not_negation():
    assert check("Sistem tidak hanya diagnosis.")


def test_plain_bibliography_heading_stops():
    assert check("DAFTAR PUSTAKA\n[50] A-B") == []


def test_fhir_resource_name_allowed():
    assert check("Resource Observation dan DiagnosticReport dipakai.") == []


def test_fenced_block_skipped():
    assert check("Teks.\n```json\n{\"date\": \"2026-11-18\"}\n```\nTeks lagi.") == []


def test_after_fence_still_checked():
    assert any("dash" in p for p in check("```json\n{}\n```\nRadar non-kontak."))
