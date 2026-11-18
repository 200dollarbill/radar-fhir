# Proposal development: Chapter III, progress and presentation materials

Date: 2026-11-18. Status: spec written for the owner's review; nothing drafted yet.

## Why

The draft `docs/proposal_md/proposal.md` (2026-10-26) has Chapters I and II, an empty
2.6 and no Chapter III. Since then the system has moved from plan to working
prototype. Examples: a FHIR R4 server with SATUSEHAT-style validation, raw capture
from the board, board identity and sessions, three web pages, and an evaluated
display method. The presentation outline still says "no system results yet" (slide 8
of `docs/presentation/ets/outline_sidang_proposal_v2.md`). The owner asked for the
proposal and the materials to follow the development, including progress and methods.

## Goals

- Chapter III (*Metodologi*) written into `proposal.md`, describing the method as built
  and as planned, with an honest progress statement.
- A notes file for the student: claims and their sources, placeholders, suggested
  (not applied) edits to Chapters I and II, open questions.
- Presentation materials updated to show progress and methods.

## Non-goals

- Editing Chapters I and II, or filling 2.6. The project rule is "record only: the
  student edits the draft" (`proposal_CLAUDE.md` §6); 2.6 is marked `[diisi mahasiswa]`.
- New literature claims. Papers the student has not read do not enter the proposal.
- Word formatting, figures as image files, a slide deck file. Each can follow on request.
- New system work.

## Anti-goals (a failure even if the text reads well)

- Presenting planned parts (RME import, 12-lead ECG intake, the integrated doctor view)
  as done.
- Presenting display processing as a contribution, a measurement or an interpretation
  algorithm. Calling the RADAR device "monitoring". Any diagnosis or risk framing.
- A number with no traceable source.
- Reporting simulated or pin-noise data as radar signal.

## Sources of truth

| Topic | Source |
|---|---|
| Style, citation and output rules | `docs/proposal_guide/panduan_proposal.md` §1 and §7 |
| Scope, framing, fix list | `proposal_CLAUDE.md`, `CLAUDE.md` |
| Current text and reference numbers [1] to [41] | `docs/proposal_md/proposal.md` |
| What each reference supports | `docs/proposal_md/daftar_sumber_dan_klaim.md`, `citations.md` |
| Server, roles, validation | `docs/.superpowers/specs/2026-09-29-fhir-r4-server-walking-skeleton-design.md`, `fhir_server/README.md` |
| Capture, chunks, Observation shape | `docs/.superpowers/specs/2026-11-04-capture-receiver-prototype-design.md` |
| Display processing and its results | `docs/.superpowers/specs/2026-11-18-radar-display-processing-design.md`, `docs/eval/2026-11-18-radar-display-processing.md` |
| Board identity, sessions, navigation, known weakness | `docs/.superpowers/specs/2026-11-18-board-sessions-and-navigation-design.md` |
| How it runs, what is stored | `docs/RUN-GUIDE.md` |
| Test counts | A fresh run of the three suites on the day of writing (not numbers copied from chat) |
| FHIR and SATUSEHAT facts | `docs/reference/claude/` via `INDEX.md` (trace to raw, as `CLAUDE.md` requires) |

## Rulings

| # | Ruling | Why |
|---|---|---|
| P1 | Chapter III goes into `proposal.md` as a new section after 2.7 and before the reference list. Chapters I and II stay byte-identical | It is empty and the owner asked for it; the rest is the student's text |
| P2 | Suggested fixes to Chapters I and II go in the notes file, quoted with the proposed wording | "Record only" rule. Known conflicts: 1.4 says "diagnosa"; 1.4 and 2.7 promise patient save-and-send, which is not built or committed; 2.7 says the ECG "memvalidasi" where 1.3 says "titik acuan" |
| P3 | Indonesian, flowing paragraphs, no hyphens or dashes, short and human, per the guide. At most two tables in Chapter III: progress per component (3.9) and the display method scores (3.6) | The guide allows tables only where many items are compared |
| P4 | Code identifiers with hyphens (`raw-capture`, `in-progress`) are described in words, not quoted | The no-hyphen rule; the reader needs the meaning, not the string |
| P5 | Every number in Chapter III comes from the project's own evidence (eval report, test runs, specs) or an existing reference, and is listed in the notes' claims table with its source path or reference number | The guide forbids invented numbers |
| P6 | Only references [1] to [41] are cited by number. Anything else (FHIR R4 specification, SATUSEHAT playbook, Web Serial, demodulation literature) is a `[cite: ...]` placeholder, with a suggested IEEE entry in the notes for the student to approve | The student reads sources before they enter the proposal |
| P7 | Before citing [10] or [11] for a method detail (the 0.5 to 10 Hz band, arctangent demodulation, 0.7 to 3 Hz), confirm the match against `docs/papers/RADAR/md/` and the catalogue. Unconfirmed matches become placeholders | The repo stores the papers under P-numbers, not reference numbers; the match is assumed, not checked |
| P8 | Progress is stated with date and evidence, built and tested versus planned, including what is not verified (I/Q order assumed; radar wired 2026-11-18; first readings near the ADC floor; no recording of a person yet) | Anti-goals |
| P9 | Presentation: a new `outline_sidang_proposal_v3.md`; v2 stays as it is. Slide 8 becomes two slides, *Metodologi dan arsitektur* and *Progres dan rencana*, within the same 5:00 (time taken from slides 1 and 2). The answers-to-examiners and avoid lists get the new facts | Default while O1 is open. The same two slides form the core of a progress talk if that is the occasion |
| P10 | Figures appear as placeholders, *[Gambar 3.x: …]*, with a one-paragraph brief each in the notes | Image files are a follow-up (non-goal) |

