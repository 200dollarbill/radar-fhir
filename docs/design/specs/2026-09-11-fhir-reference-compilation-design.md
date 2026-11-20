# FHIR / SATUSEHAT Reference Compilation — Design

**Date:** 2026-09-11
**Status:** approved (sub-project 1 of 2)
**Next:** sub-project 2 — standalone FHIR R4 server with admin / doctor / patient roles and a custom device profile. Designed separately once this reference exists.

## 1. Goal

Build a verified, local knowledge base from two documentation sources so that later
design and implementation of a SATUSEHAT-compatible FHIR server can cite checked facts
rather than memory.

Sources named in `Local/claude.md`:

- SATUSEHAT Platform playbook — `https://satusehat.kemkes.go.id/platform/docs/id/` (Indonesian, FHIR R4-based, static HTML, version 7.23 at time of writing)
- FHIR documentation — `https://build.fhir.org/documentation.html`

## 2. Decisions made during brainstorming

| Question | Decision |
|---|---|
| FHIR spec source | **Curated subset pinned to R4** from `https://hl7.org/fhir/R4/`. `build.fhir.org` is the R6 CI/nightly build and diverges from SATUSEHAT (R4); only its two orientation pages are captured, clearly labelled. |
| Relation to SATUSEHAT platform | **Standalone, SATUSEHAT-compatible.** Follows its profiles, identifiers, terminology; never calls the hosted platform. Registration, API-key, Postman, DICOM, KYC, monitoring docs are excluded. |
| Clinical focus | **Device / vital-sign monitoring**: observations from a measurement device attached to a patient, reviewed by a doctor. Later work defines a profile for a new standalone device, so profiling and Procedure pages are included. |
| Output form | Markdown in the repo, **two hand-authored views** (Claude-readable and human-readable) over a raw evidence layer. SATUSEHAT content kept in Indonesian with English gloss. |
| Method | Script-driven crawl (Python) producing raw Markdown; views authored by Claude from raw. |

## 3. Scope — pages to capture

### 3.1 SATUSEHAT playbook (`…/platform/docs/id/`)

| Section | Pages | Why |
|---|---|---|
| `playbook/` | preface, introduction, service | Platform overview, role terminology |
| `fhir/` | data types page; resource pages for Patient, Practitioner, PractitionerRole, Organization, Location, Encounter, Observation, Device, Condition, Procedure | Profile rules, Indonesian identifier systems (NIK, IHS, etc.) |
| `interoperability/` | general/module overview; the use case nearest to vital-sign monitoring (rawat jalan or equivalent) | Resource flow per visit |
| `terminology/` | LOINC, SNOMED-CT, ICD-10 pages | Codes for vital-sign / JVP-type observations |
| `master-data/` | patient index, facility index, regional data | Identifier and reference formats |
| `api-catalogue/` | prerequisites, validation | Validation rules the local server should mimic |
| `glossary/` | glossary | Term definitions |

Exact URLs are discovered from the site navigation when `sources.yaml` is written; if a listed page does not exist, it is recorded as *missing* in the validity review, not silently dropped.

### 3.2 FHIR R4 (`https://hl7.org/fhir/R4/`)

| Group | Pages |
|---|---|
| Server behaviour | `http.html`, `search.html`, `operations.html`, `bundle.html`, `capabilitystatement.html` |
| Security | `security.html`, `secpriv-module.html` |
| Data model basics | `datatypes.html`, `references.html`, `narrative.html`, `validation.html` |
| Resources (roles + monitoring) | `patient`, `practitioner`, `practitionerrole`, `organization`, `location`, `encounter`, `observation`, `observation-vitalsigns`, `device`, `devicemetric`, `devicedefinition`, `condition`, `person`, `relatedperson`, `procedure` |
| Profiling | `profiling.html`, `structuredefinition.html`, `elementdefinition.html`, `extensibility.html`, `conformance-rules.html`, `conformance-module.html`, `implementationguide.html`, `valueset.html`, `codesystem.html` |
| Workflow | `workflow.html`, `clinicalsummary-module.html` |

### 3.3 FHIR CI build (`https://build.fhir.org/`)

`documentation.html`, `overview-dev.html` only. Front-matter marks them `fhir_version: R6-ci`.

## 4. Components

### 4.1 Scraper — `tools/scrape/`

Python 3; deps: `requests`, `beautifulsoup4`, `markdownify`, `pyyaml`.

- `sources.yaml` — list of `{id, group, url, title}`. `group ∈ {satusehat, fhir-r4, fhir-ci}`. Adding a page = adding one entry.
- `extractors.py` — per-site functions that take HTML and return the main-content element with nav, footer, scripts, and sidebars removed. One for SATUSEHAT, one for hl7.org/build.fhir.org (same layout).
- `scrape.py` — for every entry: fetch (1 req/s, 3 retries, project `User-Agent`), extract, convert to Markdown, write `docs/reference/raw/<group>/<id>.md` with YAML front-matter: `id, title, source_url, group, fhir_version, fetched_at, sha256` (hash of extracted text). A 404 or empty extraction is an error printed at the end and the file is not written.
- `check.py` — re-fetches every entry and reports `unchanged / changed / failed` by comparing hashes. Used to detect stale reference later.
- Tests (`tools/scrape/tests/`): one test per extractor using a saved HTML fixture; one network smoke test on two real pages, skipped when offline.

### 4.2 Raw layer — `docs/reference/raw/`

Scraper output only. Never hand-edited. Serves as evidence for every claim in the views.

### 4.3 Claude view — `docs/reference/claude/`

- `INDEX.md` — one line per file: filename, topic, and a "load this when …" hint.
- `satusehat-*.md`, `fhir-*.md` — one file per topic. Rules: tables over prose; each resource file lists required fields, cardinality, SATUSEHAT-specific constraints, identifier systems, and a minimal example JSON skeleton; every file ends with a `Sources:` list of `raw/` paths; Indonesian terms kept with an English gloss on first use; target ≤ 400 lines per file.
- `VALIDITY-REVIEW.md` — see §5.

### 4.4 Human view — `docs/reference/human/`

- `README.md` — guided reading order.
- Numbered narrative files (`01-satusehat-overview.md`, … `10-fhir-basics.md`, …) explaining why each topic matters for the admin / doctor / patient / device model, with cross-links and diagrams where a flow needs one.
- `validity-review.md` — same findings as the Claude version, in prose.
- Published as a browsable HTML artifact once complete.

## 5. Validity review

One table row per SATUSEHAT claim that affects the server:

`claim → FHIR R4 page that confirms or contradicts → verdict → note`

Verdicts: `confirmed`, `satusehat-specific constraint` (stricter than base R4 but valid), `conflict`, `unverifiable`.

Header section for systemic issues, at minimum:
- build.fhir.org is R6 CI; SATUSEHAT is R4 — differences noted where captured.
- SATUSEHAT playbook version at fetch time.
- Pages listed in §3 that were missing, moved, or failed to fetch.

## 6. Repository and process

- `git init` at project root; `.gitignore` covers `.goutputstream-*`, Python caches, `.venv/`.
- Commit order: spec → scraper + tests → raw layer → Claude view → human view → validity review.
- Definition of done: every `sources.yaml` entry fetched or listed as failed with reason; both views exist for every topic; `VALIDITY-REVIEW.md` complete; `check.py` reports all `unchanged` immediately after the final scrape; human view published as an artifact.

## 7. Out of scope

- Translating the whole playbook.
- Scraping video, PDF, or Postman content.
- Any server code, database, or UI — that is sub-project 2.
- Calling the SATUSEHAT sandbox or production API.
