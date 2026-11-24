# CLAUDE.md: Thesis Context (FHIR Profile for RADAR Health Monitoring Devices)

This file is the working context for the thesis. Read it before helping with anything related to the proposal, the FHIR profile design, or the reference implementation.

---

## 1. Project Summary

**Working title (Indonesian):**
Pengembangan Profil Fast Healthcare Interoperability Resource (FHIR) Untuk Integrasi Perangkat RADAR Pendeteksi Jugular Vein Pulse

**Scope update:** scope has been broadened from JVP-only to **RADAR-based health monitoring devices** in general. JVP detection is the concrete case study and validation vehicle, not the boundary of the contribution. The title may need to be updated to match (e.g. "Perangkat RADAR Pemantau Kesehatan"). Confirm with the advisor.

**One-line contribution claim:**
Design and validation of a FHIR / KEMENKES (SATUSEHAT)-compliant profile for contactless RADAR-based health monitoring devices, with an end-to-end reference implementation using real measured data.

**Language:** the thesis is written in Indonesian. Drafts, proposal text and section outlines should be in Indonesian unless stated otherwise. Keep technical terms (Observation, Device, profile, etc.) in English.

---

## 2. What the Student Does and Does Not Do

**Out of scope (done by the Biomedical Engineering RADAR research group):**
- RADAR hardware and the device itself (already built)
- I/Q signal acquisition, feature extraction, JVP pulse detection, abnormality / AFib classification algorithms

