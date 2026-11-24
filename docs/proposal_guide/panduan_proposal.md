# Proposal Writing Guide (for the drafting agent)

This file tells you how to write the thesis proposal. The student has placed all materials and papers in the same folder as this file. Write the proposal text from this guide plus those materials. The student will do the Word formatting, so output plain text only.

**The proposal text itself must be written in Indonesian.** This guide is in English only because it is more compact for instructions. Indonesian wording in quotes below is for illustration.

Read sections 0 and 1 first, then write sections 2 and 3 in order.

---

## 0. Project context

The student is writing a final year thesis with a Biomedical Engineering research group that built a RADAR device measuring the jugular venous pulse (JVP) noninvasively and without contact. The student's job is the system on top of the device output: a system that takes RADAR measurement results, combines them with patient context from electronic medical records (RME), and uses a 12 lead ECG as a reference point, to support a doctor's clinical decisions. Patients can also save and send their data to another doctor or clinic (poli) when needed, like a mini SISFOR with RADAR cardiovascular data as an external source.

Working title (not final, ask the student if anything changed):

> Pengembangan Sistem Pendukung Keputusan Klinis Berbasis Interoperabilitas Data Rekam Medis Elektronik dan Pengukuran Kardiovaskular RADAR

Direction changed once. The first version was a FHIR profile for the RADAR device. The professor said the device is for measurement, not monitoring, so FHIR standardization is not the pressing need. The current version is a system that integrates RME, RADAR and ECG data for clinical decision support. Consequences:

* The contribution is the system (data management, integration, interoperability). It is not the interpretation algorithm and not the RADAR device.
* FHIR and SATUSEHAT stay as the RME side ecosystem and the interoperability bridge, not as the headline contribution.
* Do not call the RADAR device a "monitoring" device. The professor objected to that word. Use "pengukuran".
* Frame outputs as decision support. Never as diagnosis, prediction, or a validated risk score.

---

## 1. Style rules (apply to all proposal text)

**Language and tone**

* Indonesian, standard but readable, like a student who understands the topic. Not slang, not bureaucratic.
* Sound human. Vary sentence length. A paragraph may contain one short sentence in the middle. Avoid paragraphs that all follow the same neat pattern.
* Avoid cliché openers such as "Di era digital saat ini", "Seiring perkembangan teknologi", "Tidak dapat dipungkiri". Start from a concrete fact or problem.
* Do not stack connectors. "Selain itu", "Oleh karena itu", "Dengan demikian" are fine but not in every paragraph. Let the logic between sentences carry the flow.
* Avoid empty intensifiers ("sangat penting", "krusial", "signifikan") unless backed by a number or reason.
* No promotional tone. State limitations honestly.

**No hyphens**

* Do not use hyphens, em dashes or en dashes in the proposal text.
* Ways to avoid them:
  * Reduplicated words: rewrite or replace ("berbagai data" instead of "data-data").
  * Prefixed terms: write them solid ("nonivasif", "nirkontak", "antarsistem", "antarinstitusi", "multiparameter").
  * Foreign terms: use an Indonesian equivalent or italics without a hyphen ("gerakan mikro", not "mikro-gerakan").
  * Number ranges: use words ("1,2 sampai 1,4 juta kunjungan", not "1,2 - 1,4 juta").
  * Clauses set off by a dash: use a comma or split into two sentences.
* Unavoidable exceptions: DOIs, URLs, and page ranges in IEEE references (use an en dash there as IEEE requires).

**Format**

* Sections 1.1 to 1.5, 2.7 and all narrative text are flowing paragraphs, not bullet lists.
* Section 1.5 (Kontribusi) is one short paragraph, broad strokes only.
* In the literature review a table is allowed only when the material truly compares many items. Otherwise paragraphs.

**Citations (IEEE)**

* Numbered citations in square brackets: [1], [2]. Number by order of first appearance. A source keeps the same number every time.
* Multiple sources: [2], [3], or [4] sampai [6] (use the word "sampai", not a dash).
* Place the citation before the sentence end punctuation: "... turun setelah dicocokkan [4]."
* Reference list at the end, in numeric order. Shapes:
  * Journal: `[1] A. Author, B. Author, and C. Author, "Title," Journal Name, vol. X, no. Y, pp. 1–10, Month Year, doi: xx.`
  * Web page: `[2] World Health Organization, "Cardiovascular diseases (CVDs)." Accessed: Month Day, Year. [Online]. Available: URL`
  * Regulation: `[3] Menteri Kesehatan Republik Indonesia, "Peraturan Menteri Kesehatan Nomor 24 Tahun 2022 tentang Rekam Medis," 2022.`
  * Preprint: state that it is a preprint and the platform (medRxiv, arXiv).
