# Proposal merge, Bab III rewrite and Word file from the ITS template

Date: 2026-11-26. Status: design approved by the owner in session; spec awaiting review.

## Why

The owner made `docs/proposal_md/proposal_revised/proposal_prata_revised.docx` (ITS
template, edited 2026-11-26) and asked for Bab III to be added to it, using the senior
thesis `docs/reference/seniors/5023221006_Naulia Sahya Althafah_BukuTA.pdf` as a model of
how such a proposal is written.

Comparison (session 2026-11-26) found the docx body is older than `proposal.md`:

- Of 162 docx body sentences, 122 match `proposal.md` at commit `6702c56` (2026-11-04) and
  53 match the current file. The docx lacks everything added on 2026-11-24: new abstract,
  1.3 with branches A to C, 1.6, 1.7, 2.5 CDSS ([36] to [41]), the new 2.6, the clean
  reference list [1] to [41], and Bab III.
- The other docx sentences are the old 2.5 *Monitoring Kesehatan Berbasis RADAR* and the
  old 2.6 table, from the superseded FHIR-profile proposal, with old numbering ([17] Suzuki,
  [19] Yen, [20] Shi). The inner title page, *pengesahan* and both abstracts are from that
  proposal too. The docx reference list has 21 entries; its text cites up to [35].
- New in the docx only: the ITS template layout, the fishbone figure
  (`word/media/image3.jpg`, 2048 by 724), and 15 Word comments by the owner.

## Decisions (owner, 2026-11-26)

| # | Decision |
|---|---|
| D1 | Merge: `proposal.md` (current) is the base. Take the fishbone figure from the docx. Drop the old 2.5, old 2.6, old title and old abstracts |
| D2 | The senior thesis is a writing reference only. It is not cited, not added to 2.6, and has no comparison table |
| D3 | Bab III is restructured after the senior's *Metodologi dan Perancangan Sistem* pattern, keeping the proposal-only sections (data, ethics, progress, schedule) |
| D4 | Bab III may have four tables (FHIR mapping, test design, progress, schedule). This replaces the two-table limit P3 of `2026-11-18-proposal-development-design.md` |
| D5 | The Word file is a new file built from the owner's template; the owner's file stays untouched |
| D6 | The English abstract is a translation of the Indonesian abstract in `proposal.md` |

Rules kept from `2026-11-18-proposal-development-design.md`: P4 (hyphenated code
identifiers described in words), P5 (every number traceable to repo evidence or a
reference), P6 (only [1] to [41] cited by number; others are `[cite: ...]`), P8 (built
versus planned stated with date and evidence), and the anti-goals there (no planned part
as done, no monitoring, diagnosis or risk framing, no simulated data as radar signal).

## What the senior thesis contributes (writing pattern only)

Its Bab III (pages 36 to 56) opens with a paragraph naming what the chapter covers and
that results come later; states the approach (design and implementation, not a clinical
trial); describes the architecture with an overview figure, a use case diagram,
functional requirements per role and non-functional requirements, and sequence diagrams
for the main flows; maps data to FHIR in a table (parameter, code, display, unit) with a
short JSON listing; describes security in layers; and ends with a test design table
(group, aspect, metric, pass criterion) plus the formulas behind each metric. We copy the
shape, not the content.

## Part 1: `proposal.md`, Bab I and II

- Base: current `proposal.md`. Chapters I and II change only as follows.
- 2.7 Rasional gets the fishbone figure as *Gambar 2.2 Diagram fishbone* (2.6 already has
  Gambar 2.1), saved as `docs/proposal_md/figures/fishbone.jpg`, with one sentence that
  refers to it.
- No other wording change in Chapters I and II.

## Part 2: Bab III METODOLOGI DAN PERANCANGAN SISTEM

Opening paragraph: what the chapter covers; it describes method and design, and the
results belong to the thesis.

