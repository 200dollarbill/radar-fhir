# CLAUDE.md: Thesis Handoff (FHIR Profile for RADAR JVP Device Interoperability)

Read this first. It records the thesis direction as it stands (as of 2026-10-19), what has been drafted, what is wrong or unverified in the draft, the evidence gathered, and the fishbone plan. Anything marked **TODO-verify** has not been confirmed.

---

## 1. Project in One Paragraph

The student is writing a final-year thesis (tugas akhir, **in Indonesian**) in collaboration with a Biomedical Engineering RADAR research group. The group's device measures the **jugular venous pulse (JVP)** non-invasively and contactlessly with radar (FMCW / Doppler, I/Q signals). The device takes **time-interval measurements of the JVP, carotid artery and internal jugular vein (IJV)**. The student's contribution is the **interoperability layer**: a FHIR R4 profile, aligned with SATUSEHAT, that represents the device's measurement output (signals, derived features, interpretation status, device metadata), plus a full-stack reference implementation that proves the profile works end to end on real measurement data.

**Title (decided, not changing anymore):**
*Pengembangan Profil Fast Healthcare Interoperability Resource (FHIR) Untuk Interoperabilitas Perangkat RADAR Pendeteksi Jugular Vein Pulse*

---

## 2. Direction History (so the next session does not re-litigate)

1. **Version 1:** FHIR profile for the RADAR JVP device (the current direction).
2. **Professor's critique (2026-10-13):** the device is a *measurement* tool, not a *monitoring* tool, so there is little urgency for FHIR standardization. His analogy: like a thermometer, one reading does not need a FHIR environment. He suggested a higher level of health analytics.
3. **Version 2 (explored, 2026-10-14 to 10-16):** context-aware clinical decision support / interpretation system over RME + RADAR data. Explored in depth, including an urgency argument and verified JVP literature.
4. **Decision (2026-10-19): the student returns to Version 1** (title and topic unchanged). The Version 2 work is kept only as supporting material for the urgency argument and the clinical background. **Do not rewrite the thesis around decision support.**

**Open risk:** the professor has not accepted the urgency of Version 1. The defense in section 5 must be prepared before the next meeting.

---

## 3. Scope Boundary

- **RADAR group's work:** device, signal acquisition, I/Q processing, detection and quantification of pulses and intervals.
- **Student's work:** everything after the quantified output: mapping to FHIR, profile design (StructureDefinition, IG), SATUSEHAT-aligned resource design, ingestion, validation, role-based full-stack system (patient, doctor, admin), round-trip integrity testing.
- **Out of scope (state as limits):** signal-processing algorithms, clinical validation of the device, usability testing, hospital deployment, hosted connection to the live SATUSEHAT platform (BAB II already says the discussion is limited to profile compatibility, not hosted connection; **check this is consistent with the batasan masalah**).
- **TODO (ask the RADAR group):** exact output fields per session (interval definitions, waveform samples or timings only, sampling rate), number of subjects and sessions, repeated measures, any reference measurement (echo, catheter, clinical exam), intended use setting (outpatient, post-discharge, bedside), any hospital or ethics partner.

---

## 4. Fishbone Plan (cause-and-effect diagram)

**Fishbone logic:** the head is the problem; each bone is a *cause category* explaining why the problem exists, not just a topic heading. Phrase every bone as a cause.

**Head (effect):** RADAR JVP measurement output cannot be recorded in RME or exchanged through SATUSEHAT in a standard, semantically consistent way.

### Student's original four bones
1. **FHIR system** (resources, REST, profiling, IG, validation tools)
2. **Peraturan Kemenkes & UU** (Permenkes 24/2022, Kepmenkes HK.01.07/Menkes/1423/2022, UU 17/2023)
3. **RADAR for JVP and RADAR as wearable/portable device** (note: the student said "three" but listed four items)
4. **Interoperability as the main benefit in IoT devices**