* Never invent data or numbers. If a claim or figure is not in the folder materials, write a placeholder `[cite: ...]` or `[insert data: ...]` and do not fill it in yourself.
* Paraphrase. Avoid direct quotes; if unavoidable, very short.
* Do not cite patent filings or SlideShare decks.

---

## 2. Chapter I: Pendahuluan

### 1.1 Latar Belakang

Write five main paragraphs plus one short closing paragraph for the gap that bridges into the problem statement. Roughly six paragraphs, each about 5 to 8 sentences.

**P1. Cardiovascular disease and its noninvasive measurement**

Goal: open with the clinical problem for urgency. Start broad, narrow to heart failure and venous congestion.

Include:
* CVD burden worldwide and in Indonesia (figures from sources, not memory).
* Heart failure as an example needing repeated assessment because patients are at high risk of readmission after discharge.
* Venous congestion as an important marker, with central venous pressure (CVP) as the measure used, but accurate CVP needs invasive catheterization that is hard to do routinely outside hospital.
* JVP as a noninvasive indicator reflecting right atrial pressure, with bedside assessment depending on the examiner.

Sources available (see section 5): WHO, GBD Indonesia analysis, HF readmission study, residual congestion review, the 60 GHz study for the JVP definition and catheter limits.

Note: do not write that RADAR measures CVP directly. What it captures is the jugular venous pulsation as an indicator of right atrial pressure.

**P2. RADAR as a promising new modality**

Include:
* Short principle: RADAR uses the Doppler effect and backscatter to detect micro motion (heartbeat, chest motion from breathing, pulse) through phase changes in the radio signal. This is sensing, not imaging. Never write "citra RADAR". Write "data hasil pengukuran RADAR".
* Advantages: contactless, minimal preparation, no discomfort, compared with electrode based methods.
* Early work on contactless JVP with 60 GHz FMCW RADAR shows feasibility, with the honest caveat that it is a feasibility study with a very small sample.
* The research group's device produces data that can support doctor analysis outside clinic visits. Ask the student what the device outputs before writing details.

Sources: the 60 GHz paper and the contactless RADAR references in the folder.

**P3. Clinical decisions need patient data, not one device reading**

This answers the professor's thermometer critique. Explain that JVP is not an ordinary single number: it is a waveform with derived features whose meaning depends on patient context.

Include:
* One measurement becomes meaningful when read with diagnoses, medications, weight, lab results, previous visits, and change over time.
* Evidence: a propensity matched study found elevated JVP marks higher illness burden but, after matching, has no intrinsic association with mortality or hospitalization. So JVP should not be used as a standalone predictor.
* Balance it with another study finding elevated JVP before discharge linked to worse outcomes a year later, so the sentence does not overreach. Safe wording: JVP is more meaningful when read with context.
* The 12 lead ECG as a reference for RADAR data (explain its role per the folder materials, and ask the student if unclear).

**P4. RME and medical devices each have their own standardized formats and ecosystems**

Include:
* Patient context already sits in RME at large scale. Use 280 million people, 2,770 hospitals, 10,300 puskesmas and BPJS visit counts only after the sources are verified. These figures are currently unverified.
* Every visit must produce at least one RME document under Permenkes Nomor 24 Tahun 2022 tentang Rekam Medis. Write "Peraturan Menteri Kesehatan", not "Undang Undang PERMENKES".
* Patient generated health data (PGHD) is part of RME and its benefits are reported: patient awareness and participation, quality of life, less worry.
* Terminology standards have different scopes: ICD for disease classification, SNOMED CT for clinical terms, LOINC for observation and lab codes.
* National ecosystem: SATUSEHAT is based on FHIR R4 with identifiers such as NIK, IHS number and nomor RM; variables set by Keputusan Menteri Kesehatan Nomor HK.01.07/Menkes/1423/2022; UU Nomor 17 Tahun 2023 tentang Kesehatan requires health information systems and technology to follow standards.
* Devices such as portable and RADAR devices have their own output formats, different from RME.

