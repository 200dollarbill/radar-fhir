# SATUSEHAT — Observation

Ringkasan (summary): `Observation` carries patient examination results (hasil pemeriksaan); the SATUSEHAT profile page maps every element with a `*` prefix meaning wajib (mandatory). The Katalog API exposes search, read, create, update and JSON-Patch on `/fhir-r4/v1/Observation`.

General rules stated on the profile page:
- `*` before an element = **WAJIB** (mandatory / must always be present).
- Time values are sent in **UTC+00** (WIB = local − 7 h, WITA = − 8 h, WIT = − 9 h), e.g. 17:35 WIB on 2023-08-23 is sent as `2023-08-23T10:35:00+00:00`.
- Dates sent must not be earlier than **03 June 2014**.
- Whether a non-`*` element is wajib depends on the Panduan Interoperabilitas (interoperability guide) of each use case.

## Required / constrained elements
Cardinality is `n/s` (not stated) unless the raw page gives it; the page only marks elements with `*`.

| Element | Cardinality | SATUSEHAT rule | Value set / system |
|---|---|---|---|
| identifier[i] | n/s | Faskes-internal ID of the observation, type `Identifier`; `use` from IdentifierUse; `value` = local code/ID | system `http://sys-ids.kemkes.go.id/organization/{organization-ihs-number}` (see note on example below) |
| basedOn[i] | n/s | Reference to the request fulfilled (`CarePlan \| DeviceRequest \| ImmunizationRecommendation \| MedicationRequest \| NutritionOrder \| ServiceRequest`), format `ServiceRequest/{id-resource-ServiceRequest}` | — |
| partOf[i] | n/s | Reference to a larger process (`MedicationAdministration \| MedicationDispense \| MedicationStatement \| Procedure \| Immunization \| ImagingStudy`), format `Procedure/{id-resource-Procedure}` | — |
| **\*status** | n/s (wajib) | `code`; example `"final"` | `http://hl7.org/fhir/observation-status` (ObservationStatus) |
| category[i] | n/s | `CodeableConcept`; example code `vital-signs` / "Vital Signs" | `http://terminology.hl7.org/CodeSystem/observation-category` |
| **\*code** | n/s (wajib) | `CodeableConcept`; **\*code.coding** also wajib; example `8867-4` "Heart rate" | `http://loinc.org` (LOINC) |
| **\*subject** | n/s (wajib) | Reference `Patient \| Group \| Device \| Location`, format `Patient/{patient-ihs-number}` (IHS number from Master Pasien Indeks) | — |
| focus[i] | n/s | Reference to the true focus when it is not the patient (e.g. fetus in mother's record) | — |
| **\*encounter** | n/s (wajib) | Reference `Encounter/{id-resource-Encounter}` (ID returned by the server) | — |
| effective[x] | n/s | `effectiveDateTime` (formats `YYYY`, `YYYY-MM`, `YYYY-MM-DD`, `YYYY-MM-DDThh:mm:ss+zz:zz`), `effectivePeriod` (`start`/`end`, same formats), `effectiveTiming`, `effectiveInstant` | — |
| issued | n/s | `instant`, format `YYYY-MM-DDThh:mm:ss.sss+zz:zz` | — |
| performer[i] | n/s | Reference `Practitioner \| PractitionerRole \| Organization \| CareTeam \| Patient \| RelatedPerson`, format `Practitioner/{practitioner-ihs-number}` (from Master Nakes Indeks) | — |
| value[x] | n/s | `valueQuantity` (example: value 80, unit `beats/minute`, code `/min`), `valueCodeableConcept`, `valueString`, `valueBoolean` (raw page spells it `valueBooelean`), `valueInteger`, `valueRange`, `valueRatio`, `valueSampledData`, `valueTime` (hh:mm:ss), `valueDateTime`, `valuePeriod` | Quantity system `http://unitsofmeasure.org` (UCUM) |
| dataAbsentReason | n/s | `CodeableConcept`; example `unknown` | `http://terminology.hl7.org/CodeSystem/data-absent-reason` |
| interpretation[i] | n/s | `CodeableConcept` | `http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation` and `http://terminology.kemkes.go.id/CodeSystem/clinical-term` |
| note[i] | n/s | `Annotation` | — |
| bodySite | n/s | `CodeableConcept`; example `106004` | `http://snomed.info/sct` (SNOMED CT Body Structures) |
| method | n/s | `CodeableConcept` | `http://snomed.info/sct` (ObservationMethods) |
| specimen | n/s | Reference `Specimen` | — |
| device | n/s | Reference `Device` or `DeviceMetric` | — |
| referenceRange[i] | n/s | `low`/`high` (`SimpleQuantity`), `type` (`CodeableConcept`), `appliesTo[i]`, `age` (`Range`), `text` | type: `http://terminology.hl7.org/CodeSystem/referencerange-meaning` |
| hasMember[i] | n/s | Reference `Observation \| QuestionnaireResponse \| MolecularSequence` | — |
| derivedFrom[i] | n/s | Reference `DocumentReference \| ImagingStudy \| Media \| QuestionnaireResponse \| Observation \| MolecularSequence` | — |
| component[i] | n/s | `BackboneElement` | — |
| **\*component.code** | n/s (wajib within a component) | `CodeableConcept` | — (page does not name a system for component.code) |
| component.value[x] | n/s | Same eleven value types as `value[x]` | — |
| component.dataAbsentReason / interpretation[i] / referenceRange[i] | n/s | `CodeableConcept` / `CodeableConcept` / `BackboneElement` (`low`, `high`, `type`, `appliesTo`, `age`, `text`) | — |

## Identifier systems used
| Purpose | system URI |
|---|---|
| Observation.identifier[i].system (as stated in the text) | `http://sys-ids.kemkes.go.id/organization/{organization-ihs-number}` |
| Observation.identifier[i].system (as shown in the JSON example on the same page) | `http://sys-ids.kemkes.go.id/observation/1000001` |
| Observation.identifier[i].use | `http://hl7.org/fhir/identifier-use` |

The text and the example on the profile page disagree (`/organization/` vs `/observation/`); both are recorded verbatim, neither is corrected here.

## REST operations (from Katalog API)
Base (staging): `https://api-satusehat-stg.dto.kemkes.go.id/fhir-r4/v1`. Every call needs header `*Authorization: Bearer <access_token>`; write calls and `GET /:id` also list `*Content-Type: application/json`.

| Method | Path | Notes |
|---|---|---|
| GET | `/Observation?subject=<patient-id>&encounter=<encounter-id>` | Pencarian (search) by subject and/or encounter; returns `Bundle` type `searchset` |
| GET | `/Observation?subject=<patient-id>&based-on=<servicerequest-id>` | Search by subject + ServiceRequest; both `?subject` and `?based-on` are wajib in this mode |
| GET | `/Observation/:id` | Detail; `:id` is `uuid` |
| POST | `/Observation` | Penambahan (create); response `id` (UUID) must be stored for later use |
| PUT | `/Observation/:id` | Pembaruan (full update); returns the payload sent |
| PATCH | `/Observation/:id` | Pembaruan sebagian (partial update), JSON Patch array; only `op: "replace"` is available; `path` like `/language` |

Responses: `2xx`/`4xx` are `application/json` (`4xx` body is `OperationOutcome`); `5xx` is `text/plain` (e.g. `Gateway Timeout`).

## Minimal example (JSON skeleton)
Assembled from the per-element examples on the profile page (values are illustrative).

```json
{
  "resourceType": "Observation",
  "identifier": [
    { "system": "http://sys-ids.kemkes.go.id/observation/1000001", "use": "official", "value": "R100005" }
  ],
  "status": "final",
  "category": [
    { "coding": [ { "system": "http://terminology.hl7.org/CodeSystem/observation-category", "code": "vital-signs", "display": "Vital Signs" } ] }
  ],
  "code": { "coding": [ { "system": "http://loinc.org", "code": "8867-4", "display": "Heart rate" } ] },
  "subject": { "reference": "Patient/100000030009" },
  "encounter": { "reference": "Encounter/2823ed1d-3e3e-434e-9a5b-9c579d192787" },
  "effectiveDateTime": "2022-07-14",
  "issued": "2022-07-14T14:27:00+07:00",
  "performer": [ { "reference": "Practitioner/N10000001" } ],
  "valueQuantity": { "value": 80, "unit": "beats/minute", "system": "http://unitsofmeasure.org", "code": "/min" }
}
```

## Notes for our server
- Reject an Observation that lacks `status`, `code` (with at least one `code.coding`), `subject`, or `encounter` — these are the four `*` elements on the profile page.
- Inside each `component[i]`, `component.code` is `*`; a component without `code` must be rejected.
- Vital-sign Observations from devices map to `category` code `vital-signs` (system `http://terminology.hl7.org/CodeSystem/observation-category`) and `code` from LOINC (`http://loinc.org`); quantities use UCUM `http://unitsofmeasure.org`. `device` may reference a `Device`/`DeviceMetric` resource.
- `subject` must be `Patient/{patient-ihs-number}`, `encounter` must be `Encounter/{uuid}`, `performer` is `Practitioner/{practitioner-ihs-number}`; the server should validate these reference targets exist.
- Store times in UTC+00 and reject dates before 2014-06-03 if we want SATUSEHAT parity.
- Implement the same five operations: search by `subject`/`encounter`/`based-on`, read, create (return a UUID `id`), PUT, and JSON-Patch limited to `replace`.
- `identifier.system` is ambiguous in the source (`/organization/` vs `/observation/`); accept both forms rather than hard-coding one.

## Sources
- raw/satusehat/res-observation.md
- raw/satusehat/api-observation.md
