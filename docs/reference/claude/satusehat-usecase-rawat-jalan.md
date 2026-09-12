# SATUSEHAT — Use case: Resume Medis Rawat Jalan (outpatient medical summary)

Ringkasan (summary): The Panduan Interoperabilitas (interoperability guide) is split into Modul Pelayanan (service modules: Rawat Jalan, IGD, Rawat Inap, Kefarmasian) and Modul Penerapan (use cases: ANC, imunisasi, TB, …). The Rawat Jalan module (v6.3, 30 Oktober 2025) defines 28 integration steps for one outpatient visit, from Patient lookup through Encounter, clinical resources, and a closing `Composition`. Every step lists which elements are `*` (WAJIB, mandatory) and which terminology to use. Only the elements and codes the page prints are listed here; per-step "Pemetaan Nilai" lists that the page defers to the resource profile pages are not repeated.

General rules restated on every step: `*` = wajib; times in **UTC +00** (WIB −7 h, WITA −8 h, WIT −9 h; 17.35 WIB 23 Aug 2023 → `2023-08-23T10:35:00+00:00`); dates must not be earlier than **03 Juni 2014**.

## Prerequisites (before any data is sent)
| # | Step | Detail |
|---|---|---|
| 1 | Autentikasi | OAuth2 token (see satusehat-rest-api-and-validation.md) |
| 2 | Registrasi Struktur Organisasi | POST `Organization` sub-organisations (two example org structures shown as images only) |
| 3 | Registrasi Struktur Lokasi | POST `Location` sub-locations (images only) |
| 4 | Nomor IHS untuk Tenaga Kesehatan | GET `Practitioner` to obtain `{practitioner-ihs-number}` |

Version history highlights: v1.0 (14 Feb 2023) release; v3.0 merged Jilid 1 and 2; v6.0 (27 Sep 2024) added steps 6, 7, 12, 14, 19, 28; v6.2 says the method of sending `Medication` **separately** "sudah tidak bisa digunakan" (can no longer be used) for prescribing and dispensing — yet steps 16 and 18 still list "2 kali POST" as option 1 (contradiction inside the same raw file, recorded verbatim); v6.3 added `Encounter.serviceType.coding`.