Sources: folder materials (regulations, PGHD papers, SATUSEHAT). Verify each regulation's title and relevance before writing.

**P5. FHIR fills the interoperability gap between RME and the RADAR device**

Include:
* HL7 developed FHIR as an interoperability layer on REST API connecting medical devices, RME, administrative systems and doctors' notes.
* FHIR enables data exchange between devices and institutions, and between institutions.
* Here FHIR is the canonical format the system uses, not the main contribution. Do not claim the RADAR device needs FHIR because of one reading. Say the system needs it so RADAR, RME and ECG data can be read together and shared between doctors.

**P6 (closing). The gap**

Short, 3 to 4 sentences. Message: patient data and RADAR data are not connected, so doctors and patients struggle to compile everything in one consistent view, and patients struggle to save and send their data to another doctor or clinic. End with the bridge to the problem statement: a system connecting the two is needed.

Do not write "no study fuses radar JVP with RME data" as fact. That absence claim is unverified. State the gap from the system side and leave the absence of prior studies to section 2.6, which the student fills.

### 1.2 Rumusan Masalah

One paragraph. Departmental style: declarative (not a list of questions), describes the gap between current and desired state, ends with "dibutuhkan solusi ...".

Order of content:
1. The RADAR device unlocks contactless JVP measurement, but its data is supplementary, an aid to diagnosis and not decisive alone.
2. RME and other devices use different standards and formats.
3. Combining all parties needs an interoperability platform.
4. End with: a solution is needed in the form of a clinical decision support system that integrates RME, RADAR and ECG data interoperably (phrase it yourself, do not copy).

Use "pengukuran", not "pemantauan".

### 1.3 Batasan Masalah

One paragraph. Give a reason for each limit (departmental guideline).

Include:
* The RADAR device in question measures JVP only, and the system is designed for that device's output. Reason: it is the only device available from the research group and the basis of the system design.
* The RADAR device is out of scope (signal acquisition, I/Q processing, pulse detection and quantification belong to the research group). Reason: the thesis focuses on the system that receives measurement results.
* The main focus is the system integrating RME, RADAR and 12 lead ECG as a reference point.
* Suggested additions, confirm with the student first: RME data uses synthetic or test sources because real data needs ethics approval; outputs are decision support, not diagnosis, and not clinically validated.

### 1.4 Tujuan dan Manfaat

Two separate paragraphs.

**Tujuan (one paragraph).** Sentences in the form "untuk ...". Main goal: build an interoperability based clinical decision support system integrating RME data, RADAR JVP measurements and 12 lead ECG. Make it measurable (SMART) with placeholders where numbers do not exist yet, for example number of source formats supported, mapping completeness to the standard, success of sharing a record between doctors or clinics, end to end data flow correctness. Use `[insert data: target ...]` if targets are not set.

**Manfaat (one paragraph).** Name the produced results: design, method and prototype of the system. Benefits to doctors (seeing RADAR data with patient context in one view), patients (saving and sending data to another doctor or clinic), and health information system development. Note: the patient sharing feature is not yet confirmed by the professor as core versus extension, so keep the wording non binding.

### 1.5 Kontribusi

One short paragraph, broad strokes. Contribution to interoperability and system management in healthcare: an example pattern for integrating measurement data from a new device with standards based RME, and cross source data management for decision support. Do not claim clinical or algorithmic contributions.

---

## 3. Chapter II: Tinjauan Pustaka

The folder materials decide the content. Use the topics below as a frame. Each subsection is paragraphs explaining concepts, not one paper summary after another. Every claim carries an IEEE citation.

> **Subsection status**: Per user review of the draft proposal, subsections 2.1, 2.2, and 2.3 are acceptable. Subsection 2.4 (FHIR interoperability) needs a full structural rewrite — the current draft jumps between terminology, resource structure, device mapping, and pipeline without clear sub-paragraph logic. Subsection 2.5 and 2.7 are acceptable. See the detailed instructions per subsection below.

