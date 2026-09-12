# SATUSEHAT — Practitioner (and PractitionerRole)

Ringkasan (summary): `Practitioner` is a nakes (tenaga kesehatan, health worker) record keyed by `{practitioner-ihs-number}` from the Master Nakes Index (MNI); faskes only **read** it (GET search / GET by id) and reference `Practitioner/{practitioner-ihs-number}` elsewhere. `PractitionerRole` has **no SATUSEHAT profile page** in the raw set — only a Katalog API page (search / read / create / update / patch), so its element rules are not documented here.

## Required / constrained elements
The Practitioner profile page marks only `qualification.code` (and its `coding`) with `*`; no cardinalities are given (`n/s` = not stated). PractitionerRole: no profile page, so no element table.

| Element | Cardinality | SATUSEHAT rule | Value set / system |
|---|---|---|---|
| identifier[i] | n/s | `Identifier` list for the nakes' identities | NIK: `https://fhir.kemkes.go.id/id/nik` (from the search API) |
| active | n/s | `boolean` | — |
| name[i] | n/s | `HumanName` | — |
| telecom[i] | n/s | `ContactPoint` (phone, email) | — |
| address[i] | n/s | `Address`: `use` (`code`), `type` (`code`), `text`, `line[i]`, `city`, `district`, `state`, `postalCode`, `country` (ISO 2-letter, `ID`), `period` | — (no value sets named) |
| gender | n/s | `code` | — (page names no value set; search API accepts `male`/`female`) |
| birthDate | n/s | `date` | — |
| photo[i] | n/s | `Attachment` | — |
| qualification[i] | n/s | `BackboneElement`: `identifier[i]`, `period`, `issuer` (Reference `Organization`) | — |
| **\*qualification.code** | n/s (wajib within qualification) | `CodeableConcept`; **\*qualification.code.coding** also wajib | — (no system named) |
| communication[i] | n/s | `CodeableConcept` with `coding` (languages the nakes can use) | — (no system named) |

## Identifier systems used
| Purpose | system URI |
|---|---|
| NIK of the practitioner (search token `identifier=<system>\|<nik>`) | `https://fhir.kemkes.go.id/id/nik` |
| IHS number (`Practitioner.id`, e.g. `N10000001` in API examples, `10009880728` in the sandbox table) | not stated as a system URI on either page |

Sandbox dummy practitioners (staging only) — NIK, name, gender, birthDate, IHS: `7209061211900001` dr. Alexander, male, 1994-01-01, `10009880728`; `3322071302900002` dr. Yoga Yandika, Sp.A, male, 1995-02-02, `10006926841`; `3171071609900003` dr. Syarifuddin, Sp.Pd., male, 1988-03-03, `10001354453`; `3207192310600004` dr. Nicholas Evan, Sp.B., male, 1986-04-04, `10010910332`; `6408130207800005` dr. Dito Arifin, Sp.M., male, 1985-05-05, `10018180913`; `3217040109800006` dr. Olivia Kirana, Sp.OG, female, 1984-06-06, `10002074224`; `3519111703800007` dr. Alicia Chrissy, Sp.N., female, 1982-07-07, `10012572188`; `5271002009700008` dr. Nathalie Tan, Sp.PK., female, 1981-08-08, `10018452434`; `3313096403900009` Sheila Annisa S.Kep, female, 1980-09-09, `10014058550`; `3578083008700010` apt. Aditya Pradhana, S.Farm., female, 1980-10-10, `10001915884`.

## REST operations (from Katalog API)
Base (staging): `https://api-satusehat-stg.dto.kemkes.go.id/fhir-r4/v1`. `*Authorization: Bearer <access_token>` on all; `*Content-Type: application/json` on detail and write calls.

### Practitioner (read-only for faskes)
| Method | Path | Notes |
|---|---|---|
| GET | `/Practitioner?identifier=https://fhir.kemkes.go.id/id/nik\|<nik>` | Mode 1: by NIK (`?identifier` wajib in this mode) |
| GET | `/Practitioner?name=<name>&birthdate=<YYYY[-MM[-DD]]>&gender=male\|female` | Mode 2: all three wajib; name spelling validated against SATUSEHAT data |
| GET | `/Practitioner/:id` | Detail (page writes URL as `Practitioner:id`, a typo; cURL uses `/Practitioner/N10000001`); `:id` listed as `uuid` |

No POST / PUT / PATCH is documented for Practitioner.

### PractitionerRole
| Method | Path | Notes |
|---|---|---|
| GET | `/PractitionerRole?practitioner=<practitioner-id>` | Mode 1: by Practitioner ID (example `N10000001`) |
| GET | `/PractitionerRole?practitioner=<id>&organization=<id>` | Mode 2: both `?practitioner` and `?organization` wajib. The raw page describes `?organization` as "ID dari ServiceRequest" — a copy-paste error; the heading says Organization |
| GET | `/PractitionerRole/:id` | Detail; `:id` is `uuid` (example `7a44b421-677e-45a1-b7c0-5249264a3189`) |
| POST | `/PractitionerRole` | Create; store the returned `id` |
| PUT | `/PractitionerRole/:id` | Full update |
| PATCH | `/PractitionerRole/:id` | JSON Patch, only `op: "replace"`, path like `/language` |

Responses: `Bundle` `searchset` for search; `4xx` = `OperationOutcome`; `5xx` = `text/plain`.

## Minimal example (JSON skeleton)
The profile page gives no JSON examples; only the API response shape is shown.

```json
{
  "resourceType": "Practitioner",
  "id": "N10000001",
  "identifier": [ { "system": "https://fhir.kemkes.go.id/id/nik", "value": "################" } ],
  "active": true,
  "name": [ { "text": "dr. Alexander" } ],
  "gender": "male",
  "birthDate": "1994-01-01",
  "qualification": [ { "code": { "coding": [ { "code": "..." } ] } } ]
}
```

## Notes for our server
- Practitioner in SATUSEHAT is master data the faskes cannot create; our server (no MNI) must instead own practitioner creation (admin role) and mint the `Practitioner.id` used in `Observation.performer` / `Encounter.participant`.
- Enforce: every `qualification[i]` must carry `code` with at least one `coding` (the only `*` elements on the profile page).
- Support search by `identifier` token (`https://fhir.kemkes.go.id/id/nik|<nik>`) and by `name`+`birthdate`+`gender`; support read by id.
- PractitionerRole: expose the same five operations as the API page (search by `practitioner`, `practitioner`+`organization`, read, POST, PUT, PATCH-replace). Element-level validation cannot be derived from the raw set because no profile page exists; fall back to FHIR R4 base rules.
- Doctor-role accounts in our design map to a Practitioner (identity) plus a PractitionerRole (link to our Organization); Practitioner `gender` values seen in SATUSEHAT search are `male`/`female` only.

## Sources
- raw/satusehat/res-practitioner.md
- raw/satusehat/api-practitioner.md
- raw/satusehat/api-practitioner-role.md
