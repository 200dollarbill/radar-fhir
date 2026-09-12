# SATUSEHAT — Patient

Ringkasan (summary): `Patient` in SATUSEHAT is keyed by the `{patient-ihs-number}` issued by the Master Patient Index (MPI); a faskes (health facility) looks it up (GET) or creates it (POST) and then references `Patient/{patient-ihs-number}` in every other resource. Search modes are NIK-based, name+birthdate+NIK, name+birthdate+gender, and newborn-by-mother's-NIK.

General rules from the profile page: `*` = wajib (mandatory); times in UTC+00; dates not earlier than 03 June 2014; whether other elements are wajib depends on the use-case Panduan Interoperabilitas.

## Required / constrained elements
Cardinality: the profile page only marks `*`; `n/s` = not stated.

| Element | Cardinality | SATUSEHAT rule | Value set / system |
|---|---|---|---|
| **\*identifier[i]** | n/s (wajib) | `Identifier` list of patient codes/numbers; `use` = IdentifierUse (`official` in examples); `value` = the number | system per purpose (see next table); `use`: `http://hl7.org/fhir/identifier-use` |
| active | n/s | `boolean` | — |
| **\*name[i]** | n/s (wajib) | `HumanName`: `use` (`code`), `text` (full name), `family`, `given`, `prefix`, `suffix`, `period` | — |
| telecom[i] | n/s | `ContactPoint`; examples `phone`/`mobile`, `phone`/`home`, `email`/`home` | — |
| gender | n/s | `code`; example `"female"` | `http://hl7.org/fhir/administrative-gender` |
| birthDate | n/s | `date`, format `YYYY-MM-DD` | — |
| deceased[x] | n/s | `deceasedBoolean` (`boolean`) or `deceasedDateTime` (`dateTime`, `YYYY`/`YYYY-MM`/`YYYY-MM-DD`/`YYYY-MM-DDThh:mm:ss+zz:zz`) | — |
| address[i] | n/s | `Address`: `use` (AddressUse), `line[]`, `city`, `postalCode`, `country` (ISO 2-letter, `ID`), `extension` AdministrativeCode | `use`: `http://hl7.org/fhir/address-use` |
| address.extension[i] | n/s | Extension `administrativeCode` with sub-extensions `province`, `city`, `district`, `village`, `rt`, `rw` (each `valueCode`) | `https://fhir.kemkes.go.id/r4/StructureDefinition/administrativeCode` |
| maritalStatus | n/s | `CodeableConcept`; example `M` "Married" | value set `http://hl7.org/fhir/ValueSet/marital-status`; example system `http://terminology.hl7.org/CodeSystem/v3-MaritalStatus` |
| **\*multipleBirth[x]** | n/s (wajib) | `multipleBirthBoolean` (`boolean`) or `multipleBirthInteger` (`integer`) | — |
| photo[i] | n/s | `Attachment` | — |
| contact[i] | n/s | `BackboneElement` (penjamin / guarantor): `relationship[i]`, `name` (`use`, `text`), `telecom[i]` (`system`, `value`, `use`), `address`, `gender`, `organization` (Reference), `period` | relationship: value set `http://hl7.org/fhir/ValueSet/patient-contactrelationship`, example system `http://terminology.hl7.org/CodeSystem/v2-0131` code `C`; telecom system `http://hl7.org/fhir/contact-point-system`, use `http://hl7.org/fhir/contact-point-use` |
| communication[i] | n/s | `BackboneElement` | — |
| **\*communication.language** | n/s (wajib within communication) | `CodeableConcept`; example `id-ID` "Indonesian" | `urn:ietf:bcp:47` (value set `http://hl7.org/fhir/ValueSet/languages`) |
| communication.preferred | n/s | `boolean` | — |
| generalPractitioner[i] | n/s | Reference `Organization \| Practitioner \| PractitionerRole` | — |
| managingOrganization | n/s | Reference `Organization` | — |
| link[i] | n/s | `BackboneElement` | — |
| **\*link.other** | n/s (wajib within link) | Reference `Patient`; example `Patient/P02478375538` (API examples also show `RelatedPerson/{uuid}` with type `refer`) | — |
| **\*link.type** | n/s (wajib within link) | `code` | — (page names no value set) |
| extension:birthPlace | n/s | Extension with `valueAddress` (`city`, `country`) | `https://fhir.kemkes.go.id/r4/StructureDefinition/birthPlace` |
| extension citizenshipStatus | n/s | Extension with `valueCode`, example `WNI` (shown only in the JSON example, no heading of its own) | `https://fhir.kemkes.go.id/r4/StructureDefinition/citizenshipStatus` |
| meta.profile (from API responses) | n/s | `https://fhir.kemkes.go.id/r4/StructureDefinition/Patient` | — |

