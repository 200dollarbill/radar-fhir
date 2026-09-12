# SATUSEHAT — Condition

Ringkasan (summary): `Condition` carries a patient diagnosis coded in ICD-10; **one Condition payload = one ICD-10 code** (two diagnoses = two Conditions). Only `code`, `subject` and `encounter` are marked wajib on the profile page.

General rules: `*` = wajib (mandatory); times in UTC+00; dates not earlier than 03 June 2014.

## Required / constrained elements
Cardinality `n/s` (not stated) unless printed.

| Element | Cardinality | SATUSEHAT rule | Value set / system |
|---|---|---|---|
| identifier[i] | n/s | Local report/diagnosis number; `use` IdentifierUse (`official`); `value` e.g. `5234342` | `http://sys-ids.kemkes.go.id/condition/{organization-ihs-number}` (page prints `{{organization-ihs-number}}` with doubled braces) |
| clinicalStatus | n/s | `CodeableConcept`; example `active` | `http://terminology.hl7.org/CodeSystem/condition-clinical` |
| verificationStatus | n/s | `CodeableConcept`; example `provisional` | named system `http://terminology.hl7.org/CodeSystem/condition-ver-status`; example prints `https://www.hl7.org/fhir/Codesystem-condition-ver-status` (inconsistent on the page) |
| category[i] | n/s | `CodeableConcept`; example `encounter-diagnosis` | `http://terminology.hl7.org/CodeSystem/condition-category` |
| severity | n/s | `CodeableConcept`; example `24484000` "Severe" | `http://snomed.info/sct` |
| **\*code** | n/s (wajib) | `CodeableConcept`; ICD-10 (2010) for visit diagnosis, `http://terminology.kemkes.go.id/CodeSystem/clinical-term` for condition at discharge; `code.coding` example `C47.0` | `http://hl7.org/fhir/sid/icd-10`; `http://terminology.kemkes.go.id/CodeSystem/clinical-term` |
| bodySite[i] | n/s | `CodeableConcept`; example `111002` | `http://snomed.info/sct` |
| **\*subject** | n/s (wajib) | Reference `Patient \| Group`, format `Patient/{patient-ihs-number}` | — |
| **\*encounter** | n/s (wajib) | Reference `Encounter/{ID-resource-Encounter}` (server-issued) | — |
| onset[x] | n/s | `onsetDateTime` (`YYYY`…`YYYY-MM-DDThh:mm:ss+zz:zz`), `onsetAge`, `onsetPeriod` (`start`/`end`, `YYYY-MM-DD`), `onsetRange`, `onsetString` | — |
| abatement[x] | n/s | `abatementDateTime`, `abatementAge`, `abatementPeriod` (`start`/`end`, `YYYY-MM-DD`), `abatementRange`, `abatementString` | — |
| recordedDate | n/s | `dateTime` | — |
| recorder | n/s | Reference `Practitioner \| PractitionerRole \| Patient \| RelatedPerson`, format `Practitioner/{practitioner-ihs-number}` | — |
| asserter | n/s | Reference `Practitioner \| PractitionerRole \| Patient \| RelatedPerson` | — |
| stage[i] | n/s | `summary` (`CodeableConcept`, SNOMED CT), `assessment[i]` (Reference `ClinicalImpression \| DiagnosticReport \| Observation`), `type` (`CodeableConcept`, SNOMED CT) | `http://snomed.info/sct` |
| evidence[i] | n/s | `code[i]` (`CodeableConcept`, SNOMED CT), `detail[i]` (Reference to any resource) | `http://snomed.info/sct` |
| note[i] | n/s | `Annotation` | — |

## Identifier systems used
| Purpose | system URI |
|---|---|
| Condition.identifier (local diagnosis id, per parent organisation) | `http://sys-ids.kemkes.go.id/condition/{organization-ihs-number}` |
| Condition.identifier.use | `http://hl7.org/fhir/identifier-use` |
| Condition.code (ICD-10) | `http://hl7.org/fhir/sid/icd-10` |
| Condition.code (discharge condition) | `http://terminology.kemkes.go.id/CodeSystem/clinical-term` |

## REST operations (from Katalog API)
Base (staging): `https://api-satusehat-stg.dto.kemkes.go.id/fhir-r4/v1`; `*Authorization: Bearer <access_token>`; `*Content-Type: application/json` on detail/write.

| Method | Path | Notes |
|---|---|---|
| GET | `/Condition?subject=<patient-id>&encounter=<uuid>` | Search by subject (`string`) and/or encounter (`uuid`) |
| GET | `/Condition/:id` | Detail; `:id` `uuid` (example `2a4e1a13-ee52-4c8b-a2ef-f41c79de698d`) |
| POST | `/Condition` | Create; store returned `id` (referenced from `Encounter.diagnosis.condition`) |
| PUT | `/Condition/:id` | Full update |
| PATCH | `/Condition/:id` | JSON Patch, only `op: "replace"`, path like `/language` |

Responses: `Bundle` `searchset`; `4xx` `OperationOutcome`; `5xx` `text/plain`.

## Minimal example (JSON skeleton)
```json
{
  "resourceType": "Condition",
  "identifier": [ { "system": "http://sys-ids.kemkes.go.id/condition/10000004", "use": "official", "value": "5234342" } ],
  "clinicalStatus": { "coding": [ { "system": "http://terminology.hl7.org/CodeSystem/condition-clinical", "code": "active", "display": "Active" } ] },
  "category": [ { "coding": [ { "system": "http://terminology.hl7.org/CodeSystem/condition-category", "code": "encounter-diagnosis", "display": "Encounter Diagnosis" } ] } ],
  "code": { "coding": [ { "system": "http://hl7.org/fhir/sid/icd-10", "code": "C47.0", "display": "Malignant neoplasm, peripheral nerves of head, face and neck" } ] },
  "subject": { "reference": "Patient/100000030009", "display": "Budi Santoso" },
  "encounter": { "reference": "Encounter/2b2d0a3e-082a-4fe9-ae13-da9c3b5e422f" },
  "recorder": { "reference": "Practitioner/N10000001", "display": "Dokter Bronsig" }
}
```
The profile page prints `subject`, `encounter` and `recorder` examples wrapped in arrays; FHIR R4 defines them as single references, used as such above.

## Notes for our server
- Reject a Condition missing `code`, `subject`, or `encounter`.
- Enforce one ICD-10 coding per Condition (`code.coding` from `http://hl7.org/fhir/sid/icd-10`); a doctor entering two diagnoses creates two Conditions.
- Accept `http://terminology.kemkes.go.id/CodeSystem/clinical-term` as an alternate `code` system for discharge conditions.
- `subject` must resolve to a Patient, `encounter` to an Encounter, `recorder` to a Practitioner (doctor role).
- Support search by `subject` and `encounter`; read; POST; PUT; PATCH-replace.
- `identifier.system` must follow `http://sys-ids.kemkes.go.id/condition/{our-org-id}`.

## Sources
- raw/satusehat/res-condition.md
- raw/satusehat/api-condition.md
