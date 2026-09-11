# FHIR / SATUSEHAT Reference Compilation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Produce a verified local knowledge base (raw evidence + Claude view + human view + validity review) from the SATUSEHAT playbook and the FHIR R4 spec.

**Architecture:** A small Python scraper (`tools/scrape/`) fetches a fixed list of pages from `sources.yaml`, extracts the main content with a per-site extractor, and writes Markdown with YAML front-matter into `docs/reference/raw/`. Two hand-authored views (`docs/reference/claude/`, `docs/reference/human/`) are then written from the raw layer, and a lint script checks that every view file cites existing raw files. A validity review cross-checks SATUSEHAT claims against FHIR R4.

**Tech Stack:** Python 3.12, `requests`, `beautifulsoup4`, `markdownify`, `pyyaml`, `pytest`. Git for versioning. Artifact tool for publishing the human view.

**Spec:** `docs/superpowers/specs/2026-09-11-fhir-reference-compilation-design.md`

## Global Constraints

- FHIR spec pages come from `https://hl7.org/fhir/R4/` (front-matter `fhir_version: R4`). Only `documentation.html` and `overview-dev.html` come from `https://build.fhir.org/` (`fhir_version: R6-ci`).
- SATUSEHAT pages come from `https://satusehat.kemkes.go.id/platform/docs/id/`. The site is Antora: main content is `<article class="doc">`; missing pages return HTTP 200 with `<title>Redirect Notice</title>` and MUST be treated as failures.
- hl7.org pages: main content is `<div id="segment-content">`.
- Raw files under `docs/reference/raw/` are never hand-edited.
- Rate limit 1 request/second, 3 retries, `User-Agent: fhir-reference-compiler/0.1 (student project)`.
- Claude view files: tables over prose, ≤ 400 lines, end with a `## Sources` section listing `raw/` paths; Indonesian terms kept with an English gloss on first use.
- Every commit message ends with the attribution lines:
  ```
  Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
  Claude-Session: https://claude.ai/code/session_015J8WMGo1hde4fa74TJQ7Kn
  ```
- Run all Python from the project root with `python3 -m pytest tools/scrape/tests -v` and `python3 tools/scrape/scrape.py`.

## File Structure

```
tools/scrape/
├── __init__.py
├── requirements.txt          # requests, beautifulsoup4, markdownify, pyyaml, pytest
├── sources.yaml              # the page list (single source of truth)
├── extractors.py             # extract_satusehat(html) / extract_hl7(html) -> content HTML or raise
├── convert.py                # html_to_markdown(html) and front-matter helpers
├── scrape.py                 # CLI: fetch all sources -> docs/reference/raw/<group>/<id>.md
├── check.py                  # CLI: re-fetch, compare sha256, print unchanged/changed/failed
├── lint_views.py             # CLI: validate claude/ and human/ views (Sources exist, ≤400 lines, INDEX complete)
└── tests/
    ├── fixtures/
    │   ├── satusehat_page.html
    │   ├── satusehat_redirect.html
    │   └── hl7_page.html
    ├── test_extractors.py
    ├── test_convert.py
    ├── test_scrape.py
    ├── test_check.py
    └── test_lint_views.py
docs/reference/
├── raw/{satusehat,fhir-r4,fhir-ci}/*.md
├── claude/INDEX.md, satusehat-*.md, fhir-*.md, VALIDITY-REVIEW.md
└── human/README.md, NN-*.md, validity-review.md
```

---

### Task 1: Scraper scaffolding and extractors

**Files:**
- Create: `tools/scrape/__init__.py`, `tools/scrape/requirements.txt`, `tools/scrape/extractors.py`
- Create: `tools/scrape/tests/__init__.py`, `tools/scrape/tests/fixtures/satusehat_page.html`, `tools/scrape/tests/fixtures/satusehat_redirect.html`, `tools/scrape/tests/fixtures/hl7_page.html`
- Test: `tools/scrape/tests/test_extractors.py`

**Interfaces:**
- Produces: `extractors.extract(group: str, html: str) -> str` — returns the inner HTML of the main content element (nav/footer/script/aside removed). Raises `extractors.PageMissing` when the page is a SATUSEHAT "Redirect Notice" or the content element is absent. `group` is one of `"satusehat"`, `"fhir-r4"`, `"fhir-ci"`.

- [ ] **Step 1: Install dependencies**

```bash
cat > tools/scrape/requirements.txt <<'EOF'
requests>=2.31
beautifulsoup4>=4.12
markdownify>=0.12
pyyaml>=6.0
pytest>=8.0
EOF
python3 -m pip install --user -r tools/scrape/requirements.txt
touch tools/scrape/__init__.py tools/scrape/tests/__init__.py
```

- [ ] **Step 2: Save fixtures from the live sites**

```bash
mkdir -p tools/scrape/tests/fixtures
UA="fhir-reference-compiler/0.1 (student project)"
curl -sL -A "$UA" "https://satusehat.kemkes.go.id/platform/docs/id/playbook/introduction/" -o tools/scrape/tests/fixtures/satusehat_page.html
curl -sL -A "$UA" "https://satusehat.kemkes.go.id/platform/docs/id/fhir/resources/device/" -o tools/scrape/tests/fixtures/satusehat_redirect.html
curl -sL -A "$UA" "https://hl7.org/fhir/R4/device.html" -o tools/scrape/tests/fixtures/hl7_page.html
grep -c 'class="doc"' tools/scrape/tests/fixtures/satusehat_page.html      # expect 1
grep -c 'Redirect Notice' tools/scrape/tests/fixtures/satusehat_redirect.html  # expect >=1
grep -c 'id="segment-content"' tools/scrape/tests/fixtures/hl7_page.html   # expect 1
```

- [ ] **Step 3: Write the failing tests**

`tools/scrape/tests/test_extractors.py`:
```python
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
```

- [ ] **Step 4: Run tests to verify they fail**

Run: `python3 -m pytest tools/scrape/tests/test_extractors.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'tools.scrape.extractors'`

- [ ] **Step 5: Implement extractors**

