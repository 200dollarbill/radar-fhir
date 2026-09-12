# SATUSEHAT — REST API basics and validation responses

Ringkasan (summary): The Katalog API (API catalogue) splits SATUSEHAT REST resources into an onboarding set (*prerequisites*: Patient, Practitioner, Organization, Location) and an interoperability set (clinical transactions). All calls go to one FHIR R4 base per environment with a Bearer token. Validation runs in a FHIR Processor before the FHIR Server; failures come back as `OperationOutcome` whose `details.text` carries a human message and, usually, a `RuleNumber`. The full Kamus Rule Number (rule-number dictionary) is an external spreadsheet not in the corpus; the rule numbers and messages below are the only ones the raw pages print.

## Base URLs and auth header
| Purpose | Sandbox | Production |
|---|---|---|
| FHIR resources (onboarding and integration) | `https://api-satusehat-stg.dto.kemkes.go.id/fhir-r4/v1` | `https://api-satusehat.kemkes.go.id/fhir-r4/v1` |
| OAuth2 token (from `mpi-rest-api`; the Katalog pages only link to "Akses Token") | `https://api-satusehat-stg.dto.kemkes.go.id/oauth2/v1` | `https://api-satusehat.kemkes.go.id/oauth2/v1` |

- Both Katalog pages say the API "mempunyai tiga endpoint" (three endpoints) but list only Sandbox and Production — recorded as written.
- Every request **WAJIB** (must) be authenticated first; header shape: `Authorization: Bearer <access_token>`, where `<access_token>` is the `access_token` property of the token response.
- Token flow (as described on `mpi-rest-api`, same gateway): `POST {oauth2}/accesstoken?grant_type=client_credentials`, `Content-Type: application/x-www-form-urlencoded`, body `client_id` + `client_secret`; response `token_type` `BearerToken`, `expires_in` `3599`.
- Write calls additionally send `Content-Type: application/json` (per-resource API pages).
- All examples in the playbook use the sandbox environment.

## Onboarding vs interoperability (`api-onboardings`, `api-integrations`)
| Phase | Resources | Statement |
|---|---|---|
| Orientasi / prerequisites (onboarding) | `Patient`, `Practitioner` (page spells "Practicioner"), `Organization`, `Location` | "resource yang harus tersedia datanya" — must exist before any data transaction |
| Interoperabilitas (data transaction) | all clinical resources | Split into use cases: *use case* dasar (Modul Pelayanan, service modules) and *use case* tematik (Modul Penerapan); which API each use case needs is documented in the Panduan Interoperabilitas, not in the Katalog |

## Validation pipeline (`api-validasi`)
1. Faskes calls the SATUSEHAT API.
2. API Gateway first checks the request with the FHIR *Processor*.
3. Any error → failure message returned (no write).
4. No error → request forwarded to the FHIR *Server*.
5. After the data is stored → success message.

Terminology codes validated: ICD-10, ICD-9 CM, LOINC, SNOMED-CT and other FHIR HL7 code systems listed under Terminologi.

### 4xx body structure (`OperationOutcome`)
```
{ *resourceType: "OperationOutcome",
  *issue: [{ *severity: string, *code: string, *details: { *text: string }, expression: [string] }] }
```
| Field | Values stated |
|---|---|
| `issue.severity` | `error` — an error found by the system (only value listed) |
| `issue.code` | `duplicate` — the same encounter sent repeatedly; `format` — wrong format; `value` — value not allowed / not matching |
| `issue.details.text` | human message, usually with `(RuleNumber: NNNNN)` |
| `issue.expression` | resource path(s) of the offending field, e.g. `Encounter.serviceProvider` |

Examples on `api-list-response` also carry `"text": { "status": "generated" }` at the top level.

## Kamus validasi (validation dictionary) — rule → message
Only what the raw pages print. Message strings are verbatim; `xxx`/`Satu` are the playbook's placeholders.

