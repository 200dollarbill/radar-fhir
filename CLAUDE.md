# Project brief

Read this first. It tells you what exists, what we are building, and how work is done here.

## The goal

Final-year thesis (tugas akhir, written in Indonesian) with a Biomedical Engineering
RADAR group. Working title:

*Pengembangan Sistem Pendukung Keputusan Klinis Berbasis Interoperabilitas Data
Rekam Medis Elektronik dan Pengukuran Kardiovaskular RADAR*

**Final objective:** a working website that takes in RME (electronic medical record),
RADAR JVP and 12-lead ECG data and displays it visually and efficiently in one view
for the doctor. The integrated display is the decision support; the doctor decides.

- Rule-based flags are not required, and are optional only if time remains.
- Never frame output as diagnosis, prediction or a validated risk score.
- Call the RADAR device a *pengukuran* (measurement) device, not "monitoring".
- FHIR and SATUSEHAT are the interoperability bridge, not the headline contribution.
- The contribution is the system, not the RADAR device or an interpretation algorithm.

**Next phase:** literature deepening, JVP signal link to cardiovascular health first
(`docs/.superpowers/specs/2026-11-03-literature-deepening-design.md`; results in
`docs/papers/search/`). The website architecture is not designed yet and gets its own
brainstorm after that.

**Thesis work starts at `proposal_CLAUDE.md`**: direction history, scope, urgency
argument, fix list, open questions. The earlier FHIR-profile direction is superseded;
do not reopen it.

## Status

- **Reference compilation: done.** See below.
- **FHIR R4 server: walking skeleton implemented, and the base the website builds on.**
  Proves admin-provision → doctor-opened Encounter → device heart-rate Observation →
  doctor read → patient own-record, with local JWT roles, device tokens,
  SATUSEHAT-shaped OperationOutcome validation and compile-gated firmware. Spec:
  `docs/.superpowers/specs/2026-09-29-fhir-r4-server-walking-skeleton-design.md`.
- **Public exposure and request history:** spec written, not implemented
  (`docs/.superpowers/specs/2026-10-08-public-exposure-request-history-design.md`).
- **Firmware heart-rate values are placeholders**, not radar-derived measurements.
- The old roadmap's device profile is no longer the headline goal. Add a profile only
  if the website design needs one.

"SATUSEHAT-compatible" means following the Indonesian national platform's profiles,
identifier systems and terminology while running entirely locally. We never call the
hosted platform. Registration, API keys, Postman, DICOM and KYC are out of scope.

## Repo map

```
proposal_CLAUDE.md              thesis handoff
docs/proposal_md/               proposal.md, citations, source and claim catalogue
docs/proposal_guide/            how to write the proposal (style rules)
docs/presentation/ets/          sidang outline, fishbone.md
docs/notul/                     consultation notes
docs/papers/                    papers by subject (PDF + md/); search/ = literature results
docs/reference/raw/             93 scraped pages + FETCH-LOG.md: evidence, never hand-edit
docs/reference/claude/          31 dense FHIR/SATUSEHAT files + INDEX.md: what YOU load
docs/reference/human/           prose guides for the project owner
docs/.superpowers/{specs,plans} specs and implementation plans
fhir_server/, tests/            server and its tests (run guide: fhir_server/README.md)
device_client/, arduino/        Python device client, firmware
.tools/scrape/                  scraper, staleness check, view linter, 34 tests
```

**For FHIR or SATUSEHAT facts start at `docs/reference/claude/INDEX.md`.** Load the two
or three files a task needs. Every `claude/*.md` ends with `## Sources`. **Trace, don't
guess:** claude → its Sources → raw. A fact only in `human/` is not evidence.
`build.fhir.org` is the R6 CI build; SATUSEHAT is R4, and `hl7.org/fhir/R4/` binds us.

## Findings that constrain the server

From `docs/reference/claude/VALIDITY-REVIEW.md`. Read it before designing anything
that enforces a rule.

- **No SATUSEHAT Device or PractitionerRole profile page** (S2).
- **Media types conflict.** Accept `application/json` and `application/fhir+json` on
  input; emit `application/fhir+json`.
- **Blood pressure differs.** SATUSEHAT posts standalone 8480-6 and 8462-4; R4 uses an
  85354-9 panel. Store the panel, derive the two on export.
- **`Encounter.location`** is a BackboneElement in R4, with `location.location` 1..1.
- **Not in R4:** `CodeableReference`, `RatioRange`, `BillingStatus`, `ChargeItemResponse`.
- **No SpO₂ LOINC code in the SATUSEHAT corpus.** If needed, choose one and say so.
- The playbook contradicts itself (identifier systems, earliest dates, mandatory
  `Observation.performer`). **Do not silently pick a side**: decide and write down why.

## How work is done here

Any creative work starts with brainstorming, then spec → plan → implementation. Bugs
start with systematic debugging. Implementation is TDD. Never claim something works
without running it.

- **Split by input size, not by topic.** Large-input tasks go in 2–3 dispatches.
- **Review for fidelity.** When output derives from a source, the review re-derives a
  sample from that source.
- **Hand artifacts over as files**, passed by path.
- **Record contradictions verbatim; resolve them in a ruling.**
- **Cheap model for transcription, capable model for judgement.** Name the model.

## Commands

```bash
.venv/bin/python -m pytest tests -q          # server tests
python3 -m pytest .tools/scrape/tests -q     # 34 tests
python3 .tools/scrape/lint_views.py          # must print "0 problem(s)"
python3 .tools/scrape/check.py               # detect upstream doc drift (~3 min, network)
```

## Conventions

- Never hand-edit `docs/reference/raw/`. Keep `claude/*.md` ≤ 400 lines with `## Sources`
  and an `INDEX.md` line (the linter enforces this).
- Indonesian terms stay in Indonesian with an English gloss on first use.
- Commit messages end with the attribution lines the session gives you.
