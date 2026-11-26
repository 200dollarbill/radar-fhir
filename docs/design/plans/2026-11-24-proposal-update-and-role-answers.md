# Proposal Update and Indonesian Role Answers Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Update `docs/proposal_md/proposal.md` (plus a Word export) to the Research Proposal guide and the group's ethics proposal, and produce Indonesian research-role answers as `.docx`.

**Architecture:** Text lives in Markdown (`proposal.md`) and in one Node build script for the answers. Small tools in `tools/proposal/` do the repeatable parts: a Python text checker (style rules), a matplotlib figure generator (Indonesian labels), and a Node Markdown-to-docx exporter. Writing is judgement work done by the drafter; the checker gates it.

**Tech Stack:** Python 3 + pytest + matplotlib; Node 22 + `docx` npm package (installed in `tools/proposal/`, `node_modules/` is gitignored); LibreOffice + `pdftoppm` for render checks.

**Spec:** `docs/design/specs/2026-11-24-proposal-update-and-role-answers-design.md`

## Global Constraints

- Indonesian, flowing paragraphs, no bullets in body text; style per `docs/proposal_guide/panduan_proposal.md` §1.
- No `-`, `–` or `—` in body prose (bibliography, code identifiers and figure files excepted).
- Citations only `[1]` to `[41]`; no new reference numbers.
- No invented numbers: every number traces to [1] to [41], project evidence (handovers, eval report, specs), or `proposal etik.docx`.
- "diagnosa", "diagnosis", "prediksi", "monitoring", "pemantauan" only in negation or quoted PGHD background.
- CDSS is the thesis; FHIR (SATUSEHAT-compatible) is its interoperability layer; this branch collects no new subjects, reuses de-identified data from branches A to C, RME synthetic.
- Ethics placeholders (Bab IV, sample size, criteria, risks) stay as `[insert data: ...]` or "akan ditetapkan dalam protokol etik".
- Planned parts (ECG intake, RME import, integrated view) never described as done.
- Word output: Times New Roman 12 pt, A4 (11909 x 16834 twips), margins 1440, line 276, spacing 240 before/after.
- Never push. Commit each task.

## Review Focus

1. A hyphenated compound in body prose (e.g. "non-kontak", "kiri-kanan") copied from the ethics text: checker must flag it.
2. A citation like `[42]` or `[6][new]`: checker flags out-of-range and `[new]`.
3. "diagnosa" inside a negation ("bukan diagnosa") must pass, plain use must fail.
4. A figure line in Markdown whose PNG is missing: exporter must fail loudly, not drop the image.
5. Markdown bibliography with hyphens/DOIs must not be flagged (checker stops at `## DAFTAR PUSTAKA`).

---

### Task 1: Text checker

**Files:**
- Create: `tools/proposal/check_text.py`
- Test: `tools/proposal/tests/test_check_text.py`

**Interfaces:**
- Produces: `check(text: str) -> list[str]` (problems, each `"line N: <kind>: <snippet>"`); CLI `python3 tools/proposal/check_text.py FILE...` prints problems and `N problem(s)`, exit 1 if any. For `.docx` input it extracts paragraph text from `word/document.xml`.

- [ ] **Step 1: Write failing tests**

```python
from check_text import check
def test_dash_in_prose(): assert any("dash" in p for p in check("Radar non-kontak dipakai."))
def test_en_em_dash(): assert check("A – B") and check("A — B")
def test_citation_range(): assert any("citation" in p for p in check("Bukti [42]."))
def test_citation_ok(): assert check("Bukti [1][41].") == []
def test_new_marker(): assert check("Bukti [new].")
def test_banned_word(): assert any("banned" in p for p in check("Sistem ini memberi diagnosa."))
def test_banned_negated(): assert check("Keluaran bukan diagnosa.") == []
def test_bibliography_skipped(): assert check("## DAFTAR PUSTAKA\n[50] A-B, doi: 10.1-2") == []
def test_heading_and_image_skipped(): assert check("![Gambar 3.1 Alur](figures/a-b.png)") == []
```

- [ ] **Step 2: Run** `python3 -m pytest tools/proposal/tests -q` → FAIL (module missing).
- [ ] **Step 3: Implement** `check`. Rules: stop at a line starting `## DAFTAR PUSTAKA`; skip image lines and inline code spans; dash = `-` between letters or any `–`/`—`; citation = `\[(\d+)\]` outside 1..41 or `[new]`; banned = word from the list unless a negator (`bukan`, `tidak`, `tanpa`, `not`, `no`, `never`) appears within the 4 preceding words.
- [ ] **Step 4: Run** tests → all pass.
- [ ] **Step 5: Commit** `feat(proposal): text checker for proposal style rules`.

