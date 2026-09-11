# SATUSEHAT — Terminology (Terminologi)

Ringkasan (summary): SATUSEHAT mandates a fixed set of code systems: ICD-10 for diagnoses, ICD-9 CM for procedures, LOINC for laboratory / observation names, SNOMED CT for clinical terms, plus Indonesian systems (KPTL billing codes, KFA drug codes, `terminology.kemkes.go.id` code systems). The element-by-element list lives in the external "Standar Terminologi" spreadsheet (v10.3, 30 Juni 2026), which is **not** in the corpus; this file records what the terminology pages themselves state, the system URIs as they appear in the raw text, and the vital-sign LOINC codes (which come from the rawat jalan use-case page, not the terminology pages).

## Which code system is mandated for what (`term-index`)
| Code system | Mandated use (verbatim gloss) | Version stated | System URI (as used in raw pages) |
|---|---|---|---|
| ICD-10 | **standar diagnosis** (diagnosis standard) | ICD-10 versi 2010 | `http://hl7.org/fhir/sid/icd-10` |
| ICD-9 CM | **standar penamaan prosedur & tindakan medis** (procedure / medical-action naming) | ICD-9 CM versi 2010 | `http://hl7.org/fhir/sid/icd-9-cm` |
| ICD-O | **standar pengkodean neoplasma/kanker** | ICD-O versi 3.2 tahun 2019 | not printed in corpus |
| ICD-MM | identify maternal death (kematian ibu) | ICD-MM versi 2012 | not printed |
| ICD-PM | identify perinatal death | ICD-PM versi 2016 | not printed |
| LOINC | **standar penamaan uji laboratorium** (laboratory test naming); in practice also vital signs, physical exam, Composition sections | none stated | `http://loinc.org` |
| SNOMED-CT | **standar penamaan istilah klinis** (clinical term naming): findings, body structure, organisms, procedures, substances… | none stated; licence held by Kementerian Kesehatan | `http://snomed.info/sct` |
| KPTL (Kode Pembiayaan Tindakan dan Layanan Kesehatan Nasional) | national billing/procedure code, "sepadan" (equivalent) to LOINC (lab) or ICD-9 CM (procedures) | — | `http://terminology.kemkes.go.id/CodeSystem/kptl` |
| KFA (Kamus Farmasi dan Alat Kesehatan) | drug and device codes | — | `http://sys-ids.kemkes.go.id/kfa` |
| Kode Pemeriksaan Penunjang Nasional | temporary lab code when no LOINC exists: prefix `X` + 6 digits, starting `X099080` (e.g. Titer Anti-ABO); replaced by LOINC once available | — | not printed |
| Kemkes local code systems | chief complaint / previous condition categories, clinical terms, discharge disposition, service class, medication form | — | `http://terminology.kemkes.go.id`, `http://terminology.kemkes.go.id/CodeSystem/clinical-term`, `…/CodeSystem/discharge-disposition`, `…/CodeSystem/locationServiceClass-Outpatient`, `…/CodeSystem/locationUpgradeClass`, `…/CodeSystem/medication-form` |
| HL7 terminology | status/category value sets | — | `http://terminology.hl7.org/CodeSystem/...` (`observation-category`, `condition-category`, `condition-clinical`, `v3-ActCode`, `v3-RoleCode`, `diagnosis-role`, `v2-0203`, `v2-0074`, `v2-0916`, `v3-ObservationInterpretation`, `discharge-disposition`, `goal-category`, `goal-achievement`, `risk-probability`, `allergyintolerance-clinical`, `v3-orderableDrugForm`) |
| UCUM | units in every `Quantity` | — | `http://unitsofmeasure.org` |
| WHO ATC | route of administration | — | `http://www.whocc.no/atc` |
| DICOM | imaging modality | — | `http://dicom.nema.org/resources/ontology/DCM` |

Validation (`api-validasi`): the FHIR Processor validates ICD-10, ICD-9 CM, LOINC, SNOMED-CT and other HL7 code systems on write; unknown codes return `Code not found` (RuleNumber 10001), wrong systems `Invalid coding system` (10002).

Lampiran Terminologi (terminology appendices) exist per use case (22 listed: Rawat Jalan, IGD, Rawat Inap, ANC, …); only the Rawat Jalan one is in the corpus.

