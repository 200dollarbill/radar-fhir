# Project brief

Read this first. It tells you what exists, what we are building, and how work is done here.

## The goal

Build a **standalone, SATUSEHAT-compatible FHIR R4 server** that serves three roles:

1. **Administrator** — sets up facilities, practitioners, devices, accounts.
2. **Doctor / assigned caregiver** — records and reviews clinical data for their patients.
3. **Patient** — the receiving end of treatment, able to see their own record.

Clinical focus: **device-sourced vital-sign Observations** — measurements from a
monitoring device attached to a patient, reviewed by the doctor. (Origin: Pra-TA
work on contactless JVP / carotid pulse measurement by radar; papers in
`PraTAPapers/`.) A later goal is a **FHIR profile for a new standalone
measurement device**.

"SATUSEHAT-compatible" means: follow the Indonesian national platform's profiles,
identifier systems and terminology, but **run entirely locally**. We never call
the hosted platform. Registration, API keys, Postman, DICOM, KYC and the
monitoring dashboard are out of scope.

## Status

- **Sub-project 1 — reference compilation: DONE** (merged to `master`).
- **Sub-project 2 — the server: NOT STARTED.** Its brainstorm was opened and
  interrupted; nothing is designed yet. Start with `superpowers:brainstorming`.

## What is already here

```
docs/reference/
├── raw/       93 scraped pages + FETCH-LOG.md   — primary evidence, never hand-edit
├── claude/    31 dense files + INDEX.md         — what YOU load; facts live here
└── human/     13 prose guides + README.md       — for the project owner
tools/scrape/  scraper, staleness check, view linter, site builder, 34 tests
docs/superpowers/{specs,plans}/                  — spec + implementation plan of sub-project 1
```

**Start at `docs/reference/claude/INDEX.md`.** Every line says what a file covers
and when to load it. Load the two or three files a task needs — never the whole
directory.

Every `claude/*.md` ends with `## Sources` listing the `raw/*.md` files it came
from. **Trace, don't guess:** claude → its Sources → raw. A fact that appears
only in `human/` is not evidence.

`Local/claude.md` names the two upstream sites. They are already scraped — do not
re-scrape them to answer a question. Note that `build.fhir.org` is the **R6 CI
build**; SATUSEHAT is **R4**, and R4 (`hl7.org/fhir/R4/`) is what binds us.

## Findings that constrain the server

From `docs/reference/claude/VALIDITY-REVIEW.md` (310 claims checked: 172
confirmed, 108 SATUSEHAT-specific tightenings, 9 conflicts with R4, 21
unverifiable; 29 systemic issues S1–S29). Read it before designing anything that
enforces a rule. The ones that change design decisions:

- **No SATUSEHAT Device profile, and no PractitionerRole profile page** (S2). The
  device profile must be derived from base R4 — see the 13-step checklist at the
  end of `claude/fhir-profiling.md`.
- **Media types conflict.** SATUSEHAT mandates `Content-Type: application/json`;
  R4 says clients and servers SHALL use `application/fhir+json`
  (`application/json-patch+json` for PATCH). Accept both on input, emit
  `application/fhir+json`.
- **Blood pressure shape differs.** SATUSEHAT posts standalone systolic (8480-6)
  and diastolic (8462-4) Observations; R4's Vital Signs profile uses one 85354-9
  panel with components. Store the panel, derive the two on export.
- **`Encounter.location` typed as a plain Reference** in the playbook; in R4 it is
  a BackboneElement with `location.location` 1..1.
- **Documented types/resources that do not exist in R4**: `CodeableReference`,
  `RatioRange`, `BillingStatus`, `ChargeItemResponse`.
- **No SpO₂ LOINC code anywhere in the SATUSEHAT corpus** — if the device
  measures it, we choose the code ourselves and say so.
- The playbook contradicts itself in several places (identifier systems, earliest
  allowed dates, mandatory `Observation.performer`). Those are recorded as
  systemic issues, not resolved. **Do not silently pick a side** — decide
  explicitly and write down why.

## How work is done here

**Process is not optional.** The `superpowers` skills drive it:

- Any creative work — a feature, a component, a behaviour change — starts with
  `superpowers:brainstorming`. Architectural work then goes
  brainstorm → spec (`docs/superpowers/specs/`) → `superpowers:writing-plans` →
  `superpowers:subagent-driven-development`.
- Bugs start with `superpowers:systematic-debugging`. Implementation is TDD
  (`superpowers:test-driven-development`): failing test, watch it fail, minimal
  code, watch it pass, commit.
- Never claim something works without running it
  (`superpowers:verification-before-completion`).

**Execution techniques that worked in sub-project 1** — reuse them:

- **Split by input size, not by topic.** A task whose raw input ran to tens of
  thousands of lines was split into 2–3 dispatches; each stayed accurate. One big
  dispatch does not.
- **Review for fidelity, not just for style.** Every authored file was checked
  row-by-row against the raw text by a fresh reviewer. This caught a systematic
  bug — every search-parameter table had silently dropped its first row — that no
  amount of reading the file itself would have found. When output is derived from
  a source, the review must re-derive a sample from that source.
- **Hand artifacts over as files.** Diffs, briefs and reports go in files passed
  by path; never paste a large diff into a prompt.
- **Record contradictions verbatim; resolve them in a ruling.** Every deviation
  from a plan was written down with its cost if wrong.
- **Cheap model for transcription, capable model for judgement.** Always name the
  model when dispatching.

## Commands

```bash
python3 -m pytest tools/scrape/tests -q     # 34 tests
python3 tools/scrape/lint_views.py          # reference-view consistency; must print "0 problem(s)"
python3 tools/scrape/check.py               # re-fetch both sites, detect upstream drift (~3 min, network)
python3 tools/scrape/scrape.py --only <id>  # re-fetch one page from tools/scrape/sources.yaml
```

`check.py` exits 0 when everything still matches. `res-device` and
`res-practitioner-role` report `expected-missing` — documented gaps, not errors.
Anything reported `changed` means the upstream docs moved: re-scrape that page,
then re-check the `claude/` file built from it.

## Conventions

- Never hand-edit `docs/reference/raw/` — it changes only through `scrape.py`.
- Keep `claude/*.md` files ≤ 400 lines, tables over prose, `## Sources` at the end,
  and add a line to `INDEX.md` for every new file (the linter enforces this).
- Indonesian terms stay in Indonesian with an English gloss on first use
  (*wajib* = mandatory).
- Commit messages end with the attribution lines the session gives you.
- The human view is published at
  https://claude.ai/code/artifact/cc73fa7d-27a7-4454-bf84-8b20f8a0f843 — rebuild
  with `python3 tools/scrape/build_human_site.py <out.html>` and republish to the
  same URL if `docs/reference/human/` changes.
