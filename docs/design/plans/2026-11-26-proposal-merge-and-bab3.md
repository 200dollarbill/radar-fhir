# Proposal Merge, Bab III Rewrite and Template Docx Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Merge the owner's template docx into `proposal.md` (fishbone only), rewrite Bab III after the senior thesis's writing pattern, and build `proposal_prata_revised_v2.docx` from the owner's ITS template.

**Architecture:** `proposal.md` stays the single source of text. A new Python builder reads it, copies the owner's docx, keeps covers, styles, footers and TOC fields, replaces titles, abstracts, Bab I to III and the reference list in `word/document.xml` with lxml, and embeds figures. Writing is judgement work by the drafter; `check_text.py` and builder tests gate it.

**Tech Stack:** system `python3` (lxml 5.2.1, Pillow 10.2.0, matplotlib, pytest); LibreOffice `soffice` for the render check. Not `.venv` (it has no lxml).

**Spec:** `docs/design/specs/2026-11-26-proposal-merge-and-bab3-design.md` (and rules P4, P5, P6, P8 and anti-goals of `docs/design/specs/2026-11-18-proposal-development-design.md`)

## Global Constraints

- Indonesian, flowing paragraphs, style per `docs/proposal_guide/panduan_proposal.md` §1. Read it before Task 4.
- No `-`, `–`, `—` in body prose. Code identifiers described in words (P4). Fenced blocks are exempt.
- Citations only `[1]` to `[41]` (P6); anything else is `[cite: ...]`. The senior thesis is never cited (D2).
- Every number in Bab III traces to repo evidence or a reference and is listed in `catatan_bab3.md` (P5).
- "diagnosa", "diagnosis", "prediksi", "monitoring", "pemantauan" only in negation. RADAR is a *pengukuran* device.
- Planned parts (branch A to C intake, ECG intake, RME import, integrated doctor view, challenge and response) never described as done (P8).
- Bab III: at most four tables (D4): Tabel 3.1 FHIR mapping, 3.2 test design, 3.3 progress, 3.4 schedule.
- Chapters I and II change only by the fishbone figure and one sentence referring to it.
- The owner's `docs/proposal_md/proposal_revised/proposal_prata_revised.docx` is never written.
- Commit each task (stage only files the task touched). Never push.

## Markdown conventions the builder reads (pinned here, used by Tasks 3 to 8)

| Markdown in `proposal.md` | Word output |
|---|---|
| `## Judul:` then one line | Indonesian title (covers, pengesahan) |
| `## Judul (Inggris):` then one line | English cover title |
| `## ABSTRAK` paragraphs, last line `Kata kunci: ...` | abstract and keyword paragraphs |
| `## ABSTRACT` paragraphs, last line `Keywords: ...` | English abstract and keywords |
| `## BAB III METODOLOGI DAN PERANCANGAN SISTEM` | Heading1, `BAB III` line break `METODOLOGI DAN PERANCANGAN SISTEM`, page break before |
| `### 3.1 Judul` / `#### 3.4.1 Judul` | Heading2 / Heading3, number kept in text, no numPr |
| `![Gambar 3.1 Alur penelitian](figures/alur.png)` | centered inline image (width at most 14 cm) + caption in Heading5, "Gambar 3.1" bold |
| paragraph `Tabel 3.1 ...` directly before a pipe table | caption in Heading6 (feeds DAFTAR TABEL field), then Word table, header row bold, single borders |
| ```` ```json ```` block then paragraph `Listing 3.1 ...` | Courier New 9 pt lines, then centered caption |
| ```` ```rumus ```` block, lines like `E = ... (3.1)` | one centered paragraph per line |
| `[n] text` under `## DAFTAR PUSTAKA` | reference paragraph, hanging indent 567 |
| `` `x` ``, `**x**`, `<!-- ... -->`, `---` | backticks dropped, bold run, removed, ignored |

## Review Focus

