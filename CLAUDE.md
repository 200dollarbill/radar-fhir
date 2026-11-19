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

**Next session: start with `docs/handover/2026-11-18-handover.md`.** Next task: proposal
development (Chapter III, progress, presentation), spec
`docs/design/specs/2026-11-18-proposal-development-design.md`, awaiting the owner's
approval. Literature deepening (`docs/design/specs/2026-11-03-literature-deepening-design.md`;
results in `docs/papers/search/`) has produced L1 to L8. The website architecture is not designed yet and gets its own
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
  `docs/design/specs/2026-09-29-fhir-r4-server-walking-skeleton-design.md`.
- **Public exposure and request history:** spec written, not implemented
  (`docs/design/specs/2026-10-08-public-exposure-request-history-design.md`).
- **Raw capture receiver: prototype.** A browser page at `/capture/` posts raw radar
  chunks to the server. Passed in real Chrome with the simulator and with real bytes
  from an AtomS3R (unwired pins, so pin noise, not radar signal), through a stand-in
  port. Chrome's own Web Serial port layer is not verified because the picker needs a
  click. Run guide: `docs/RUN-GUIDE.md`.
- **Firmware (`firmware/radar_json/`) runs on the AtomS3R** at 100 Hz, timer-driven, and
  reads radar I/Q on **G7 (I) and G8 (Q)**. The pins were given by the owner; the I/Q
  order is assumed. Flashed and checked on 2026-11-16 (`READY ... i_pin=7 q_pin=8`).
  The owner reports the radar wired as of 2026-11-18; captures before that are pin noise.
  Idle read: both channels near 1.53 V, about 1 mV spread. Recordings on 2026-11-18 (85 and
  4 chunks) spread 90 to 170 mV and show clean I/Q arcs in some windows, so the radar
  responds to movement; not yet reviewed as physiology (handover §5).
- **Firmware heart-rate values are placeholders**, not radar-derived measurements.
- **Display processing: `hybrid` chosen (2026-11-18), unsupervised, owner to confirm.**
  `/capture/` now shows a movement waveform (0.5 to 10 Hz, relative units) and an I/Q
  plane; `/capture/review.html` compares six methods on a saved CSV or Bundle. Chosen
  by a fixed rule on synthetic ground truth; the real RABITS capture only checks the
  guard. Display only, never a measurement. Spec:
  `docs/design/specs/2026-11-18-radar-display-processing-design.md`; results:
  `docs/eval/2026-11-18-radar-display-processing.md`.
- **Board sessions and site navigation (2026-11-18, implemented).** The board answers
  `BOARD?` with its chip ID and a key it made itself (sent in clear on request: known
  weakness, fix = challenge and response). Admins register boards and create test
  patients; admins or doctors open sessions on `/capture/sessions.html`; the capture page
  gets the plugged-in board's session (preview, then Record). All pages share a top bar.
  Flashed 2026-11-18: the AtomS3R answers `BOARD?` (ID `CCBA97030AD4`). Spec:
  `docs/design/specs/2026-11-18-board-sessions-and-navigation-design.md`.
- **Repo tidy-up and Cloudflare hosting (2026-11-19): implemented.** Folders renamed by
  role, top-level README and Makefile. The site is live at `https://prata.haifa.workers.dev`
  while the laptop runs `make server` and `make tunnel`: a free Cloudflare Worker serves the
  pages and forwards API calls through Workers VPC (tunnel `prata-laptop`). Accounts are
  created on the laptop (`add-account`; guides in `docs/accounts/`). Live checks 1 and 3 to
  7 passed; check 2 (login rate limit) is partial: slow guessing is not stopped, fix is the
  owner's call. Not yet done: the owner's real-board check on the hosted address. Results:
  end of `docs/design/specs/2026-11-19-tidy-up-and-cloudflare-hosting-design.md`.
- The old roadmap's device profile is no longer the headline goal. Add a profile only
  if the website design needs one.

"SATUSEHAT-compatible" means following the Indonesian national platform's profiles,
identifier systems and terminology. Data is stored only on the owner's laptop; the public
site is a Cloudflare Worker that forwards requests to it. We never call the hosted
platform. Registration, API keys, Postman, DICOM and KYC are out of scope.