MPI minimum data for a new patient **with NIK** (`mpi-pasien-nik`, Tabel 1): `*identifier` (NIK), `*name`, `*birthDate` (`YYYY-MM-DD`), `*gender` (`male`/`female`), `*address`, `*address-extension` (province/city/district/village/rt/rw, Kemendagri codes); optional `birthPlace`, Nomor Kartu Keluarga, `telecom`, `maritalStatus` (`S`/`M`/`W`/`D`), `citizenshipStatus` (`WNI`/`WNA`), `communication-language` (BCP 47: `en`, `id-ID`, `zh-CN`). Every record must be unique (TIDAK BOLEH duplicated). Create is verified against DUKCAPIL; a mismatch returns an error.

## Identifier systems used
| Purpose | system URI |
|---|---|
| IHS number (nomor IHS, the `Patient.id` / `{patient-ihs-number}`) | `https://fhir.kemkes.go.id/id/ihs-number` |
| NIK (Nomor Induk Kependudukan) | `https://fhir.kemkes.go.id/id/nik` |
| Mother's NIK for newborns (NIK ibu) | `https://fhir.kemkes.go.id/id/nik-ibu` |
| Passport (paspor) | `https://fhir.kemkes.go.id/id/paspor` |
| Kartu Keluarga (family card) | `https://fhir.kemkes.go.id/id/kk` |
| Stated in the profile text as the generic `identifier.system` format (literal, not an example) | `https://fhir.kemkes.go.id/id/patient-ihs-number` |

The profile text gives `https://fhir.kemkes.go.id/id/patient-ihs-number` as the identifier system, but every API example uses `https://fhir.kemkes.go.id/id/ihs-number`. Both are recorded verbatim.

Sandbox dummy patients (staging only) — NIK, name, gender, birthDate, IHS: `9271060312000001` Ardianto Putra, male, 1992-01-09, `P02478375538`; `9204014804000002` Claudia Sintia, female, 1989-11-03, `P03647103112`; `9104224509000003` Elizabeth Dior, female, 1976-07-07, `P00805884304`; `9104223107000004` Dr. Alan Bagus Prasetya, male, 1977-09-03, `P00912894463`; `9104224606000005` Ghina Assyifa, female, 2004-08-21, `P01654557057`; `9104025209000006` Salsabilla Anjani Rizki, female, 2001-04-16, `P02280547535`; `9201076001000007` Theodore Elisjah, female, 1985-09-18, `P01836748436`; `9201394901000008` Sonia Herdianti, female, 1996-06-08, `P00883356749`; `9201076407000009` Nancy Wang, female, 1955-10-10, `P01058967035`; `9210060207000010` Syarif Muhammad, male, 1988-11-02, `P02428473601`.

## REST operations (from Katalog API)
Base (staging): `https://api-satusehat-stg.dto.kemkes.go.id/fhir-r4/v1`. Header `*Authorization: Bearer <access_token>` on all; `*Content-Type: application/json` on detail/POST/PATCH. There is **no PUT** section on the Patient API page.

| Method | Path | Notes |
|---|---|---|
| GET | `/Patient?identifier=https://fhir.kemkes.go.id/id/nik\|<nik>` | Mode 1: search by NIK (`?identifier` wajib in this mode) |
| GET | `/Patient?name=<name>&birthdate=<YYYY[-MM[-DD]]>&nik=<nik>` | Mode 2: name + birthdate + NIK; name spelling is validated against SATUSEHAT data |
| GET | `/Patient?identifier=https://fhir.kemkes.go.id/id/nik-ibu\|<nik-ibu>` | Mode 3: newborn (bayi baru lahir) by mother's NIK; returns all children linked to that NIK |
| GET | `/Patient?name=<name>&birthdate=<date>&gender=male\|female` | Mode 4: name + birthdate + gender |
| GET | `/Patient/:id` | Detail by IHS number (page writes the URL as `Patient:id`, a typo; cURL uses `/Patient/100000000001`). `:id` type listed as `uuid` although IHS numbers look like `P02478375538` |
| POST | `/Patient` | Create with `identifier` NIK **or** `identifier` NIK ibu (newborn); response `id` must be stored (page writes URL as `Patient:` — typo) |
| PATCH | `/Patient/:id` | JSON Patch array; only `op: "replace"`; `path` like `/language` |

