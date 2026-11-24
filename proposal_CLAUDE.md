# Thesis Handoff: CDSS for RME, RADAR JVP and 12-Lead ECG

Read this before thesis work. **Since 2026-11-18 the system is a working prototype** (see `docs/handover/2026-11-18-handover.md` for methods, numbers and status; since 2026-11-19 it is also hosted at `https://prata.haifa.workers.dev`, see `docs/handover/2026-11-24-handover.md`); the next thesis task is Chapter III and the presentation update, spec `docs/design/specs/2026-11-18-proposal-development-design.md`. It records the current direction (as of 2026-11-03), scope, urgency argument, what is wrong or unverified in the draft, and open questions. Anything marked **TODO-verify** has not been confirmed. The draft itself is `docs/proposal_md/proposal.md`; if the two disagree on content, check the draft and update this file.

---

## 1. Project in One Paragraph

The student is writing a final-year thesis (tugas akhir, **in Indonesian**) with a Biomedical Engineering RADAR research group whose device measures the **jugular venous pulse (JVP)** non-invasively and contactlessly. The student builds the system on top of the device output: it takes RADAR measurement results, combines them with patient context from electronic medical records (RME), and uses a 12-lead ECG as a reference point, to support a doctor's clinical decisions.

**Working title (not final):**
*Pengembangan Sistem Pendukung Keputusan Klinis Berbasis Interoperabilitas Data Rekam Medis Elektronik dan Pengukuran Kardiovaskular RADAR*

**Final objective:** a working website that takes in RME, RADAR JVP and 12-lead ECG data and displays it visually and efficiently in one view for the doctor.

**Next phase:** literature deepening to strengthen the justification and urgency, JVP signal link to cardiovascular health first. Spec: `docs/design/specs/2026-11-03-literature-deepening-design.md`. Results: `docs/papers/search/`.

---

## 2. Direction History (so the next session does not relitigate)

**Current direction: CDSS. Versions below are superseded.**

1. **FHIR profile for the RADAR JVP device.** Superseded.
2. **Professor's critique (2026-10-13):** the device is a *measurement* tool, not a *monitoring* tool, so there is little urgency for FHIR standardization. His analogy: one thermometer reading does not need a FHIR environment. He suggested a higher level of health analytics.
3. **Context-aware decision support explored (2026-10-14 to 10-16).**
4. **Brief return to the FHIR profile (2026-10-19).** Superseded.
5. **CDSS adopted (`proposal.md`, 2026-10-26; confirmed by the student 2026-11-03).** The profile work survives only as the interoperability layer inside the system.

**Open risk:** the professor's objection still needs an evidence-backed answer. See section 5.

---

## 3. Scope Boundary

- **RADAR group's work:** device, signal acquisition, I/Q processing, detection and quantification of pulses and intervals.
- **Student's work:** the system after the quantified output: data intake, mapping RADAR, ECG and RME to FHIR as the canonical format, data management, and the integrated display.
- **Required:** the integrated display. It is the decision support; the doctor decides. Source [38] supports this reading: adopted CDSS are mostly assistive and present a synthesis.
- **Optional only if time remains:** rule-based flags or recommendations.
- **Limits:** RME data is synthetic or test data, because real data needs ethics approval. Output is not diagnosis, prediction or a validated risk score, and is not clinically validated. No signal-processing or interpretation algorithm contribution. No hosted SATUSEHAT connection. No usability study or hospital deployment.
- **Existing base:** the local FHIR R4 walking-skeleton server. See `CLAUDE.md`.
- **Not designed yet:** the website architecture, including ECG intake. It gets its own brainstorm after the literature phase.
- **TODO (ask the RADAR group):** exact output fields per session (interval definitions, waveform samples or timings only, sampling rate), number of subjects and sessions, intended use setting.

---

## 4. Fishbone

The current fishbone is `docs/presentation/ets/fishbone.md`, with the head: RADAR JVP data, RME context and 12-lead ECG are not connected, so the doctor cannot easily assess congestion in one view. Any `.svg` fishbone in the repo is generated from that file, which remains the source. Items marked (?) there are unverified.

---

## 5. Urgency Argument

**Concede first:** the device is a point-of-care measurement device. The thesis must not depend on long-term monitoring.

The argument is a chain. A weak link weakens everything after it. The literature phase tested each link. See `docs/papers/search/README.md` for the assessment, based on abstracts until the student reads the papers. **L6 (radar) is now the weakest link. JVP outcome evidence is about wave shape and depth, and carotid interval evidence comes from echo and Doppler. No JVP interval outcome study was found. Ask the RADAR group whether X and Y descent depth is available and which carotid intervals they report.**