## Chapter III structure

Each subsection lists what it says and where the facts come from. Paragraphs, not
bullets, in the written text.

| Section | Content | Main sources |
|---|---|---|
| 3.1 Alur Penelitian | Study steps: literature, requirements, design, incremental build, testing, evaluation, writing. [Gambar 3.1: alur penelitian] | `proposal_CLAUDE.md`, specs' dates |
| 3.2 Arsitektur Sistem | Board, capture page, FHIR R4 server, SQLite store; Sessions and Review pages; the planned integrated doctor view fed by RME and ECG. Built versus planned stated plainly. [Gambar 3.2: arsitektur] | `RUN-GUIDE.md` picture, board-sessions spec |
| 3.3 Perangkat dan Akuisisi Data | 24 GHz radar module on an AtomS3R, 12-bit ADC at 3.3 V, 100 samples per second, I and Q plus IMU, one text record per sample, timing that shows lost time as gaps, chunks of up to 10 s, upload retries that never duplicate. The I/Q pin order is an assumption | firmware README, capture spec |
| 3.4 Interoperabilitas dan Pemodelan Data | FHIR R4, SATUSEHAT-compatible locally with no connection to the national platform; the resources used (Patient, Practitioner, Organization, Location, Encounter, Device, Observation); raw signal as Observation with sampled data; validation answering with OperationOutcome; local code system because no standard code for radar I/Q was found (a limitation). Plan: ECG mapping following [20], RME mapping, and the syntactic versus semantic caution of [23] | walking-skeleton and capture specs, `docs/reference/claude/` |
| 3.5 Manajemen Sesi, Peran, dan Keamanan | Roles (admin, doctor, patient, device); board identity from the chip ID and a key it makes itself; a session is a visit plus one assigned board; uploads allowed only into an open session; test patients only. The known weakness and the planned challenge and response | board-sessions spec |
| 3.6 Pemrosesan Tampilan Sinyal | Display processing only. Six candidate methods, synthetic ground truth with 12-bit quantization, selection rule fixed before running, independent re-derivation of scores. Result: hybrid, median 0.92, with the 0.5 to 10 Hz band. Weak signal is a hardware limit (0.42; 0.88 with 16 averaged reads, a what-if). Table: method against median score | display-processing spec and eval report |
| 3.7 Rancangan Tampilan Terpadu | Planned: one view for the doctor with RME context, the radar waveform and the 12-lead ECG on one time axis; decision support, the doctor decides; rule-based flags optional. Not built | `CLAUDE.md` goal, 2.5 references [36] to [38] |
| 3.8 Metode Pengujian dan Evaluasi | Automated tests (counts from a fresh run), browser end-to-end checks, fidelity re-derivation; indicators from 1.4 (mapping completeness, number of source formats, end-to-end data integrity) with targets as `[insert data: ...]` unless measured. Record sharing only if O2 keeps it in scope | test suites, browser-check reports |
| 3.9 Progres Penelitian | Status table per component (done and tested / prototype / planned), with the date and what is not yet verified | all specs, `CLAUDE.md` status |
| 3.10 Rencana Kerja | Remaining work in order: record a person with the wired radar, ECG intake, synthetic RME, integrated view, evaluation, writing. Dates as `[insert data: jadwal]` | `CLAUDE.md`, open questions |

## Notes file

`docs/proposal_md/catatan_bab3.md` (Indonesian headings, English allowed in notes):
claims table (claim, number, source); placeholders and suggested reference entries;
reference matches confirmed or not (P7); suggested Chapter I and II edits (P2);
figure briefs (P10); open questions.

## Process

Per `CLAUDE.md`: spec, then plan, then work; judgement by a capable model, review for
fidelity.

1. **Draft** Chapter III and the notes (Claude Opus 5.5, this session; it is judgement
   work).
2. **Mechanical checks**: no hyphen or dash characters in the new Chapter III text;
   every bracketed number is in [1] to [41]; every digit sequence in Chapter III appears
   in the claims table; Chapters I and II unchanged (`git diff` shows only an
   insertion); no "monitoring", "pemantauan", "diagnosis" or "prediksi" except in
   negations.
3. **Fidelity review** by a fresh reviewer (Claude Opus 5.5 subagent, only if the owner
   agrees to a subagent; otherwise a second pass by the drafter): re-derive at least
   five numbers and three built-versus-planned statements from the source files.
4. **Style pass** against guide §1 (connectors, intensifiers, clichés, sentence variety).
5. **Outline v3** (P9), then the same checks 2 and 4 on it.

## Acceptance

1. `proposal.md` has Chapter III with 3.1 to 3.10; Chapters I and II are unchanged.
2. Checks in Process step 2 pass, with the commands and their output reported.
3. The notes file exists and every number in Chapter III is in its claims table.
4. `outline_sidang_proposal_v3.md` exists; v2 is unchanged.
5. Nothing planned is described as done, and the progress table matches `CLAUDE.md`.

## Open questions (defaults apply until answered)

| # | Question | Default |
|---|---|---|
| O1 | Which presentation is next: the proposal defense, or a progress talk after it? Outline only, or a slide deck? | Outline v3 for the proposal defense with progress slides (P9); no deck yet |
| O2 | Is patient save-and-send in scope? | Not built, not claimed; listed as undecided |
| O3 | Where will the 12-lead ECG data come from? | `[insert data: sumber ECG]` |
| O4 | Which synthetic RME source? | `[insert data: sumber RME sintetis]` |
| O5 | Dates for the remaining work? | `[insert data: jadwal]` |
| O6 | Final title? | The working title, unchanged |