### Suggested additional bones (to cover "almost all relevant material")
| # | Bone (cause) | Sub-branches | Why add it |
|---|---|---|---|
| 5 | **Clinical context of JVP and cardiovascular disease** (urgency) | HF rehospitalization burden; invasive CVP vs bedside exam vs non-invasive sensing; why spot measurements still enter RME | Answers the professor's urgency objection; currently missing from the background |
| 6 | **Terminology and coding gap** (semantic interoperability) | ICD, SNOMED CT, LOINC; UCUM units; absence of a standard code for radar JVP/carotid/IJV intervals (**TODO-verify**) | The draft names the standards but not the specific gap |
| 7 | **Device-output data modelling** | Raw signal vs derived features vs interpretation; Observation (component), DiagnosticReport, Device, Provenance; sampled-data representation; time/interval semantics | This is the core design problem of the profile |
| 8 | **Data quality, provenance and measurement conditions** | Radar-subject distance, motion, posture, SNR; device identity, firmware, algorithm version; flagged-unreliable status | Related work shows RADAR output needs context metadata to be reusable |
| 9 | **PGHD in RME** | PGHD benefits (engagement, QoL, reduced worry); clinician trust; integration into workflow | Already in P1 of the draft; promote to its own bone |
| 10 | **Security, privacy and data governance** | UU PDP 27/2022, PP 71/2019 (**TODO-verify**), SATUSEHAT OAuth 2.0, no uniform access control across institutions (IOTA paper), consent | Health data; regulators and examiners will ask |
| 11 | **Medical-device regulatory status** | Alat kesehatan registration, research-prototype status, why outputs are framed as measurements not diagnoses (**TODO-verify** applicable Indonesian rules) | Explains scope limits honestly |
| 12 | **Implementation and validation methodology** | FSH/SUSHI, IG Publisher, HL7 FHIR Validator, round-trip testing, role-based dashboards, source adapters; validator pass is not clinical correctness | Defines how the contribution is measured |
| 13 | **Related work and gap** | ISO/IEEE 11073-10207 to FHIR IG; SATUSEHAT ECG IG (Chaidir and Hareva); FHIR biosignal framework; RADAR-IoT; Garmin to FHIR; radar vital-sign systems | Draws the boundary of novelty |

**Recommendation:** a readable fishbone has about 6 to 8 main bones. Suggested grouping if it gets crowded: merge 7+8 ("data modelling and quality"), merge 10+11 ("regulation, privacy and device status" under bone 2), and keep 9 as a sub-branch of bone 4. That leaves bones 1, 2, 3, 4, 5, 6, 7, 12, 13 (or fewer).

### Mapping to BAB II headings (current draft)
- Interoperabilitas Data Kesehatan -> bones 4, 6, 9
- Layer Interoperabilitas FHIR -> bone 1
- SATUSEHAT Sebagai Standar Nasional -> bone 2 (add bone 10/11 content)
- Pembuatan dan Validasi Profil FHIR -> bones 7, 12
- Monitoring Kesehatan Berbasis RADAR -> bone 3 (rename heading, see section 6; add bones 5 and 8)
- Penelitian Terkait dan Kesenjangan -> bone 13
- **Missing subsections:** clinical JVP context (bone 5), terminology gap (bone 6), security and privacy (bone 10).

---

## 5. Urgency Defense (for the professor)

**Concede first:** the device is a *point-of-care measurement* device, not a continuous monitoring device. The student previously answered "monitoring", which weakened the argument. The thesis must not depend on long-term monitoring.

**Arguments:**
1. **Spot measurements still enter RME.** A single blood pressure reading is also a spot measurement, yet it is recorded as a structured Observation. The need is not continuity but structured, interpretable, exchangeable recording.
2. **JVP output is not a single scalar.** It is waveform-derived time intervals across JVP, carotid and IJV, with measurement conditions. There is no ready code or profile for it, so each integration would be ad hoc.
3. **A thermometer reading has a universal reference range; these intervals vary between patients.** They only become meaningful when stored with patient context, quality information and device provenance, which is exactly what a profile enforces.
4. **Interoperability is a precondition for validation.** The correlation between radar intervals and clinical status is not established. A standard representation lets future studies pair measurements with RME data (diagnoses, labs, medications). State this as a precondition, not as present demand.
5. **The device itself is not the thesis.** Whether a contactless method should exist is the RADAR group's justification. The thesis starts after the measurement exists.