### Task 2: Indonesian figures

**Files:**
- Create: `tools/proposal/figures.py` (adapted from the session's `figs.py`: same helpers `box/term/diamond/cyl/arrow/poly`, black and white, 300 dpi)
- Output: `docs/proposal_md/figures/{posisi,alur,arsitektur,pengujian,protokol}.png`

**Interfaces:**
- Produces: CLI `python3 tools/proposal/figures.py OUT_DIR` writing the five PNGs above.

Labels (exact):
- `posisi`: circles "Pengukuran RADAR\n(cabang A sampai C)", "Rekam medis\n(RME)", "EKG"; centre "penelitian\nini"; top "FHIR R4 (kompatibel SATUSEHAT) sebagai format bersama".
- `alur`: "Pertanyaan penelitian" → "Studi literatur\n(rantai argumen L1 sampai L8)" → "Kebutuhan\n(pembimbing, dokter, tim)" → "Spesifikasi rancangan" → "Pembangunan bertahap\n(uji lebih dulu)" → ◇"Uji\nlolos?" (tidak → back) → "Pengujian sistem\n(data cabang A sampai C)" → "Evaluasi dan laporan"; dashed loop "temuan baru".
- `arsitektur`: built path "Sensor radar\nCW 24 GHz" → "Papan\nAtomS3R" (I/Q) → "Halaman Capture\n(peramban)" (USB) → "Cloudflare\nWorker" (HTTPS) → "Server\nFHIR R4" (tunnel) → "Basis data"; planned (dashed): "Data cabang\nA sampai C" (EKG, USG), "RME\n(sintetis)", "Tampilan dokter\n(satu layar)"; legend "sudah dibangun" / "direncanakan".
- `pengujian`: "Uji unit dan\nintegrasi" → "Simulator dengan\nnilai acuan" → "Uji bangku\ndengan papan" → "Uji ujung ke ujung\nlewat hosting" → "Uji gangguan"; ◇"Kriteria\nterpenuhi?" tidak: "perbaiki dan ulangi"; ya → "Uji dengan data subjek".
- `protokol`: dashed group box "Protokol tim (etik bersama)": "Persetujuan etik" → "Rekrutmen dan\npersetujuan subjek" → parallel "Radar\nCW 24 GHz", "EKG", "USG\nmode A"; then "Data dianonimkan" → (handover arrow labelled "cabang D") "Penerimaan data\noleh sistem" → ◇"Lengkap dan\nselaras?" (tidak: "kembalikan ke tim") → "Tampilan dokter" → "Simpan di laptop".

- [ ] **Step 1:** Write script; run `python3 tools/proposal/figures.py docs/proposal_md/figures`; expect 5 files.
- [ ] **Step 2:** Read each PNG; check no text overlaps lines, nothing clipped, no dash characters in labels.
- [ ] **Step 3: Commit** `feat(proposal): Indonesian black and white figures`.

### Task 3: Abstrak and Bab I

**Files:** Modify `docs/proposal_md/proposal.md` (top through 1.5; add 1.6, 1.7).

Content decisions (from spec):
- Abstrak 200 to 300 words (count with `wc -w`), no citations, no abbreviations.
- Fix list `proposal_CLAUDE.md` §6 items 1, 3 (check [3] in `daftar_sumber_dan_klaim.md`; use 27,66% six-month mortality wording if 27% readmission is unsupported), 4, 5, 6 (fill only from the catalogue; otherwise `[cite: ...]`), 8, 9, 10.
- New paragraph in 1.1 or 1.3: one research tree, CW 24 GHz, branches A (karotis, irama normal dan aritmia, EKG acuan temporal), B (asimetri karotis, CAD), C (JVP, USG mode A), D (this work); RSUD Dr. Soetomo.
- 1.6 Hipotesis dan Asumsi; 1.7 Definisi Istilah (JVP, RME, FHIR, CDSS, sinyal I/Q, sesi pengukuran), as paragraphs.

- [ ] **Step 1:** Edit. **Step 2:** `python3 tools/proposal/check_text.py docs/proposal_md/proposal.md` → no problems in the edited region (Bab II/III problems may remain until their tasks). **Step 3:** abstract word count 200 to 300. **Step 4: Commit** `docs(proposal): abstrak, Bab I aligned with ethics proposal`.

### Task 4: Bab II corrections and 2.6

**Files:** Modify `docs/proposal_md/proposal.md` (Bab II, reference list entry [6], [12]).
- Radar wording consistent with CW 24 GHz platform; [6] becomes Das et al., R. Soc. Open Sci. 12(6) 242231, 2025, doi 10.1098/rsos.242231; [12] authors/title from `proposal_CLAUDE.md` §6 item 10 (Meyer et al., Am J Cardiol 2009) only if the catalogue confirms, else keep placeholder.
- 2.6 from [1] to [41] only; gap stated as "tidak ditemukan dalam penelusuran".
- Remove the stray "u" after "objektif." in Bab II.
- [ ] **Step 1:** Edit. **Step 2:** checker clean for Bab I and II. **Step 3: Commit** `docs(proposal): Bab II corrections and 2.6`.

### Task 5: Bab III Metodologi

**Files:** Modify `docs/proposal_md/proposal.md` (insert after 2.7, before DAFTAR PUSTAKA); figures referenced as `![Gambar 3.N Caption](figures/<name>.png)`.

Sections 3.1 to 3.12 exactly as named in the spec. Numbers allowed (sources): 100 Hz, chunks up to 10 s, idle 1,53 V and about 1 mV, movement 90 to 170 mV, hybrid median 0,92 (handover 2026-11-18 §3); 236/179/23 tests (handover 2026-11-24 §3); Worker at most 3 ms, recovery 16 to 17 s (same); 100 subjects only as "dibahas pada konsultasi 15 Oktober 2026". Progress table (3.11) allowed (guide permits one table); everything else paragraphs.

- [ ] **Step 1:** Write. **Step 2:** checker on whole file → `0 problem(s)`. **Step 3:** grep that "ECG intake", "RME", "tampilan terpadu" are stated as direncanakan in 3.11. **Step 4: Commit** `docs(proposal): Bab III Metodologi`.

### Task 6: Markdown to Word exporter and proposal.docx

**Files:**
- Create: `tools/proposal/package.json` (dependency `docx`), `tools/proposal/md_to_docx.mjs`
- Test: `tools/proposal/tests/md_to_docx.test.mjs`
- Output: `docs/proposal_md/proposal.docx`

**Interfaces:**
- Produces: `mdToDocx(markdown: string, baseDir: string) -> Promise<Buffer>`; CLI `node tools/proposal/md_to_docx.mjs IN.md OUT.docx`.
- Handles: `#`/`##`/`###` headings (bold, TNR 14/12/12, keepNext), paragraphs (justified), `**bold**`/`*italic*`, image lines (centred, 6 in max width, italic caption below), simple pipe tables (DXA widths, borders), `---` ignored. Global constraints for page/font.

- [ ] **Step 1: Failing tests:** heading produces a heading paragraph; missing image path throws `Error(/figures\/x.png/)`; table with 3 columns yields a table; output buffer starts with `PK`.
- [ ] **Step 2:** `node --test tools/proposal/tests/` → FAIL.
- [ ] **Step 3:** Implement; `cd tools/proposal && npm install`.
- [ ] **Step 4:** Tests pass; build `proposal.docx`; `zip -d ... '*/'`; render to PDF in scratchpad; look at every page.
- [ ] **Step 5: Commit** (package.json, package-lock.json, script, test, proposal.docx) `feat(proposal): Word export of the proposal`.

### Task 7: Indonesian research-role answers

**Files:**
- Create: `tools/proposal/role_answers_id.mjs` (layout from the session's `build.js`: name and NIM centred bold, questions bold, answers justified TNR 12)
- Output: `docs/proposal_guide/proposal_questions_template/research_role_answers_id.docx`

Content per spec Deliverable 2; figures `posisi`, `alur`, `arsitektur`, `pengujian`, `protokol` from Task 2. Questions translated: "Peran dan kegiatan saya dalam kelompok riset"; a), b), c)(1), c)(2) in Indonesian.

- [ ] **Step 1:** Write and build. **Step 2:** `python3 tools/proposal/check_text.py <docx>` → `0 problem(s)`. **Step 3:** render, look at every page. **Step 4: Commit** `docs(proposal): Indonesian research role answers`.

### Task 8: Final verification

- [ ] Run `python3 -m pytest tools/proposal/tests -q`, `node --test tools/proposal/tests/`, the checker on both outputs; English `research_role_answers.docx` unchanged (`git status` shows it untracked/unmodified as before).
- [ ] Report results with command output; do not push.
