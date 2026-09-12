# SATUSEHAT — Organization and Location

Ringkasan (summary): A faskes (organisasi induk, parent organisation) receives its `{organization-ihs-number}` from Kemenkes at registration, then POSTs its suborganisations (`Organization`, hierarchy via `partOf`) and its physical places (`Location`, hierarchy via `partOf`, owner via `managingOrganization`). Both APIs expose the standard search / read / create / update / patch operations.

Both profile pages: `*` = wajib (mandatory); other elements depend on the use-case Panduan Interoperabilitas. Neither page states numeric cardinalities (`n/s`).

## Required / constrained elements

### Organization
| Element | Cardinality | SATUSEHAT rule | Value set / system |
|---|---|---|---|
| identifier[i] | n/s | Internal code/number of the suborganisation held by the parent; `use` IdentifierUse (`official`); `value` = internal code (example `Pos Imunisasi LUBUK BATANG`) | `http://sys-ids.kemkes.go.id/organization/{organization-ihs-number}` |
| active | n/s | `boolean` | — |
| type[i] | n/s | `CodeableConcept`; example `dept` "Hospital Department" | `http://terminology.hl7.org/CodeSystem/organization-type` |
| name | n/s | `string`; example `Pos Imunisasi` | — |
| alias[i] | n/s | `string` | — |
| telecom[i] | n/s | `ContactPoint` (`system`, `value`, `use`); may hold >1 (phone, email, url) | `http://hl7.org/fhir/contact-point-system`, `http://hl7.org/fhir/contact-point-use` |
| address[i] | n/s | `Address`: `use`, `type`, `line[]`, `city`, `postalCode`, `country` (ISO 2-letter `ID`), `extension` administrativeCode (`province`, `city`, `district`, `village`) | `http://hl7.org/fhir/address-use`, `http://hl7.org/fhir/address-type`, `https://fhir.kemkes.go.id/r4/StructureDefinition/administrativeCode` |
| partOf | n/s — **WAJIB when the organisation is a suborganisation** | Reference `Organization`. Tahap 1 (stage 1): `Organization/{organization-ihs-number}` (parent IHS from Master Sarana Indeks); Tahap 2: `Organization/{id-suborganisasi}` (UUID returned by the server) | — |
| contact[i] | n/s | `BackboneElement`: `purpose`, `name` (`use`, `text`), `telecom[i]`, `address` | — |
| **\*contact.purpose.coding** | n/s (wajib within contact.purpose) | `Coding`; example `BILL` "Billing" | `http://terminology.hl7.org/CodeSystem/contactentity-type`; name.use: `http://hl7.org/fhir/name-use` |
| endpoint[i] | n/s | Reference to Endpoint | `https://fhir.kemkes.go.id/r4/StructureDefinition/Endpoint` |

### Location
| Element | Cardinality | SATUSEHAT rule | Value set / system |
|---|---|---|---|
| identifier[i] | n/s | Internal code of the sub-location; `use` IdentifierUse; `value` e.g. `G-2-R-1A` | `http://sys-ids.kemkes.go.id/location/{organization-ihs-number}` |
| status | n/s | `code`; example `active` | `http://hl7.org/fhir/location-status` |
| operationalStatus | n/s | `Coding`, mainly for beds/rooms; example `O` "Occupied" | `http://terminology.hl7.org/CodeSystem/v2-0116` |
| name | n/s | `string`; example `Ruang 1A IRJT` | — |
| alias[i] / description | n/s | `string` | — |
| mode | n/s | `code`; `instance` (specific place) vs kind (class of place) | `http://hl7.org/fhir/location-mode` |
| type[i] | n/s | `CodeableConcept`; example `ICU` | `http://terminology.hl7.org/CodeSystem/v3-RoleCode` |
| telecom[i] | n/s | `ContactPoint` (`system`, `value`, `use`) | `http://hl7.org/fhir/contact-point-system`, `http://hl7.org/fhir/contact-point-use` |
| address | n/s | `Address`: `use`, `line`, `city`, `postalCode`, `country`, `extension` administrativeCode (`province`, `city`, `district`, `village`, `rt`, `rw`) | `http://hl7.org/fhir/address-use`, `https://fhir.kemkes.go.id/r4/StructureDefinition/administrativeCode` |
| physicalType.coding | n/s | `Coding`; example `ro` "Room" | `http://terminology.hl7.org/CodeSystem/location-physical-type` |
| position | n/s | `BackboneElement` | — |
| **\*position.longitude**, **\*position.latitude** | n/s (wajib within position) | `decimal`; `altitude` optional. Example: longitude `-6.23115426275766`, latitude `106.83239885393944` (values look swapped for Jakarta; recorded as printed) | — |
| managingOrganization | n/s | Reference `Organization`: Tahap 1 `Organization/{organization-ihs-number}`, Tahap 2 `Organization/{id-suborganisasi}` | — |
| partOf | n/s | Reference `Location/{id-resource-Location}` (server-issued UUID of the parent location) | — |
| hoursOfOperation[i] | n/s | `daysOfWeek[]` (`code`), `allDay` (`boolean`), `openingTime`/`closingTime` (`time`) | `http://hl7.org/fhir/days-of-week` |
| availabilityExceptions | n/s | `string`; example `Libur Nasional` | — |
| endpoint[i] | n/s | Reference to Endpoint | `https://fhir.kemkes.go.id/r4/StructureDefinition/Endpoint` |
| **\*extension.serviceClass** | n/s (wajib) | `CodeableConcept` for ward class: Kelas 1, 2, 3, VIP, VVIP (anything above VVIP is sent as VVIP) | extension LocationServiceClass (Simplifier page; URL not printed on the raw page) |