## Sequence of steps (the posting order the page prescribes)
| Step | Name (Indonesian) | Resource(s) | `*` elements the step lists | References to earlier steps |
|---|---|---|---|---|
| 1 | Pendaftaran Pasien | `Patient` (GET only) | — (lookup by MPI rules) | — |
| 2 | Pendaftaran Kunjungan | `Encounter` (POST) | identifier, status, statusHistory.status/period, class, classHistory.class/period, subject, participant.type/individual, period, diagnosis.condition, hospitalization.dischargeDisposition, location, serviceProvider | subject → Patient (1); participant.individual → Practitioner; location → Location; serviceProvider → Organization |
| 3 | Anamnesis | `Condition`, `AllergyIntolerance`, `FamilyMemberHistory`, `MedicationStatement` | Condition: code, subject, encounter. AllergyIntolerance: category, code, patient, encounter, recorder, reaction.manifestation. FamilyMemberHistory: status, patient, relationship, condition.code. MedicationStatement: status, medication[x], subject | encounter → Encounter (2) |
| 4 | Hasil Pemeriksaan Fisik | `Observation` | status, code, subject, encounter, **performer** | encounter → (2) |
| 5 | Pemeriksaan Fungsional | `Observation` | same as 4 | (2) |
| 6 | Riwayat Perjalanan Penyakit | `ClinicalImpression` | status, subject, encounter, investigation.code, prognosisCodeableConcept | (2) |
| 7 | Tujuan Perawatan | `Goal` | lifecycleStatus, description, subject | addresses → Condition (3/13); outcomeReference → Observation |
| 8 | Rencana Rawat | `CarePlan` | status, intent, title, description, subject, encounter, author, activity.detail.status | goal → Goal (7) |
| 9 | Instruksi Medik dan Keperawatan | `CarePlan` | same as 8 | — |
| 10 | Pemeriksaan Penunjang Laboratorium | `ServiceRequest` → `Specimen` (+`Substance`) → `Observation` → `DiagnosticReport` | SR: status, intent, code, subject, encounter, requester, performer. Substance: status, category, code. Specimen: status, type, subject. Obs: status, code, subject, encounter, performer, value[x]. DR: basedOn, status, code, subject, encounter, performer, specimen, result | DR.basedOn → SR; DR.specimen → Specimen; DR.result → Observation; SR.supportingInfo → Procedure (fasting) |
| 11 | Pemeriksaan Penunjang Radiologi | `ServiceRequest` → `ImagingStudy` (by DICOM router) → `Observation` → `DiagnosticReport` | SR: status, intent, category, code, subject, encounter, requester, performer. ImagingStudy: identifier, status, modality, subject, started, basedOn, endpoint, series.uid, series.modality. Obs: status, code, subject, encounter, issued, performer, value[x]. DR: basedOn, status, code, subject, encounter, performer, result, imagingStudy, conclusion | ImagingStudy.basedOn → SR; Obs.derivedFrom → ImagingStudy; DR.imagingStudy → ImagingStudy |
| 12 | Rasional Klinis | `ClinicalImpression` | as 6 | investigation.item → Observation/QuestionnaireResponse/FamilyMemberHistory/DiagnosticReport/RiskAssessment/ImagingStudy; problem → Condition/AllergyIntolerance |
| 13 | Diagnosis | `Condition` (one diagnosis per payload) | code, subject, encounter | stage.assessment → ClinicalImpression (12) |
| 14 | Penilaian Risiko | `RiskAssessment` | status, subject | condition → Condition (13); ClinicalImpression.prognosisReference → RiskAssessment |
| 15 | Tindakan/Prosedur Medis | `ServiceRequest` (request) → `Procedure` → `Observation` (result) | Procedure: status, code, subject, encounter, performer.actor, focalDevice.manipulated | — |
| 16 | Peresepan Obat | `Medication` + `MedicationRequest` | Medication: identifier, extension:medicationType. MR: identifier, status, intent, medicationReference, subject, dosageInstruction.timing.repeat, dosageInstruction.route, substitution.allowed[x] | medicationReference → Medication (contained or separate) |
| 17 | Pengkajian Resep | `QuestionnaireResponse` | status, subject, encounter, author, source, item.item | — |
| 18 | Pengeluaran Obat | `Medication` + `MedicationDispense` | MD: identifier, status, medicationReference, subject, context | authorizingPrescription → MedicationRequest (16) |
| 19 | Pemberian Obat | `Medication` + `MedicationAdministration` | MA: status | — |
| 20 | Diet | `NutritionOrder` | status, intent, patient, encounter, dateTime | — |
| 21 | Edukasi | `Procedure` | (as 15) | — |
| 22 | Prognosis | `ClinicalImpression` | as 6 | — |
| 23 | Rencana Tindak Lanjut | `ServiceRequest` | status, intent, code, subject, encounter | — |
| 24 | Instruksi Tindak Lanjut & Sarana Transportasi | `ServiceRequest` | status, intent, code, subject, encounter, performer | — |
| 25 | Kondisi Saat Meninggalkan RS | `Condition` or `Encounter.hospitalization.dischargeDisposition` | Condition: code, subject, encounter | — |
| 26 | Cara Keluar dari RS | `Encounter.hospitalization.dischargeDisposition` | — | — |
| 27 | Pembaharuan Data Kunjungan | `Encounter` (**PUT**, must carry `Encounter.id` returned at step 2) | adds keluhan utama, diagnosis primer/sekunder, period end, lama perawatan (minutes), condition at discharge, follow-up, cara keluar | diagnosis.condition → Condition (3, 13) |
| 28 | Resume Medis | `Composition` | status, type, subject, date, author, title, attester.mode, relatesTo.code, relatesTo.target[x] | section entries → all resources above |