## Vital-sign and physical-exam LOINC codes
The terminology pages themselves list **no** vital-sign codes. The codes below are printed in `interop-rme-rawat-jalan.md` (step 4) and, for heart rate, on `res-observation.md`. `term-loinc-laboratory` only notes that "pemeriksaan tanda-tanda vital" falls under the LOINC *klinis* scope.

| Variable | LOINC | Display | UCUM unit / code | Category |
|---|---|---|---|---|
| Heart rate (denyut jantung) | `8867-4` | Heart rate | `beats/min` / `/min` | `vital-signs` |
| Respiratory rate (pernapasan) | `9279-1` | Respiratory rate | `breaths/min` / `/min` | `vital-signs` |
| Systolic BP | `8480-6` | Systolic blood pressure | `mm[Hg]` / `mm[Hg]` | `vital-signs` |
| Diastolic BP | `8462-4` | Diastolic blood pressure | `mm[Hg]` / `mm[Hg]` | `vital-signs` |
| Body temperature (suhu tubuh) | `8310-5` | Body temperature | `C` / `Cel` | `vital-signs` |
| Body height (tinggi badan) | `8302-2` | Body height | `cm` / `cm` | `vital-signs` |
| Body weight (berat badan) | `29463-7` | Body weight | `kg` / `kg` | `vital-signs` |
| Body surface area (anak) | `8277-6` | Body surface area | `m²` / `m²` | `vital-signs` |
| Level of responsiveness (tingkat kesadaran) | `67775-7` | Level of responsiveness | value = SNOMED (see below) | `exam` |
| Mental status (status psikologis) | `8693-4` | Mental Status | value = SNOMED | `survey` |
| Pregnancy status | `82810-3` | Pregnancy status | SNOMED `77386006` / `60001007` | `survey` |

Oxygen saturation (`2708-6`, `59408-5`) appears **nowhere** in the corpus (grep over all raw files).

## Code migrations recorded in the Rawat Jalan appendix (`term-lampiran-rawat-jalan`)
Versi 1.2 used Kemkes `clinical-term` codes; Versi 2.0 (playbook v2.0, 03 Mei 2023) replaced them with SNOMED CT. Both are printed; the current use-case page uses only the SNOMED codes.

| Variable | Versi 1.2 (`http://terminology.kemkes.go.id/CodeSystem/clinical-term`) | Versi 2.0 (`http://snomed.info/sct`) |
|---|---|---|
| Prognosis: Baik / Dubia et bonam / Dubia et malam / Tidak baik | `PR000001` … `PR000004` | `170968001` Prognosis good, `65872000` Fair prognosis, `67334001` Guarded prognosis, `170969009` Prognosis bad |
| Kondisi saat meninggalkan RS: Stabil / Tidak stabil / Perbaikan | `MN000001` … `MN000003` | `359746009`, `162668006`, `268910001` |
| Tingkat kesadaran: Alert / Voice / Pain / Unresponsive / Gelisah / Acute Confusional States | `TK000001` … `TK000006` | `248234008` Mentally alert, `300202002` Response to voice, `450847001` Response to pain, `422768004` Unresponsive, `130987000` Acute confusion, `2776000` Delirium |
| Rencana tindak lanjut: Rawat inap | `TL000001` | `737481003` Inpatient care management (only this row is printed) |
| Edukasi (7 topics) | `ED000001` … `ED000007` | `84635008`, `967006`, `410082002`, `712651001`, `61310001`, `698608004`, `362978005` |

Contradiction to record: the appendix places the tingkat-kesadaran SNOMED codes on `Observation.code.coding`, while the use-case page (step 4) puts LOINC `67775-7` in `Observation.code` and the SNOMED codes in `Observation.valueCodeableConcept`. Display strings also differ slightly (`Response to pain` vs `Responds to pain`). Both recorded verbatim, neither resolved.

## KFA structure (`term-lampiran-rawat-jalan`, `interop-rme-rawat-jalan`)
| Tag | Name | Code format | Naming | Example |
|---|---|---|---|---|
| BZA | Bahan Zat Aktif (active substance) | `91xxxxxx` | Nama molekul kimia | Paracetamol (`91000101`) |
| POV | Produk Obat Virtual | `92xxxxxx` | Zat aktif + kekuatan + satuan + bentuk sediaan | Paracetamol 500 mg Tablet |
| POA | Produk Obat Aktual | `93xxxxxx` | POV + (merek dagang) | Paracetamol 500 mg Tablet (Panadol) |
| POAK | Produk Obat Aktual dalam Kemasan | `94xxxxxx` | packaged actual product | `94002470` |
| Alat kesehatan (temporary) | — | `32999999` virtual / `33999999` actual | display = device name | — |

