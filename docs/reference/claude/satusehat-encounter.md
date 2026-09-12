# SATUSEHAT — Encounter

Ringkasan (summary): `Encounter` records a kunjungan (visit): when it started and ended, which nakes served, which patient, plus diagnoses and location. It is the hub every clinical resource (Observation, Condition, Procedure) references; the profile page marks many elements wajib, including a `statusHistory` that must carry `arrived`, `in-progress` and `finished`.

General rules: `*` = wajib (mandatory); times in UTC+00; dates not earlier than 03 June 2014.

## Required / constrained elements
Cardinality `n/s` (not stated) unless printed.

| Element | Cardinality | SATUSEHAT rule | Value set / system |
|---|---|---|---|
| **\*identifier[i]** | n/s (wajib) | Local visit number; `use` IdentifierUse (`official`); `value` e.g. `P20240001` | `http://sys-ids.kemkes.go.id/encounter/{organization-ihs-number}` |
| **\*status** | n/s (wajib) | `code`; example `arrived` | `http://hl7.org/fhir/encounter-status` |
| **\*statusHistory.status** | n/s (wajib) | `code`; **three statuses must be sent: `arrived`, `in-progress`, `finished`** (page writes "In-progress") | `http://hl7.org/fhir/encounter-status` |
| **\*statusHistory.period** | n/s (wajib) | `Period`; **\*start** and **\*end** both wajib; text says format `YYYY-MM-DD` but examples are full `dateTime` (`2022-06-14T07:00:00+07:00`) | — |
| **\*class** | n/s (wajib) | `Coding`; example `AMB` "ambulatory" | `http://terminology.hl7.org/CodeSystem/v3-ActCode` (ActEncounterCode) |
| **\*classHistory.class** | n/s (wajib) | `Coding`, same set as `class` | `http://terminology.hl7.org/CodeSystem/v3-ActCode` |
| **\*classHistory.period** | n/s (wajib) | `Period` (`start`, `end`; the `end` heading is mislabeled `statusHistory.period.end` on the page) | — |
| type[i] | n/s | `CodeableConcept`; example `ADMS` | `http://terminology.hl7.org/CodeSystem/encounter-type` |
| serviceType | n/s | `CodeableConcept`; example `7` "Friendly Visiting" | `http://terminology.hl7.org/CodeSystem/service-type` |
| priority | n/s | `CodeableConcept`; example `A` "ASAP" | `http://terminology.hl7.org/CodeSystem/v3-ActPriority` |
| **\*subject** | n/s (wajib) | Reference `Patient/{patient-ihs-number}` | — |
| episodeOfCare[i] | n/s | Reference `EpisodeOfCare/{id}` | — |
| basedOn[i] | n/s | Reference `ServiceRequest/{id}` | — |
| participant.type[i] | n/s | `CodeableConcept`; example `ATND` "attender" | `http://terminology.hl7.org/CodeSystem/v3-ParticipationType` |
| participant.individual | n/s | Reference `Practitioner/{practitioner-ihs-number}` (SATUSEHAT ID of the doctor/nakes) | — |
| **\*period** | n/s (wajib) | `Period`: `start` = arrival, `end` = departure; `dateTime` formats `YYYY`, `YYYY-MM`, `YYYY-MM-DD`, `YYYY-MM-DDThh:mm:ss+zz:zz` | — |
| length | n/s | `Duration` | — |
| reasonCode[i] | n/s | `CodeableConcept` | — |
| **\*reasonCode[i].coding** | n/s (wajib within reasonCode) | `Coding` | EncounterReasonCodes (`http://hl7.org/fhir/R4/valueset-encounter-reason.html`) |
| reasonReference[i] | n/s | Reference `Condition \| Procedure \| Observation \| ImmunizationRecommendation`, format `Condition/{id-condition}` | — |
| **\*diagnosis.condition** | n/s (wajib) | Reference `Condition \| Procedure`, format `Condition/{id-resource-Condition}`; may be >1 (admission and/or discharge diagnoses) | — |
| **\*diagnosis.use** | n/s (wajib) | `CodeableConcept`; example `AD` "Admission diagnosis" | printed system `https://www.hl7.org/fhir/Codesystem-diagnosis-role` (DiagnosisRole) |
| **\*diagnosis.rank** | n/s (wajib) | `positiveInt`; lower = more primary when >1 condition | — |
| account[i] | n/s | Reference `Account/{id-account}` | — |
| hospitalization.preAdmissionIdentifier | n/s | `Identifier` | — |
| hospitalization.origin / destination | n/s | Reference `Location \| Organization`, format `Location/{id-resource-Location}` (page example prints `"Location 4adccec5-..."` without the slash — typo) | — |
| hospitalization.admitSource | n/s | example `hosp-trans` | `http://terminology.hl7.org/CodeSystem/admit-source` |
| hospitalization.reAdmission | n/s | example `R` "Re-admission"; empty = not a readmission | `http://terminology.hl7.org/CodeSystem/v2-0092` |
| hospitalization.dietPreference[i] | n/s | example `vegetarian` | `http://terminology.hl7.org/CodeSystem/diet` |
| hospitalization.specialArrangement[i] | n/s | example `wheel` | `http://terminology.hl7.org/CodeSystem/encounter-special-arrangements` |
| hospitalization.dischargeDisposition | n/s | example `rehab` | `http://terminology.hl7.org/CodeSystem/discharge-disposition` |
| **\*location[i]** | n/s (wajib) | Reference `Location/{id-resource-Location}` (exam room / poli) | — |
| location.extension:serviceClass (`value`, `upgradeClassIndicator`) | n/s | `CodeableConcept` each: ward class (Kelas 1/2/3/VIP/VVIP) and class-change indicator (tetap, kenaikan, penurunan, titip) | extension `serviceClass` (Simplifier page; URL not printed) |
| **\*serviceProvider** | n/s (wajib) | Reference `Organization/{organization-ihs-number}` | — |
| partOf | n/s | Reference `Encounter/{id-encounter}` | — |