## Key terminology per step (systems and fixed codes as printed)
### Step 2 — Encounter
| Element | Value |
|---|---|
| `identifier.system` | `http://sys-ids.kemkes.go.id/encounter/{{Organization_ID}}` |
| `status` at registration | `arrived` (patient present, not yet seen) or `in-progress` (being seen) |
| `class` | `http://terminology.hl7.org/CodeSystem/v3-ActCode` \| `AMB` \| ambulatory |
| `serviceType.coding` | from Lampiran Standar Terminologi (no codes printed) |
| `location` | Reference to `Location` (ruangan/poli) |
| `location.extension.serviceClass…coding` | `http://terminology.kemkes.go.id/CodeSystem/locationServiceClass-Outpatient` \| `reguler` "Kelas Reguler" / `eksekutif` "Kelas Eksekutif" |
| `…upgradeClassIndicator…coding` | `http://terminology.kemkes.go.id/CodeSystem/locationUpgradeClass` \| `kelas-tetap`, `naik-kelas`, `turun-kelas`, `titip-rawat` |
| `period.start` | dateTime |

### Step 3 — Anamnesis
| Variable | Element → value |
|---|---|
| Keluhan Utama (chief complaint) | `Condition.category` `http://terminology.kemkes.go.id` \| `chief-complaint`; `Condition.code` SNOMED CT ECL `< 404684003 |Clinical finding|`; `Encounter.diagnosis.use` `http://terminology.hl7.org/CodeSystem/diagnosis-role` \| `CC` — must be included in the finishing PUT Encounter |
| Keluhan Penyerta | `Condition.category` `http://terminology.hl7.org/CodeSystem/condition-category` \| `problem-list-item`; code SNOMED CT (same ECL) |
| Riwayat Penyakit Pribadi | category `http://terminology.kemkes.go.id` \| `previous-condition`; code SNOMED ECL `< 417662000` OR `< 443508001`; `clinicalStatus` `http://terminology.hl7.org/CodeSystem/condition-clinical` \| `active` / `inactive` |
| Riwayat Penyakit Keluarga | `FamilyMemberHistory.relationship` `http://terminology.hl7.org/CodeSystem/v3-RoleCode` \| `FAMMEMB`; `condition.code` SNOMED ECL `< 416471007` OR `< 160266009`; `condition.outcome` SNOMED ECL `< 418138009` |
| Riwayat Alergi | `AllergyIntolerance.category` `medication` / `food` / `environment` / `biologic`; `clinicalStatus` `http://terminology.hl7.org/CodeSystem/allergyintolerance-clinical` \| `active` / `inactive`; code per Lampiran |
| Riwayat Pengobatan | `MedicationStatement.medicationReference` when the drug came from this fasyankes (GET prior `MedicationDispense`); otherwise `medicationCodeableConcept` with KFA `http://sys-ids.kemkes.go.id/kfa` — prefix `93` (brand known, e.g. `93005512`) or `92` (template, e.g. `92001087`) |

### Step 4 — Pemeriksaan Fisik: tanda vital (vital signs) and antropometri
All use `Observation.category` = `http://terminology.hl7.org/CodeSystem/observation-category` \| `vital-signs` "Vital Signs", `code.system` = `http://loinc.org`, `valueQuantity.system` = `http://unitsofmeasure.org`, value type Decimal.