1. Word "repair" on open caused by duplicate `w14:paraId`, duplicate `wp:docPr/@id` or a dangling `r:embed`: builder test asserts uniqueness and that every embed resolves (Task 8).
2. Old title split over several runs on a cover page: the replace works on joined paragraph text, test asserts the old title string is absent from the whole document (Task 8).
3. A figure path in `proposal.md` that does not exist: builder raises `FileNotFoundError` naming the path, not a silent skip (Task 7 test).
4. Placeholders `[insert data: ...]` and `[cite: ...]` must survive verbatim into the docx (the owner fills them): parser test (Task 7).
5. TOC fields keep stale entries from the old text: `settings.xml` gets `<w:updateFields w:val="true"/>`, test asserts it (Task 8).

---

### Task 1: Checker skips fenced code blocks

**Files:**
- Modify: `tools/proposal/check_text.py` (`check`)
- Test: `tools/proposal/tests/test_check_text.py`

- [ ] **Step 1: Write the failing tests**

```python
def test_fenced_block_skipped():
    assert check("Teks.\n```json\n{\"date\": \"2026-11-18\"}\n```\nTeks lagi.") == []

def test_after_fence_still_checked():
    assert any("dash" in p for p in check("```json\n{}\n```\nRadar non-kontak."))
```

- [ ] **Step 2: Run** `python3 -m pytest tools/proposal/tests -q` → the two new tests FAIL.
- [ ] **Step 3: Implement** in `check`: a line whose stripped text starts with ```` ``` ```` toggles an `in_fence` flag; lines inside (and the fence lines) are skipped.
- [ ] **Step 4: Run** `python3 -m pytest tools/proposal/tests -q` → all pass.
- [ ] **Step 5: Commit** `fix(proposal): checker skips fenced code blocks`.

### Task 2: Figures (fishbone and three new diagrams)