* **2.1 Cardiovascular disease, heart failure and venous congestion.** Burden (global + Indonesia), heart failure readmission, the vulnerable post-discharge phase, congestion phenotypes (4-compartment model per Núñez), CVP and JVP as markers, catheterization limits, multiparameter monitoring advantage, ESC 2026 recommendations.
* **2.2 Jugular venous pulse and noninvasive RADAR measurement.** JVP waveform physiology (a, c, v peaks; x, y troughs; ECG alignment), bedside assessment and its limits, Doppler and FMCW RADAR principle, phase-change detection, Six-Port 24 GHz dataset, linear correlation radar vs ultrasound (Shi et al. [34]), quality assessment SVM module, 60 GHz FMCW feasibility study (Das et al. [6]).
* **2.3 Electronic medical records and patient data.** Mandatory RME framework (Permenkes 24/2022 [16], Kepmenkes 1423/2022 [21], UU 17/2023 [22]), fragmentation evidence (Aisyah et al.: 30 apps per Puskesmas [18]), barriers in district hospitals (Savandha [24]), patient access rights and PGHD benefits (Tapuria [19]), decentralized access control (Purnama [17]), PGHD pipelines (Abedian Garmin [27], Wesley SMART on FHIR [28]), eSource concept (Garza [35]).
* **2.4 Interoperabilitas melalui Platform FHIR** — see detailed rewrite guide below.
* **2.5 Clinical decision support systems and data management.** CDSS definition and rule-based dominance, standalone problem, assistive framing, data flow architecture (ingest → quality check → context join → rules → display), microservices FHIR platform (~50k transactions/day), radar signal quality gating, ECG as temporal reference, CDS Hooks workflow trigger, standards-based accuracy results.

### Detailed rewrite guide for 2.4 (FHIR Interoperability)

This subsection must be rewritten with a clear **five sub-paragraph logical flow**. Do NOT mix topics across paragraphs.

**Sub-paragraph A — Terminology standards (ICD, SNOMED CT, LOINC)**

Goal: establish that clinical terminology standards solve the *semantic* question (what does this code mean?) before FHIR solves the *exchange* question. Source for statistics: Vorisek et al. [25] reports that 63% of FHIR implementations use additional terminology: LOINC (37%), SNOMED CT (29%), ICD-10 (18%). If the student cannot find a dedicated official source for ICD/SNOMED CT/LOINC definitions, use `[cite: dokumentasi resmi ICD, SNOMED CT, dan LOINC]` — do NOT invent a citation.

Content:
- ICD: disease and cause-of-death classification.
- SNOMED CT: clinical concept terminology (diagnoses, findings, procedures).
- LOINC: observation and laboratory test codes.
- Each answers a different question; none of them is a data exchange format.

**Sub-paragraph B — FHIR as modular exchange framework**

Goal: explain what FHIR is and what it does. Source: Vorisek et al. [25].

Content:
- HL7 FHIR structures data as modular resources (Observation, Patient, Encounter, DiagnosticReport, Device).
- Profiles constrain resources to specific use cases.
- REST API enables exchange between any system that speaks HTTP.
- Achieves syntactic *and* semantic interoperability in one framework.
- The 49-study systematic review: coverage across data capture (29%), standardization (41%), clinical analysis (12%).

**Sub-paragraph C — Device-to-FHIR mapping and its challenges**

Goal: explain that physical devices need a bridge. Source: Riech et al. [23].

Content:
- Medical devices use ISO/IEEE 11073-10207 as their data model — a different abstraction from RME.
- Systematic mapping to FHIR `Observation` and `Device` resources is possible through an Implementation Guide, preserving origin context.
- 25 technical challenges identified: metric context handling, device status representation, timestamp accuracy.
- Critical caveat: syntactically valid FHIR profile ≠ semantically correct data — explicit meaning validation is required.

**Sub-paragraph D — Real-time IoT-to-FHIR pipeline**

Goal: establish feasibility for streaming physiological time-series data. Source: Adochiei et al. [26].

Content:
- Open-source framework maps wireless biomedical sensor signals to FHIR Observation resources in real time.
- Demonstrated latency under 1 second, 0% packet loss.
- Validates the pipeline concept for RADAR output: raw measurement → FHIR Observation → server → display.

**Sub-paragraph E — Indonesia-specific: SATUSEHAT ECG IG and CDS Hooks**

Goal: connect global FHIR standards to the Indonesian SATUSEHAT ecosystem. Sources: Chaidir & Hareva [20], Strasberg et al. [29].