## Identifier systems used
| Purpose | system URI |
|---|---|
| Encounter.identifier (local visit number, per parent organisation) | `http://sys-ids.kemkes.go.id/encounter/{organization-ihs-number}` |
| Encounter.identifier.use | `http://hl7.org/fhir/identifier-use` |

## REST operations (from Katalog API)
Base (staging): `https://api-satusehat-stg.dto.kemkes.go.id/fhir-r4/v1`; `*Authorization: Bearer <access_token>`; `*Content-Type: application/json` on detail/write.

| Method | Path | Notes |
|---|---|---|
| GET | `/Encounter?subject=<patient-id>` | Only documented search parameter (example `100000000001`) |
| GET | `/Encounter/:id` | Detail; `:id` `uuid` (example `4f735a03-128b-464d-bf91-e6eacdf1c38f`) |
| POST | `/Encounter` | Create; store returned `id` (used by every later resource's `encounter` reference) |
| PUT | `/Encounter/:id` | Full update (how `statusHistory`/`period.end` get filled after the visit) |
| PATCH | `/Encounter/:id` | JSON Patch, only `op: "replace"`, path like `/language` |

Responses: `Bundle` `searchset`; `4xx` `OperationOutcome`; `5xx` `text/plain`.

## Minimal example (JSON skeleton)
```json
{
  "resourceType": "Encounter",
  "identifier": [ { "system": "http://sys-ids.kemkes.go.id/encounter/10000004", "use": "official", "value": "P20240001" } ],
  "status": "arrived",
  "class": { "system": "http://terminology.hl7.org/CodeSystem/v3-ActCode", "code": "AMB", "display": "ambulatory" },
  "subject": { "reference": "Patient/100000030009", "display": "Budi Santoso" },
  "participant": [ { "type": [ { "coding": [ { "system": "http://terminology.hl7.org/CodeSystem/v3-ParticipationType", "code": "ATND", "display": "attender" } ] } ],
                     "individual": { "reference": "Practitioner/N10000001", "display": "Dokter Bronsig" } } ],
  "period": { "start": "2022-06-14T07:00:00+07:00", "end": "2022-06-14T08:00:00+07:00" },
  "location": [ { "location": { "reference": "Location/408ba28c-3115-4df5-85c6-60f15b44e7fa", "display": "Ruang 1A, Poliklinik Rawat Jalan" } } ],
  "diagnosis": [ { "condition": { "reference": "Condition/4bbbe654-14f5-4ab3-a36e-a1e307f67bb8" },
                   "use": { "coding": [ { "system": "https://www.hl7.org/fhir/Codesystem-diagnosis-role", "code": "AD", "display": "Admission diagnosis" } ] },
                   "rank": 1 } ],
  "statusHistory": [ { "status": "arrived", "period": { "start": "2022-06-14T07:00:00+07:00", "end": "2022-06-14T08:00:00+07:00" } } ],
  "serviceProvider": { "reference": "Organization/1000004" }
}
```
Note: the profile page prints `class` and `subject` examples wrapped in a JSON array; FHIR R4 defines both as single values, and the skeleton above uses single values.

## Notes for our server
- Reject an Encounter missing `identifier`, `status`, `class`, `subject`, `period`, `location`, or `serviceProvider` (all `*`).
- Enforce within sub-elements: every `statusHistory[i]` needs `status` and `period.start`/`period.end`; every `classHistory[i]` needs `class` and `period`; every `diagnosis[i]` needs `condition`, `use`, `rank`; every `reasonCode[i]` needs `coding`.
- Finished visits must carry `statusHistory` entries for `arrived`, `in-progress` and `finished` — the server should validate this when `status` becomes `finished` (relaxable while the visit is open).
- `subject` must resolve to a Patient, `participant.individual` to a Practitioner, `location.location` to a Location, `serviceProvider` to an Organization, `diagnosis.condition` to a Condition/Procedure.
- Search only by `subject` is required for parity; our doctor/patient views will also want `date`/`status` filters (local extension).
- Class for outpatient vital-sign visits: `AMB` from `http://terminology.hl7.org/CodeSystem/v3-ActCode`.

## Sources
- raw/satusehat/res-encounter.md
- raw/satusehat/api-encounter.md
