# SATUSEHAT — Procedure

Ringkasan (summary): `Procedure` reports a tindakan/prosedur medis (medical action) — diagnostic or therapeutic, non-invasive (consultation, education) or invasive (surgery) — coded with **ICD-9 CM**. Wajib elements: `status`, `code` (+ `code.coding`), `subject`, `encounter`, and `performer.actor` / `focalDevice.manipulated` when their parent is present.

General rules: `*` = wajib (mandatory); times in UTC+00; dates not earlier than 03 June 2014.

## Required / constrained elements
Cardinality `n/s` (not stated) unless printed.

| Element | Cardinality | SATUSEHAT rule | Value set / system |
|---|---|---|---|
| identifier[i] | n/s | Faskes-internal procedure id; `use` IdentifierUse (`official`); `value` e.g. `5234342` | `http://sys-ids.kemkes.go.id/procedure/{organization-ihs-number}` (text prints `{{...}}/` with a trailing slash; example has no trailing slash) |
| instantiatesCanonical[i] / instantiatesUri[i] | n/s | `canonical` / `uri` | — |
| basedOn[i] | n/s | Reference `CarePlan \| ServiceRequest`, format `ServiceRequest/{id}` | — |
| partOf[i] | n/s | Reference `Procedure \| Observation \| MedicationAdministration` | — |
| **\*status** | n/s (wajib) | `code`; example `completed` | `http://hl7.org/fhir/event-status` (EventStatus) |
| statusReason | n/s | `CodeableConcept`; example `182840001` | `http://snomed.info/sct` (value set `http://hl7.org/fhir/ValueSet/procedure-not-performed-reason`) |
| category | n/s | `CodeableConcept`; example `103693007` "Diagnostic procedure" | `http://snomed.info/sct` |
| **\*code** | n/s (wajib) | `CodeableConcept`; **\*code.coding** wajib; example `87.44` "Routine chest x-ray, so described" | `http://hl7.org/fhir/sid/icd-9-cm` (ICD-9 CM) |
| **\*subject** | n/s (wajib) | Reference `Patient \| Group`, format `Patient/{patient-ihs-number}` | — |
| **\*encounter** | n/s (wajib) | Reference `Encounter/{id-resource-Encounter}` | — |
| performed[x] | n/s | `performedDateTime`, `performedPeriod` (`start`/`end` `dateTime`; examples use `+01:00` offset), `performedString`, `performedAge`, `performedRange` | — |
| recorder / asserter | n/s | Reference `Patient \| RelatedPerson \| Practitioner \| PractitionerRole` | — |
| performer[i] | n/s | `BackboneElement` | — |
| performer.function | n/s | `CodeableConcept` (surgeon, anaesthetist, ...) | `http://snomed.info/sct` (ProcedurePerformerRoleCodes) |
| **\*performer.actor** | n/s (wajib within performer) | Reference `Practitioner \| PractitionerRole \| Organization \| Patient \| RelatedPerson \| Device`, format `Practitioner/{practitioner-ihs-number}` | — |
| performer.onBehalfOf | n/s | Reference `Organization/{organization-ihs-number}` | — |
| location | n/s | Reference `Location/{id-resource-Location}` | — |
| reasonCode[i] | n/s | `CodeableConcept`; ICD-10 (2010); example `A15.0` | `http://hl7.org/fhir/sid/icd-10` |
| reasonReference[i] | n/s | Reference `Condition \| Observation \| Procedure \| DiagnosticReport \| DocumentReference` | — |
| bodySite[i] | n/s | `CodeableConcept`; example `302551006` "Entire Thorax" | `http://snomed.info/sct` |
| outcome | n/s | `CodeableConcept`; example `385669000` "Successful" | `http://snomed.info/sct` |
| report[i] | n/s | Reference `DiagnosticReport \| DocumentReference \| Composition` | — |
| complication[i] | n/s | `CodeableConcept`; ICD-10 (2010); example `A41.9` | `http://hl7.org/fhir/sid/icd-10` |
| complicationDetail[i] | n/s | Reference `Condition/{id-resource-Condition}` | — |
| followUp[i] | n/s | `CodeableConcept` | `http://snomed.info/sct` (value set `http://hl7.org/fhir/ValueSet/procedure-followup`) |
| note[i] | n/s | `Annotation`: `authorReference` (`Practitioner/{practitioner-ihs-number}`), `time` (`dateTime`), `text` | — |
| focalDevice[i] | n/s | `BackboneElement`; `action` (`CodeableConcept`, example `360325005`) | `http://snomed.info/sct` (value set `http://hl7.org/fhir/ValueSet/device-action`) |
| **\*focalDevice.manipulated** | n/s (wajib within focalDevice) | Reference `Device` | — |
| usedReference[i] | n/s | Reference `Device \| Medication \| Substance` | — |
| usedCode[i] | n/s | `CodeableConcept`; text names FHIRDeviceTypes but the example uses KFA (`Kode KFA` / product name) | `http://sys-ids.kemkes.go.id/kfa` (example); `http://hl7.org/fhir/ValueSet/device-kind` (text) |