**In scope (the student's work):**
1. **FHIR profile design** for RADAR monitoring devices: the core research contribution
2. **Validation** against base FHIR R4 and KEMENKES/SATUSEHAT resources
3. **Full-stack reference system**: raw data parsing, then storage, then FHIR API, then dashboards for end users
4. **Injection of actual measured data** from the RADAR group's device into the system

**Framing rule:** the website/dashboard is not the contribution (the advisor agrees it is not novel). It exists to prove the FHIR layer works end to end. The thesis must read as profile-centric, matching the title. Chapter weighting target:

| Part | Weight |
|---|---|
| Background / literature (interoperability + profiling methodology) | ~20-25% |
| **FHIR profile design and justification** (core chapter, largest) | ~30-35% |
| System implementation (architecture, dashboards, data flow) | ~25% |
| Validation / results | ~15-20% |

---

## 3. Problem Statement and Research Gap

**Narrative arc for the background (BAB I Latar Belakang):**
1. Indonesia generates massive clinical data daily (about 280M population, large number of hospitals, 1.2-1.4M hospital visits per day claimed from BPJS data in the draft).
2. Patient-generated health data (PGHD) is valuable, but it needs standardization (data types, units, device identifiers, clinical terminology).
3. Existing standards cover different scopes (ICD, SNOMED CT, LOINC) and need a connector, which is FHIR.
4. FHIR is mandated in Indonesia through SATUSEHAT (regulatory basis in section 5).
5. **Bridge:** the mandate covers established data flows (visits, labs, conventional EMR). Novel device categories and sensing modalities are not automatically covered, so mapping is left to individual developers.
6. RADAR is a new, contactless, portable sensing modality with high clinical potential, but **no established FHIR representation**, so its data risks becoming another silo. This motivates the profile.
7. JVP monitoring is the concrete application. Its clinical value is only realized if the output can be represented as standardized clinical data.
8. Closing sentence (bridge to Rumusan Masalah): a profile alone is a paper artifact until proven in a real end-to-end pipeline, so a full-stack reference implementation validates it.

**Research gap (state explicitly; this is an absence claim):**
No FHIR profile / Implementation Guide is known to cover RADAR-derived physiological signals. **TODO: verify before asserting.** Search Simplifier.net, the HL7 FHIR registry, SATUSEHAT docs, and the literature for existing coverage. A wrong "gap" claim is an easy committee critique.

**Rhetorical mirror worth using:** institutional fragmentation (400+ unintegrated government health apps) and device-level fragmentation are the same problem at different scales. A new RADAR device without a FHIR interface becomes "device #401".

---

## 4. FHIR Background (what the thesis needs to know)

- FHIR (Fast Healthcare Interoperability Resources) is developed by HL7. It is REST-API based, with resources serialized as JSON/XML. Version in use in Indonesia: **R4**.
- **Profiling** = constraining and/or extending a base resource through a `StructureDefinition` (cardinality, fixed values, terminology bindings, must-support flags, extensions). Profiles are packaged into an **Implementation Guide (IG)**.
- **Profile-authoring tooling to look at:** FHIR Shorthand (FSH) and SUSHI, IG Publisher, the HL7 FHIR Validator, Simplifier.net / Forge.
- **Good practice (Johner Institute):** before creating a profile, check whether an existing profile or extension already covers the case. This justifies the gap analysis section.
- **Known field-level problem ("profiliferation"):** authors tend to create new profiles instead of reusing existing ones. Keep the profile deliberately minimal and justified.

### Candidate resources for RADAR monitoring data (design space, decisions still open)

| Need | Candidate FHIR element | Notes |
|---|---|---|
| Continuous waveform (I/Q-derived signal, JVP waveform) | `Observation.valueSampledData` | Precedent: HL7 FHIR open-source IoMT biosignal framework (MDPI 2025) encodes ECG as SampledData with period, scaling factor, units. Check how SampledData handles multi-channel (I and Q) data. |
| Derived features (pulse rate, intervals, quality index) | `Observation` with `component` entries, or separate Observations linked via `hasMember` | Decide based on how clinicians will query trends. |
| Interpreted result (abnormality / AFib flag) | `DiagnosticReport` referencing the Observation(s), or a `Condition`/`Observation` for the finding | Precedent: CAD results encoded as DiagnosticReport + Observation (FHIR/DICOMweb workflow paper). |
| The RADAR device itself | `Device` (+ `DeviceMetric` if applicable) | Identifiers, manufacturer, model, software/firmware version, calibration. Thin on its own, so it must not be the whole thesis. |
| Data lineage / provenance | `Observation.device`, `Provenance` | Which device, which raw signal, when, calibration state. |
| Raw I/Q file storage (if too large for inline) | `DocumentReference` / `Binary` | Trade-off against SampledData inline size. |
| Patient / practitioner / org context | `Patient`, `Practitioner`, `Organization`, `Encounter` | SATUSEHAT-mandatory resources. |
| Consent / role-based access | `Consent`, SMART-on-FHIR style scopes (consider) | Three roles: patient, doctor, admin. |

### Terminology (coding) questions to resolve
- Find the closest existing **LOINC / SNOMED CT** codes for each element (RADAR-derived heart/respiratory signals, JVP, arrhythmia / AFib).
- Where no exact code exists: (a) use the closest code and document the semantic gap, or (b) define a project-specific CodeSystem / extension. Both are defensible, but the choice must be justified.
- Because scope is now generic RADAR monitoring, design the profile around **measurement categories** (e.g. waveform, derived vital sign, interpretation) rather than one diagnosis, so the algorithm can change without changing the profile.

---

## 5. SATUSEHAT / KEMENKES Context

- **SATUSEHAT** is Indonesia's national health data exchange platform (Indonesia Health Services, IHS), run by the Digital Transformation Office (DTO) of Kementerian Kesehatan. It consolidates and standardizes EMR data across the national platform.
- **Implementation Guide:** SATUSEHAT FHIR R4 IG (published on Simplifier.net; base URL `https://fhir.kemkes.go.id/r4/`).
- **KEMENKES Observation profile (canonical URL):**
  `https://fhir.kemkes.go.id/r4/StructureDefinition/Observation`
  It is described as used for simple observations such as device measurements, lab results and vital signs. The RADAR Observation profile should derive from this, not from vanilla base R4.
- **Resource obligations:** Organization, Patient, Practitioner, Encounter and Condition are described as mandatory in integrations. Observation is conditional.
- **Auth:** OAuth 2.0 **Client Credentials** flow. Register an application in the developer portal to get `client_id` and `client_secret`, then exchange them for an access token. Include this in the architecture diagram.
- **Identifiers:** SATUSEHAT uses its own identifier systems (e.g. NIK-based patient identity, organization IDs, IHS numbers). **TODO: verify exact identifier systems and formats in the current IG.**
- **Regulatory basis:** the draft cites "UU No. 24 Tahun 2022" for FHIR use in SATUSEHAT. **TODO: verify.** This is likely *Peraturan Menteri Kesehatan No. 24 Tahun 2022 tentang Rekam Medis* (a Permenkes, not a UU). Also check *Permenkes No. 18 Tahun 2022* on health data governance and the *UU Kesehatan No. 17 Tahun 2023*, and consider *UU PDP (No. 27/2022)* and *PP 71/2019* for privacy and consent.
- **Known SATUSEHAT limitation (useful for the background and access design):** per the IOTA EMR access-control paper, SATUSEHAT works at the level of data aggregation and interoperability and does not impose a uniform access-control mechanism across institutions. This partly justifies the role-based architecture.

### Open technical check (high priority)
Pull the KEMENKES `Observation` StructureDefinition and check whether it keeps `valueSampledData`, `component`, `device`, `derivedFrom`, and `hasMember` available as in base R4, or restricts them. This decides whether the contribution is a true **extension / new profile** (stronger) or just a **conformant instance** (weaker).

---

## 6. System Architecture (reference implementation)

Pipeline: **RADAR device output (I/Q or processed result) -> parsing / ingestion -> transformation to FHIR (per the profile) -> FHIR validation -> FHIR store / API -> role-based dashboards**.

Roles:
- **Patient:** interpreted results and summaries
- **Doctor:** raw waveform plus trends
- **Admin:** device fleet, system status, user management

Open question to settle with the RADAR group: do they hand over **raw I/Q data** (the student integrates parsing) or an **already-processed result file** (JSON/CSV of detected pulses plus abnormality flag)? This sets where the architecture starts.

Data requirement: use **actual measured data** from the device, not only synthetic data.

---

## 7. Validation Plan (draft)

1. **Conformance:** run all generated resources through the official HL7 FHIR Validator against base R4 and the KEMENKES profiles. Report pass/fail and issues.
2. **Mapping coverage table:** RADAR output field -> FHIR element -> coding system -> justification. Also a thesis artifact in its own right.
3. **Semantic review:** a domain expert (RADAR group clinician/engineer) reviews a sample of resources for preserved clinical meaning (units, timing, coding, provenance).
4. **End-to-end round trip:** ingest real data, transform, store, retrieve via API, render on dashboards, and check data integrity.
5. **(Optional)** test against the SATUSEHAT sandbox if access is available.

"Converts to valid FHIR JSON" is a low bar on its own. Frame validation around *correctness, appropriateness and compliance*, not just "it works".

---

## 8. Methodology Backbone

Cite the FHIR IG creation scoping review as the process model:
**requirements analysis -> data dictionary -> profile/extension modeling -> terminology binding -> automated + clinical validation**, then package as an IG.
MIMIC-IV on FHIR gives a clean model-transform-validate-package structure to mirror.

---

## 9. Source List (found so far; verify details before citing)

**Profile creation methodology**
- FHIR Implementation Guide creation process: scoping review (ScienceDirect, 2024)
- "FHIR: Three Steps to Your Own Profile" (Johner Institute)
- "FHIR Profiliferation: A Data Science Approach" (medRxiv)
- MIMIC-IV on FHIR (PMC)

**Biosignal / device to FHIR precedents**
- HL7 FHIR-Based Open-Source Framework for Real-Time Biomedical Signal Acquisition and IoMT Interoperability (MDPI, 2025)
- Creating a Medical Imaging Workflow Based on FHIR, DICOMweb, and SVG (PMC)

**SATUSEHAT / Indonesia**
- SATUSEHAT FHIR R4 Implementation Guide (Simplifier.net, DTO Kemenkes)
- Developer's Guide to SATUSEHAT integration (DEV Community; secondary source)
- Access Control Development Within an IOTA-Based EMR Management System (PMC): Indonesian fragmentation, SATUSEHAT limits
- Understanding Health Information Systems Utilization Across Public Health Centers in Indonesia (PMC)
- An exploratory study of EMR implementation and recordkeeping culture: hospitals in Indonesia (BMC Health Services Research, 2025)
- Digitalise Healthcare Indonesia: A summary (HMA): over 400 non-integrated government health apps (older source; check for a newer figure)

**General / LMIC / IoMT interoperability**
- FHIRconnect: Towards a seamless integration of openEHR and FHIR (arXiv): semantic vs. syntactic interoperability
- Enhancing interoperability among health information systems in LMICs (arXiv)
- Transforming digital health using IoT for personalized interoperable and secure healthcare systems (Springer, 2025): proprietary device protocols, inconsistent sampling and units
- Advances in IoMT for Healthcare Systems (PMC)
- Multirole of IoMT in biomedical systems (ScienceDirect)

**Still needed**
- Literature on RADAR-based vital sign / cardiac monitoring (capabilities, clinical promise)
- Clinical background on JVP significance (and AFib, if kept)
- Evidence of RADAR devices lacking standardized data representation (the gap)
- Statistics: Indonesian hospital count, interoperability/integration rates, BPJS visit figures (the draft's "1.2-1.4 million visits per day" needs a source), personal-device adoption

---

## 10. Working Preferences

- Respond in the language the user writes in (the thesis text itself is Indonesian).
- Keep citation placeholders explicit (`[cite: ...]`) rather than inventing sources.
- Mark absence claims and uncertain facts as TODO-verify.
- Keep the thesis profile-centric. If implementation detail starts to dominate, flag it.
- Quotes from sources: short, paraphrase by default.

---

## 11. Open Decisions Checklist

- [ ] Final title after scope change (RADAR health monitoring devices vs. JVP)
- [ ] Profile scope: Observation/output only, or Device + provenance as well
- [ ] Waveform representation: inline SampledData vs. DocumentReference/Binary
- [ ] Observation vs. DiagnosticReport split for interpreted results
- [ ] Terminology: closest codes vs. custom CodeSystem/extension
- [ ] Derive from KEMENKES Observation profile (check constraints first)
- [ ] Raw I/Q vs. processed-result ingestion boundary
- [ ] Verify the regulatory citation (UU vs. Permenkes 24/2022)
- [ ] Verify the "no existing RADAR FHIR profile" gap
- [ ] SATUSEHAT sandbox access
