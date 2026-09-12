# Human view — reading guide

This is the human-readable layer of the reference compilation for the SATUSEHAT-compatible FHIR server project. It exists so the project owner (a student) can read connected prose instead of dense tables, while still being able to trace every sentence back to a primary source.

## The three views, and how they relate

The reference lives in `docs/reference/` as three layers, each built from the one before:

1. **`raw/`** — scraped copies of the actual SATUSEHAT playbook pages and the FHIR R4 specification pages. This is the primary source. Nothing here is edited or interpreted; it is exactly what the pages said when scraped.
2. **`claude/`** — a dense, fact-checked distillation of `raw/`, one file per topic, written by Claude and cross-checked against the raw pages during compilation. Every `claude/*.md` file ends with a `## Sources` section listing the exact `raw/*.md` files it was built from. This is the layer you trust for facts, and the layer this human view is written from.
3. **`human/`** (this directory) — the same material rewritten as readable prose for a person designing the server, organised by "why does this matter for the admin / doctor / patient / device system" rather than by playbook section. It adds no facts beyond what `claude/` states.

**Rule of thumb for tracing a fact:** if something in a `human/*.md` file looks surprising or you want the primary evidence, open the matching `claude/*.md` file, then follow its `## Sources` list into `raw/`. Never trust a fact that only appears in `human/` — it should always be traceable to a `claude/` file and from there to `raw/`.

There is also `claude/VALIDITY-REVIEW.md` and `claude/VALIDITY-REVIEW-claims.md`, a systematic check of playbook/spec claims against the raw pages (confirmed / SATUSEHAT-specific / conflict / unverifiable). Its findings are rewritten as prose in `validity-review.md` in this directory.

## Reading order

The files are grouped by subject: SATUSEHAT first (files 01–05, what the Indonesian national platform requires), then FHIR R4 fundamentals (files 10–15, the base standard SATUSEHAT profiles on top of), then the validity review. Read them in numeric order the first time through; afterwards use them as topic references.

| # | File | Covers |
|---|---|---|
| 01 | `01-satusehat-overview.md` | What SATUSEHAT is, its services and master indexes, the 46 resources it lists, onboarding order, glossary of Indonesian terms |
| 02 | `02-satusehat-identifiers.md` | NIK / IHS number / MPI identity system, patient registration rules for the three patient kinds, facility (MSI) and region lookups |
| 03 | `03-satusehat-resources.md` | The eight SATUSEHAT clinical/master resources one by one: Patient, Practitioner, RelatedPerson, Organization/Location, Encounter, Observation, Condition, Procedure |
| 04 | `04-satusehat-api-and-validation.md` | The REST API shape, auth, and how the validation pipeline reports errors |
| 05 | `05-satusehat-usecase-and-terminology.md` | The rawat jalan (outpatient) posting order end to end, and which code system (ICD-10, LOINC, SNOMED CT, KFA…) is mandated for what |
| 10 | `10-fhir-basics.md` | FHIR R4 data-model fundamentals: primitive/complex types, References, Resource anatomy |
| 11 | `11-fhir-rest-and-search.md` | FHIR R4 REST interactions, search parameters, Bundle, CapabilityStatement |
| 12 | `12-fhir-security-and-roles.md` | FHIR R4 security guidance mapped onto our three roles: administrator, doctor, patient |
| 13 | `13-fhir-resources-for-monitoring.md` | Observation, Encounter, Condition, Procedure as FHIR R4 defines them (compared against the SATUSEHAT profile) |
| 14 | `14-fhir-profiling-a-new-device.md` | How to define a new Device profile/extension the FHIR R4 way |
| 15 | `15-fhir-workflow.md` | FHIR R4 workflow patterns — how Observation/Procedure/Condition/Encounter reference each other |
| — | `validity-review.md` | What was checked, the systemic issues, the conflicts found, and what that means for building the server |

## Re-checking freshness

The raw pages can go stale (playbook revisions, spec updates). To check whether the scraped copies in `raw/` still match what is currently published, run:

```bash
python3 tools/scrape/check.py
```

from the repository root. It exits `0` when every source reports `unchanged` or `expected-missing`, and `1` otherwise. Two ids (`res-device`, `res-practitioner-role`) are expected to report `expected-missing` on every run — SATUSEHAT has no profile page for either resource (see `validity-review.md`, S2) — so seeing those two by name is not drift. If any other id reports `changed` or `failed`, the `claude/` and `human/` files built from that page should be re-verified against the new raw content before being trusted again.

To verify the reference views themselves are internally consistent (every `claude/*.md` has sources that exist, every `human/*.md` is indexed here), run:

```bash
python3 tools/scrape/lint_views.py
```

Read next: `01-satusehat-overview.md`

Browsable version: https://claude.ai/code/artifact/cc73fa7d-27a7-4454-bf84-8b20f8a0f843