| Variable | LOINC code | display | `valueQuantity.unit` | `valueQuantity.code` |
|---|---|---|---|---|
| Denyut Jantung (heart rate) | `8867-4` | Heart rate | `beats/min` | `/min` |
| Pernapasan (respiratory rate) | `9279-1` | Respiratory rate | `breaths/min` | `/min` |
| Tekanan Darah Sistole | `8480-6` | Systolic blood pressure | `mm[Hg]` | `mm[Hg]` |
| Tekanan Darah Diastole | `8462-4` | Diastolic blood pressure | `mm[Hg]` | `mm[Hg]` |
| Suhu Tubuh (body temperature) | `8310-5` | Body temperature | `C` | `Cel` |
| Tinggi Badan (height) | `8302-2` | Body height | `cm` | `cm` |
| Berat Badan (weight) | `29463-7` | Body weight | `kg` | `kg` |
| Luas Permukaan Tubuh anak (BSA) | `8277-6` | Body surface area | `m²` | `m²` |

Not listed on this page: oxygen saturation (`2708-6` / `59408-5`) — grep finds none; systolic and diastolic are separate Observations, not components.

Other physical-exam items (category `exam`): Tingkat Kesadaran `67775-7` "Level of responsiveness" with `valueCodeableConcept` SNOMED `248234008` Mentally alert, `300202002` Response to voice, `450847001` Responds to pain, `422768004` Unresponsive, `130987000` Acute confusion, `2776000` Delirium. Head-to-toe narratives use LOINC "Physical findings of … Narrative" codes (Kepala `10199-8`, Mata `10197-2`, Telinga `10195-6`, Hidung `10203-8`, Rambut `32436-8`, Bibir `32446-7`, Gigi `85910-8`, Lidah `32483-0`, Langit-langit/Tonsil `10201-2` + SNOMED body site `72914001` / `91636008`, Leher `11411-6`, Tenggorokan `56867-5`, Dada `11391-0`, Payudara `10193-1`, Punggung `10192-3`, Perut `10191-5`, Genital `11400-9`, Anus `11388-6` + `53505006`, Lengan atas `11386-0`, Lengan bawah `11398-5`, Jari tangan `11404-1` + `7569003`, Kuku `32456-6` + `770812000`/`770805009`, Pergelangan `11415-7`, Paha `11414-0`, Betis `11389-4`, Jari kaki `11397-7` + `29707007`, Sendi kaki `11385-2` + `26552008`); the page writes their value as `Observation.valueQuantity.value` "(Tipe data String)" — as printed.

### Step 5 — Pemeriksaan Fungsional
Status Psikologis: category `survey`, code LOINC `8693-4` "Mental Status", `valueCodeableConcept` SNOMED `17326005` Well in self, `48694002` Feeling anxious, `1402001` Afraid, `75408008` Feeling angry, `420038007` Feeling unhappy, `74964007` Other (+ free text). v6.1 removed Skor ADL.

### Steps 6, 12, 22 — ClinicalImpression
| Use | `code.coding` |
|---|---|
| Riwayat Perjalanan Penyakit | `http://snomed.info/sct` \| `312850006` History of disorder; `summary` string |
| Rasional Klinis | `http://terminology.kemkes.go.id` \| `TK000056` Rasional Klinis |
| Prognosis | `http://snomed.info/sct` \| `20481000` Determination of prognosis; `*prognosisCodeableConcept` SNOMED `170968001` Prognosis good (Baik), `65872000` Fair (Dubia et bonam), `67334001` Guarded (Dubia et malam), `170969009` Prognosis bad (Tidak baik) |

### Steps 7–9 — Goal and CarePlan
Goal: `lifecycleStatus` `planned`; `achievementStatus` `http://terminology.hl7.org/CodeSystem/goal-achievement`; `category` `http://terminology.hl7.org/CodeSystem/goal-category` \| `nursing`; `description` SNOMED ECL `< 404684003`; `outcomeCode` SNOMED ECL `< 390800000`; `target.measure` LOINC; `expressedBy` → Practitioner. CarePlan (both steps): `category` SNOMED `736271009` Outpatient care plan; `goal` → Goal.

