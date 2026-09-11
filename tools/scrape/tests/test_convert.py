from tools.scrape import convert


def test_html_to_markdown_uses_atx_headings_and_tables():
    md = convert.html_to_markdown(
        "<h2>Judul</h2><p>Isi.</p><table><tr><th>A</th></tr><tr><td>1</td></tr></table>"
    )
    assert "## Judul" in md
    assert "| A |" in md
    assert "\n\n\n" not in md


def test_text_hash_is_stable_sha256():
    assert convert.text_hash("abc") == (
        "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"
    )


def test_render_and_parse_roundtrip():
    meta = {"id": "x", "title": "T", "source_url": "https://e.com/", "group": "fhir-r4",
            "fhir_version": "R4", "fetched_at": "2026-09-11T00:00:00Z", "sha256": "0" * 64}
    text = convert.render_document(meta, "# T\n\nbody\n")
    assert text.startswith("---\n")
    parsed_meta, body = convert.parse_document(text)
    assert parsed_meta == meta
    assert body == "# T\n\nbody\n"