## Identifier systems used
| Purpose | system URI |
|---|---|
| Procedure.identifier (local id, per parent organisation) | `http://sys-ids.kemkes.go.id/procedure/{organization-ihs-number}` |
| Procedure.identifier.use | `http://hl7.org/fhir/identifier-use` |
| Procedure.code (ICD-9 CM) | `http://hl7.org/fhir/sid/icd-9-cm` |
| reasonCode / complication (ICD-10) | `http://hl7.org/fhir/sid/icd-10` |
| usedCode (KFA product code, from example) | `http://sys-ids.kemkes.go.id/kfa` |

## REST operations (from Katalog API)
Base (staging): `https://api-satusehat-stg.dto.kemkes.go.id/fhir-r4/v1`; `*Authorization: Bearer <access_token>`; `*Content-Type: application/json` on detail/write.

| Method | Path | Notes |
|---|---|---|
| GET | `/Procedure?subject=<patient-id>&encounter=<uuid>` | Search by subject (`string`) and/or encounter (`uuid`) |
| GET | `/Procedure/:id` | Detail; `:id` `uuid` (example `6c9cb16e-7775-4c80-b5b2-3d04901df1f3`) |
| POST | `/Procedure` | Create; store returned `id` |
| PUT | `/Procedure/:id` | Full update |
| PATCH | `/Procedure/:id` | JSON Patch, only `op: "replace"`, path like `/language` |

Responses: `Bundle` `searchset`; `4xx` `OperationOutcome`; `5xx` `text/plain`.

## Minimal example (JSON skeleton)
```json
{
  "resourceType": "Procedure",
  "identifier": [ { "system": "http://sys-ids.kemkes.go.id/procedure/1000001", "use": "official", "value": "5234342" } ],
  "status": "completed",
  "category": { "coding": [ { "system": "http://snomed.info/sct", "code": "103693007", "display": "Diagnostic procedure" } ] },
  "code": { "coding": [ { "system": "http://hl7.org/fhir/sid/icd-9-cm", "code": "87.44", "display": "Routine chest x-ray, so described" } ] },
  "subject": { "reference": "Patient/100000030009", "display": "Budi Santoso" },
  "encounter": { "reference": "Encounter/2823ed1d-3e3e-434e-9a5b-9c579d192787" },
  "performedPeriod": { "start": "2022-06-14T13:31:00+01:00", "end": "2022-06-14T14:27:00+01:00" },
  "performer": [ { "actor": { "reference": "Practitioner/N10000001", "display": "Dokter Bronsig" },
                   "onBehalfOf": { "reference": "Organization/1000004" } } ],
  "location": { "reference": "Location/08f9fc38-f899-4c3c-ba42-be4baa4dbd54", "display": "Ruang 1A, Poliklinik Rawat Jalan" },
  "reasonCode": [ { "coding": [ { "system": "http://hl7.org/fhir/sid/icd-10", "code": "A15.0", "display": "Tuberculosis of lung, confirmed by sputum microscopy with or without culture" } ] } ],
  "note": [ { "authorReference": { "reference": "Practitioner/N10000001" }, "time": "2015-02-07T13:28:17-05:00", "text": "Rontgen thorax melihat perluasan infiltrat dan kavitas." } ]
}
```
The profile page prints single-valued references (`subject`, `encounter`, `onBehalfOf`, `location`) wrapped in arrays; the skeleton uses FHIR R4 single values.

## Notes for our server
- Reject a Procedure missing `status`, `code` (with `code.coding`), `subject`, or `encounter`.
- Inside each `performer[i]` require `actor`; inside each `focalDevice[i]` require `manipulated`.
- `code.coding.system` must be `http://hl7.org/fhir/sid/icd-9-cm`; `reasonCode` and `complication` use ICD-10 `http://hl7.org/fhir/sid/icd-10`.
- `subject` → Patient, `encounter` → Encounter, `performer.actor` → Practitioner (doctor role), `location` → Location, `complicationDetail` → Condition.
- Support search by `subject` and `encounter`; read; POST; PUT; PATCH-replace.
- `identifier.system` follows `http://sys-ids.kemkes.go.id/procedure/{our-org-id}` (no trailing slash, per the example).

## Sources
- raw/satusehat/res-procedure.md
- raw/satusehat/api-procedure.md