**Honest weakness:** the device is a research prototype, so the need is anticipatory. Do not overclaim urgency.

**Factual correction for the professor (he believed JVP is only invasive or PPG):** three levels exist: (a) invasive CVP via catheter (gold standard); (b) bedside clinical exam (non-invasive but subjective); (c) newer non-invasive sensing (camera, PPG, ultrasound, radar).

---

## 6. Thesis Document Status

Department guideline for the proposal:
- **Rumusan masalah:** declarative or question form, gap between current and desired state, avoid many questions.
- **Batasan masalah:** optional, with reasons.
- **Tujuan dan manfaat:** "untuk ..." goals, SMART; manfaat names the design/method/prototype produced.
- **Kontribusi:** useful results for specific fields.

**Format preferences:** batasan, rumusan, tujuan/manfaat and kontribusi are **flowing paragraphs, not lists**; kontribusi is **one short paragraph, broad strokes**. Rumusan ends with "Dibutuhkan ..." rather than numbered questions.

### Draft contents (latar belakang, as of 2026-10-19)
- P1: scale of Indonesian clinical data (280 million people, 2,770 hospitals, 10,300 puskesmas [1]; BPJS 1.2-1.4 million visits per day in 2026; Permenkes 24/2022); PGHD is part of RME [2]; PGHD benefits [3][4].
- P2: PGHD needs standardization; ICD, SNOMED CT, LOINC; need for a connector [5].
- P3: HL7 FHIR on REST API [6].
- P4: SATUSEHAT on FHIR R4, identifiers NIK, IHS number, Nomor RM [7][8]; Kepmenkes 1423/2022 [9]; UU 17/2023 [10].
- P5: wearable and portable devices generate PGHD, multi-parameter modalities [11].
- P6: RADAR via Doppler/backscatter, contactless; radar data as PGHD; standardized recording needed for SATUSEHAT interoperability [12].
- Rumusan, batasan, tujuan/manfaat, kontribusi: written around the FHIR profile plus full-stack reference implementation (validator pass target, round-trip integrity). BAB II drafted with six sections; Tabel 2.1 (related work comparison) is still empty.

### Issues found in the current draft (fix list)
1. **"Monitoring" wording conflicts with the professor's point and with the device.** "perangkat monitoring berbasis RADAR" appears in rumusan, tujuan, kontribusi and BAB II heading "Monitoring Kesehatan Berbasis RADAR"; P5-P6 also say "monitoring kontinu". Replace with "pengukuran" / "perangkat pengukuran berbasis RADAR" for the JVP device. Keep "wearable/portable" only as general background, and state that this device is a spot-measurement device.
2. **No JVP clinical context in the latar belakang.** JVP is never explained (right atrial pressure, heart failure). Add a paragraph (bone 5).
3. **"Undang Undang PERMENKES No. 24 Tahun 2022" is wrong** in the latar belakang (BAB II already says it correctly). Use "Peraturan Menteri Kesehatan (Permenkes) No. 24 Tahun 2022 tentang Rekam Medis".
4. **Terminology:** "data hasil citra RADAR" -> "data hasil pengukuran/sensing RADAR" (not imaging); "pergerakan akustik micro" -> "mikro-gerakan" (mechanical, not acoustic); "Rekaman Medis Elektronik" -> "Rekam Medis Elektronik"; "Salahsatu" -> "Salah satu".
5. **Citation numbers may collide across sections:** [5] is used for PGHD standardization (latar belakang P2) and for a systematic review of FHIR in research (BAB II); [6] is used for HL7 FHIR (P3) and for the FHIR biosignal framework (BAB II); [12] is used for radar backscatter (P6) and for the Schellenberger dataset (BAB II); [4] is used for PGHD benefits and for Garmin-FHIR. **TODO-verify** that these are the same sources or renumber.
6. **Kepmenkes 1423/2022 is described two different ways** ("pengembangan sistem elektronik dalam ekosistem alat medis berbasis SSP" vs "pedoman variabel dan metadata RME"). **TODO-verify** the actual title and subject.
7. **Statistics in P1** (hospital counts, BPJS visits) need verified sources, and "2026" visit figures need checking.
8. **"Diagnosis" definition of health technology** (UU 17/2023) is quoted loosely; **TODO-verify** the exact wording.
9. **Latar belakang P6 says radar data "dapat divalidasi dan digunakan oleh pekerja klinis"**; the device is not clinically validated. Soften to "berpotensi".
10. **Batasan vs BAB II:** the batasan says the profile is generalizable to other RADAR devices but proof is limited to one device; keep this wording consistent in rumusan and kontribusi.