Search responses are `Bundle` type `searchset` with `entry[].resource` (Patient), `link` (`search`/`first`/`self`), `total`. Search results carry `meta.profile` `https://fhir.kemkes.go.id/r4/StructureDefinition/Patient`. `4xx` returns `OperationOutcome`; `5xx` is `text/plain`.

Search without NIK (`mpi-pasien-no-nik`): `*name` (similar-case match, at least 3 characters), `*birthDate` exact `YYYY-MM-DD`, `*gender` exact `male`/`female`; response exposes only the IHS number as identifier, address masked, `multipleBirthInteger` (0 if not a twin), `maritalStatus` `Married`/`unmarried`.

## Minimal example (JSON skeleton)
Assembled from the profile page examples plus the search response shape.

```json
{
  "resourceType": "Patient",
  "meta": { "profile": [ "https://fhir.kemkes.go.id/r4/StructureDefinition/Patient" ] },
  "identifier": [
    { "use": "official", "system": "https://fhir.kemkes.go.id/id/nik", "value": "################" }
  ],
  "active": true,
  "name": [ { "use": "official", "text": "John Smith" } ],
  "telecom": [ { "system": "phone", "value": "08123456789", "use": "mobile" } ],
  "gender": "female",
  "birthDate": "1945-11-17",
  "deceasedBoolean": false,
  "address": [
    {
      "use": "home",
      "line": [ "Gd. Prof. Dr. Sujudi Lt.5, Jl. H.R. Rasuna Said Blok X5 Kav. 4-9 Kuningan" ],
      "city": "Jakarta", "postalCode": "12950", "country": "ID",
      "extension": [ {
        "url": "https://fhir.kemkes.go.id/r4/StructureDefinition/administrativeCode",
        "extension": [
          { "url": "province", "valueCode": "10" }, { "url": "city", "valueCode": "1010" },
          { "url": "district", "valueCode": "1010101" }, { "url": "village", "valueCode": "1010101101" },
          { "url": "rt", "valueCode": "2" }, { "url": "rw", "valueCode": "2" }
        ] } ]
    }
  ],
  "maritalStatus": { "coding": [ { "system": "http://terminology.hl7.org/CodeSystem/v3-MaritalStatus", "code": "M", "display": "Married" } ] },
  "multipleBirthBoolean": false,
  "communication": [ { "language": { "coding": [ { "system": "urn:ietf:bcp:47", "code": "id-ID", "display": "Indonesian" } ] }, "preferred": true } ],
  "extension": [
    { "url": "https://fhir.kemkes.go.id/r4/StructureDefinition/birthPlace", "valueAddress": { "city": "Bandung", "country": "ID" } },
    { "url": "https://fhir.kemkes.go.id/r4/StructureDefinition/citizenshipStatus", "valueCode": "WNI" }
  ]
}
```

## Notes for our server
- Profile-level wajib: `identifier`, `name`, `multipleBirth[x]`; plus `communication.language` inside any `communication`, and `link.other` + `link.type` inside any `link`. Reject a Patient missing `identifier` or `name`; treat `multipleBirth[x]` as required for SATUSEHAT parity (relaxable locally).
- For patients created with NIK, MPI additionally requires `birthDate`, `gender`, `address` with the `administrativeCode` extension (province/city/district/village/rt/rw) — enforce these when the identifier system is `https://fhir.kemkes.go.id/id/nik`.
- Accept identifier systems `.../id/nik`, `.../id/nik-ibu`, `.../id/paspor`, `.../id/kk`, `.../id/ihs-number`; our server issues the `ihs-number` identifier (and `Patient.id`) itself since we have no MPI/DUKCAPIL.
- Enforce uniqueness of a patient per NIK (MPI: no duplicates).
- Implement the four search parameter combinations (`identifier` with `system|value` token syntax, `name`+`birthdate`+`nik`, `name`+`birthdate`+`gender`, `nik-ibu` token), read by id, POST, and PATCH-replace. Do not need PUT for SATUSEHAT parity.
- Name search: substring/similar-case with a 3-character minimum; birthdate and gender exact.
- `gender` values limited to `male`/`female` in MPI even though AdministrativeGender has more.

## Sources
- raw/satusehat/res-patient.md
- raw/satusehat/api-patient.md
- raw/satusehat/mpi-pasien-nik.md
- raw/satusehat/mpi-pasien-no-nik.md