`tools/scrape/extractors.py`:
```python
"""Per-site main-content extraction. Returns inner HTML of the content element."""
from bs4 import BeautifulSoup


class PageMissing(Exception):
    """The page exists over HTTP but has no real content (404-as-200, redirect notice)."""


_STRIP_TAGS = ("script", "style", "nav", "aside", "footer", "header", "iframe", "svg")


def _strip(el):
    for tag in el.find_all(_STRIP_TAGS):
        tag.decompose()
    return el


def _extract_satusehat(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    title = soup.title.get_text(strip=True) if soup.title else ""
    if "Redirect Notice" in title:
        raise PageMissing("SATUSEHAT redirect notice (page does not exist)")
    article = soup.select_one("article.doc")
    if article is None:
        raise PageMissing("no <article class='doc'> found")
    return _strip(article).decode_contents()


def _extract_hl7(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    content = soup.select_one("div#segment-content")
    if content is None:
        raise PageMissing("no <div id='segment-content'> found")
    return _strip(content).decode_contents()


_EXTRACTORS = {
    "satusehat": _extract_satusehat,
    "fhir-r4": _extract_hl7,
    "fhir-ci": _extract_hl7,
}


def extract(group: str, html: str) -> str:
    try:
        fn = _EXTRACTORS[group]
    except KeyError:
        raise ValueError(f"unknown group: {group!r}") from None
    return fn(html)
```

- [ ] **Step 6: Run tests to verify they pass**

Run: `python3 -m pytest tools/scrape/tests/test_extractors.py -v`
Expected: 5 passed

- [ ] **Step 7: Commit**

```bash
git add tools/scrape
git commit -m "feat(scrape): add per-site content extractors with fixtures

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_015J8WMGo1hde4fa74TJQ7Kn"
```

---

### Task 2: HTML→Markdown conversion and front-matter helpers

**Files:**
- Create: `tools/scrape/convert.py`
- Test: `tools/scrape/tests/test_convert.py`

**Interfaces:**
- Consumes: nothing from earlier tasks.
- Produces:
  - `convert.html_to_markdown(html: str) -> str` — Markdown with ATX headings, collapsed blank lines.
  - `convert.text_hash(markdown: str) -> str` — sha256 hex of the Markdown body.
  - `convert.render_document(meta: dict, body: str) -> str` — YAML front-matter (`---\n...\n---\n`) followed by body.
  - `convert.parse_document(text: str) -> tuple[dict, str]` — inverse of `render_document`.

- [ ] **Step 1: Write the failing tests**

`tools/scrape/tests/test_convert.py`:
```python
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
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python3 -m pytest tools/scrape/tests/test_convert.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'tools.scrape.convert'`

- [ ] **Step 3: Implement convert.py**

`tools/scrape/convert.py`:
```python
"""HTML -> Markdown conversion and front-matter (de)serialisation for raw reference files."""
import hashlib
import re

import yaml
from markdownify import markdownify

_BLANKS = re.compile(r"\n{3,}")


def html_to_markdown(html: str) -> str:
    md = markdownify(html, heading_style="ATX", bullets="-")
    md = _BLANKS.sub("\n\n", md).strip() + "\n"
    return md


def text_hash(markdown: str) -> str:
    return hashlib.sha256(markdown.encode("utf-8")).hexdigest()


def render_document(meta: dict, body: str) -> str:
    front = yaml.safe_dump(meta, sort_keys=False, allow_unicode=True).rstrip("\n")
    return f"---\n{front}\n---\n{body}"


def parse_document(text: str) -> tuple[dict, str]:
    if not text.startswith("---\n"):
        raise ValueError("document has no front-matter")
    end = text.index("\n---\n", 4)
    meta = yaml.safe_load(text[4:end])
    body = text[end + len("\n---\n"):]
    return meta, body
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python3 -m pytest tools/scrape/tests/test_convert.py -v`
Expected: 3 passed

- [ ] **Step 5: Commit**

```bash
git add tools/scrape/convert.py tools/scrape/tests/test_convert.py
git commit -m "feat(scrape): add markdown conversion and front-matter helpers

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_015J8WMGo1hde4fa74TJQ7Kn"
```

---

### Task 3: sources.yaml and scrape.py

**Files:**
- Create: `tools/scrape/sources.yaml`, `tools/scrape/scrape.py`
- Test: `tools/scrape/tests/test_scrape.py`

**Interfaces:**
- Consumes: `extractors.extract`, `extractors.PageMissing`, `convert.html_to_markdown`, `convert.text_hash`, `convert.render_document`.
- Produces:
  - `scrape.load_sources(path: Path) -> list[dict]` — each dict has keys `id, group, url, title`.
  - `scrape.fetch(url: str, session=None) -> str` — GET with UA and retries; raises `requests.HTTPError` on non-200.
  - `scrape.build_document(source: dict, html: str, fetched_at: str) -> str` — full file text (front-matter + body).
  - `scrape.output_path(root: Path, source: dict) -> Path` — `root / group / f"{id}.md"`.
  - `scrape.run(sources, root, fetch_fn, sleep_fn) -> list[tuple[str, str]]` — returns list of `(source_id, error_message)` failures.
  - CLI: `python3 tools/scrape/scrape.py [--only ID ...]` writes to `docs/reference/raw/`, prints a summary, exits 1 if any failures.

- [ ] **Step 1: Write sources.yaml**