### Step 10 — Laboratorium
- Tunggal (single): 1 ServiceRequest, 1 Specimen, 1 Observation, 1 DiagnosticReport. Panel: 1 SR (panel LOINC), 1 Specimen, N Observations (one LOINC each), 1 DR (panel LOINC) referencing all N.
- One SR / Specimen / DR payload = one code; `DiagnosticReport.code` equals the related `ServiceRequest.code`.
- SR: `identifier.system` `http://sys-ids.kemkes.go.id/servicerequest/{{Organization_ID}}`; `category` SNOMED `108252007` Laboratory procedure; `code` LOINC (categories "Permintaan"/"Permintaan & Hasil" in Lampiran LOINC Laboratorium) and/or `http://terminology.kemkes.go.id/CodeSystem/kptl`; `priority` `stat` (CITO) / `routine`; `reasonReference` → Condition; `supportingInfo` → Procedure fasting (SNOMED category `103693007`, code `792805006` Fasting, `status` `done`/`not-done`).
- Specimen: `type` SNOMED ECL `< 123038009`; `collection.bodySite` ECL `< 123037004`; `collection.method` ECL `< 118292001`; `collection.fastingStatusCodeableConcept` `http://terminology.hl7.org/CodeSystem/v2-0916` \| `F` / `NF`; `processing.procedure` SNOMED `787378005` Fixation of specimen or ECL `≤ 9265001`; `processing.additive` → Substance with KFA code (temporary device codes `32999999` virtual / `33999999` actual).
- Observation: `category` `laboratory`; `code` LOINC (categories "Hasil"/"Permintaan & Hasil"); `value[x]`: Nominal/Ordinal → `valueCodeableConcept`, Kuantitatif → `valueQuantity`; `interpretation` `http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation`; `effectiveDateTime` = result out of lab, `issued` = result received by sending unit.
- DiagnosticReport: `category` `http://terminology.hl7.org/CodeSystem/v2-0074`; `code` LOINC; `result`, `specimen`, `basedOn`, `conclusionCode`, `conclusion`.

### Step 11 — Radiologi
Flow depends on where the Accession Number is issued (SIMRS/SIMPUS vs RIS vs DICOM router); DICOM files go to the National Imaging Data Repository (NIDR), which returns a WADO URL; the DICOM router POSTs `ImagingStudy` and its `id` is later referenced. SR: `identifier[0]` servicerequest system, `identifier[1]` type `http://terminology.hl7.org/CodeSystem/v2-0203` \| `ACSN` with system `http://sys-ids.kemkes.go.id/acsn/{{Organization_ID}}`; `category` SNOMED `363679005` Imaging; `orderDetail` KFA contrast, DICOM modality `http://dicom.nema.org/resources/ontology/DCM`, AE title `http://sys-ids.kemkes.go.id/ae-title`; `supportingInfo` → AllergyIntolerance (contrast, category `medication`), pregnancy Observation (LOINC `82810-3`, SNOMED `77386006` Pregnancy / `60001007` Not pregnant; the page prints `category.coding.system` as `http://snomed.info/sct` with code `survey`), fasting Procedure. Result Observation: `category` `imaging`, `derivedFrom` → ImagingStudy, `valueString`. DR adds `imagingStudy`, `conclusion`.

### Steps 13–15 — Diagnosis, RiskAssessment, Procedure
| Element | Value |
|---|---|
| `Condition.category` (diagnosis) | `http://terminology.hl7.org/CodeSystem/condition-category` \| `encounter-diagnosis` |
| `Condition.code` | `http://hl7.org/fhir/sid/icd-10` (ICD-10) plus SNOMED CT ECL `< 404684003`; one diagnosis per payload; `stage.assessment` → ClinicalImpression |
| `RiskAssessment.code` | SNOMED ECL `< 225338004`; `prediction.outcome` ECL `< 64572001`; `prediction.qualitativeRisk` `http://terminology.hl7.org/CodeSystem/risk-probability` (page spells the resource `RiskAssesment` in several paths) |
| `ServiceRequest.code` (tindakan request) | `http://hl7.org/fhir/sid/icd-9-cm` and/or KPTL |
| `Procedure.category` | SNOMED ECL `< 71388002` |
| `Procedure.code` | `http://hl7.org/fhir/sid/icd-9-cm` (ICD-9 CM) plus SNOMED ECL `< 71388002`; `performedPeriod.start/end`; `usedCode` KFA |
| Hasil tindakan (`Observation`) | `code`/`component.code` LOINC, national code or SNOMED; value types Nominal/Ordinal → CodeableConcept, Kuantitatif → Quantity, Naratif → String, ya/tidak → Boolean; one payload per diagnostic action |