## Repo map

`README.md` is the human entry point (folder map, `make` commands, old-name table).

```
README.md, Makefile             start here; `make` lists every command
proposal_CLAUDE.md              thesis handoff
docs/proposal_md/               proposal.md, citations, source and claim catalogue
docs/proposal_guide/            how to write the proposal (style rules)
docs/presentation/ets/          sidang outline, fishbone.md
docs/notul/                     consultation notes
docs/papers/                    papers by subject (PDF + md/); search/ = literature results
docs/reference/raw/             93 scraped pages + FETCH-LOG.md: evidence, never hand-edit
docs/reference/claude/          31 dense FHIR/SATUSEHAT files + INDEX.md: what YOU load
docs/reference/human/           prose guides for the project owner
docs/design/{specs,plans,reports} specs, implementation plans, build reports
docs/RUN-GUIDE.md               owner's walkthrough: server, board, website, hosted site
docs/HOW-IT-WORKS.md            the whole flow, radar to database, roles, failures
docs/accounts/                  account setup guides (admin, doctor, patient; placeholders)
fhir_server/, tests/            server and its tests (internals: fhir_server/README.md)
device_client/, firmware/       Python device client, board firmware (firmware/radar_json/)
website/                        Sessions, Capture, Review pages (plain JS), Node tests
hosting/                        Cloudflare Worker: build.mjs, src/worker.js, wrangler.jsonc, tests
website/src/dsp/, eval/         display processing (demodulation, filters) and its evaluation
docs/eval/                      generated evaluation reports (do not hand-edit)
tools/scrape/                   scraper, staleness check, view linter, 34 tests
data/                           sample CSVs and data/fhir_server.db (the real database, gitignored)
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

Any creative work starts with brainstorming, then spec → plan → implementation.
Specs go in `docs/design/specs/`, plans in `docs/design/plans/`. Bugs
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
make setup       # .venv + pip install -e .
make server      # loads .env/prata.env, serves http://127.0.0.1:8000 (website at /capture/)
make test        # all of: .venv/bin/python -m pytest tests -q
                 #         node --test "website/tests/*.test.js"
                 #         node --test "hosting/tests/*.test.js"
                 #         python3 -m pytest tools/scrape/tests -q   (34 tests)
                 #         python3 tools/scrape/lint_views.py        (must print "0 problem(s)")
make eval        # node website/eval/run.mjs: rescore display methods, rewrites docs/eval/
make firmware    # arduino-cli compile --fqbn "$FQBN" firmware/radar_json
make flash       # compile, then arduino-cli upload -p /dev/ttyACM0 (override: PORT=...)
                 # FQBN = m5stack:esp32:m5stack_atoms3r:USBMode=hwcdc,CDCOnBoot=cdc
make tunnel      # TUNNEL_TOKEN from .env/prata.env → cloudflared tunnel run (hosted site)
make deploy      # hosting/: node build.mjs && wrangler deploy → https://prata.haifa.workers.dev
python3 tools/scrape/check.py   # detect upstream doc drift (~3 min, network)

# accounts (laptop only; password asked twice, or --from-env VAR)
.venv/bin/python -m fhir_server add-account --role {admin,doctor,patient} --username U [--name N] [--ref Patient/<id>]
.venv/bin/python -m fhir_server list-accounts
.venv/bin/python -m fhir_server disable-account --username U
```

The real database is `data/fhir_server.db`. Never run `seed --reset` on it.

## Conventions

- Never hand-edit `docs/reference/raw/`. Keep `claude/*.md` ≤ 400 lines with `## Sources`
  and an `INDEX.md` line (the linter enforces this).
- Indonesian terms stay in Indonesian with an English gloss on first use.
- **Claude may stage and commit its own work** whenever a unit of work is done (owner,
  2026-11-19; replaces "do not commit" in `Local/claude.md` and the 2026-11-18 handover).
  Stage only the files that work touched. **Never push without asking**: the GitHub repo
  is public.
- Commit messages end with the attribution lines the session gives you.
