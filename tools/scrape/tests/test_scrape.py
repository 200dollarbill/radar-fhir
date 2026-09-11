from pathlib import Path
import pytest
from tools.scrape import scrape, convert

FIX = Path(__file__).parent / "fixtures"


def test_load_sources_resolves_base_urls(tmp_path):
    y = tmp_path / "s.yaml"
    y.write_text(
        "satusehat_base: https://s.example/\nfhir_r4_base: https://r4.example/\n"
        "fhir_ci_base: https://ci.example/\nsources:\n"
        "  - {id: a, group: satusehat, url: x/, title: A}\n"
        "  - {id: b, group: fhir-r4, url: y.html, title: B}\n"
        "  - {id: c, group: fhir-ci, url: z.html, title: C}\n"
    )
    srcs = scrape.load_sources(y)
    assert [s["url"] for s in srcs] == [
        "https://s.example/x/", "https://r4.example/y.html", "https://ci.example/z.html"]


def test_load_sources_rejects_duplicate_ids(tmp_path):
    y = tmp_path / "s.yaml"
    y.write_text(
        "satusehat_base: https://s/\nfhir_r4_base: https://r/\nfhir_ci_base: https://c/\n"
        "sources:\n  - {id: a, group: satusehat, url: x/, title: A}\n"
        "  - {id: a, group: satusehat, url: y/, title: B}\n")
    with pytest.raises(ValueError):
        scrape.load_sources(y)


def test_build_document_has_frontmatter_and_hash():
    src = {"id": "device", "group": "fhir-r4", "url": "https://hl7.org/fhir/R4/device.html",
           "title": "Device"}
    html = (FIX / "hl7_page.html").read_text(encoding="utf-8")
    text = scrape.build_document(src, html, "2026-09-11T00:00:00Z")
    meta, body = convert.parse_document(text)
    assert meta["id"] == "device"
    assert meta["fhir_version"] == "R4"
    assert meta["sha256"] == convert.text_hash(body)
    assert "Device" in body


def test_fhir_version_by_group():
    assert scrape.fhir_version_for("satusehat") == "R4"
    assert scrape.fhir_version_for("fhir-r4") == "R4"
    assert scrape.fhir_version_for("fhir-ci") == "R6-ci"


def test_output_path():
    p = scrape.output_path(Path("/r"), {"id": "x", "group": "fhir-r4"})
    assert p == Path("/r/fhir-r4/x.md")


def test_run_writes_files_and_collects_failures(tmp_path):
    good = (FIX / "satusehat_page.html").read_text(encoding="utf-8")
    bad = (FIX / "satusehat_redirect.html").read_text(encoding="utf-8")
    sources = [
        {"id": "ok", "group": "satusehat", "url": "https://s/ok/", "title": "OK"},
        {"id": "missing", "group": "satusehat", "url": "https://s/missing/", "title": "M"},
    ]
    pages = {"https://s/ok/": good, "https://s/missing/": bad}
    failures = scrape.run(sources, tmp_path, fetch_fn=pages.__getitem__, sleep_fn=lambda s: None)
    assert (tmp_path / "satusehat" / "ok.md").exists()
    assert not (tmp_path / "satusehat" / "missing.md").exists()
    assert failures == [("missing", "SATUSEHAT redirect notice (page does not exist)")]


@pytest.mark.network
def test_fetch_real_page_smoke():
    html = scrape.fetch("https://hl7.org/fhir/R4/patient.html")
    assert 'id="segment-content"' in html