### Steps 16–19 — Farmasi
- KFA drug code = 8 digits: prefix `91` BZA (active substance), `92` POV (virtual/template product), `93` POA (actual product), `94` POAK (packaged). Examples: `91000101` Paracetamol, `92000511` Paracetamol 120 mg/5 mL Sirup, `93002205` … (ERPHAMOL), `94002470` dus isi 1.
- `Medication.code` system `http://sys-ids.kemkes.go.id/kfa`: MedicationRequest may use `92` or `93`; MedicationDispense **wajib** `93`. `Medication.form` `http://terminology.kemkes.go.id/CodeSystem/medication-form`. `Medication.ingredient` optional for non-racikan, wajib for racikan (compounded); strength numerator UCUM, denominator `http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm` (`TAB`, `CAP`).
- `MedicationRequest.identifier` is an array of two: `http://sys-ids.kemkes.go.id/prescription/{{Organization_ID}}` (resep) and `http://sys-ids.kemkes.go.id/prescription-item/{{Organization_ID}}` (per item), both `use: official`.
- `dosageInstruction.route` `http://www.whocc.no/atc`; `additionalInstruction` SNOMED ECL `< 419492006`; `timing.repeat` tables map phrases to `frequency/period/periodUnit/when` (e.g. "3 times a day" = frequency 3, period 1, periodUnit d; BID = 2/1/d; Q6H = 1/6/h; AM = 1/1/d when MORN); `timing.code` must be accompanied by an equivalent `timing.repeat`; `sequence` increments for tapering.
- MedicationDispense adds `Medication.batch.lotNumber/expirationDate`, `whenPrepared`, `whenHandedOver`, `authorizingPrescription`. MedicationAdministration: `dosage.route` ATC, `dosage.dose`, `effectivePeriod` (page spells `effecticePeriod`), `performer.actor`.

### Steps 20–26 — Diet, edukasi, follow-up, discharge
| Variable | Element → value |
|---|---|
| Diet | `NutritionOrder.intent` `proposal` (recommendation) / `order` (for dietitian); `oralDiet.nutrient.modifier` SNOMED ECL `< 226355009` / `< 87918000`; `excludeFoodModifier` ECL `< 255620007` |
| Edukasi (`Procedure`) | `category` SNOMED `409073007` Education; two `code` codings per payload: KPTL `10913` "Edukasi Kesehatan Individu" **and** SNOMED `84635008`, `967006`, `410082002`, `712651001`, `61310001`, `698608004`, `362978005` |
| Rencana Tindak Lanjut (`ServiceRequest`) | `category` SNOMED `3457005` Patient referral; `code` SNOMED `737481003` Inpatient care management, `185389009` Follow-up visit, `11429006` Consultation, `737492002` Outpatient care management |
| Instruksi tindak lanjut | `ServiceRequest.locationCode` `http://terminology.hl7.org/CodeSystem/v3-RoleCode` \| `OF` (Poli), `HOSP` / `PC` (Fasyankes), `AMB` (Ambulance); `occurrenceDateTime`; `patientInstruction` |
| Kondisi saat meninggalkan RS | `Condition.category` `problem-list-item`, `code` SNOMED `359746009` stable, `162668006` unstable, `268910001` improved; or `Encounter.hospitalization.dischargeDisposition` `http://terminology.hl7.org/CodeSystem/discharge-disposition` \| `aadvice`, `other-hcf`, `oth`; `http://terminology.kemkes.go.id/CodeSystem/discharge-disposition` \| `exp-lt48h`, `exp-gt48h` |
| Cara keluar dari RS | `dischargeDisposition` `home`, `aadvice`, `oth` |