| Link | Claim | Current support |
|---|---|---|
| L1 | Heart failure burden and readmission are high | [1] to [4]; Indonesian HF-specific figure still missing |
| L2 | Residual congestion drives readmission; venous pressure rises before symptoms | [4], [31], [32]; implanted-monitor studies in `docs/papers/search/L2-congestion.md` |
| L3 | JVP waveform features carry cardiovascular information beyond a single height value | [7], plus Harada 2019, 2023, 2024 (deep Y descent, HR 2.05, 3.15, 2.68, one group), pending reading |
| L4 | A single measurement at discharge or in clinic has value. Answers the thermometer objection | [13] and Drazner 2001; [12] argues against. Contested, pending reading |
| L5 | Bedside assessment is limited, so objective measurement is needed | [6], [8]; two-object-method figures still marked `[new]` |
| L6 | RADAR captures those features, not only the pulse | [6], [10]; small feasibility studies. **Weakest link** |
| L7 | JVP is only meaningful with context, so combining it with RME and ECG is justified | [7], [12], [14], [15] |
| L8 | Integrated display helps clinicians | [36] to [38] |

**Answer to the thermometer analogy:** a thermometer reading has a universal reference range, while JVP is a waveform whose reading varies between patients and only means something alongside their context. This depends on L3, L4 and L7 holding up.

**Honest weaknesses, do not overclaim:**
- The device is a research prototype, so the need is partly anticipatory.
- No evidence found so far that radar yields calibrated pressure (cmH2O). Do not imply it replaces CVP.
- Das [6] is a small feasibility study with one catheter comparison.
- [12] is real counter-evidence. Present it, then show why context answers it.

**Factual correction for the professor (he believed JVP is only invasive or PPG):** three levels exist: invasive CVP via catheter, bedside exam, and newer non-invasive sensing (camera, PPG, ultrasound, radar).

---

## 6. Draft Status and Fix List

**State of `proposal.md`:** BAB I and BAB II drafted, 2.6 empty, BAB III not written. Presentation outline: `docs/presentation/ets/outline_sidang_proposal_v2.md`. BAB II blueprint: `docs/proposal_md/bab2_outline.md`.

**Open items. Record only: the student edits the draft.**

1. **Output framing conflict.** 1.4 says "kelengkapan pemetaan dan diagnosa penyakit kardiovaskular", while 1.3 and 2.7 say the output is not a diagnosis.
2. **Recommendations.** 2.7 says "Seluruh luaran rekomendasi". Soften to match the display-first objective.
3. **Possible number error.** 1.1 says "10,9% pasien dirawat ulang dalam 30 hari dan 27% dalam enam bulan", while BAB II gives "mortalitas enam bulan 27,66%" from the same source [3]. The fishbone also marks this "cek angka". Check against the paper.
4. **Clinical wording.** 1.1 says "Gagal jantung berupa salah satu gejala fisiologis yang umum ditemukan dari stroke dan IHD". Heart failure is a syndrome, not a symptom, and the stroke link needs a source.
5. **Terminology.** 1.1 still says "pergerakan akustik jantung". The motion is mechanical.
6. **Placeholders.** `[new]` in 1.1; "Survey oleh cite"; "terbuktikan oleh cite"; "Studi oleh di RSUD"; "Survei lintas Puskesmas oleh mencatat"; `[cite: ...]` markers; the citation-repair notes at the end of the file.
7. **Missing content.** 2.6 is `[diisi mahasiswa]`, and BAB III is not written.
8. **PGHD definition.** 1.1 says "diluar kunjungan klinis", but data collection is planned in a polyclinic. Decide whether RADAR data counts as PGHD here. The same paragraph also says "alat monitoring", which is acceptable only as general PGHD background.
9. **Patient features.** 2.7 says the platform facilitates patients "menyimpan dan membagikan data". The supervisor has not confirmed this is committed.
10. **Source [12].** Identified on 2026-11-03: Meyer et al., Am J Cardiol 2009, doi 10.1016/j.amjcard.2008.11.045, a propensity-matched analysis of the DIG trial. 1.1 wrongly calls it "Suatu studi meta analisis", and the catalogue wrongly names Drazner.
11. **Source [13].** The title, pages and DOI (ihj.23-181) do not match the paper found: Kenichi Kasai et al., "Jugular Venous Pressure and Kussmaul's Sign as Predictors of Outcome in Heart Failure", ihj.23-183. Check the student's copy.
12. **Source [6].** Cited as a preprint. A peer-reviewed version exists: Royal Society Open Science 2025, doi 10.1098/rsos.242231.

---