Content:
- Chaidir & Hareva [20]: Implementation Guide for 12-lead ECG compliant with SATUSEHAT FHIR R4. Maps HL7 aECG v1 → Observation + DiagnosticReport + Device. 17 core attributes from 312 aECG attributes. Provisional ValueSets for SNOMED CT gaps (13 of 32 lead types only).
- This IG serves as the methodological blueprint: the same approach applies to RADAR waveform data.
- CDS Hooks (per Strasberg [29]): separates clinical logic from the EHR codebase, enables event-driven triggering across institutions, resolves the "curly braces problem" of heterogeneous data access.

**Closing sentence of 2.4:**
Frame FHIR as the canonical format: one data model that holds RADAR, ECG, and RME data so they can be read together and shared across institutions.

If the folder materials do not fit this frame, follow the materials and tell the student in the closing notes.

### 2.6 Penelitian Terkait dan Kesenjangan Penelitian

**Leave empty.** The student already has this part. Write only the heading and one placeholder line `[diisi mahasiswa]`.

### 2.7 Rasional

At most two paragraphs. Base it on the literature review (2.1 to 2.5) and bring in no new facts that are not discussed there.

* Paragraph one: summarize the research logic from the literature. JVP and RADAR give interesting measurement data, but its meaning depends on patient context held in RME. RME and devices use different formats, so a standards based interoperability layer is needed.
* Paragraph two: state why the system (not the device, not an algorithm) is what gets built, how the 12 lead ECG serves as reference, and what the system should offer doctors and patients. End with the limit of the claim: the system supports decisions, it does not diagnose.

---

## 4. Corrections already flagged

* "Undang Undang PERMENKES No. 24 Tahun 2022" is wrong. Correct: Peraturan Menteri Kesehatan Nomor 24 Tahun 2022 tentang Rekam Medis. UU Nomor 17 Tahun 2023 tentang Kesehatan is correct as is.
* "data hasil citra RADAR" becomes "data hasil pengukuran RADAR".
* "pergerakan akustik micro" becomes "gerakan mikro" (mechanical motion, not acoustic).
* "Rekaman Medis Elektronik" becomes "Rekam Medis Elektronik".
* The old opening figures (280 million people, 2,770 hospitals, 10,300 puskesmas, 1.2 to 1.4 million BPJS visits per day in 2026) have no verified source yet.
* Watch the words "citra", "monitoring" and "diagnosis".

---

## 5. Source map (updated for citations [1]–[41])

> **IMPORTANT**: The proposal now uses citations [1]–[41] in IEEE first-appearance order. The new proposal text is the ground truth. This table is a reference guide — always verify numbers against the actual proposal before writing.

