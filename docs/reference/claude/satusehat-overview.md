# SATUSEHAT — Overview (what it is, FHIR basis, prerequisites, glossary)

Ringkasan (summary): SATUSEHAT is Indonesia's national Health Information Exchange (HIE) run by Kementerian Kesehatan; every fasyankes (health facility) system integrates with it over an HTTPS REST API using HL7 FHIR resources, after an onboarding phase (auth, Organization, Location, Practitioner, Patient IHS numbers). This file records what the playbook's preface, introduction, service, FHIR-framework and glossary pages state, and lists the resources SATUSEHAT says it supports.

## What SATUSEHAT is (`playbook-introduction`, `playbook-service`)
| Topic | Statement |
|---|---|
| Definition | "ekosistem pertukaran data kesehatan (HIE: Health Information Exchange)" connecting fasyankes, regulators, payers (penjamin) and digital-service providers; aligned with the Cetak Biru Transformasi Digital Kesehatan 2024 (dto.kemkes.go.id) |
| Problems it addresses | > 400 unintegrated government health apps; duplicate data collection; non-uniform metadata; no interoperability standard |
| Goals | standard specs for business process, data, technical and security; any programming language via **HL7 FHIR** + **HTTPS REST API**; issue a **nomor SATUSEHAT** as single identifier of a patient's health information |
| Services | MPI (get a patient's SATUSEHAT number from NIK and/or demographics); Master SDMK (get a practitioner's IHS number from NIK/demographics); Patient Registration (send visit data); Submit Patient Diagnostic Data |
| Master data indexes | MPI (patients, Dukcapil-validated), Master SDMK / MNI (nakes: STR, SIP…), MSI (35 facility types; from SISDMK, SIRS, SIMADA), Kamus KFA (drugs/devices; BPOM, LKPP), Data Pembiayaan, Data Layanan |

## FHIR version and profile location
- No page in the corpus states a FHIR version number in prose. The version is evidenced only by the API base path `/fhir-r4/v1` and the profile canonical `https://fhir.kemkes.go.id/r4/StructureDefinition/<Resource>` (e.g. in `mpi-rest-api`). `fhir-index` says SATUSEHAT "menggunakan HL7 FHIR" and points to the Indonesian profiles on Simplifier ("Simplifier FHIR Profiles", no URL printed).
- `fhir-index` names the acronym (Fast Healthcare Interoperability Resources, pronounced "fire") and the standards body HL7 (`https://www.hl7.org/fhir/`).

## Prerequisites / onboarding (`fhir-prerequisites`, `fhir-index`)
The page's numbered list says "4 langkah" but prints five:

| # | Step | Resource / action |
|---|---|---|
| 1 | Autentikasi ke SATUSEHAT | OAuth2 token (api-catalogue/authentication) |
| 2 | Registrasi Struktur Organisasi | POST `Organization` (sub-organisations) |
| 3 | Registrasi Struktur Lokasi | POST `Location` (sub-locations) |
| 4 | Menyimpan Nomor IHS untuk Tenaga Kesehatan | GET `Practitioner` → `{practitioner-ihs-number}` |
| 5 | Mendapatkan Nomor IHS Pasien | GET `Patient` per MPI playbook → `{patient-ihs-number}` |

After prerequisites comes Interoperabilitas (integrasi), split into Modul Pelayanan (use case dasar) and Modul Penerapan (use case tematik).

## Resources SATUSEHAT lists as used for interoperability (`fhir-resources-index`)
46 resource names, verbatim (note `BillingStatus`, `ChargeItemResponse` are not FHIR R4 resource names; recorded as printed):

`Account`, `AllergyIntolerance`, `BillingStatus`, `CarePlan`, `ChargeItem`, `ChargeItemDefinition`, `ChargeItemResponse`, `Claim`, `ClaimResponse`, `ClinicalImpression`, `Composition`, `Condition`, `Coverage`, `CoverageEligibilityRequest`, `CoverageEligibilityResponse`, `DiagnosticReport`, `DocumentReference`, `Encounter`, `Endpoint`, `EpisodeOfCare`, `FamilyMemberHistory`, `Goal`, `ImagingStudy`, `Immunization`, `Invoice`, `Location`, `Medication`, `MedicationAdministration`, `MedicationDispense`, `MedicationRequest`, `MedicationStatement`, `NutritionOrder`, `Observation`, `Organization`, `Patient`, `PaymentNotice`, `PaymentReconciliation`, `Practitioner`, `Procedure`, `QuestionnaireResponse`, `RelatedPerson`, `RiskAssessment`, `ServiceRequest`, `Specimen`, `Substance`, `Task`.

Not in this list but referenced elsewhere in the corpus: `PractitionerRole` (API page only), `Bundle` (framework page; search results), `OperationOutcome` (error responses), `Device`/`DeviceMetric` (Observation.device targets), `Consent`, `Provenance`, `Communication`, `Appointment` etc. (only in the Standar Terminologi changelog).