Prescribing matrix: `Medication.code` on MedicationRequest may be `92` or `93` (`91` is **Invalid**); on MedicationDispense must be `93`.

## LOINC structure and lab mapping rules (`term-loinc`, `term-loinc-laboratory`)
| Topic | Rule |
|---|---|
| Code shape | numeric, 3–7 characters, last digit a check digit after the hyphen (`xxxxxx-x`); > 90,000 codes |
| Names | Fully Specified Name (6 parts: analyte, property, time, system, scale, method); **Long Common Name** is the recommended display for exchange; Short Name (≤ 40 chars, not unique) discouraged |
| Categories | radiologi, klinis, HIPAA attachment, standardized survey instrument; lab scope = anything measured on a specimen; clinical scope includes vital signs, EKG, USG… |
| Scale types | `Qn` quantitative (numeric, may carry `<`, `>`, `>=`, `<=`), `Ord` ordinal, `OrdQn`, `Nom` nominal, `Nar` narrative, `Multi`, `Doc`, `Set` |
| Answer lists | LOINC answer lists (`LL…` ids) are Normative (wajib), Preferred, or Example; used for Nominal/Ordinal results |
| Mapping template | columns Kategori, Kode Lokal, Nama Pemeriksaan, Permintaan/Hasil (Permintaan / Hasil / Permintaan & Hasil), Spesimen, Tipe Hasil (Nominal, Ordinal, Quantitative, Narrative, OrdQn), Satuan, Metode |
| Missing code | request via form to Kemenkes; ~1 month to appear; interim national code `X099080`+ |
| Relation to others (FAQ) | ICD-10 = diseases; LOINC = observation/test *question*, SNOMED CT = *answer*; ICD-9 CM = procedures for billing |

## SNOMED CT facts stated (`term-snomed-ct`)
- 19 top-level concepts; components Concept, Description (FSN + Synonym), Relationship; SCTID 6–18 digits, partition identifiers `00`/`01`/`02` (short) or `10`/`11`/`12` (long), Verhoeff check digit.
- Data types: Time `YYYYMMDD`, Boolean 1/0, String UTF-8, Integer 32-bit signed.
- Use-case pages constrain SNOMED values with ECL queries, e.g. `< 404684003 |Clinical finding|` for conditions, `< 71388002 |Procedure|` for procedures, `< 123038009 |Specimen|` for specimen types.

## Notes for our server
- Ship a terminology table keyed by (system, code) seeded with: the eight vital-sign LOINC codes above, `observation-category` codes `vital-signs`/`exam`/`survey`/`laboratory`/`imaging`, `v3-ActCode` `AMB`, `condition-category` `encounter-diagnosis`/`problem-list-item`, `diagnosis-role` `CC`, and the SNOMED answer sets for tingkat kesadaran and prognosis.
- Validate ICD-10 / ICD-9 CM codes by format only (we cannot embed the Kemenkes spreadsheets); return the playbook's `Code not found` / `Invalid coding system` messages.
- Enforce UCUM on every `valueQuantity` and store `unit` and `code` separately, because the playbook prints different `unit` and `code` strings (`beats/min` vs `/min`, `C` vs `Cel`).
- If we add SpO2 we must choose a LOINC code ourselves (not in the playbook) and flag it as a local extension.
- Keep the migration table so old Kemkes `clinical-term` codes can be accepted and mapped to SNOMED on read.

## Sources
- raw/satusehat/term-index.md
- raw/satusehat/term-standar.md
- raw/satusehat/term-loinc.md
- raw/satusehat/term-loinc-laboratory.md
- raw/satusehat/term-snomed-ct.md
- raw/satusehat/term-icd-10.md
- raw/satusehat/term-icd-9-cm.md
- raw/satusehat/term-lampiran-rawat-jalan.md
- raw/satusehat/interop-rme-rawat-jalan.md
- raw/satusehat/api-validasi.md