| New # | Author & Year | Paper File in `papers/` | Where Used in New Proposal |
|---|---|---|---|
| **[1]** | WHO (2022 data, accessed Oct 2026) | *External web* | Bab 1.1 P1, Bab 2.1 P1 |
| **[2]** | Muharram et al. (2024) | `P36 GBD...Indonesia.md` | Bab 1.1 P1, Bab 2.1 P1 |
| **[3]** | Tung et al. (2016) | `P23 Readmissions and HF.md` | Bab 1.1 P1, Bab 2.1 P1 |
| **[4]** | Metra et al. (2023) | `P26 Pre and Post discharge.md` | Bab 1.1 P1, Bab 2.1 P1 |
| **[5]** | Mullens et al. (2009) | *Secondary cite – cited in P25, P6* | Bab 1.1 P1, Bab 2.1 P3 |
| **[6]** | Das et al. (2024) | `P4 RADAR JVP.md` | Bab 1.1 P1/P2, Bab 2.1 P3, Bab 2.2 P2/P3 |
| **[7]** | Kenny et al. (2025) | `P6 JVP Doppler Ultrasound.md` | Bab 1.1 P1/P3, Bab 2.1 P3, Bab 2.2 P1, Bab 2.5 P2 |
| **[8]** | [Storrow? – INCOMPLETE] Am.J.Cardiol 2007, doi 10.1016/j.amjcard.2007.01.037 | *Secondary cite – cited in P4 Das* | Bab 1.1 P1, Bab 2.1 P3 |
| **[9]** | Schellenberger et al. (2020) | `P16 RADAR Dataset.md` | Bab 1.1 P2, Bab 2.2 P2, Bab 2.5 P2 |
| **[10]** | Suzuki et al. (2021) | `P5 mmWave JVP RADAR.md` | Bab 2.2 P3 |
| **[11]** | Yen et al. (2022) | `P13 RADAR Summary.md` | Bab 1.1 P2, Bab 2.2 P2, Bab 2.5 P2 |
| **[12]** | [Drazner? – INCOMPLETE] Am.J.Cardiol 2009, doi 10.1016/j.amjcard.2008.11.045 | *Secondary cite – cited in P24* | Bab 1.1 P3, Bab 2.1 P2 |
| **[13]** | Kasai et al. (2023) | *Secondary cite – cited in P26 Metra* | Bab 1.1 P3, Bab 2.1 P2 |
| **[14]** | Fudim et al. (2025) – SCALE-HF 1 | `P20 Noninvasive monitoring for HF.md` | Bab 1.1 P3, Bab 2.1 P2 |
| **[15]** | Weiner et al. (2022) – RCT JAMA | `P38 Effect of EHR for CDSS.md` | Bab 1.1 P3 |
| **[16]** | Permenkes 24/2022 | `UU PERMENKES 24 2024 TENTANG RME.md` | Bab 1.1 P4, Bab 2.3 P1 |
| **[17]** | Purnama et al. (2026) – IOTA DecMed | `P10 INDO RME Management FHIR.md` | Bab 1.1 P4, Bab 2.3 P3 |
| **[18]** | Aisyah et al. (2025) – DTO Kemenkes/UCL | `P29 Health information system...Indonesia.md` | Bab 1.1 P4, Bab 2.3 P1/P2 |
| **[19]** | Tapuria et al. (2021) – PGHD access | `P11 Impact of MIM.md` | Bab 1.1 P4/P5, Bab 2.3 P3 |
| **[20]** | Chaidir & Hareva (2025) – ECG IG SATUSEHAT | `P14 SSP Implementation Guide.md` | Bab 1.1 P5, Bab 2.4 P3, Bab 2.5 P2 |
| **[21]** | Kepmenkes 1423/2022 | `2022kepmenkes1423.md` | Bab 1.1 P4, Bab 2.3 P1 |
| **[22]** | UU No. 17 Tahun 2023 | `UU Nomor 17 Tahun 2023.md` | Bab 1.1 P4, Bab 2.3 P1 |
| **[23]** | Riech et al. (2021) – ISO/IEEE 11073 to FHIR | `P18 ISO to FHIR.md` | Bab 1.1 P4/P5, Bab 2.4 P2 |
| **[24]** | Savandha et al. (2026) – RSUD barriers | `P22 FHIR Implementation barriers Indonesia.md` | Bab 1.1 P4, Bab 2.3 P2 |
| **[25]** | Vorisek et al. (2022) – FHIR systematic review | `P2 FHIR Review.md` | Bab 1.1 P5, Bab 2.4 P1/P2 |
| **[26]** | Adochiei et al. (2024) – IoT FHIR real-time | `P9 IoT FHIR Implementation.md` | Bab 2.4 P2 |
| **[27]** | Abedian et al. (2025) – Garmin to FHIR | `P3 Garmin to FHIR.md` | Bab 1.1 P4, Bab 2.3 P3 |
| **[28]** | Wesley et al. (2021) – SMART on FHIR PGHD | `P8 FHIR Integration.md` | Bab 2.3 P3 |
| **[29]** | Strasberg et al. (2021) – CDS standards JAMIA | `P30 CDSS with FHIR.md` | Bab 1.1 P5, Bab 2.4 P3, Bab 2.5 P1/P3 |
| **[30]** | Kamil et al. (2020) – Indonesia doctor perceptions | `P28 Indonesia Doctor opinions.md` | Bab 1.1 P4 (implied) |
| **[31]** | Núñez et al. (2022) – 4-phenotype congestion | `P25 Biomarkers and HF.md` | Bab 2.1 P2 |
| **[32]** | Stevenson et al. (2023) – JACC remote monitoring | `P37 Remote Monitoring for HF.md` | Bab 2.1 P2 |
| **[33]** | Køber et al. (2026) – ESC Guidelines 2026 | `P24 Guidance for HF Management.md` | Bab 2.1 P2 |
| **[34]** | Shi et al. (2018) – CW radar carotid pulse linear | `P7 mmWave Carotid Pulse.md` | Bab 2.2 P2 |
| **[35]** | Garza et al. (2021) – eSource FHIR | `P21 eSource for FHIR and RME.md` | Bab 2.3 P3 |
| **[36]** | Papadopoulos et al. (2022) – rule-based CDSS review | `P35 Rule based CDSS review.md` | Bab 2.5 P1 |
| **[37]** | Hak et al. (2022) – CDSS systematic review PLOS | `P34 Systematic review for CDS.md` | Bab 2.5 P1 |
| **[38]** | Susanto et al. (2023) – ML CDSS scoping review | `P32 ML for CDSS review.md` | Bab 2.5 P1 |
| **[39]** | Semenov et al. (2019) – FHIR CDSS platform | `P27 FHIR and CDSS making.md` | Bab 2.5 P2 |
| **[40]** | Isabelle et al. (2025) – CQL CDS Hooks eval | `P33 EHR, Interoperability and CDSS.md` | Bab 2.5 P3 |
| **[41]** | Morgan et al. (2022) – CDS Hooks RCT 130% | `P31 CDSS with FHIR and SMART.md` | Bab 2.5 P3 |

