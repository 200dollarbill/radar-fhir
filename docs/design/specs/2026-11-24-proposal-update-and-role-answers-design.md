# Proposal update and Indonesian research-role answers

Date: 2026-11-24. Status: design approved in conversation; spec awaiting the owner's review.

Supersedes `2026-11-18-proposal-development-design.md` for the proposal text (Chapter III
and its rules P1 to P10). That spec's presentation outline (P9) is not part of this work.

## Why

The owner asked for three things on 2026-11-24:

1. Update `docs/proposal_md/proposal.md` using the structure guidance in
   `docs/proposal_guide/Research Proposal.pdf`.
2. Align it with the group's ethics proposal `docs/proposal_guide/proposal etik.docx`.
3. Rewrite the research-role answers
   (`docs/proposal_guide/proposal_questions_template/research_role_answers.docx`, English)
   in Indonesian, consistent with the ethics proposal and the updated proposal.

## Contradiction found and its ruling

The ethics proposal describes this branch as (verbatim):

> "Menyusun profil Fast Healthcare Interoperability Resources (FHIR) untuk keluaran
> perangkat radar leher agar sesuai dengan kebutuhan interoperabilitas rekam medis
> elektronik dan SATUSEHAT, dengan memakai ulang data dari cabang A-C."

> "...dengan memakai ulang data yang telah diperoleh tanpa pengumpulan data subjek baru."

The thesis direction (`proposal_CLAUDE.md` §2) is a CDSS website, with the FHIR profile
superseded as headline.

**Ruling (owner, 2026-11-24): CDSS, ethics-consistent.** The thesis stays the CDSS
website. FHIR (SATUSEHAT-compatible) is its interoperability layer, which is how the
ethics wording is read. This branch collects no new subjects: it reuses de-identified
data from branches A to C, and RME is synthetic or test data.

## Facts adopted from the ethics proposal

- Platform: radar continuous wave (CW) 24 GHz, one research tree, three acquisition
  branches: (A) carotid pulse morphology in normal rhythm and arrhythmia via fiducial
  points, with ECG as temporal reference; (B) CAD detection via left-right carotid
  asymmetry (cross-correlation, DTW, BAI); (C) JVP estimation from internal jugular
  pulsation with A-mode ultrasound as reference. This branch (D) is the informatics one.
- Site: RSUD Dr. Soetomo. Team: dr. Ruth Irena Gunadi, Sp.JP, FIHA (clinician);
  Rezki El Arif, S.T., M.T., Ph.D (supervisor); four students.
- Not adopted: anything empty or placeholder in the ethics proposal (Bab IV, sample size,
  inclusion and exclusion criteria, research risk 1.5, arrhythmia types). These appear as
  `[insert data: ...]` or "akan ditetapkan dalam protokol etik". The 100-subject figure is
  mentioned only as discussed at the 2026-10-15 consultation.
- Ethics references [1] to [6] are not added to the thesis reference list unless already
  present (Das et al. RSOS 2025 replaces the preprint citation of [6]).

## Ground rules (both documents)

- Style per `docs/proposal_guide/panduan_proposal.md`: Indonesian, flowing paragraphs, no
  bullets, no hyphens or dashes in body text, IEEE numeric citations, Indonesian terms with
  English gloss on first use.
- No invented numbers; every number traces to a reference in [1] to [41], the project's own
  evidence (handovers, eval report, specs), or the ethics proposal.
- Never diagnosis, prediction, validated risk score; RADAR is a *pengukuran* device, not
  monitoring (except when quoting general PGHD background).
- Built versus planned stated honestly (ECG intake, RME import, integrated view: planned).

## Deliverable 1: updated `proposal.md` and `proposal.docx`

Structure:

- **Abstrak** (new, 200 to 300 words): problem, aim, method, expected result, conclusion.
  No citations, figures or abbreviations (PDF rule).
- **Bab I**: keep 1.1 to 1.5. Apply the fix list in `proposal_CLAUDE.md` §6: remove
  "diagnosa" in 1.4; heart failure as a syndrome, not "gejala"; "pergerakan akustik" →
  mechanical; check 27% vs 27,66% against [3] via the catalogue; [12] is a propensity-matched
  analysis, not a meta-analysis; patient save-and-send stated as not committed; fill
  "Survey oleh cite"-type placeholders only where the catalogue names the authors. Add a
  short paragraph placing this branch in the group's research tree. New:
  - **1.6 Hipotesis dan Asumsi**: a design hypothesis (one FHIR canonical format can hold
    radar, ECG and RME data and present them on one time axis without data loss) and the
    assumptions (branches provide de-identified data with timestamps; synthetic RME is
    representative of the RME variables in Kepmenkes 1423/2022).
  - **1.7 Definisi Istilah**: JVP, RME, FHIR, CDSS, sinyal I/Q, sesi pengukuran.
- **Bab II**: content kept; corrections only where it conflicts with the ethics proposal
  (radar type, Das et al. published version). Fill 2.6 from sources [1] to [41] only, with
  the gap stated as "not found in the searches".
- **Bab III Metodologi** (PDF methods-and-materials shape): 3.1 Alur Penelitian; 3.2 Sumber
  Data dan Subjek; 3.3 Perangkat dan Perangkat Lunak; 3.4 Arsitektur Sistem; 3.5 Protokol
  Akuisisi dan Penerimaan Data; 3.6 Pemodelan Data FHIR; 3.7 Sesi, Peran, dan Keamanan;
  3.8 Rancangan Tampilan Terpadu; 3.9 Metode Pengujian dan Analisis (measurable criteria:
  data integrity, FHIR validation, mapping completeness, time alignment tolerance, Worker
  latency); 3.10 Etika Penelitian dan Perlindungan Data; 3.11 Progres; 3.12 Rencana Kerja
  (dates `[insert data: jadwal]`).
- Figures: the five diagrams relabelled in Indonesian; architecture shows data arriving
  from branches A to C.
- Chapters I and II edits are allowed this time (owner's explicit request overrides the
  "record only" rule in `proposal_CLAUDE.md` §6 for this task).
- Word export `docs/proposal_md/proposal.docx`: Times New Roman 12, A4, 1 inch margins,
  figures embedded.

## Deliverable 2: `research_role_answers_id.docx`

Next to the English file, which stays unchanged. Template layout (name and NIM centred bold,
question bold, answer paragraphs, no bullets).

- **Peran**: four student branches on one CW 24 GHz platform, per the ethics proposal; this
  branch receives their output. Evidence adds the group's ethics proposal.
- **a)**: same argument (critique-driven redirection, L1 to L8, gap, contribution), stating
  that device and signal analysis belong to branches A to C.
- **b)**: mirrors Bab III; flow and architecture figures.
- **c(1)**: test ladder, real numbers, criteria (unchanged content, translated).
- **c(2)**: the human-subject acquisition is the group's protocol under one ethics approval
  at RSUD Dr. Soetomo (radar, ECG as temporal reference, A-mode USG for JVP). This branch
  adds no subjects or procedures; it receives de-identified data and checks completeness
  and time alignment. Figure: group protocol → handover → system checks → doctor view.

## Checks and acceptance

1. Mechanical: no `-` or `—` in body prose of new or edited Indonesian text (bibliography
   and code identifiers excepted); every `[n]` within 1 to 41; banned words ("diagnosa",
   "prediksi", "monitoring", "pemantauan") only in negations or quoted background.
2. Every digit sequence in Bab III and the answers traces to a source listed in the commit
   message or the notes.
3. Both `.docx` files rendered to PDF and every page looked at.
4. Nothing planned described as done.
5. Committed (not pushed).
