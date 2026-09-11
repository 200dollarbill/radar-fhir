from pathlib import Path
from tools.scrape import check, scrape

FIX = Path(__file__).parent / "fixtures"
SRC = {"id": "intro", "group": "satusehat", "url": "https://s/intro/", "title": "Intro"}


def _write_raw(tmp_path, html):
    text = scrape.build_document(SRC, html, "2026-09-11T00:00:00Z")
    p = scrape.output_path(tmp_path, SRC)
    p.parent.mkdir(parents=True)
    p.write_text(text, encoding="utf-8")


def test_unchanged(tmp_path):
    html = (FIX / "satusehat_page.html").read_text(encoding="utf-8")
    _write_raw(tmp_path, html)
    assert check.classify(SRC, tmp_path, lambda u: html) == ("unchanged", "")


def test_changed(tmp_path):
    html = (FIX / "satusehat_page.html").read_text(encoding="utf-8")
    _write_raw(tmp_path, html)
    edited = html.replace("<strong>SATUSEHAT</strong>", "<strong>SATUSEHAT v99</strong>", 1)
    status, detail = check.classify(SRC, tmp_path, lambda u: edited)
    assert status == "changed"
    assert "sha256" in detail


def test_failed_when_page_missing(tmp_path):
    html = (FIX / "satusehat_page.html").read_text(encoding="utf-8")
    _write_raw(tmp_path, html)
    bad = (FIX / "satusehat_redirect.html").read_text(encoding="utf-8")
    status, _ = check.classify(SRC, tmp_path, lambda u: bad)
    assert status == "failed"


def test_missing_local(tmp_path):
    html = (FIX / "satusehat_page.html").read_text(encoding="utf-8")
    assert check.classify(SRC, tmp_path, lambda u: html)[0] == "missing-local"