**Files:**
- Create: `docs/proposal_md/figures/fishbone.jpg` (byte copy of `word/media/image3.jpg` from the owner's docx: `unzip -p <docx> word/media/image3.jpg > ...`)
- Modify: `tools/proposal/figures.py` (append three figures using the existing `canvas`, `box`, `arrow`, `poly`, `save` helpers)
- Create: `docs/proposal_md/figures/usecase.png`, `seq_sesi.png`, `seq_dokter.png`

Content (labels Indonesian, black and white, planned items dashed and marked *(direncanakan)*):

- `usecase.png`: actors Admin, Dokter, Pasien, Papan radar. Use cases: Admin: *daftarkan papan*, *buat pasien uji*, *buka dan tutup sesi*; Dokter: *buka sesi pasiennya*, *rekam pengukuran*, *tinjau rekaman (Review)*, *lihat tampilan terpadu* (dashed); Pasien: *baca rekaman sendiri*, *simpan dan bagikan data* (dashed, *belum ditetapkan*); Papan: *kirim potongan sinyal ke sesi terbuka*. System boundary labelled *Sistem PRATA*. Account creation is drawn outside the boundary as *dibuat di laptop*.
- `seq_sesi.png` (built): lifelines Dokter, Halaman Sessions, Halaman Capture, Papan, Server FHIR, Basis data. Messages: buka sesi (pasien, papan) → Encounter dibuat; Capture: `BOARD?` → ID chip dan kunci; ambil sesi papan; pratinjau; Rekam; potongan 10 detik disimpan di peramban → kirim dengan pembuatan bersyarat → Observation tersimpan → konfirmasi → hapus salinan lokal; tutup sesi.
- `seq_dokter.png` (all dashed, title note *direncanakan*): Dokter, Tampilan terpadu, Server FHIR: pilih pasien → ambil RME sintetis, Observation radar, EKG → selaraskan pada satu sumbu waktu → tampilkan; dokter memutuskan.

Verify against `docs/HOW-IT-WORKS.md` and `docs/design/specs/2026-11-18-board-sessions-and-navigation-design.md` before drawing; if a message differs from the code, the code wins.

- [ ] **Step 1:** Copy the fishbone; `file docs/proposal_md/figures/fishbone.jpg` → `JPEG image data ... 2048x724`.
- [ ] **Step 2:** Add the three figures; run `python3 tools/proposal/figures.py docs/proposal_md/figures` → eight files exist, existing five unchanged in content (`git diff --stat` shows them only if the script redraws them identically; if bytes change, accept only after viewing).
- [ ] **Step 3:** View each new PNG with the Read tool; no overlapping text, every label readable.
- [ ] **Step 4: Commit** `feat(proposal): fishbone, use case and sequence figures`.

### Task 3: `proposal.md` front matter and fishbone

**Files:** Modify `docs/proposal_md/proposal.md` (title block, ABSTRAK, new ABSTRACT, 2.7)

- [ ] **Step 1:** Add `## Judul (Inggris):` with *Development of a Clinical Decision Support System Based on the Interoperability of Electronic Medical Record Data and RADAR Cardiovascular Measurements*.
- [ ] **Step 2:** End ABSTRAK with `Kata kunci: FHIR, SATUSEHAT, interoperabilitas, sistem pendukung keputusan klinis, RADAR, jugular venous pulse, rekam medis elektronik.`
- [ ] **Step 3:** Add `## ABSTRACT` after ABSTRAK: a faithful English translation of the ABSTRAK paragraph (no added claims), ending `Keywords: FHIR, SATUSEHAT, interoperability, clinical decision support system, RADAR, jugular venous pulse, electronic medical record.`
- [ ] **Step 4:** In 2.7, after the first paragraph: one sentence pointing to the figure, then `![Gambar 2.2 Diagram fishbone](figures/fishbone.jpg)`.
- [ ] **Step 5:** `git diff docs/proposal_md/proposal.md` shows nothing else in Chapters I and II; `python3 tools/proposal/check_text.py docs/proposal_md/proposal.md` → `0 problem(s)`.
- [ ] **Step 6: Commit** `docs(proposal): English abstract, keywords, fishbone in 2.7`.

### Task 4: Bab III part 1 (opening, 3.1 to 3.5)

**Files:** Modify `docs/proposal_md/proposal.md` (replace `## BAB III METODOLOGI` through the end of 3.5)

Section content is fixed by the spec's Part 2 table. Additions over the current text:

- Heading `## BAB III METODOLOGI DAN PERANCANGAN SISTEM`; an opening paragraph naming what the chapter covers and that results belong to the thesis report.
- 3.1 *Pendekatan dan Alur Penelitian*: approach paragraph (design and implementation, not a clinical trial), then current 3.1 text and Gambar 3.1.
- 3.4 *Arsitektur Sistem* with `#### 3.4.1 Gambaran Umum` (current 3.4 + Gambar 3.2), `#### 3.4.2 Use Case Diagram` (Gambar 3.3 `usecase.png`, paragraph per actor), `#### 3.4.3 Kebutuhan Sistem` (functional per role, then non-functional: interoperability, data integrity, security, availability through hosting while the laptop runs), `#### 3.4.4 Alur Kerja Sistem` (Gambar 3.4 `seq_sesi.png` built, Gambar 3.5 `seq_dokter.png` planned).
- 3.5 *Perancangan Akuisisi dan Penerimaan Data*: current 3.5 text, Gambar 3.6 `protokol.png`.
- Every new number goes into a scratch list for Task 6.

- [ ] **Step 1:** Write the sections.
- [ ] **Step 2:** `python3 tools/proposal/check_text.py docs/proposal_md/proposal.md` → `0 problem(s)`.
- [ ] **Step 3:** Commit `docs(proposal): Bab III part 1, approach and system design`.

### Task 5: Bab III part 2 (3.6 to 3.12)

**Files:** Modify `docs/proposal_md/proposal.md` (3.6 to 3.12)

- 3.6 *Perancangan Pemodelan Data FHIR*: current text + `Tabel 3.1 Pemetaan data ke resource FHIR` with columns *Data*, *Resource*, *Elemen*, *Sistem kode dan kode*. Rows read from the code, not memory: Patient (NIK and IHS identifiers, `fhir_server/cli.py`), Practitioner, Organization, Location, Encounter (class code, `fhir_server/services/sessions.py`), Device (board identifier `urn:prata:board`), raw signal Observation (code and local code system from the capture code in `website/` and server validation), planned ECG (per [20]) and RME (per [21]) rows marked *direncanakan*. Then a shortened raw-signal Observation as a ```` ```json ```` block (taken from a real stored resource or a test fixture, data arrays cut to a few values) and `Listing 3.1 ...`.
- 3.7 *Perancangan Antarmuka*: Sessions, Capture, Review (built), integrated doctor view (planned); current 3.8 display-method text.
- 3.8 *Perancangan Keamanan*: current 3.7 text arranged in layers (accounts, roles, board identity, transport through Cloudflare, known weaknesses).
- 3.9 *Perancangan Pengujian*: current text and Gambar 3.7 `pengujian.png`, then `Tabel 3.2 Rancangan pengujian` (columns *Kelompok*, *Aspek yang diuji*, *Metrik*, *Kriteria lolos*; rows: unit and integration, keutuhan data, interoperabilitas FHIR, penyelarasan waktu, keamanan dan peran, hosting) and a ```` ```rumus ```` block with (3.1) kelengkapan sampel = sampel tersimpan / sampel terkirim × 100%, (3.2) jumlah duplikat = sampel tersimpan dikurangi sampel unik, (3.3) kelengkapan pemetaan = variabel wajib terpetakan / variabel wajib × 100%, (3.4) galat penyelarasan = |t radar − t EKG| per peristiwa yang dipasangkan; each followed by a sentence defining its symbols. Targets `[insert data: ...]` unless fixed already.
- 3.10: current text.
- 3.11: run `make test` first; replace the counts with the fresh ones and the date with 26 November 2026 (or the run date); `Tabel 3.3 Status komponen` = current table (check it against `CLAUDE.md` Status).
- 3.12: current text + `Tabel 3.4 Rencana kerja` (*Langkah*, *Luaran*, *Waktu*), times `[insert data: jadwal]`.

- [ ] **Step 1:** `make test 2>&1 | tail -30`; record the four suite results.
- [ ] **Step 2:** Write the sections.
- [ ] **Step 3:** `python3 tools/proposal/check_text.py docs/proposal_md/proposal.md` → `0 problem(s)`; count tables in Bab III = 4.
- [ ] **Step 4:** Commit `docs(proposal): Bab III part 2, data model, testing, progress`.

### Task 6: Notes file `catatan_bab3.md`

**Files:** Create `docs/proposal_md/catatan_bab3.md`

Sections (Indonesian headings): *Tabel klaim* (every number in Bab III: claim, number, source path or reference); *Placeholder* (each `[insert data]` and `[cite]` in Bab III with what fills it); *Komentar Word pemilik* (the 15 comments from the owner's docx, each with the sentence it is on and *selesai di proposal.md* or *masih terbuka*); *Usulan referensi* (comments 1 and 2: DOI 10.4103/JCPC.JCPC_4_20 and 10.1016/j.cjco.2025.12.001 as suggested IEEE entries for the two object method numbers, pending owner confirmation, metadata from doi.org only if the owner allows a lookup, else DOI only); *Perubahan struktur* (old to new Bab III section map).

- [ ] **Step 1:** Extract comments with the anchored text (script in the session scratchpad, not committed).
- [ ] **Step 2:** Write the file; check every digit sequence in Bab III appears in the claims table: `python3 - <<'EOF'` script that pulls numbers from the Bab III slice and greps the notes; prints missing ones → none.
- [ ] **Step 3:** Commit `docs(proposal): notes for Bab III, comments and claims`.

### Task 7: Markdown parser for the builder

**Files:**
- Create: `tools/proposal/md_blocks.py`
- Test: `tools/proposal/tests/test_md_blocks.py`

**Interfaces:**
- Produces: `parse(text: str, base: pathlib.Path) -> Doc` where `Doc` is a dataclass with `title_id: str`, `title_en: str`, `abstrak: list[str]`, `kata_kunci: str`, `abstract: list[str]`, `keywords: str`, `body: list[Block]` (from `## BAB I` up to `## DAFTAR PUSTAKA`), `references: list[str]`. `Block` is a dataclass `kind: str` in `{"h1","h2","h3","p","img","table","listing","formula"}`, `text: str` (heading or paragraph text, caption for img/table/listing), `runs: list[tuple[str,bool]]` (text, bold) for `p`, `path: pathlib.Path | None` for img, `rows: list[list[str]]` for table, `lines: list[str]` for listing and formula.

- [ ] **Step 1: Write failing tests**

```python
def test_heading_levels(): # "## BAB I PENDAHULUAN", "### 1.1 X", "#### 3.4.1 Y" -> h1, h2, h3 with text kept
def test_table_caption_attached(): # "Tabel 3.1 Cap\n\n| a | b |\n|---|---|\n| 1 | 2 |" -> one table block, text "Tabel 3.1 Cap", rows [["a","b"],["1","2"]]
def test_listing_caption_after_fence(): # "```json\n{}\n```\n\nListing 3.1 Cap" -> listing, lines ["{}"], text "Listing 3.1 Cap"
def test_formula_block(): # "```rumus\nA = B (3.1)\n```" -> formula, lines ["A = B (3.1)"]
def test_placeholders_verbatim(): # "[insert data: x] dan [cite: y]" survives in runs text
def test_code_and_comment_stripped(): # "a `b` c <!-- check:ok x -->" -> "a b c"
def test_bold_runs(): # "a **b** c" -> [("a ",False),("b",True),(" c",False)]
def test_missing_image_raises(tmp_path): # FileNotFoundError mentioning the path
def test_real_proposal(): # parse(docs/proposal_md/proposal.md): references length 41, title_en non empty, h2 texts include "3.1 Pendekatan dan Alur Penelitian" and "3.12 Rencana Kerja"
```

- [ ] **Step 2:** `python3 -m pytest tools/proposal/tests/test_md_blocks.py -q` → FAIL (module missing).
- [ ] **Step 3:** Implement `md_blocks.py` (line scanner; no Markdown library).
- [ ] **Step 4:** Tests pass.
- [ ] **Step 5:** Commit `feat(proposal): markdown block parser for the docx builder`.

### Task 8: Template docx builder

**Files:**
- Create: `tools/proposal/build_docx.py` (CLI: `python3 tools/proposal/build_docx.py TEMPLATE.docx proposal.md OUT.docx`)
- Test: `tools/proposal/tests/test_build_docx.py`

**Interfaces:**
- Consumes: `md_blocks.parse`, `Doc`, `Block` (Task 7).
- Produces: `build(template: Path, md: Path, out: Path) -> None`.

Template facts (owner's docx, Google Docs export): body children are `w:p`, `w:tbl`, `w:sdt`; Heading1 paragraph `BAB I` / br / `PENDAHULUAN` at the start of Bab I; `DAFTAR PUSTAKA` and `LAMPIRAN` are Heading1; DAFTAR ISI and DAFTAR TABEL are `w:sdt` TOC fields (`\t "Heading 6,1"` for tables); old ID title starts `Pengembangan Profil Fast Healthcare`, old EN title starts `Development of a Fast Healthcare`; old abstract paragraphs start `Penelitian ini mengembangkan` and `This research develops`; keyword paragraphs start `Kata kunci:` and `Keywords:`; fishbone is `rId12` (`media/image3.jpg`).

Operations, in order: replace every paragraph whose joined text starts with an old title by one run with the new title (first run's `rPr` kept); replace abstract and keyword paragraphs likewise (extra abstract paragraphs inserted after with the same `pPr`); delete body children from the Bab I Heading1 up to (not including) DAFTAR PUSTAKA; delete children between DAFTAR PUSTAKA and LAMPIRAN; insert generated body and references; clone the DAFTAR TABEL heading and `sdt` after the DAFTAR TABEL `sdt` as DAFTAR GAMBAR with `\t "Heading 5,1"` and cached entries cleared; add images to `word/media/`, relationships and `[Content_Types].xml` defaults (`png`, `jpg`); set `<w:updateFields w:val="true"/>` in `word/settings.xml`; strip `w14:paraId`/`w14:textId` from cloned and generated elements; give each `wp:docPr` a unique id. Body paragraph `pPr`: `<w:ind w:firstLine="425"/><w:jc w:val="both"/>`. Heading1 for chapters gets `<w:pageBreakBefore/>`. Write all other zip entries byte for byte.

- [ ] **Step 1: Write failing tests** (build into `tmp_path` from the real template and real `proposal.md`):

```python
def test_owner_docx_untouched(built):      # sha256 of template before == after
def test_xml_parses(built):                # every .xml part parses with lxml
def test_old_strings_gone(built):          # "Pengembangan Profil Fast Healthcare", "Development of a Fast Healthcare",
                                           # "Monitoring Kesehatan Berbasis RADAR", "Penelitian ini mengembangkan" absent from document text
def test_headings(built):                  # Heading2 texts include "3.1 Pendekatan dan Alur Penelitian" ... "3.12 Rencana Kerja"; Heading1 "DAFTAR GAMBAR" present
def test_references(built):                # 41 paragraphs between DAFTAR PUSTAKA and LAMPIRAN start with "[1]".."[41]"
def test_ids_unique_and_embeds_resolve(built)  # no duplicate w14:paraId, no duplicate docPr id, every r:embed in rels and its media in the zip
def test_update_fields(built):             # settings.xml has updateFields true
def test_checker_clean(built):             # check_text.check(read(out)) == []
```

- [ ] **Step 2:** `python3 -m pytest tools/proposal/tests/test_build_docx.py -q` → FAIL.
- [ ] **Step 3:** Implement `build_docx.py`.
- [ ] **Step 4:** Tests pass; full `python3 -m pytest tools/proposal/tests -q` passes.
- [ ] **Step 5:** Build the real file: `python3 tools/proposal/build_docx.py docs/proposal_md/proposal_revised/proposal_prata_revised.docx docs/proposal_md/proposal.md docs/proposal_md/proposal_revised/proposal_prata_revised_v2.docx`.
- [ ] **Step 6: Render check:** `soffice --headless --convert-to pdf --outdir <scratchpad> <v2.docx>`, then `pdftoppm -png -r 50` on pages with Bab III, a table, a formula, the fishbone and the cover; view them with Read. Fix layout issues in the builder, not by hand.
- [ ] **Step 7: Commit** `feat(proposal): build v2 docx from the ITS template` (script, tests, and the v2 docx).

### Task 9: Fidelity review and handover

- [ ] **Step 1:** Fidelity review (fresh Claude Opus 5.5 subagent only if the owner agrees; otherwise a second pass by the drafter): re-derive at least five Bab III numbers and three built versus planned statements from the repo files named in `catatan_bab3.md`; check Tabel 3.1 rows against `fhir_server/` code; fix findings, rebuild the docx, rerun tests.
- [ ] **Step 2:** `git diff 4c4af04 -- docs/proposal_md/proposal.md` limited to Chapters I and II shows only the fishbone sentence and figure.
- [ ] **Step 3:** Update `CLAUDE.md` *Next session* line and write `docs/handover/2026-11-26-handover.md` (what was built, owner actions: open v2 in Word and accept the field update, fill placeholders, confirm DOIs, answer open comments).
- [ ] **Step 4:** Commit `docs: handover 2026-11-26`. Ask the owner to open the v2 docx in Word (acceptance 6).
