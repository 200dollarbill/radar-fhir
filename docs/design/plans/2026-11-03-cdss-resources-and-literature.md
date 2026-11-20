# CDSS Resource Update and Literature Deepening Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make every Claude-facing resource describe the CDSS topic, then produce a searchable, downloadable evidence set organised by the thesis's urgency argument.

**Architecture:** Part 1 edits Markdown briefs only. Part 2 runs Exa searches by argument link (L1 to L8) and writes one Markdown file per link plus a summary and a download list. Parts are independent, but Part 1 runs first.

**Tech Stack:** Markdown, git, Exa MCP tools (`web_search_exa`, `web_fetch_exa`, loaded via ToolSearch), Python 3 for verification scripts.

**Spec:** `docs/.superpowers/specs/2026-11-03-cdss-topic-resource-update-design.md` (Part 1) and `docs/.superpowers/specs/2026-11-03-literature-deepening-design.md` (Part 2). Executors read both.

## Global Constraints

- The repo path contains spaces. Quote every path.
- Stage files by explicit path. Never `git add -A` or `git add .`: the working tree holds many unrelated owner changes.
- Commit messages end with `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`.
- Do not edit `docs/proposal_md/*`, `docs/proposal_guide/*`, `docs/presentation/*`, `docs/reference/raw/*`, past specs and plans, or server code.
- Do not open or change `.env/notes.env`.
- Final objective wording: a working website that takes in RME, RADAR JVP and 12-lead ECG data and displays it visually and efficiently in one view for the doctor.
- Rule-based flags are not required, and are optional only if time remains.
- Never frame output as diagnosis, prediction or a validated risk score. Use "pengukuran", not "monitoring", for the RADAR device.
- `docs/presentation/ets/fishbone.md` is the fishbone source. The owner will add an `.svg` generated from it, at a path not yet known. Do not name an SVG path.
- Claude-authored notes are always labelled. Abstracts and bibliographic details come only from a source page.

## Review Focus

1. A later session reads "FHIR profile" in the direction history as the current goal: the history must be explicitly marked superseded (Task 2 check).
2. Paths in the briefs are wrong, such as `docs/superpowers` instead of `docs/.superpowers`: every named path must resolve (Tasks 1 and 2 path check).
3. Exa highlights are excerpts, and pasting one as an abstract misrepresents the paper: abstracts come from a fetched page, and truncated ones are labelled (Task 4 rule, Task 7 sample check).
4. The same paper appears as a preprint and as a published article: keep one entry, published version first, noting the preprint (Task 7 duplicate check).
5. A paper has been retracted or corrected: mark it if the source page or PubMed says so, and never count it as support (Task 4 rule).

---

## Part 1: Resource update

### Task 1: Restore `CLAUDE.md` and retire `project_CLAUDE.md`