---

## 7. Evidence Gathered (JVP clinical context, verified via search on 2026-10-16)

**Invasive CVP (catheter):** gold standard but time-consuming, impractical in pre-hospital settings, with risks including infection, catheter-induced thrombosis and arrhythmias (Medical Devices: Evidence and Research, VenCoM paper). Invasive measurement guides treatment in hospital but is impractical after discharge (PMC10898581). CVP is a poor static marker; trend is more useful than a single reading (MDedge pitfalls review).

**Bedside exam:** less reliable due to human limitations (PMC10898581). Blinded catheter comparison: correlation with CVP 0.57 (external JVP) and 0.50 (internal JVP), CVP often underestimated (Deol et al., Chest 2011, PMID 20798190). Catheter studies show inconsistent correlation (PMC6181725). Difficulties: neck adiposity, anatomical variability, positioning (radar feasibility paper). **Counterpoint:** expert HF clinicians estimate right atrial pressure reasonably well from JVP (PMC2744520). Do not call the exam useless; say operator-dependent and hard to standardize.

**Non-invasive sensing:** handheld ultrasound had a higher imaging success rate than visual inspection but obesity still reduced accuracy (Wang et al., Ann Intern Med 2021, via Clinician.com summary). IJV ultrasound shows inter-observer variability for some parameters (Italian Journal of Medicine, 2026). A device paper states there is a lack of non-invasive methods accurate enough to replace invasive CVP and easy enough for routine outpatient and home use.

**Radar feasibility (closest to the device):** 60 GHz FMCW study (PMC12187424; preprint on medRxiv 2024.06.04.24308313). Validated morphology against simultaneous PPG and compared with previously recorded catheter data from **one** early-stage HF patient. Not validated against CVP. **TODO-verify** journal and peer-review status (figshare supplementary suggests Royal Society Open Science, article 242231). Radar yields pulsation waveforms and timings; **no evidence found that it yields calibrated pressure (cmH2O)**, so do not imply it replaces CVP.

**Link to cardiovascular disease (heart failure):**
- Rehospitalization after HF admission: up to 50% in six months (PMC10898581) and 30-60% (PMC2744520); cite the range.
- Residual congestion is a target to prevent readmission (Cardiac Failure Review 2025, PMC11959577).
- Elevated JVP was the only congestion sign independently associated with 60-day HF rehospitalization, HR 1.64, in 1,551 patients (ESC Heart Failure).
- Congestion score (including JVP) associated with mortality and rehospitalization (Am J Cardiol, Duke record).
- **Counterweight:** propensity-matched study (Meyer et al., Am J Cardiol 2009, PMID 19268742): elevated JVP is a marker of higher illness burden with no intrinsic association with mortality or HF hospitalization after matching. Supports reading JVP with context, not alone.

**Not found / still open:** Indonesian heart failure burden figure; any radar JVP plus RME/patient-context fusion work (absence claim, **TODO-verify** with a targeted search before asserting).

**Source caveats:** several items are preprints, trial pages or abstracts; check peer-review status and dates. Do not cite patents or SlideShare decks that surfaced in searches.