**Open placeholder `[new]` × 2**: A JVP two-object method study (4 resident doctors, 40 patients, reliability 82.9%, sensitivity 43.3%, specificity 67.7%) is cited in Bab 1.1 P1 but the paper has not been identified. Use `[new]` placeholder until the student supplies it.

**Incomplete citations**: [8] Storrow (authors/title blank, doi available) and [12] Drazner (authors/title blank, doi available) — student must complete from the actual papers. [26] Adochiei DOI is a placeholder.

**Unverified / unused claims** (same as before; do not write without a verified source):
- CVP as early warning of HF worsening (no folder source → write "kongesti" instead)
- SATUSEHAT lacks uniform access control (unverified)
- 280 million people, 2,770 hospitals, 10,300 puskesmas, BPJS visit counts (unverified)
- Remote video JVP (PMC7330819) — unverified, do not cite
- Drazner N. Engl. J. Med. 2001 (PMID 11529211) — unverified, do not cite; use Am. J. Cardiol. 2009 placeholder [12] instead

---

## 6. Open questions for the student

* Exact RADAR output per session (pulse rate, intervals, amplitude, waveform morphology?), number of subjects and sessions, any repeated measures.
* The role of the 12 lead ECG: reference for validating what, and where its data comes from.
* RME data source: synthetic, SIMRS export, or SATUSEHAT staging.
* Whether patient save and send to another doctor or clinic is core to the research.
* Whether the RADAR data really goes beyond JVP (the title says "kardiovaskular").
* Final title.
* **`[new]` placeholder citation (×2 in Bab 1.1 P1)**: The proposal cites a study on the JVP two-object method with reliability 82.9%, sensitivity 43.3%, specificity 67.7%, tested by four resident doctors on 40 patients. The paper has not been identified. The student must supply the full citation before submission. The doi 10.1016/j.amjcard.2007.01.037 (Am. J. Cardiol. vol. 99, no. 11, 2007) is a candidate — verify whether it matches the figures.
* **Incomplete citations [8] and [12]**: Authors and titles are blank in the DAFTAR PUSTAKA. [8] doi: 10.1016/j.amjcard.2007.01.037; [12] doi: 10.1016/j.amjcard.2008.11.045. Student must retrieve full bibliographic data from these papers.
* **[26] Adochiei DOI**: Marked as `[cite: lengkapi DOI]`. Retrieve from the paper or journal website.

If this guide conflicts with the folder materials, follow the materials and note the conflict at the end of the output.

---

## 7. Output format

* One text document in this order: 1.1, 1.2, 1.3, 1.4, 1.5, then 2.1 to 2.7, then the IEEE reference list.
* Each subsection has a numbered heading exactly as in the structure above.
* After the text, add "Catatan untuk mahasiswa": claims that use placeholders, sources not found in the folder, and open questions.
* Before handing off, check: no hyphens or dashes in the text, no bullet lists in narrative, all citations numbered in order, no numbers without a source.