**Files:**
- Modify: `CLAUDE.md` (restored from HEAD, then rewritten)
- Delete: `project_CLAUDE.md` (untracked, identical to HEAD's `CLAUDE.md`)

**Interfaces:**
- Produces: the auto-loaded brief that points to `proposal_CLAUDE.md` for thesis work.

- [ ] **Step 1:** Run `git restore CLAUDE.md`. Confirm `git diff --quiet HEAD -- CLAUDE.md` exits 0 and `diff CLAUDE.md project_CLAUDE.md` prints nothing. If they differ, stop and report.
- [ ] **Step 2:** Rewrite `CLAUDE.md`, under 120 lines, per the resource spec's `CLAUDE.md` section. Keep the sections "How work is done here", "Commands" and "Conventions" and the SATUSEHAT and R4 constraints. Replace "The goal" and "Status". Fix the stale `PraTAPapers/` reference to `docs/papers/`.
- [ ] **Step 3:** Verify: `wc -l CLAUDE.md` is under 120, and every backticked repo path in it exists. Paths that do not yet exist because later tasks create them (`docs/papers/search/`) are allowed if listed as upcoming.
- [ ] **Step 4:** Run `rm project_CLAUDE.md`. Its content stays recoverable from `git show HEAD:CLAUDE.md`.
- [ ] **Step 5:** Commit `CLAUDE.md` with message `docs: rewrite CLAUDE.md for the CDSS topic`.

### Task 2: Rewrite `proposal_CLAUDE.md`

**Files:**
- Modify: `proposal_CLAUDE.md` (currently untracked)

**Interfaces:**
- Consumes: `docs/proposal_md/proposal.md`, `docs/proposal_guide/panduan_proposal.md`, `docs/presentation/ets/fishbone.md`, `docs/notul/konsultasi_15okt.txt`.
- Produces: the argument chain L1 to L8 restated in the urgency section, matching the literature spec.

- [ ] **Step 1:** Commit the current file unchanged, with message `docs: snapshot pre-CDSS proposal handoff`, so the old version is recoverable. It has never been committed.
- [ ] **Step 2:** Rewrite section by section per the table in the resource spec. Open the direction history with "Current direction: CDSS. Versions below are superseded."
- [ ] **Step 3:** Write the fix list from the spec's nine items. Check each against `proposal.md` and quote the exact phrase. Then check each of the ten old fix-list items and carry over only those still present.
- [ ] **Step 4:** Verify: `grep -n "decision support\|Pengembangan Profil" proposal_CLAUDE.md`. Every hit is either in the direction history or consistent with the CDSS framing. Every backticked repo path exists.
- [ ] **Step 5:** Commit with message `docs: rewrite proposal handoff for the CDSS topic`.

### Task 3: Update the human brief and reference index

**Files:**
- Modify: `docs/reference/human/16-project-proposal-brief.md` (untracked)
- Modify: `docs/reference/human/README.md` (has the owner's uncommitted row for file 16)
- Modify: `docs/reference/claude/INDEX.md`

- [ ] **Step 1:** Commit the current `16-project-proposal-brief.md` and `README.md` unchanged, with message `docs: snapshot proposal brief before CDSS update`.
- [ ] **Step 2:** Update the brief's goal, contribution and roadmap sections per the spec. Keep the claim-boundary text and the FHIR methodology. Update the README row's description.
- [ ] **Step 3:** In `INDEX.md`, add the line stating these files are FHIR and SATUSEHAT facts independent of the thesis topic, and reword the `fhir-device.md` and `fhir-profiling.md` "Load when" notes so a device profile is one possible use.
- [ ] **Step 4:** Run `python3 .tools/scrape/lint_views.py`. Expected output includes `0 problem(s)`.
- [ ] **Step 5:** Commit the three files with message `docs: align proposal brief and reference index with CDSS topic`.

---

## Part 2: Literature deepening

**Entry format, used in every `L*.md` file:**

```markdown
### <Title>
- **Authors:** ...
- **Year / venue / type:** ...
- **DOI:** ... (blank if not seen on a source page)
- **URL:** ...
- **Stance:** supports | contradicts | qualifies
- **Owner has it:** P<n> | no
- **Found by:** <query>
- **Claude's note:** <one line>

**Abstract:** <as found, or "abstract not retrieved">
```

**Output files in `docs/papers/search/`:** `L1-hf-burden.md`, `L2-congestion.md`, `L3-jvp-waveform.md`, `L4-single-measurement.md`, `L5-bedside-limits.md`, `L6-radar-capture.md`, `L7-context-fusion.md`, `L8-display-cdss.md`, `README.md`, `download-list.md`.

### Task 4: Exclusion list and L3 and L4 searches

**Files:**
- Create: `docs/papers/search/L3-jvp-waveform.md`, `docs/papers/search/L4-single-measurement.md`
- Scratch: `known-papers.md` in the session scratchpad, not committed

**Interfaces:**
- Produces: the entry format above, and a running search log (query, date, result count) kept in the scratchpad for Task 7.

- [ ] **Step 1:** Load the Exa tools with ToolSearch `select:mcp__plugin_exa_exa__web_search_exa,mcp__plugin_exa_exa__web_fetch_exa`. If they are unavailable, stop and report it, and do not switch sources.
- [ ] **Step 2:** Build `known-papers.md` from filenames under `docs/papers/` and the titles and DOIs in `docs/proposal_md/daftar_sumber_dan_klaim.md`.
- [ ] **Step 3:** Run L3 searches with at least six differently worded queries, covering: jugular venous waveform morphology and clinical meaning; right atrial pressure waveform features in heart failure; x and y descent, a and v wave abnormalities and the conditions they indicate (tricuspid regurgitation, AF, constriction, RV failure); jugular venous Doppler pattern and prognosis; quantitative features derived from JVP signals. Include explicit counter-evidence queries. Target 15 to 25 entries.
- [ ] **Step 4:** Run L4 searches with at least five queries, covering: JVP at discharge and outcomes; a single clinic JVP or IJV ultrasound measure and prognosis; spot measurement versus trend; elevated JVP with no independent prognostic value. Target 15 to 25 entries.
- [ ] **Step 5:** For each entry, fetch the publisher, PubMed or PMC page for the abstract and metadata. Apply the rules: label a truncated abstract `(truncated at source)`; mark `RETRACTED` or `CORRECTED` when the page says so, and set the stance note accordingly; label preprints; exclude patents and SlideShare; follow citations from the strongest results.
- [ ] **Step 6:** Commit both files with message `docs(lit): JVP waveform and single-measurement evidence (L3, L4)`.

### Task 5: L6 and L7 searches

**Files:**
- Create: `docs/papers/search/L6-radar-capture.md`, `docs/papers/search/L7-context-fusion.md`

**Interfaces:**
- Consumes: `known-papers.md`, the entry format and the rules from Task 4.

- [ ] **Step 1:** Run L6 searches with at least five queries, covering: FMCW, CW and mmWave radar jugular or neck venous signals; separating venous and carotid signals; waveform feature recovery; validation against ultrasound or catheter; motion artifact and signal quality. Target 8 to 15 entries.
- [ ] **Step 2:** Run L7 searches with at least four queries, covering: JVP or congestion combined with labs, medication or EHR data; multiparameter congestion assessment; ECG alignment of venous waveforms. Target 8 to 15 entries.
- [ ] **Step 3:** Fetch abstracts and metadata under the Task 4 rules.
- [ ] **Step 4:** Commit with message `docs(lit): radar capture and clinical context evidence (L6, L7)`.

### Task 6: L1, L2, L5 and L8 searches

**Files:**
- Create: `docs/papers/search/L1-hf-burden.md`, `L2-congestion.md`, `L5-bedside-limits.md`, `L8-display-cdss.md` in the same directory

**Interfaces:**
- Consumes: `known-papers.md`, the entry format and the rules from Task 4.

- [ ] **Step 1:** Run at least three queries per link, 8 to 15 entries each. L1 must include Indonesian heart failure burden and readmission. L8 covers clinician-facing data display, information overload, and adoption of assistive CDSS.
- [ ] **Step 2:** Fetch abstracts and metadata under the Task 4 rules.
- [ ] **Step 3:** Commit with message `docs(lit): burden, congestion, bedside and display evidence (L1, L2, L5, L8)`.

### Task 7: Summary, download list and verification

**Files:**
- Create: `docs/papers/search/README.md`, `docs/papers/search/download-list.md`
- Scratch: `verify_lit.py` in the session scratchpad

- [ ] **Step 1:** Write `verify_lit.py <search-dir>`. It parses `L*.md` and reports: any entry missing a field from the format; entries with neither an abstract nor the "abstract not retrieved" text; duplicates by DOI and by lowercased, punctuation-stripped title across all files; invalid `Stance` values; and the HTTP status of each URL, reporting 401, 403 and 429 separately as "blocked, not verified".
- [ ] **Step 2:** Run it. Fix missing fields. Merge duplicates into the entry for the strongest link, naming the other link in the note and keeping the published version over a preprint. Replace dead links or report them.
- [ ] **Step 3:** Fidelity review: choose every tenth entry, re-fetch its source page, and compare the abstract, authors, year and DOI character by character. Any mismatch means checking the rest of that file.
- [ ] **Step 4:** Write `README.md`: argument chain, per-link strength assessment including counter-evidence, named gaps, search log, the abstracts-only caveat, and absence findings worded "not found in these searches". L3 includes a table of waveform feature, condition, evidence quality and entries. L4 states plainly whether the evidence supports the value of a single measurement.
- [ ] **Step 5:** Write `download-list.md`: all entries by priority (L3, L4, L6, L7, then the rest), one line each with title, year, URL and link code, skipping papers the owner already has.
- [ ] **Step 6:** Re-run `verify_lit.py` and confirm no missing fields or duplicates. Commit the two new files and any corrected `L*.md` files with message `docs(lit): evidence summary and download list`.
