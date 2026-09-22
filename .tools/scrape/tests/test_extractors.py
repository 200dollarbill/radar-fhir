from pathlib import Path
import pytest
from tools.scrape import extractors

FIX = Path(__file__).parent / "fixtures"


def read(name):
    return (FIX / name).read_text(encoding="utf-8")


def test_satusehat_extracts_article_body():
    html = extractors.extract("satusehat", read("satusehat_page.html"))
    assert "Apa itu SATUSEHAT" in html
    assert "<nav" not in html
    assert "<script" not in html
    assert 'class="toc' not in html


def test_satusehat_redirect_notice_raises():
    with pytest.raises(extractors.PageMissing):
        extractors.extract("satusehat", read("satusehat_redirect.html"))


def test_hl7_extracts_segment_content():
    html = extractors.extract("fhir-r4", read("hl7_page.html"))
    assert "Device" in html
    assert "<script" not in html
    assert 'id="segment-header"' not in html


def test_hl7_missing_content_raises():
    with pytest.raises(extractors.PageMissing):
        extractors.extract("fhir-r4", "<html><body><p>nothing</p></body></html>")


def test_unknown_group_raises():
    with pytest.raises(ValueError):
        extractors.extract("nope", "<html></html>")