## Conventions from the Pengantar Teknis (`playbook-preface`)
| Convention | Rule |
|---|---|
| Priority keywords (RFC 2119 in Indonesian) | **WAJIB** = MUST; **TIDAK BOLEH** = MUST NOT; **SEBAIKNYA** / **DIREKOMENDASIKAN** = SHOULD; **SEBAIKNYA TIDAK** / **TIDAK DIREKOMENDASIKAN** = SHOULD NOT; **BOLEH** / **OPSIONAL** = MAY; **PERLU** used for "needs to" |
| Symbols | `string` = `""`; `number` = numeric string; `uuid` = 36 characters (32 hex + 4 hyphens), e.g. `123e4567-e89b-12d3-a456-426614174000` |
| HTTP methods | `GET` read, `POST` create, `PUT` update, `PATCH` partial update, `DELETE` delete |
| HTTP status codes listed | `200`, `201` (with `location` header), `202`, `204`, `206`; `400`, `401`, `403`, `404`, `405`, `409`, `413`, `415`, `422`, `429` (rate limiter); `500`, `501`, `503`, `504` |
| ISO 8601 | `YYYY`, `MM`, `DD`, `hh` (00–23), `mm`, `ss` (00–60), `.sss` ms, `.ssssss`; `Z` or `+0000` = UTC; `10:10:58Z` = `17:10:58+0700` Asia/Jakarta |
| Admonitions | Catatan, Tips, Penting, Perhatian, Peringatan |

## FHIR framework as restated (`fhir-framework`)
| Concept | JSON shape stated |
|---|---|
| `Element` | value in `{nama_element}`; `id` and `extension[]` in a sibling `_{nama_element}` object for primitives; non-primitives carry `id`/`extension` inline; repeated primitives become parallel arrays with `null` placeholders |
| `Resource` | `resourceType`, `id`, `meta` (Meta), `implicitRules` (uri), `language` (code, ValueSet languages) |
| `DomainResource` | adds `text` (Narrative, XHTML), `contained[]` (inline resources), `extension[]`, `modifierExtension[]` |
| `Bundle` | `identifier`, `type` (BundleType), `timestamp`, `total` (wajib for search), `link[] {relation, url}`, `entry[] {link, fullUrl, resource, search {mode, score}, request {method, url, ifNoneMatch, ifModifiedSince, ifMatch, ifNoneExist}, response {status, location, etag, lastModified, outcome}}`, `signature`; used for search results, history, messaging, documents, transactions, collections |

## Glossary — terms that appear in our other files (`glossary` unless noted)
| Term | Gloss |
|---|---|
| SATUSEHAT | national HIE platform (also "SSP", SATUSEHAT Platform) |
| IHS | Indonesia Health Services — issuer of IHS Numbers (`{patient-ihs-number}`, `{practitioner-ihs-number}`) |
| NIK | Nomor Induk Kependudukan — national ID number on the KTP |
| Dukcapil | Kependudukan dan Catatan Sipil — civil registry that validates NIK |
| MPI / MNI / MSI | Master Patient Index / Master Nakes Index / Master Sarana Index |
| SDMK, SISDMK | Sistem Informasi Sumber Daya Manusia Kesehatan (health-workforce information system) |
| Nakes | tenaga kesehatan (health worker); STR = Surat Tanda Registrasi, SIP = Surat Izin Praktik |
| Fasyankes | fasilitas pelayanan kesehatan (health facility); RS = rumah sakit; Puskesmas = community health centre |
| RME | Rekam Medis Elektronik (electronic medical record) |
| KFA | Kamus Farmasi dan Alat Kesehatan (drug/device dictionary; BPOM, LKPP sources) |
| KPTL | Kode Pembiayaan Tindakan dan Layanan Kesehatan Nasional (`term-index`) |
| SIRS, SIMADA | Sistem Informasi Rumah Sakit; Sistem Informasi Manajemen Data Kefarmasian |
| Modul Pelayanan / Penerapan (Use Case) | service module (Rawat Jalan, Rawat Inap…) / disease-specific use case (ANC, Gizi…) |
| Rawat jalan / rawat inap / IGD | outpatient / inpatient / emergency department (`interop-index`) |
| Wajib | mandatory (`*` marker) |
| Kamus | dictionary; Kamus Validasi = validation rule dictionary |
| Pemetaan Nilai / Pemetaan Variabel | value mapping / variable mapping (per-resource element lists in the playbooks) |
| Lampiran | appendix |
| HIE, HL7, FHIR, LOINC, SNOMED CT, ICD-10, ICD-9-CM, JSON, XML, cURL, API | as in the glossary; DICOM C-STORE and FHIRPath also defined |
| BPOM, LKPP | Badan Pengawas Obat dan Makanan; Lembaga Kebijakan Pengadaan Barang dan Jasa |

## Notes for our server
- Advertise ourselves as FHIR R4 (base path `/fhir-r4/v1`, profiles under an `.../r4/StructureDefinition/` canonical) since that is the only version evidence the playbook gives.
- Implement `Bundle` type `searchset` with `total` and `link` for every search, and `OperationOutcome` for errors, matching the framework page.
- Onboarding order for admin seeding: Organization → Location → Practitioner → Patient (the playbook's prerequisites) before any Encounter.
- Support the listed HTTP methods (GET/POST/PUT/PATCH; the playbook lists DELETE in the preface but no resource page uses it) and map failures to the status codes above (`400`/`422` validation, `401`/`403` auth, `404`, `409` duplicate, `429` rate limit).
- Reuse the wajib/tidak boleh vocabulary in our own specs so rule text stays comparable with the playbook.

## Sources
- raw/satusehat/playbook-preface.md
- raw/satusehat/playbook-introduction.md
- raw/satusehat/playbook-service.md
- raw/satusehat/glossary.md
- raw/satusehat/fhir-index.md
- raw/satusehat/fhir-framework.md
- raw/satusehat/fhir-prerequisites.md
- raw/satusehat/fhir-resources-index.md