## 7. Evidence Gathered Before the Literature Phase (2026-10-16)

From searches, not all read in full. New results go to `docs/papers/search/`.

**Invasive CVP:** gold standard but impractical pre-hospital, with risks including infection, thrombosis and arrhythmia (VenCoM paper, Medical Devices: Evidence and Research). Impractical after discharge (PMC10898581). CVP is a poor static marker and trend is more useful (MDedge pitfalls review), which cuts against L4.

**Bedside exam:** blinded catheter comparison, correlation with CVP 0.57 (external JVP) and 0.50 (internal JVP), CVP often underestimated (Deol et al., Chest 2011, PMID 20798190). **Counterpoint:** expert HF clinicians estimate right atrial pressure reasonably well (PMC2744520). Say operator-dependent and hard to standardize, not useless.

**Non-invasive sensing:** handheld ultrasound had a higher imaging success rate than inspection, but obesity still reduced accuracy (Wang et al., Ann Intern Med 2021, via a summary). IJV ultrasound shows inter-observer variability for some parameters (Italian Journal of Medicine, 2026).

**Radar:** the 60 GHz FMCW study (PMC12187424; preprint medRxiv 2024.06.04.24308313) validated morphology against PPG, and compared with catheter data from **one** early-stage HF patient. Peer-reviewed version: Royal Society Open Science 2025 (section 6, item 12).

**Heart failure link:** elevated JVP was the only congestion sign independently associated with 60-day rehospitalization, HR 1.64, in 1,551 patients (ESC Heart Failure, **TODO-verify**). Rehospitalization up to 50% in six months (PMC10898581), 30 to 60% (PMC2744520).

**Not found yet:** Indonesian heart failure burden figure; any radar JVP plus RME fusion work. Treat absence as "not found in searches", never as proof.

**Source rules:** check peer-review status and dates. Do not cite patents or SlideShare.

---

## 8. FHIR and SATUSEHAT Background

- FHIR and SATUSEHAT facts live in `docs/reference/claude/` (start at `INDEX.md`). Do not restate them here.
- **Role in the thesis:** canonical format so RADAR, ECG and RME can be read together. Chaidir and Hareva [20] is the Indonesian 12-lead ECG precedent. Riech [23] warns a syntactically valid profile does not guarantee semantic correctness.
- **Regulation:** Permenkes 24/2022 [16], Kepmenkes HK.01.07/Menkes/1423/2022 [21], UU 17/2023 [22]. **TODO-verify:** UU PDP 27/2022 and PP 71/2019 relevance.
- **Open:** whether LOINC or SNOMED codes exist for JVP, carotid and IJV time intervals. **TODO-verify.**

---

## 9. Research Logistics (consultation notes, 2026-10-15)

Source: `docs/notul/konsultasi_15okt.txt`. Informal notes; confirm before relying on them.

- Four students sit in one research tree: two on arrhythmia from pulse, one on JVP detection, and this thesis on the role-based informatics system.
- Data collection is at Soetomo, in a polyclinic rather than inpatient. A general polyclinic was suggested as faster than the vascular one.
- USG is the validator for JVP. The polyclinic has no equipment for measuring veins and arteries, so that work goes through the echo division.
- Sample size discussed: 100 people, possibly more than one month in total.
- Contacts: Dr. Ruth (arrhythmia and AFib, ECG focus); Dr. Irawati (echo division, controls the USG and samples); Dr. Kevin (vascular, performs or directs the venous work).

---

## 10. Open Questions

- [ ] **Professor:** does the CDSS direction and display-first objective answer the critique? Is patient save-and-send committed?
- [ ] **RADAR group:** output fields, interval definitions, subjects and sessions, reference measurements.
- [ ] Is the data source for 12-lead ECG real or synthetic? The draft only states RME is synthetic.
- [ ] Fill 2.6 and write BAB III, after the literature phase.
- [ ] Work through the fix list in section 6.
- [ ] Final title.

---

## 11. Working Preferences

- Respond in the language the user writes in; thesis text is **Indonesian**. The user is casual in chat and sometimes mixes languages.
- Style, format and citation rules for proposal text: `docs/proposal_guide/panduan_proposal.md`. These include no hyphens, flowing paragraphs, IEEE citations and a short kontribusi.
- Use bracketed placeholders (`[cite: ...]`, `[insert data: ...]`). Never invent figures.
- Mark absence claims and uncertain facts as TODO-verify.
- Frame the output as decision support, never as diagnosis, prediction or a validated risk score. Use "pengukuran" for the RADAR device.
- Paraphrase sources; keep any quote very short.
- The student reads papers before they enter the proposal. Search results do not go into `proposal.md` automatically.