`tools/scrape/sources.yaml` (all URLs verified reachable on 2026-09-11):
```yaml
# group: satusehat | fhir-r4 | fhir-ci
# id becomes the filename: docs/reference/raw/<group>/<id>.md
satusehat_base: https://satusehat.kemkes.go.id/platform/docs/id/
fhir_r4_base: https://hl7.org/fhir/R4/
fhir_ci_base: https://build.fhir.org/

sources:
  # --- SATUSEHAT: overview ---
  - {id: playbook-preface,      group: satusehat, url: playbook/preface/,      title: Pengantar Teknis}
  - {id: playbook-introduction, group: satusehat, url: playbook/introduction/, title: Apa itu SATUSEHAT?}
  - {id: playbook-service,      group: satusehat, url: playbook/service/,      title: Layanan SATUSEHAT}
  - {id: glossary,              group: satusehat, url: glossary/,              title: Kamus Istilah}
  # --- SATUSEHAT: FHIR framework and data types ---
  - {id: fhir-index,            group: satusehat, url: fhir/,                     title: FHIR}
  - {id: fhir-framework,        group: satusehat, url: fhir/framework/,           title: Kerangka FHIR}
  - {id: fhir-prerequisites,    group: satusehat, url: fhir/prerequisites/,       title: Orientasi/Onboarding/Prerequisites}
  - {id: fhir-resources-index,  group: satusehat, url: fhir/resources/,           title: Interoperabilitas (daftar resource)}
  - {id: datatype-primitive,    group: satusehat, url: fhir/data-type/primitive/, title: Data Type - Primitive}
  - {id: datatype-general,      group: satusehat, url: fhir/data-type/general/,   title: Data Type - General}
  - {id: datatype-metadata,     group: satusehat, url: fhir/data-type/metadata/,  title: Data Type - Metadata}
  - {id: datatype-special,      group: satusehat, url: fhir/data-type/special/,   title: Data Type - Special}
  # --- SATUSEHAT: resource profiles ---
  - {id: res-patient,           group: satusehat, url: fhir/resources/patient/,        title: Patient}
  - {id: res-practitioner,      group: satusehat, url: fhir/resources/practitioner/,   title: Practitioner}
  - {id: res-organization,      group: satusehat, url: fhir/resources/organization/,   title: Organization}
  - {id: res-location,          group: satusehat, url: fhir/resources/location/,       title: Location}
  - {id: res-encounter,         group: satusehat, url: fhir/resources/encounter/,      title: Encounter}
  - {id: res-observation,       group: satusehat, url: fhir/resources/observation/,    title: Observation}
  - {id: res-condition,         group: satusehat, url: fhir/resources/condition/,      title: Condition}
  - {id: res-procedure,         group: satusehat, url: fhir/resources/procedure/,      title: Procedure}
  - {id: res-related-person,    group: satusehat, url: fhir/resources/related-person/, title: RelatedPerson}
  - {id: res-device,            group: satusehat, url: fhir/resources/device/,         title: Device (expected missing)}
  # --- SATUSEHAT: REST API catalogue ---
  - {id: api-onboardings,          group: satusehat, url: api-catalogue/onboardings/,                         title: API Onboardings}
  - {id: api-patient,              group: satusehat, url: api-catalogue/onboardings/apis/patient/,            title: API Patient}
  - {id: api-practitioner,         group: satusehat, url: api-catalogue/onboardings/apis/practitioner/,       title: API Practitioner}
  - {id: api-organization,         group: satusehat, url: api-catalogue/onboardings/apis/organization/,       title: API Organization}
  - {id: api-location,             group: satusehat, url: api-catalogue/onboardings/apis/location/,           title: API Location}
  - {id: api-integrations,         group: satusehat, url: api-catalogue/integrations/,                        title: API Integrations}
  - {id: api-encounter,            group: satusehat, url: api-catalogue/integrations/apis/encounter/,         title: API Encounter}
  - {id: api-observation,          group: satusehat, url: api-catalogue/integrations/apis/observation/,       title: API Observation}
  - {id: api-condition,            group: satusehat, url: api-catalogue/integrations/apis/condition/,         title: API Condition}
  - {id: api-procedure,            group: satusehat, url: api-catalogue/integrations/apis/procedure/,         title: API Procedure}
  - {id: api-practitioner-role,    group: satusehat, url: api-catalogue/integrations/apis/practitioner-role/, title: API PractitionerRole}
  - {id: api-validasi,             group: satusehat, url: api-catalogue/validasi/,                            title: Validasi}
  - {id: api-kamus-validasi,       group: satusehat, url: api-catalogue/validasi/kamus-validasi/,             title: Kamus Validasi}
  - {id: api-list-response,        group: satusehat, url: api-catalogue/validasi/list-response/,              title: List Response}
  # --- SATUSEHAT: interoperability use case ---
  - {id: interop-index,            group: satusehat, url: interoperability/,                 title: Panduan Interoperabilitas}
  - {id: interop-rme-rawat-jalan,  group: satusehat, url: interoperability/rme-rawat-jalan/, title: Resume Medis - Rawat Jalan}
  # --- SATUSEHAT: terminology ---
  - {id: term-index,               group: satusehat, url: terminology/,                                          title: Terminologi}
  - {id: term-standar,             group: satusehat, url: terminology/standar-terminologi/,                      title: Standar Terminologi SATUSEHAT}
  - {id: term-loinc,               group: satusehat, url: terminology/loinc/,                                    title: LOINC}
  - {id: term-loinc-laboratory,    group: satusehat, url: terminology/loinc/laboratory/,                         title: LOINC Laboratory}
  - {id: term-snomed-ct,           group: satusehat, url: terminology/snomed-ct/,                                title: SNOMED-CT}
  - {id: term-icd-10,              group: satusehat, url: terminology/icd/icd-10/,                               title: ICD-10}
  - {id: term-icd-9-cm,            group: satusehat, url: terminology/icd/icd-9-cm/,                             title: ICD-9-CM}
  - {id: term-lampiran-rawat-jalan, group: satusehat, url: terminology/lampiran-terminologi/rme-rawat-jalan1/,   title: Lampiran Terminologi Resume Medis Rawat Jalan}
  # --- SATUSEHAT: master data ---
  - {id: master-index,             group: satusehat, url: master-data/,                                        title: Master Data}
  - {id: mpi-preliminary,          group: satusehat, url: master-data/master-patient-index/preliminary/,       title: MPI Preliminary}
  - {id: mpi-pasien-nik,           group: satusehat, url: master-data/master-patient-index/pasien-nik/,        title: MPI Pasien dengan NIK}
  - {id: mpi-pasien-no-nik,        group: satusehat, url: master-data/master-patient-index/pasien-no-nik/,     title: MPI Pasien tanpa NIK}
  - {id: mpi-pasien-bayi,          group: satusehat, url: master-data/master-patient-index/pasien-bayi/,       title: MPI Pasien Bayi}
  - {id: mpi-rest-api,             group: satusehat, url: master-data/master-patient-index/rest-api-mpi/,      title: MPI REST API}
  - {id: msi-preliminary,          group: satusehat, url: master-data/master-sarana-index/preliminary/,        title: MSI Preliminary}
  - {id: msi-rest-api,             group: satusehat, url: master-data/master-sarana-index/rest-api-msi/,       title: MSI REST API}
  - {id: wilayah-preliminary,      group: satusehat, url: master-data/master-wilayah/preliminary/,             title: Master Wilayah Preliminary}
  # --- FHIR R4: server behaviour ---
  - {id: http,                 group: fhir-r4, url: http.html,                title: RESTful API}
  - {id: search,               group: fhir-r4, url: search.html,              title: Search}
  - {id: operations,           group: fhir-r4, url: operations.html,          title: Operations}
  - {id: bundle,               group: fhir-r4, url: bundle.html,              title: Bundle}
  - {id: capabilitystatement,  group: fhir-r4, url: capabilitystatement.html, title: CapabilityStatement}
  # --- FHIR R4: security ---
  - {id: security,             group: fhir-r4, url: security.html,            title: Security}
  - {id: secpriv-module,       group: fhir-r4, url: secpriv-module.html,      title: Security and Privacy Module}
  # --- FHIR R4: data model basics ---
  - {id: datatypes,            group: fhir-r4, url: datatypes.html,           title: Data Types}
  - {id: references,           group: fhir-r4, url: references.html,          title: Resource References}
  - {id: narrative,            group: fhir-r4, url: narrative.html,           title: Narrative}
  - {id: validation,           group: fhir-r4, url: validation.html,          title: Validation}
  # --- FHIR R4: resources ---
  - {id: patient,              group: fhir-r4, url: patient.html,             title: Patient}
  - {id: practitioner,         group: fhir-r4, url: practitioner.html,        title: Practitioner}
  - {id: practitionerrole,     group: fhir-r4, url: practitionerrole.html,    title: PractitionerRole}
  - {id: organization,         group: fhir-r4, url: organization.html,        title: Organization}
  - {id: location,             group: fhir-r4, url: location.html,            title: Location}
  - {id: encounter,            group: fhir-r4, url: encounter.html,           title: Encounter}
  - {id: observation,          group: fhir-r4, url: observation.html,         title: Observation}
  - {id: observation-vitalsigns, group: fhir-r4, url: observation-vitalsigns.html, title: Vital Signs Profile}
  - {id: device,               group: fhir-r4, url: device.html,              title: Device}
  - {id: devicemetric,         group: fhir-r4, url: devicemetric.html,        title: DeviceMetric}
  - {id: devicedefinition,     group: fhir-r4, url: devicedefinition.html,    title: DeviceDefinition}
  - {id: condition,            group: fhir-r4, url: condition.html,           title: Condition}
  - {id: person,               group: fhir-r4, url: person.html,              title: Person}
  - {id: relatedperson,        group: fhir-r4, url: relatedperson.html,       title: RelatedPerson}
  - {id: procedure,            group: fhir-r4, url: procedure.html,           title: Procedure}
  # --- FHIR R4: profiling ---
  - {id: profiling,            group: fhir-r4, url: profiling.html,           title: Profiling FHIR}
  - {id: structuredefinition,  group: fhir-r4, url: structuredefinition.html, title: StructureDefinition}
  - {id: elementdefinition,    group: fhir-r4, url: elementdefinition.html,   title: ElementDefinition}
  - {id: extensibility,        group: fhir-r4, url: extensibility.html,       title: Extensibility}
  - {id: conformance-rules,    group: fhir-r4, url: conformance-rules.html,   title: Conformance Rules}
  - {id: conformance-module,   group: fhir-r4, url: conformance-module.html,  title: Conformance Module}
  - {id: implementationguide,  group: fhir-r4, url: implementationguide.html, title: ImplementationGuide}
  - {id: valueset,             group: fhir-r4, url: valueset.html,            title: ValueSet}
  - {id: codesystem,           group: fhir-r4, url: codesystem.html,          title: CodeSystem}
  # --- FHIR R4: workflow ---
  - {id: workflow,             group: fhir-r4, url: workflow.html,            title: Workflow}
  - {id: clinicalsummary-module, group: fhir-r4, url: clinicalsummary-module.html, title: Clinical Summary Module}
  # --- FHIR CI build (R6 draft) ---
  - {id: documentation,        group: fhir-ci, url: documentation.html,       title: Documentation Index (CI build)}
  - {id: overview-dev,         group: fhir-ci, url: overview-dev.html,        title: Overview for Developers (CI build)}
```

