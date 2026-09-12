# SATUSEHAT — RelatedPerson

Ringkasan (summary): `RelatedPerson` records a person related to a patient (e.g. natural mother of a newborn), identified by NIK. Only `patient` and `communication.language` (+ its `coding`) are marked wajib. **There is no Katalog API page for RelatedPerson in the raw set**; the only API evidence is the Patient search response, where `Patient.link.other` points at `RelatedPerson/{uuid}` with `type: "refer"`.

The profile page opens with "Pengiriman data informasi orang terkait dapat dikirimkan menggunakan resource `Observation`" — an evident copy-paste error (the resource is RelatedPerson).

## Required / constrained elements
Cardinality `n/s` (not stated) unless printed.

| Element | Cardinality | SATUSEHAT rule | Value set / system |
|---|---|---|---|
| identifier[i] | n/s | `Identifier`; `use` IdentifierUse (`official`); `value` = NIK (`string`) | `https://fhir.kemkes.go.id/id/nik` (the only system format printed) |
| active | n/s | `boolean` | — |
| **\*patient** | n/s (wajib) | Reference `Patient`; example `Patient/P02029102701` | — |
| relationship[i] | n/s | `CodeableConcept`; example `NMTH` "natural mother" | `http://terminology.hl7.org/CodeSystem/v3-RoleCode` |
| name[i] | n/s | `HumanName`; example `use: official`, `text: Jane Smith` | — |
| telecom[i] | n/s | `ContactPoint`: `system`, `value`, `use`; examples phone/mobile, phone/home, email/home | `http://hl7.org/fhir/contact-point-system`, `http://hl7.org/fhir/contact-point-use` |
| gender | n/s | `code`; example `female` | — (page names no value set) |
| birthDate | n/s | `date`; example `2023-03-08` | — |
| address[i] | n/s | `Address`: `use`, `line[]`, `city`, `postalCode`, `country` (ISO 2-letter `ID`); no administrativeCode extension shown | `http://hl7.org/fhir/address-use` |
| photo[i] | n/s | `Attachment` | — |
| period | n/s | `Period` during which the relationship is active | — |
| communication[i] | n/s | `BackboneElement` | — |
| **\*communication.language** | n/s (wajib within communication) | `CodeableConcept`; ISO-639-1 lowercase, optionally `-` + ISO-3166-1 uppercase (`en`, `en-US`); **\*communication.language.coding** wajib; example `id-ID` | `urn:ietf:bcp:47` |
| communication.preferred | n/s | `boolean` | — |

## Identifier systems used
| Purpose | system URI |
|---|---|
| RelatedPerson.identifier (NIK) | `https://fhir.kemkes.go.id/id/nik` |
| RelatedPerson.identifier.use | `http://hl7.org/fhir/identifier-use` |

## REST operations (from Katalog API)
| Method | Path | Notes |
|---|---|---|
| — | — | No `api-related-person` page exists in the raw set; no endpoints can be stated. The Patient API shows `RelatedPerson/{uuid}` referenced from `Patient.link.other` (`type: refer`), implying RelatedPerson resources exist server-side with UUID ids. |

## Minimal example (JSON skeleton)
```json
{
  "resourceType": "RelatedPerson",
  "identifier": [ { "use": "official", "system": "https://fhir.kemkes.go.id/id/nik", "value": "################" } ],
  "active": true,
  "patient": { "reference": "Patient/P02029102701" },
  "relationship": [ { "coding": [ { "system": "http://terminology.hl7.org/CodeSystem/v3-RoleCode", "code": "NMTH", "display": "natural mother" } ] } ],
  "name": [ { "use": "official", "text": "Jane Smith" } ],
  "telecom": [ { "system": "phone", "value": "08123456789", "use": "mobile" } ],
  "gender": "female",
  "birthDate": "2023-03-08",
  "address": [ { "use": "home", "line": [ "Gd. Prof. Dr. Sujudi Lt.5, Jl. H.R. Rasuna Said Blok X5 Kav. 4-9 Kuningan" ], "city": "Jakarta", "postalCode": "12950", "country": "ID" } ],
  "communication": [ { "language": { "coding": [ { "system": "urn:ietf:bcp:47", "code": "id-ID", "display": "Indonesian" } ] }, "preferred": true } ]
}
```

## Notes for our server
- Reject a RelatedPerson without `patient`; if `communication[i]` is present, require `language.coding`.
- `patient` must resolve to an existing Patient; `identifier.system` for NIK is `https://fhir.kemkes.go.id/id/nik` (same system as Patient NIK).
- `relationship` codes come from `http://terminology.hl7.org/CodeSystem/v3-RoleCode` (e.g. `NMTH`).
- Because no SATUSEHAT endpoint list exists, expose plain FHIR R4 CRUD locally and mirror the Patient link: when a RelatedPerson is created, the server may add `Patient.link` `{ other: RelatedPerson/{id}, type: refer }` as seen in the Patient search examples.
- Useful for our patient role: a guardian/parent account may be modelled as a RelatedPerson linked to the child Patient (newborn use case searches Patient by `nik-ibu`).

## Sources
- raw/satusehat/res-related-person.md
- raw/satusehat/api-patient.md