## Identifier systems used
| Purpose | system URI |
|---|---|
| Organization.identifier (suborganisation internal code) | `http://sys-ids.kemkes.go.id/organization/{organization-ihs-number}` |
| Location.identifier (location internal code) | `http://sys-ids.kemkes.go.id/location/{organization-ihs-number}` |
| Location search token | `http://sys-ids.kemkes.go.id/location/<id-lokasi-induk>\|<nomor-identifikasi-lokasi>` |
| Address administrative codes | `https://fhir.kemkes.go.id/r4/StructureDefinition/administrativeCode` |

Worked example on both pages: RSUD Jati Asih has IHS `100000004` but the JSON references `Organization/10000004` (one digit fewer) — an inconsistency in the source.

## REST operations (from Katalog API)
Base (staging): `https://api-satusehat-stg.dto.kemkes.go.id/fhir-r4/v1`; `*Authorization: Bearer <access_token>`; `*Content-Type: application/json` on detail/write.

| Method | Path | Notes |
|---|---|---|
| GET | `/Organization?name=<partial-or-full>` | Search by organisation name (`?name` wajib in this mode) |
| GET | `/Organization?partof=<parent-id>` | Search suborganisations of a parent (example `10000004`) |
| GET | `/Organization/:id` | Detail; `:id` `uuid` (example `38d2fd4d-1402-4e5f-8f09-618fca5ce313`) |
| POST / PUT / PATCH | `/Organization`, `/Organization/:id` | Create (store returned `id`), full update, JSON-Patch `replace` only |
| GET | `/Location?identifier=http://sys-ids.kemkes.go.id/location/<id-lokasi-induk>\|<nomor>` | Search by location identifier token (example `.../location/1000001\|G-2-R-1A`) |
| GET | `/Location?name=<partial-or-full>` | Search by location name |
| GET | `/Location?organization=<uuid>` | Search locations of an organisation |
| GET | `/Location/:id` | Detail; `:id` `uuid` (example `3362d984-af65-43ac-8e5c-7db2b3be3f8b`) |
| POST / PUT / PATCH | `/Location`, `/Location/:id` | Create, full update, JSON-Patch `replace` only |

Responses: `Bundle` `searchset`; `4xx` `OperationOutcome`; `5xx` `text/plain`.

## Minimal example (JSON skeleton)
```json
{
  "resourceType": "Organization",
  "identifier": [ { "use": "official", "system": "http://sys-ids.kemkes.go.id/organization/1000079374", "value": "Pos Imunisasi LUBUK BATANG" } ],
  "active": true,
  "type": [ { "coding": [ { "system": "http://terminology.hl7.org/CodeSystem/organization-type", "code": "dept", "display": "Hospital Department" } ] } ],
  "name": "Pos Imunisasi",
  "partOf": { "reference": "Organization/10000004" }
}
```
```json
{
  "resourceType": "Location",
  "identifier": [ { "use": "official", "system": "http://sys-ids.kemkes.go.id/location/1000001", "value": "G-2-R-1A" } ],
  "status": "active",
  "name": "Ruang 1A IRJT",
  "mode": "instance",
  "physicalType": { "coding": [ { "system": "http://terminology.hl7.org/CodeSystem/location-physical-type", "code": "ro", "display": "Room" } ] },
  "managingOrganization": { "reference": "Organization/10000004", "display": "RSUD Jati Asih" },
  "partOf": { "reference": "Location/4adccec5-776d-435e-9ac5-98763cb216bb" }
}
```

## Notes for our server
- Our single faskes is the organisasi induk; the admin role creates the `Organization` root and suborganisations. Enforce `partOf` on every Organization that is not the root (the page says WAJIB for suborganisations).
- Enforce `Location.extension.serviceClass` (wajib) if we model wards; for a vital-sign/outpatient-only server this can be relaxed but must be flagged.
- If `Location.position` is present, require both `longitude` and `latitude`.
- If `Organization.contact[i].purpose` is present, require `purpose.coding`.
- Identifier systems are per-parent: `http://sys-ids.kemkes.go.id/organization/{ihs}` and `http://sys-ids.kemkes.go.id/location/{ihs}`; the server should accept the token search `identifier=<system>|<value>` on Location.
- Support search params: Organization `name`, `partof`; Location `identifier`, `name`, `organization`. Plus read / POST / PUT / PATCH-replace on both.
- Two-stage `partOf`/`managingOrganization` references (IHS number first, then server UUID) mean references may point at either an IHS-style id or a UUID; resolve both.

## Sources
- raw/satusehat/res-organization.md
- raw/satusehat/res-location.md
- raw/satusehat/api-organization.md
- raw/satusehat/api-location.md