- [ ] **Step 2: Write the failing tests**

`tools/scrape/tests/test_scrape.py`:
```python
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
```

Add `tools/scrape/tests/conftest.py`:
```python
import socket
import pytest


def _online():
    try:
        socket.create_connection(("hl7.org", 443), timeout=3).close()
        return True
    except OSError:
        return False


def pytest_configure(config):
    config.addinivalue_line("markers", "network: needs internet")


def pytest_collection_modifyitems(config, items):
    if _online():
        return
    skip = pytest.mark.skip(reason="offline")
    for item in items:
        if "network" in item.keywords:
            item.add_marker(skip)
```

- [ ] **Step 3: Run tests to verify they fail**

Run: `python3 -m pytest tools/scrape/tests/test_scrape.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'tools.scrape.scrape'`

- [ ] **Step 4: Implement scrape.py**

`tools/scrape/scrape.py`:
```python
"""Fetch every page in sources.yaml and write docs/reference/raw/<group>/<id>.md."""
import argparse
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import requests
import yaml

if __package__ in (None, ""):  # allow `python3 tools/scrape/scrape.py`
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from tools.scrape import convert, extractors  # noqa: E402

HERE = Path(__file__).resolve().parent
PROJECT_ROOT = HERE.parents[1]
SOURCES_PATH = HERE / "sources.yaml"
RAW_ROOT = PROJECT_ROOT / "docs" / "reference" / "raw"
USER_AGENT = "fhir-reference-compiler/0.1 (student project)"
_BASE_KEY = {"satusehat": "satusehat_base", "fhir-r4": "fhir_r4_base", "fhir-ci": "fhir_ci_base"}
_FHIR_VERSION = {"satusehat": "R4", "fhir-r4": "R4", "fhir-ci": "R6-ci"}


def fhir_version_for(group: str) -> str:
    return _FHIR_VERSION[group]


def load_sources(path: Path) -> list[dict]:
    data = yaml.safe_load(Path(path).read_text(encoding="utf-8"))
    out, seen = [], set()
    for s in data["sources"]:
        if s["id"] in seen:
            raise ValueError(f"duplicate source id: {s['id']}")
        seen.add(s["id"])
        base = data[_BASE_KEY[s["group"]]]
        out.append({**s, "url": base + s["url"]})
    return out


def fetch(url: str, session: requests.Session | None = None, retries: int = 3) -> str:
    session = session or requests.Session()
    last_err: Exception | None = None
    for attempt in range(retries):
        try:
            r = session.get(url, headers={"User-Agent": USER_AGENT}, timeout=30)
            r.raise_for_status()
            r.encoding = r.apparent_encoding or "utf-8"
            return r.text
        except requests.RequestException as e:  # retry on any transport/HTTP error
            last_err = e
            time.sleep(2 * (attempt + 1))
    raise last_err  # type: ignore[misc]


def build_document(source: dict, html: str, fetched_at: str) -> str:
    body_html = extractors.extract(source["group"], html)
    body = convert.html_to_markdown(body_html)
    meta = {
        "id": source["id"],
        "title": source["title"],
        "source_url": source["url"],
        "group": source["group"],
        "fhir_version": fhir_version_for(source["group"]),
        "fetched_at": fetched_at,
        "sha256": convert.text_hash(body),
    }
    return convert.render_document(meta, body)


def output_path(root: Path, source: dict) -> Path:
    return Path(root) / source["group"] / f"{source['id']}.md"


def run(sources: list[dict], root: Path, fetch_fn=fetch, sleep_fn=time.sleep) -> list[tuple[str, str]]:
    failures: list[tuple[str, str]] = []
    for i, src in enumerate(sources):
        if i:
            sleep_fn(1.0)
        fetched_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        try:
            html = fetch_fn(src["url"])
            text = build_document(src, html, fetched_at)
        except (extractors.PageMissing, requests.RequestException) as e:
            failures.append((src["id"], str(e)))
            print(f"FAIL  {src['id']}: {e}")
            continue
        path = output_path(root, src)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        print(f"ok    {src['id']} -> {path.relative_to(PROJECT_ROOT) if path.is_relative_to(PROJECT_ROOT) else path}")
    return failures


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--only", nargs="*", help="source ids to fetch (default: all)")
    args = ap.parse_args(argv)
    sources = load_sources(SOURCES_PATH)
    if args.only:
        sources = [s for s in sources if s["id"] in set(args.only)]
    failures = run(sources, RAW_ROOT)
    print(f"\n{len(sources) - len(failures)} written, {len(failures)} failed")
    for sid, msg in failures:
        print(f"  - {sid}: {msg}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `python3 -m pytest tools/scrape/tests -v`
Expected: all pass (the network smoke test passes when online, is skipped when offline)

- [ ] **Step 6: Commit**

```bash
git add tools/scrape
git commit -m "feat(scrape): add sources.yaml and scrape CLI

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_015J8WMGo1hde4fa74TJQ7Kn"
```

---

### Task 4: check.py (staleness detection)

**Files:**
- Create: `tools/scrape/check.py`
- Test: `tools/scrape/tests/test_check.py`

**Interfaces:**
- Consumes: `scrape.load_sources`, `scrape.fetch`, `scrape.output_path`, `extractors.extract`, `convert.html_to_markdown`, `convert.text_hash`, `convert.parse_document`.
- Produces: `check.classify(source, root, fetch_fn) -> tuple[str, str]` returning `(status, detail)` with status in `{"unchanged", "changed", "failed", "missing-local"}`; CLI `python3 tools/scrape/check.py` prints one line per source and a summary, exit 0 only if every source is `unchanged`.

- [ ] **Step 1: Write the failing tests**

`tools/scrape/tests/test_check.py`:
```python
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
    edited = html.replace("SATUSEHAT", "SATUSEHAT v99", 1)
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
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python3 -m pytest tools/scrape/tests/test_check.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'tools.scrape.check'`

- [ ] **Step 3: Implement check.py**

`tools/scrape/check.py`:
```python
"""Re-fetch every source and report whether the local raw copy is still current."""
import sys
import time
from pathlib import Path