| RuleNumber | `issue.code` | `details.text` (verbatim) | Example `expression` | Rule stated on the page |
|---|---|---|---|---|
| — | `duplicate` | `Found duplicate resource: Encounter` | — | A payload request **TIDAK BOLEH** (must not) be sent more than once |
| 10001 | `value` | `Code not found: 'xxx' in system: http://terminology.hl7.org/CodeSystem/v3-ActCode (RuleNumber: 10001)` | `Encounter.class.code` | Codes must come from the SATUSEHAT / FHIR HL7 code systems listed under Terminologi |
| 10002 | `value` | `Invalid coding system: http://xxx.org (RuleNumber: 10002)` | `Encounter.participant[0].type[0].coding[0].system` | The `system` used is not allowed for that element |
| 10117 | `value` | `Invalid identifier system: http://xxx.org (RuleNumber: 10117)` | `Encounter.identifier[0].system` | `Identifier.system` must be a valid SATUSEHAT system (see Panduan Interoperabilitas / Terminologi) |
| 10124 | `value` | `Reference is mandatory : Encounter.serviceProvider (RuleNumber: 10124)` | `Encounter.serviceProvider` | A **VALID** resource reference is required on the element |
| 10132 | `format` | `Invalid date time format : 2022-06-14 (RuleNumber: 10132). Format allowed : YYYY-MM-DDThh:mm:ss+00:00` | `Composition.date` | Date-times must be `YYYY-MM-DDThh:mm:ss+00:00` |
| 10132 | `value` | `Invalid date time value : 2021-06-02T12:28:03Z (RuleNumber: 10132) Not Allowed : Future Date or Past Date older than 31st August 2022` | `Composition.date` | No future dates; no past dates older than a cut-off (this page: 31 August 2022) |
| 10134 | `value` | `Text is empty: '' (RuleNumber: 10134)` | `Composition.title` | Elements **TIDAK BOLEH** be an empty string |
| 10171 | `value` | `Use /operationalStatus instead of /operationalStatus/system to patch Location (RuleNumber: 10171)` | `Location.operationalStatus` | PATCH on `Location` must follow the latest public Postman collection |
| 10254 | `value` | `Integer formated as a string: 'Satu' (RuleNumber: 10254)` | `Claim.supportingInfo[0].sequence` | Integer values must be unquoted integers |
| 10263 | `value` | `Element not found: Claim.insurance[0].focal (RuleNumber: 10263)` | `Claim.insurance[0].focal` | A `*`-marked (wajib) element is missing; which elements are `*` depends on the Panduan Interoperabilitas of the Modul Pelayanan / Use Case |

Notes on the table:
- The same RuleNumber `10132` is printed for both the format error (`issue.code: format`) and the value error (`issue.code: value`).
- The rule-number dictionary itself is a Google-Sheets download linked from `api-kamus-validasi`; it is **not** in the corpus, so no other rule numbers can be stated.

### Time-zone rule (stated on the date-format error)
- Standard time format for sending data is **UTC +00**: WIB → subtract 7 h, WITA → 8 h, WIT → 9 h. Example: 17.35 WIB on 23 August 2023 is sent as `2023-08-23T10:35:00+00:00`.
- Purpose: so the value is not detected as a future date. Exceptions allowed for genuinely future periods: appointments, drug expiry, insurance membership validity, "dan lainnya".

### Contradiction on the earliest allowed date (record, do not resolve)
| Raw file | Statement |
|---|---|
| `api-list-response.md` | "Not Allowed : Future Date or Past Date older than 31st August 2022" |
| `res-observation.md` (see satusehat-observation.md) | dates sent must not be earlier than **03 June 2014** |

## Response conventions common to every API page (from the per-resource pages, e.g. `mpi-rest-api`)
| Status | Content-Type | Body |
|---|---|---|
| 2xx | `application/json` | the resource (create returns `id` to be stored) or a `Bundle` `searchset` |
| 4xx | `application/json` | `OperationOutcome` as above |
| 5xx | `text/plain` | e.g. `Gateway Timeout` |

## Notes for our server
- Serve everything under one base path shaped like `/fhir-r4/v1`; require `Authorization: Bearer <token>` on every request and reply 401 with an `OperationOutcome` (`severity: error`, `code: value`, `details.text` like the playbook's authentication message) when missing.
- Emit validation failures as `OperationOutcome` with `issue[].severity = error`, `issue[].code ∈ {duplicate, format, value}`, `details.text` including `(RuleNumber: N)` and `expression` = FHIRPath-style element path; reuse the playbook rule numbers where our rule matches (10001 code not found, 10002 invalid coding system, 10117 invalid identifier system, 10124 mandatory reference, 10132 date-time, 10134 empty text, 10254 integer as string, 10263 element not found), and choose distinct numbers for our own rules.
- Validate before persisting (processor-then-server), so a failed request writes nothing.
- Store and compare instants in UTC; reject dateTimes without a zone; reject future dates except on period-type elements; decide one lower bound (the corpus gives two) and document it.
- Onboarding order for seed data: Organization → Location → Practitioner → Patient before any Encounter.
- Reject duplicate Encounter submissions (same identifier) with `issue.code = duplicate`.

## Sources
- raw/satusehat/api-onboardings.md
- raw/satusehat/api-integrations.md
- raw/satusehat/api-validasi.md
- raw/satusehat/api-kamus-validasi.md
- raw/satusehat/api-list-response.md
- raw/satusehat/mpi-rest-api.md