### Step 28 — Composition (resume medis)
`type` LOINC `88645-7` "Outpatient hospital Discharge summary"; `category` LOINC `LP173421-1` Report. Section codes: Anamnesis `TK000003` (kemkes) with sub-sections LOINC `10154-3`, `11450-4`, `48765-2`, `11348-0`, `10164-2`, `10157-6`, `10160-0`; Pemeriksaan Fisik `TK000007` with `8716-3` Vital signs and `10187-3`; Pemeriksaan Fungsional `47420-5`; Perencanaan Perawatan `18776-5`; Pemeriksaan Penunjang `TK000009` with `11502-2`, `18782-3`; Diagnosis `TK000004` with `42347-5`, `78375-3`; Tindakan `TK000005`; Farmasi `TK000013` with `42346-7`, `75311-1`; Diet `42344-2`, `61144-2`; Edukasi `34895-3`; Kondisi keluar `10184-0`; Rencana Tindak Lanjut `8653-8`; Perjalanan Kunjungan `8648-8` (narrative, `text.status` `generated`).

## Contradictions / ambiguities recorded
| Where | Statement A | Statement B |
|---|---|---|
| `interop-rme-rawat-jalan` step 4 vs `res-observation` (satusehat-observation.md) | `*Observation.performer` is wajib for physical-exam Observations | profile page does not mark `performer` |
| `interop-rme-rawat-jalan` v6.2 changelog vs steps 16/18 | separate `Medication` POST "sudah tidak bisa digunakan" | steps still list "2 kali POST" as option 1 |
| Head-to-toe rows | value element printed as `Observation.valueQuantity.value` "(Tipe data String)" | value list includes `valueString` |
| Pregnancy status | `Observation.category.coding.system` printed as `http://snomed.info/sct` with code `survey` | every other category uses `observation-category` |
| Encounter identifier system | `{{Organization_ID}}` placeholder here | `{organization-ihs-number}` on the profile pages (satusehat-encounter.md) |

## Notes for our server
- Enforce this dependency order: Organization/Location/Practitioner exist → Patient exists → Encounter POST (status `arrived`/`in-progress`, class `AMB`) → clinical resources referencing `Encounter/{id}` → Encounter PUT to `finished` carrying `diagnosis` (chief complaint `CC` + ICD-10 conditions), `period.end`, `dischargeDisposition`.
- Vital-sign Observations from devices: one Observation per measurement using the LOINC/UCUM table above (8867-4, 9279-1, 8480-6, 8462-4, 8310-5, 8302-2, 29463-7, 8277-6); category `vital-signs`; include `performer` since this page marks it wajib; SpO2 is not covered by the playbook, so if we add it we must document our own choice.
- Diagnosis: one `Condition` per ICD-10 code, category `encounter-diagnosis`; chief complaint is a separate `Condition` with kemkes category `chief-complaint` and SNOMED code.
- Procedures: ICD-9 CM (`http://hl7.org/fhir/sid/icd-9-cm`) on `Procedure.code`; education is a `Procedure` with KPTL + SNOMED codes.
- Do not model lab, radiology, pharmacy or Composition in the first iteration, but keep reference fields (`basedOn`, `derivedFrom`, `result`) open so they can be added.
- Reject dateTimes before 2014-06-03 and non-UTC offsets if we want playbook parity.

## Sources
- raw/satusehat/interop-index.md
- raw/satusehat/interop-rme-rawat-jalan.md