---

## 8. FHIR / SATUSEHAT Background

- **FHIR R4** (HL7): REST API, JSON/XML resources; profiling constrains resources via `StructureDefinition`; IGs package profiles. Tools: FSH/SUSHI, IG Publisher, HL7 FHIR Validator.
- **SATUSEHAT** (DTO Kemenkes): FHIR R4 IG on Simplifier.net; KEMENKES `Observation` profile `https://fhir.kemkes.go.id/r4/StructureDefinition/Observation`; mandatory resources include Organization, Patient, Practitioner, Encounter, Condition (Observation conditional); auth via OAuth 2.0 client credentials; identifiers NIK, IHS number, Nomor RM. Staging base: `https://api-satusehat-stg.dto.kemkes.go.id/fhir-r4/v1` (**TODO-verify** currency).
- **Regulatory references to verify:** Permenkes 24/2022 (Rekam Medis), Kepmenkes HK.01.07/Menkes/1423/2022, UU 17/2023 (Kesehatan), UU PDP 27/2022, PP 71/2019. **TODO-verify** exact titles and relevance.
- **Known SATUSEHAT limitation** (IOTA EMR access-control paper): works at data aggregation / interoperability level, no uniform access control across institutions.
- **Indonesian fragmentation evidence:** IOTA EMR paper; HIS utilization across puskesmas (PMC); EMR recordkeeping culture (BMC Health Serv Res 2025); older HMA source on 400+ non-integrated government health apps.
- **Profile-methodology papers:** FHIR IG creation scoping review (ScienceDirect 2024); Johner "Three Steps to Your Own Profile"; "FHIR Profiliferation" (medRxiv); MIMIC-IV on FHIR; MDPI open-source biosignal framework (valueSampledData precedent); FHIR/DICOMweb/SVG workflow (DiagnosticReport pattern).
- **Related work in the draft:** Riech et al. (ISO/IEEE 11073-10207 to FHIR IG); Chaidir and Hareva 2025 (SATUSEHAT-compliant ECG IG); RADAR-IoT gateway; Garmin to FHIR integration; Suzuki et al. (microwave JVP); Das et al. (60 GHz JVP); Yen et al. (radar vital signs, elderly inpatients); Schellenberger et al. (clinical radar dataset); Shi et al. (carotid pulse, CW radar); JVP Doppler ultrasound review.

---

## 9. Open Questions / Decisions

- [ ] **Professor:** accepts the urgency argument (section 5)? Is the full-stack system plus profile enough contribution? Keep the three-role dashboard?
- [ ] **RADAR group:** output fields, interval definitions, subjects and sessions, intended use setting, reference measurements.
- [ ] Final fishbone: how many bones (section 4 recommends 6-8 after grouping).
- [ ] Is there an existing LOINC/SNOMED code for JVP, carotid and IJV time intervals? If not, how will the profile handle codes (local CodeSystem)? **TODO-verify**.
- [ ] Rewrite latar belakang to add JVP clinical context (bone 5) and remove "monitoring" framing.
- [ ] Fix the section 6 issues list in the draft.
- [ ] Fill Tabel 2.1 (related work comparison with gap column).
- [ ] Draft metodologi chapter and system architecture diagram.
- [ ] Verify: Permenkes and Kepmenkes titles, P1 statistics, "no study fuses radar JVP with EMR/RME", Indonesian HF burden figure.

---

## 10. Working Preferences

- Respond in the language the user writes in; thesis text is **Indonesian**. The user is casual in chat and sometimes mixes languages.
- Drafts as **paragraphs**, concise; kontribusi short. Use bracketed placeholders (`[cite: ...]`, `[insert data: ...]`) instead of inventing figures.
- Mark absence claims and uncertain facts as TODO-verify; keep thesis claims honest about limitations (single device, no clinical validation, no hosted SATUSEHAT connection).
- Do not frame the thesis as diagnosis or decision support; the contribution is the interoperability profile and the reference implementation.
- Quotes from sources: paraphrase; keep any quote very short.