| Section | Content | Sources |
|---|---|---|
| 3.1 Pendekatan dan Alur Penelitian | Design and implementation research, not a clinical trial; spec, test first build, staged testing. Gambar 3.1 (existing `alur.png`) | current 3.1 |
| 3.2 Sumber Data dan Subjek | Unchanged in substance | current 3.2 |
| 3.3 Perangkat dan Perangkat Lunak | Unchanged in substance | current 3.3, firmware README |
| 3.4 Arsitektur Sistem | 3.4.1 Gambaran Umum (Gambar 3.2 `arsitektur.png`); 3.4.2 Use Case Diagram (Gambar 3.3, new); 3.4.3 Kebutuhan Sistem: functional per role (admin, dokter, pasien, papan) and non-functional (interoperability, data integrity, security, availability through hosting); 3.4.4 Alur Kerja Sistem: Gambar 3.4 sequence *buka sesi dan perekaman* (built), Gambar 3.5 sequence *tinjauan dokter* (planned, labelled) | current 3.4 and 3.7, board-sessions spec, `docs/HOW-IT-WORKS.md` |
| 3.5 Perancangan Akuisisi dan Penerimaan Data | Current 3.5 content. Gambar 3.6 (existing `protokol.png`) | current 3.5, capture spec |
| 3.6 Perancangan Pemodelan Data FHIR | Current 3.6 content plus Tabel 3.1: data element, resource, element, code system and code. Radar I/Q under a local code system, stated as a limitation. Listing 3.1: shortened raw-signal Observation as the server stores it | `fhir_server/`, capture spec, `docs/reference/claude/` |
| 3.7 Perancangan Antarmuka | Pages per role: Sessions, Capture, Review (built), integrated doctor view (planned). The display method (hybrid, median 0.92) is described only as what the doctor sees | current 3.8, display-processing eval |
| 3.8 Perancangan Keamanan | Current 3.7 content in layers: accounts, roles, board identity, transport through Cloudflare, known weaknesses (board key sent on request; slow login guessing not stopped) | current 3.7, hosting spec |
| 3.9 Perancangan Pengujian | Current 3.9 stages (Gambar 3.7 existing `pengujian.png`), Tabel 3.2: test group, aspect, metric, pass criterion. Formulas, numbered (3.1) onward: sample completeness (received over sent), duplicate count, mapping completeness (mapped mandatory variables over mandatory variables), time alignment error (absolute difference of matched event times). Targets as `[insert data: ...]` unless already fixed | current 3.9, 1.4 indicators |
| 3.10 Etika Penelitian dan Perlindungan Data | Unchanged in substance | current 3.10 |
| 3.11 Progres Penelitian | Current text with test counts from a fresh `make test` on the day; Tabel 3.3 status per component | fresh run, `CLAUDE.md` status |
| 3.12 Rencana Kerja | Ordered steps plus Tabel 3.4 schedule (step, output, dates `[insert data: jadwal]`) | current 3.12 |

New figures (black and white, Indonesian, drawn by `tools/proposal/figures.py` like the
existing five): `usecase.png`, `seq_sesi.png`, `seq_dokter.png`. Planned functions and
steps are drawn dashed and labelled *direncanakan*.

## Part 3: the Word file

Output: `docs/proposal_md/proposal_revised/proposal_prata_revised_v2.docx`, built by a
new script in `tools/proposal/` that copies the owner's docx and rewrites its
`word/document.xml`, keeping the template's styles, cover images, section properties
and footers.

- Title on every cover and on the *pengesahan* page: the working title in `proposal.md`.
  The English cover title is its translation.
- ABSTRAK from `proposal.md`; ABSTRACT a translation (D6). Keywords updated to match.
- Bab I and II from the merged `proposal.md`, Bab III inserted before DAFTAR PUSTAKA,
  reference list [1] to [41] from `proposal.md`.
- Headings use the template's Heading1 and Heading2. Figures embedded with captions,
  tables as Word tables with captions above, formulas as numbered text lines.
- DAFTAR ISI, DAFTAR TABEL and DAFTAR GAMBAR rebuilt as text lists (no page numbers
  computed; the owner updates them in Word). The owner's comments are not carried over.
- Comments become a to-do list in `docs/proposal_md/catatan_bab3.md`, marked done where
  `proposal.md` already resolves them. Comments 1 and 2 give DOIs
  (10.4103/JCPC.JCPC_4_20, 10.1016/j.cjco.2025.12.001) for the two object method figures:
  suggested reference entries go in the notes and enter the list only after the owner
  confirms them.

## Checks and acceptance

1. `proposal.md`: Chapters I and II differ from HEAD only by the fishbone figure and its
   sentence (`git diff`).
2. `python3 tools/proposal/check_text.py docs/proposal_md/proposal.md` and the same on the
   v2 docx print `0 problem(s)` (no hyphen or dash characters outside listings, no
   monitoring, pemantauan, diagnosis or prediksi except in negations, citations within [1]
   to [41]). The checker currently skips inline code but not fenced code blocks, so it
   gains a test and a rule to skip fenced blocks (the JSON listing holds dates with
   hyphens). In the docx the listing is skipped by its paragraph style.
3. Every number in Bab III appears in the claims table of `catatan_bab3.md` with its source.
4. Fidelity review: at least five numbers and three built versus planned statements
   re-derived from repo files (fresh Claude Opus 5.5 subagent if the owner agrees,
   otherwise a second pass by the drafter).
5. The script has tests; the v2 docx opens (unzips, XML parses), contains no old title
   string, no old 2.5 heading, Bab III headings 3.1 to 3.12, and 41 reference entries.
   The owner's docx is byte-identical afterwards.
6. Owner opens the v2 docx in Word and confirms the layout.

## Non-goals

New system work; new literature; edits to Chapters I and II beyond the fishbone; a
slide deck or presentation outline (stays in the 2026-11-18 spec); computing page numbers
for the lists.