import requests

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from tools.scrape import convert, extractors, scrape  # noqa: E402


def classify(source: dict, root: Path, fetch_fn=scrape.fetch) -> tuple[str, str]:
    local = scrape.output_path(root, source)
    if not local.exists():
        return "missing-local", str(local)
    meta, _ = convert.parse_document(local.read_text(encoding="utf-8"))
    try:
        html = fetch_fn(source["url"])
        body = convert.html_to_markdown(extractors.extract(source["group"], html))
    except (extractors.PageMissing, requests.RequestException) as e:
        return "failed", str(e)
    new_hash = convert.text_hash(body)
    if new_hash == meta["sha256"]:
        return "unchanged", ""
    return "changed", f"sha256 {meta['sha256'][:12]} -> {new_hash[:12]} (fetched {meta['fetched_at']})"


def main() -> int:
    sources = scrape.load_sources(scrape.SOURCES_PATH)
    counts: dict[str, int] = {}
    for i, src in enumerate(sources):
        if i:
            time.sleep(1.0)
        status, detail = classify(src, scrape.RAW_ROOT)
        counts[status] = counts.get(status, 0) + 1
        print(f"{status:<14}{src['id']}  {detail}")
    print("\n" + ", ".join(f"{k}: {v}" for k, v in sorted(counts.items())))
    return 0 if set(counts) <= {"unchanged"} else 1


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python3 -m pytest tools/scrape/tests/test_check.py -v`
Expected: 4 passed

- [ ] **Step 5: Commit**

```bash
git add tools/scrape/check.py tools/scrape/tests/test_check.py
git commit -m "feat(scrape): add check.py for staleness detection

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_015J8WMGo1hde4fa74TJQ7Kn"
```

---

### Task 5: Run the scrape and commit the raw layer

**Files:**
- Create: `docs/reference/raw/{satusehat,fhir-r4,fhir-ci}/*.md` (scraper output)
- Create: `docs/reference/raw/FETCH-LOG.md`

**Interfaces:**
- Consumes: `python3 tools/scrape/scrape.py`, `python3 tools/scrape/check.py`.
- Produces: the raw evidence layer; `FETCH-LOG.md` listing the run date, counts, and every failed id with reason (input for the validity review in Task 9).

- [ ] **Step 1: Run the scraper**

```bash
python3 tools/scrape/scrape.py 2>&1 | tee /tmp/scrape-run.log
```
Expected: ~100 lines of `ok`, exit code 1 with at least `res-device` listed as failed (SATUSEHAT has no Device page). Any *other* failure: open the URL in a browser; if the page genuinely does not exist, keep it in the log; if the URL merely moved, fix it in `sources.yaml` and re-run with `--only <id>`.

- [ ] **Step 2: Spot-check three raw files**

```bash
head -12 docs/reference/raw/satusehat/res-observation.md
head -12 docs/reference/raw/fhir-r4/observation.md
wc -l docs/reference/raw/*/*.md | tail -1
grep -L '^sha256:' docs/reference/raw/*/*.md   # expect no output
```
Expected: each file starts with `---`, has all seven front-matter keys, and body text is readable Indonesian / English (no nav menus, no `<script>`).

- [ ] **Step 3: Verify check.py reports all unchanged**

```bash
python3 tools/scrape/check.py | tail -3
```
Expected: last line like `failed: 1, unchanged: 99` — the only non-`unchanged` entries are the ids that failed in Step 1.

- [ ] **Step 4: Write FETCH-LOG.md**

`docs/reference/raw/FETCH-LOG.md` — fill in the real numbers from `/tmp/scrape-run.log`:
```markdown
# Fetch log

| Run date (UTC) | Sources | Written | Failed |
|---|---|---|---|
| 2026-09-11 | <N> | <N-written> | <N-failed> |

## Failed sources

| id | url | reason | action |
|---|---|---|---|
| res-device | https://satusehat.kemkes.go.id/platform/docs/id/fhir/resources/device/ | SATUSEHAT redirect notice (page does not exist) | kept in sources.yaml as a documented gap; see VALIDITY-REVIEW |

## Notes
- SATUSEHAT playbook version at fetch time: 7.23 (from the site navigation "Yang Baru di Versi 7.23").
- Re-run `python3 tools/scrape/check.py` to detect upstream changes.
```

- [ ] **Step 5: Commit**

```bash
git add docs/reference/raw tools/scrape/sources.yaml
git commit -m "docs(reference): add raw scraped layer from SATUSEHAT and FHIR R4

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_015J8WMGo1hde4fa74TJQ7Kn"
```

---

### Task 6: lint_views.py (view validator)

**Files:**
- Create: `tools/scrape/lint_views.py`
- Test: `tools/scrape/tests/test_lint_views.py`

**Interfaces:**
- Consumes: nothing from the scraper modules (pure filesystem checks).
- Produces: `lint_views.lint(reference_root: Path) -> list[str]` returning human-readable problems (empty = clean); CLI `python3 tools/scrape/lint_views.py` exits 1 when problems exist. Rules:
  1. Every `claude/*.md` except `INDEX.md` and `VALIDITY-REVIEW.md` has a `## Sources` heading followed by at least one line of the form `- raw/<group>/<id>.md`, and each such path exists under `reference_root`.
  2. Every `claude/*.md` is ≤ 400 lines.
  3. Every `claude/*.md` (except `INDEX.md`) is mentioned by filename in `claude/INDEX.md`.
  4. Every `human/*.md` (except `README.md`) is mentioned by filename in `human/README.md`.

- [ ] **Step 1: Write the failing tests**

`tools/scrape/tests/test_lint_views.py`:
```python
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
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python3 -m pytest tools/scrape/tests/test_lint_views.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'tools.scrape.lint_views'`

- [ ] **Step 3: Implement lint_views.py**

`tools/scrape/lint_views.py`:
```python
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
        if f.name not in index_text:
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
        if f.name != "README.md" and f.name not in readme:
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
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python3 -m pytest tools/scrape/tests/test_lint_views.py -v`
Expected: 6 passed

- [ ] **Step 5: Commit**

```bash
git add tools/scrape/lint_views.py tools/scrape/tests/test_lint_views.py
git commit -m "feat(scrape): add lint_views.py to validate reference views

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_015J8WMGo1hde4fa74TJQ7Kn"
```

---

### Task 7: Claude view — SATUSEHAT topics

**Files:**
- Create: `docs/reference/claude/INDEX.md` and these topic files:
  - `satusehat-overview.md` (from raw `playbook-*`, `glossary`, `fhir-index`, `fhir-framework`, `fhir-prerequisites`)
  - `satusehat-datatypes.md` (from `datatype-*`)
  - `satusehat-identifiers-and-master-data.md` (from `mpi-*`, `msi-*`, `wilayah-preliminary`, `master-index`)
  - `satusehat-patient.md`, `satusehat-practitioner.md` (incl. PractitionerRole from `api-practitioner-role`), `satusehat-organization-location.md`, `satusehat-encounter.md`, `satusehat-observation.md`, `satusehat-condition.md`, `satusehat-procedure.md`, `satusehat-related-person.md` (each from its `res-*` + `api-*` raw pair)
  - `satusehat-rest-api-and-validation.md` (from `api-onboardings`, `api-integrations`, `api-validasi`, `api-kamus-validasi`, `api-list-response`)
  - `satusehat-usecase-rawat-jalan.md` (from `interop-index`, `interop-rme-rawat-jalan`)
  - `satusehat-terminology.md` (from `term-*`)

**Interfaces:**
- Consumes: `docs/reference/raw/satusehat/*.md`.
- Produces: files that pass `lint_views.lint` (rules in Task 6). `INDEX.md` line format: `- <filename> — <topic>. Load when: <hint>`.

Each resource file MUST use this template (fill from the raw pages; do not invent fields not in the raw text):
```markdown
# SATUSEHAT — <Resource>

Ringkasan (summary): <1–2 sentences, English>.

## Required / constrained elements
| Element | Cardinality | SATUSEHAT rule | Value set / system |
|---|---|---|---|
| identifier | 1..* | ... | https://fhir.kemkes.go.id/id/... |

## Identifier systems used
| Purpose | system URI |
|---|---|

## REST operations (from Katalog API)
| Method | Path | Notes |
|---|---|---|

## Minimal example (JSON skeleton)
```json
{ "resourceType": "...", ... }
```

## Notes for our server
- <bullet: constraints the local server must enforce / can relax>

## Sources
- raw/satusehat/res-<x>.md
- raw/satusehat/api-<x>.md
```

- [ ] **Step 1: Read the raw SATUSEHAT files for one topic, write the file**

Start with `satusehat-observation.md`: read `docs/reference/raw/satusehat/res-observation.md` and `api-observation.md` in full, then write the file following the template. Record every identifier `system` URI, every fixed `code`, and every "wajib" (mandatory) element exactly as written.

- [ ] **Step 2: Add the INDEX.md line and lint**

```bash
python3 tools/scrape/lint_views.py
```
Expected: `0 problem(s)` (INDEX.md must already contain the new filename).

- [ ] **Step 3: Repeat Steps 1–2 for every remaining SATUSEHAT topic file listed above**

Order: patient → practitioner → organization-location → encounter → condition → procedure → related-person → identifiers-and-master-data → datatypes → rest-api-and-validation → usecase-rawat-jalan → terminology → overview. Run the linter after each file.

- [ ] **Step 4: Commit after every 3–4 files**

```bash
git add docs/reference/claude
git commit -m "docs(reference): add Claude view for SATUSEHAT <topics>

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_015J8WMGo1hde4fa74TJQ7Kn"
```

---

### Task 8: Claude view — FHIR R4 topics

**Files:**
- Create in `docs/reference/claude/`:
  - `fhir-rest-api.md` (from raw `http`, `search`, `operations`, `bundle`, `capabilitystatement`)
  - `fhir-security.md` (from `security`, `secpriv-module`)
  - `fhir-datamodel-basics.md` (from `datatypes`, `references`, `narrative`, `validation`)
  - `fhir-patient-person-relatedperson.md`, `fhir-practitioner-practitionerrole.md`, `fhir-organization-location.md`, `fhir-encounter.md`, `fhir-observation.md` (incl. `observation-vitalsigns`), `fhir-device.md` (incl. `devicemetric`, `devicedefinition`), `fhir-condition.md`, `fhir-procedure.md`
  - `fhir-profiling.md` (from `profiling`, `structuredefinition`, `elementdefinition`, `extensibility`, `conformance-rules`, `conformance-module`, `implementationguide`)
  - `fhir-terminology-resources.md` (from `valueset`, `codesystem`)
  - `fhir-workflow.md` (from `workflow`, `clinicalsummary-module`)
  - `fhir-ci-build-notes.md` (from `fhir-ci/*`; must open with a warning box that this is the R6 CI build and not normative for SATUSEHAT)
- Modify: `docs/reference/claude/INDEX.md`

**Interfaces:**
- Consumes: `docs/reference/raw/fhir-r4/*.md`, `docs/reference/raw/fhir-ci/*.md`.
- Produces: files passing `lint_views.lint`.

Resource file template:
```markdown
# FHIR R4 — <Resource>

Purpose: <1–2 sentences>.

## Elements (summary table)
| Element | Card. | Type | Notes |
|---|---|---|---|

## Search parameters
| Name | Type | Expression |
|---|---|---|

## Invariants / constraints
- <id>: <rule>

## Relationships
- references: ...
- referenced by: ...

## Notes for our server
- ...

## Sources
- raw/fhir-r4/<x>.md
```

Non-resource files (rest-api, security, profiling, …) use freeform headings but keep the same "tables over prose" rule and end with `## Notes for our server` and `## Sources`.

- [ ] **Step 1: Write `fhir-rest-api.md`** from the five raw files. Must include: the interaction table (read/vread/update/patch/delete/create/search/capabilities/transaction/batch/history) with HTTP verb, URL pattern, success status codes, and required headers; the search-parameter type table; Bundle types; what a CapabilityStatement must declare.

- [ ] **Step 2: Lint, then write `fhir-profiling.md`**. Must include: what a profile is vs. base; StructureDefinition key elements (`url`, `kind`, `type`, `baseDefinition`, `derivation`, `snapshot` vs `differential`); ElementDefinition constraints usable in a profile (`min`/`max`, `type`, `fixed[x]`, `pattern[x]`, `binding.strength`, `mustSupport`, `slicing`); how extensions are defined and where they can appear; the four binding strengths; how an ImplementationGuide packages profiles. End with a concrete checklist "Steps to define a new Device profile" derived only from these pages.

- [ ] **Step 3: Write the remaining files in this order**, linting after each: security → datamodel-basics → observation → device → encounter → patient-person-relatedperson → practitioner-practitionerrole → organization-location → condition → procedure → terminology-resources → workflow → ci-build-notes.

- [ ] **Step 4: Commit after every 3–4 files**

```bash
git add docs/reference/claude
git commit -m "docs(reference): add Claude view for FHIR R4 <topics>

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_015J8WMGo1hde4fa74TJQ7Kn"
```

---

### Task 9: Validity review

**Files:**
- Create: `docs/reference/claude/VALIDITY-REVIEW.md`
- Modify: `docs/reference/claude/INDEX.md`

**Interfaces:**
- Consumes: every `docs/reference/claude/satusehat-*.md` and `fhir-*.md`, `docs/reference/raw/FETCH-LOG.md`.
- Produces: the review file with the structure below; Task 10 renders the same findings in prose.

- [ ] **Step 1: Write the systemic-issues header**

```markdown
# Validity review — SATUSEHAT playbook vs FHIR R4

Reviewed: 2026-09-11. Playbook version 7.23. FHIR R4 (4.0.1) from hl7.org/fhir/R4.

## Systemic issues
| # | Issue | Impact on our server |
|---|---|---|
| S1 | `build.fhir.org` is the R6 CI build; SATUSEHAT is R4. Only two orientation pages were captured from it. | Never cite fhir-ci files for element rules. |
| S2 | SATUSEHAT has no `Device` resource page (`fhir/resources/device/` → redirect notice); Device is absent from its resource list. | Device/DeviceMetric profiles must be defined by us from base R4 — no national profile to conform to. |
| S3 | <any other page listed as failed in FETCH-LOG.md> | ... |
```
Add one row per failed id in `FETCH-LOG.md` beyond `res-device`.

- [ ] **Step 2: Write the claim table**

For every SATUSEHAT resource file, list each row of its "Required / constrained elements" table as a claim and check it against the matching `fhir-*.md` element table:
```markdown
## Claim-by-claim
| # | SATUSEHAT claim (file) | FHIR R4 source | Verdict | Note |
|---|---|---|---|---|
| 1 | Patient.identifier with system `https://fhir.kemkes.go.id/id/nik` is required (satusehat-patient.md) | fhir-patient-person-relatedperson.md: identifier 0..* | satusehat-specific constraint | Stricter than base; valid profile constraint. |
```
Verdict vocabulary exactly: `confirmed`, `satusehat-specific constraint`, `conflict`, `unverifiable`. A `conflict` is anything SATUSEHAT states that base R4 forbids (wrong cardinality direction, element that does not exist in R4, type mismatch). `unverifiable` is used when the raw SATUSEHAT text asserts something the captured R4 pages do not cover.

- [ ] **Step 3: Write the summary**

```markdown
## Summary
| Verdict | Count |
|---|---|
| confirmed | n |
| satusehat-specific constraint | n |
| conflict | n |
| unverifiable | n |

## Consequences for sub-project 2 (the server)
- <one bullet per conflict or gap, stating what the server should do>
```

- [ ] **Step 4: Lint and commit**

```bash
python3 tools/scrape/lint_views.py
git add docs/reference/claude
git commit -m "docs(reference): add validity review of SATUSEHAT vs FHIR R4

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_015J8WMGo1hde4fa74TJQ7Kn"
```

---

### Task 10: Human view

**Files:**
- Create in `docs/reference/human/`:
  - `README.md` — reading order, what each file covers, how the three views relate (raw → claude → human), how to re-check freshness.
  - `01-satusehat-overview.md`, `02-satusehat-identifiers.md`, `03-satusehat-resources.md`, `04-satusehat-api-and-validation.md`, `05-satusehat-usecase-and-terminology.md`
  - `10-fhir-basics.md`, `11-fhir-rest-and-search.md`, `12-fhir-security-and-roles.md`, `13-fhir-resources-for-monitoring.md`, `14-fhir-profiling-a-new-device.md`, `15-fhir-workflow.md`
  - `validity-review.md`

**Interfaces:**
- Consumes: every `docs/reference/claude/*.md` (the human view is written from the Claude view, which cites raw).
- Produces: files passing `lint_views.lint` rule 4; content used for the artifact in Task 11.

Rules for each numbered file: opens with "Why this matters for the admin / doctor / patient / device system" (≤ 120 words); explains concepts in prose; includes at least one worked example (a JSON fragment or a request/response pair) taken from the Claude view; uses a Mermaid diagram (```mermaid fence) wherever a flow involves ≥ 3 resources; ends with "Read next: <file>". `12-fhir-security-and-roles.md` must map the three roles to FHIR concepts (Practitioner/PractitionerRole for the doctor, Patient + Person for the patient, no FHIR resource for the administrator — an application-level role — and the security page's guidance on access control and audit).

- [ ] **Step 1: Write `README.md` and files 01–05** (SATUSEHAT), linting after each.

- [ ] **Step 2: Write files 10–15** (FHIR), linting after each.

- [ ] **Step 3: Write `validity-review.md`** — the Task 9 findings rewritten as prose: what was checked, the systemic issues, the conflicts (each in its own paragraph), and what it means for building the server.

- [ ] **Step 4: Run full verification and commit**

```bash
python3 -m pytest tools/scrape/tests -q
python3 tools/scrape/lint_views.py
git add docs/reference/human
git commit -m "docs(reference): add human-readable view

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_015J8WMGo1hde4fa74TJQ7Kn"
```

---

### Task 11: Publish the human view as an artifact and close out

**Files:**
- Create: `tools/scrape/build_human_site.py`
- Create (generated, in scratchpad, not committed): `<scratchpad>/reference-site.html`
- Modify: `docs/reference/human/README.md` (add artifact URL)

**Interfaces:**
- Consumes: `docs/reference/human/*.md`.
- Produces: `build_human_site.build(human_dir: Path) -> str` returning a single self-contained HTML string with a sidebar of file titles and each Markdown file rendered in order; Mermaid fences emitted as `<pre class="mermaid">` blocks (the artifact runtime renders them).

- [ ] **Step 1: Install markdown renderer and write the builder**

```bash
python3 -m pip install --user markdown>=3.5
echo "markdown>=3.5" >> tools/scrape/requirements.txt
```

`tools/scrape/build_human_site.py`:
```python
"""Render docs/reference/human/*.md into one self-contained HTML page for publishing."""
import re
import sys
from pathlib import Path

import markdown

_MERMAID = re.compile(r"```mermaid\n(.*?)```", re.S)
_STYLE = """
:root{--bg:#fafaf8;--fg:#1a1a1a;--muted:#666;--line:#ddd;--accent:#0b5}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--bg:#141414;--fg:#eee;--muted:#aaa;--line:#333}}
:root[data-theme="dark"]{--bg:#141414;--fg:#eee;--muted:#aaa;--line:#333}
body{background:var(--bg);color:var(--fg);font:16px/1.55 system-ui,sans-serif;margin:0;padding-block:24px;padding-inline:16px}
.wrap{display:flex;gap:32px;max-width:1100px;margin:auto}
nav{flex:0 0 220px;position:sticky;top:16px;align-self:flex-start;font-size:14px}
nav a{display:block;color:var(--fg);text-decoration:none;padding:4px 0}
main{flex:1;min-width:0}
section{border-top:1px solid var(--line);padding-top:24px;margin-top:24px}
table{border-collapse:collapse;display:block;overflow-x:auto;max-width:100%}
td,th{border:1px solid var(--line);padding:4px 8px;text-align:left;vertical-align:top}
pre{overflow-x:auto;background:rgba(127,127,127,.12);padding:12px}
code{font-size:.92em}
@media (max-width:760px){.wrap{flex-direction:column}nav{position:static;flex:none}}
"""


def _order(human_dir: Path) -> list[Path]:
    files = sorted(p for p in human_dir.glob("*.md") if p.name != "README.md")
    return [human_dir / "README.md"] + files


def build(human_dir: Path) -> str:
    md = markdown.Markdown(extensions=["tables", "fenced_code", "toc"])
    parts, nav = [], []
    for f in _order(human_dir):
        text = f.read_text(encoding="utf-8")
        text = _MERMAID.sub(lambda m: f'<pre class="mermaid">{m.group(1)}</pre>', text)
        html = md.reset().convert(text)
        title = next((l[2:] for l in text.splitlines() if l.startswith("# ")), f.stem)
        sid = f.stem
        nav.append(f'<a href="#{sid}">{title}</a>')
        parts.append(f'<section id="{sid}">{html}</section>')
    return (f"<title>SATUSEHAT FHIR Reference</title><style>{_STYLE}</style>"
            f'<div class="wrap"><nav>{"".join(nav)}</nav><main>{"".join(parts)}</main></div>')


if __name__ == "__main__":
    human = Path(__file__).resolve().parents[2] / "docs" / "reference" / "human"
    out = Path(sys.argv[1])
    out.write_text(build(human), encoding="utf-8")
    print(f"wrote {out} ({out.stat().st_size} bytes)")
```

- [ ] **Step 2: Build and publish**

```bash
python3 tools/scrape/build_human_site.py "$SCRATCHPAD/reference-site.html"
```
Then call the `Artifact` tool with `file_path` = that file, `favicon` = `"🩺"`, `description` = "Human-readable reference compiled from the SATUSEHAT playbook and FHIR R4 for the local FHIR server project." Record the returned URL.

- [ ] **Step 3: Add the URL to README.md and run the full verification**

Append to `docs/reference/human/README.md`: `Browsable version: <artifact URL>`.
```bash
python3 -m pytest tools/scrape/tests -q
python3 tools/scrape/lint_views.py
python3 tools/scrape/check.py | tail -1
```
Expected: tests pass; `0 problem(s)`; check reports only the known-failed ids as non-`unchanged`.

- [ ] **Step 4: Commit**

```bash
git add tools/scrape/build_human_site.py tools/scrape/requirements.txt docs/reference/human/README.md
git commit -m "docs(reference): publish human view and record artifact URL

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_015J8WMGo1hde4fa74TJQ7Kn"
```

---

## Self-review notes

- Spec §3.1–3.3 page lists → Task 3 `sources.yaml` (ICD-10 lives at `terminology/icd/icd-10/`; SATUSEHAT PractitionerRole only exists under the API catalogue; Device is deliberately kept as an expected failure).
- Spec §4.1 scraper (sources, extractors, scrape, check, tests) → Tasks 1–4. Spec §4.2 raw → Task 5. §4.3 Claude view → Tasks 7–8 (+ linter Task 6). §5 validity review → Task 9. §4.4 human view + artifact → Tasks 10–11. §6 definition of done → Task 11 Step 3.
- Names used consistently: `extractors.extract/PageMissing`, `convert.html_to_markdown/text_hash/render_document/parse_document`, `scrape.load_sources/fetch/build_document/output_path/run/fhir_version_for/SOURCES_PATH/RAW_ROOT`, `check.classify`, `lint_views.lint`.
