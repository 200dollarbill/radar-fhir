# SATUSEHAT-Compatible FHIR R4 Server — Walking Skeleton Design

**Date:** 2026-09-29
**Status:** Design decisions approved through brainstorming; written spec pending user review
**Sub-project:** 2 of the PRATA server brief (see `CLAUDE.md`)

## Goal

A standalone, local-only FHIR R4 server that proves the brief's core flow end to end:
an administrator provisions a flat facility plus accounts, a doctor opens an Encounter,
a device submits heart-rate Observations into it, the participating doctor reads them,
and the patient reads their own record — all under the three-role model
(administrator / doctor / patient), SATUSEHAT-shaped where the corpus binds us and
base R4 where it does not. Never calls the hosted platform.

## Decisions taken in brainstorming (with rationale)

| # | Decision | Rationale |
|---|---|---|
| D1 | Decompose sub-project 2; first spec = **walking skeleton** (FHIR REST core + minimal auth + just enough resources for device→doctor→patient) | Multiple independent subsystems; brainstorming scope-check rule |
| D2 | Stack: **Python 3.12, FastAPI, SQLite** | Matches repo pytest tooling; `python_receiver` precedent; SQLite enough for local-only |
| D3 | Human auth: **local JWT with role claims** (admin / doctor / patient) | Fully local, no IdP; SMART/OAuth subset deferred |
| D4 | **Minimal web UI is a later sub-project**; skeleton is API-only | Brief puts the monitoring dashboard out of scope; keeps slice thin |
| D5 | First flow: **device-to-patient** (all three roles in one slice) | Proves the clinical focus in one thin path |
| D6 | Device ingest: **device POSTs FHIR directly** with a **provisioned opaque bearer token** (hashed at rest, standard FHIR route, no anonymous ingest) | User first chose direct POST, then chose token over the no-credential exception after the auth conflict was surfaced |
| D7 | Validation: **fhir.resources (pydantic v2) parses every payload in the request path** for base-R4 structure; hand-written SATUSEHAT rules layer on top, behind a `Validator` interface | User chose in-prod engine; interface keeps profile-driven validation swappable later |
| D8 | Vital sign scope: **heart rate only** (LOINC `8867-4`, UCUM `/min`) | What the radar device can genuinely measure; smallest terminology seed (BP/SpO₂ later) |
| D9 | **Doctor opens the visit**; device posts into it; doctor finishes it | Clinical control stays with the clinician; exercises statusHistory lifecycle |
| D10 | Doctor access = **participant on one of the patient's Encounters** | Derives from resources already in the slice; no extra tables |
| D11 | Admin scope: **flat single Organization + Location**, practitioner accounts, patient accounts, device-token provisioning; one bootstrap admin | Proves the admin role without hierarchy (partOf tree, beds, serviceClass later) |
| D12 | Encounter wajib set: **lifecycle-aware subset** (see Validation) | Full SATUSEHAT Encounter set is unsatisfiable at create time |
| D13 | Patient creation: **NIK required** + S12 MPI union (name, birthDate, gender, address with administrativeCode); server mints ihs-number | SATUSEHAT MPI parity from day one; NIK validated locally, no MPI call |
| D14 | Id minting: **IHS-shaped per type** — Patient `P`+11 digits, Practitioner `N`+8 digits, Organization 9–11 digits, Location/Device/Encounter/Observation UUID v4 | Matches every playbook example |
| D15 | Doctor review = **read-only** (search/read); no stored acknowledgment | Acknowledgment/worklist is a later sub-project |
| D16 | **Firmware HTTP POST included**: radar sketch gains placeholder-HR WiFi ingest; verified by `arduino-cli compile` only (existing README rule: no upload) | User chose "firmware included"; same verify-without-hardware pattern as the dummy-receiver spec |

## Scope

### Included

- Package `fhir_server/` with a FHIR REST surface under `/fhir-r4/v1`.
- Resources: `Organization`, `Location`, `Practitioner`, `Patient`, `Device`,
  `Encounter`, `Observation` (heart rate), plus `CapabilityStatement` on `GET /metadata`.
- Interactions: `POST` (create), `GET` by id, `PUT` (full update), `DELETE`,
  `GET` search with a fixed per-resource parameter set (listed below).
- Auth: `POST /auth/token` (username/password → JWT, 1 h expiry); `Authorization: Bearer`
  on every route except `POST /auth/token` and `GET /metadata` (public capability
  discovery, per R4); device token accepted on the same FHIR routes with device scope.
- Authorization: admin full; doctor write/read limited by encounter-participant rule;
  patient read-only on own Patient, own Encounters, and Observations with own `subject`.
- Bootstrap: `python3 -m fhir_server.cli seed --reset` creates one admin account,
  one organization, one location, a demo doctor/patient/device set, and prints an
  initial admin password if none configured.
- Validation pipeline: parse (fhir.resources) → structural → SATUSEHAT rules →
  reference existence checks → persist. Failures never write (processor-then-server).
- `OperationOutcome` errors carrying RuleNumbers and FHIRPath `expression`.
- UTC date policy, identifier-system checks, duplicate-Encounter rejection (S4 ruling).
- Radar firmware extension: WiFi + provisioned token + placeholder heart-rate
  Observation POST at ~1 Hz; `arduino-cli compile` gate.
- Python device-client test double speaking the identical wire contract.

### Excluded (each named as a later sub-project or out of brief)

- Web UI (D4; later sub-project), encounter-participant management flows (participants
  are added implicitly when a doctor opens a visit), PractitionerRole resource (base R4
  only, no national profile — S2; accounts link to Practitioner directly), CareTeam,
  Condition/Procedure/Composition, pharmacy (S9), `Bundle` transactions and `PATCH`
  (deferred; PUT only), `Patient/$match`, related-person flows, organization hierarchy,
  Location wards/serviceClass, terminology server ops (`$expand` etc.), StructureDefinition
  profile authoring/validation (the later device-profile sub-project; D7's interface is
  the seam), SpO₂ and BP (no BP device), registration/KYC/API-key/Postman/DICOM,
  any hosted SATUSEHAT call, HTTPS termination (localhost/LAN HTTP only), paging beyond
  `_count` cap of 100.

## Architecture

```text
HTTP client (admin/doctor/patient curl or test)      ESP32 radar firmware
        |                                              |  (device bearer token)
        |            FastAPI app                        |
        +----> auth middleware (JWT / device token) <---+
                     |
              routes/fhir.py   routes/auth.py   routes/admin.py
                     |
              services/  create / read / update / delete / search
                     |
              validation/  parse (fhir.resources) -> structural rules
                           -> satusehat rules -> references -> OperationOutcome
                     |
              repositories/ sqlite (resources, accounts, device_tokens)
```

- **One file, one responsibility.** Each rule module is small and independently tested;
  `services/` owns orchestration so routes stay thin; `repositories/` is the only code
  that touches SQLite.
- **Validator interface:** `validate(resource_type, payload, *, persist_context) -> list[Issue]`.
  Structural issues come from fhir.resources parse results mapped to FHIRPath expressions;
  SATUSEHAT rules live in per-resource rule functions. Profile-driven validation later
  implements the same interface.
- **Store:** `resources(type, id, json, version, created, updated)` — FHIR JSON stored
  verbatim after validation; search is implemented by loading the type's rows and
  filtering in Python (fine at local scale; the repository interface hides this so a
  SQL search layer can replace it).
- **Secrets:** JWT signing key and bootstrap password from environment
  (`FHIR_JWT_SECRET`, `FHIR_ADMIN_PASSWORD`), generated into a local `.env` file by the
  CLI if absent; device tokens are random 32-byte values, stored as SHA-256 hashes,
  plaintext returned exactly once at provisioning.

## Data flow — the proving scenario

1. `seed` → admin account, Organization, Location, doctor (with Practitioner), patient
   (with NIK union identifiers), device record + provisioned token, patient login.
2. Admin `POST /auth/token` → JWT (role admin).
3. Admin provisions a device token via `POST /fhir-r4/v1/Device/{id}/$provision`
   (admin-only operation; body `{"patient": "Patient/{id}"}` records the device's
   assignment; returns the plaintext token exactly once). Assignment binds device→patient
   only — the encounter is checked at Observation write time (subject must equal the
   assigned patient; encounter must be that patient's, with status `in-progress`).
4. Doctor logs in → creates `Encounter` (status `arrived`, statusHistory `arrived` entry,
   class `AMB`, subject, period.start, identifier with `sys-ids` system, serviceProvider,
   location). Server auto-adds the doctor as `participant.individual`.
5. Doctor `PUT` the Encounter to `in-progress` → statusHistory grows an `in-progress`
   entry (period.start = now, no end yet).
6. Device POSTs `Observation` (status final, category vital-signs, code 8867-4,
   valueQuantity `/min`, subject, encounter, effectiveDateTime UTC, device reference,
   identifier) with its device token. Server validates, checks the device token's
   assignment (device reference must equal the provisioned device; `subject` must equal
   the assigned patient; `encounter` must belong to that subject and be `in-progress`),
   persists.
7. Doctor searches `GET /Observation?subject=Patient/{id}` → authorized because they
   participate in one of that patient's Encounters (read-only review, D15).
8. Doctor `PUT` Encounter to `finished` → statusHistory grows `finished` (start+end).
9. Patient logs in → `GET /Observation?subject=Patient/{own-id}` and
   `GET /Patient/{own-id}` succeed; any other patient's id → 403.

## Components

| Component | Responsibility | Depends on |
|---|---|---|
| `fhir_server/config.py` | Settings (db path, JWT secret/TTL, base URL) from env | — |
| `fhir_server/db.py` | SQLite schema + connection helper | config |
| `fhir_server/repositories/{resources,accounts,devices}.py` | Persistence APIs | db |
| `fhir_server/auth/jwt.py` | Mint/verify local JWT (role + subject claims) | config |
| `fhir_server/auth/middleware.py` | Route-level principal resolution (human JWT vs device token) | jwt, devices repo |
| `fhir_server/validation/parse.py` | fhir.resources parse → structural `Issue` list | fhir.resources |
| `fhir_server/validation/rules_*.py` | Per-resource SATUSEHAT rules (RuleNumbers) | parse |
| `fhir_server/validation/outcome.py` | Build `OperationOutcome` from issues; HTTP mapping | — |
| `fhir_server/services/fhir_service.py` | create/read/update/delete/search orchestration | validation, repos, authz |
| `fhir_server/authz.py` | Role × resource × action matrix; encounter-participant rule | resources repo |
| `fhir_server/routes/{fhir,auth,admin}.py` | HTTP surface | services |
| `fhir_server/ids.py` | IHS-shaped id minting (D14) | — |
| `fhir_server/cli.py` | `seed --reset`, `init-db` | all |
| `device_client/` | Python device test double (wire contract) | — |
| `arduino/radar_json/` | Firmware: serial stream + WiFi HR ingest | — |

## Validation rules (the enforceable subset)

Structural (fhir.resources parse, all resources): JSON object; `resourceType` matches
route; unknown elements rejected by pydantic `extra="forbid"`; **quoted booleans and
quoted integers rejected without coercion** (S15 — verified by test, not assumed);
arrays-on-scalars rejected (S13); primitive formats per R4 regex.

SATUSEHAT rules by resource (RuleNumber → reuse the nine printed numbers, allocate
local numbers ≥ 20000 for our own, per S22):

| Resource | Rule | Number |
|---|---|---|
| all | dateTimes must carry an offset; canonical form `+00:00` on output; reject future dates except `period.end`-type allowances | 10132 (format), 10132 (value) |
| all | dates not earlier than **2014-06-03** (S4 ruling: profile-page value; configurable) | local 20001 |
| all | no empty strings | 10134 |
| all | integers must be unquoted (covered structurally; message parity) | 10254 |
| all | mandatory element missing | 10263 |
| all | `Coding.system` must be an allow-listed URI; `hl7.org/fhir/...web-page` forms mapped on input with warning, `terminology.hl7.org` emitted (S14) | 10002 |
| all | references must resolve to an existing resource of the right type | 10124 (missing), local 20002 (unresolvable) |
| Organization | identifier system prefix `http://sys-ids.kemkes.go.id/organization/`; if `contact` present, `contact.purpose.coding` required | 10117 |
| Location | if `position` present, lon+lat required; `serviceClass` **not** enforced (no wards in scope — flagged, not silent) | local 20003 |
| Practitioner | `qualification.code.coding` required when `qualification` present | 10263 |
| Patient | NIK identifier (`https://fhir.kemkes.go.id/id/nik`, 16 digits) **required** (D13); plus name, birthDate, gender ∈ {male, female}, address with administrativeCode sub-extensions province/city/district/village/rt/rw (S12 union); `multipleBirth[x]` required (profile wajib); ihs-number identifier and `Patient.id` minted by server, client-sent ihs-number rejected; NIK uniqueness | 10117 / 10263 / local 20004 |
| Device | base R4 only (no national profile, S2); `status` ∈ device-status; belongs to provisioning org | local 20005 |
| Encounter | identifier wajib, system `sys-ids.kemkes.go.id/encounter/{org}`; class `AMB` (v3-ActCode); subject, serviceProvider, location, period.start; **lifecycle subset (D12)**: statusHistory starts with `arrived` (period.start only), grows `in-progress` on first PUT, grows `finished` (start+end) on completion; transitions only forward; `diagnosis`/`reasonCode`/`classHistory` not required and not validated beyond R4 structure; duplicate identifier → `issue.code=duplicate` | 10263 / 10117 / duplicate |
| Observation | wajib: status, code.coding, subject, encounter; category `vital-signs` when present; code must be LOINC `8867-4` in this slice (seed set per S29: use-case table + R4 Vital Signs); valueQuantity code `/min`, system UCUM; identifier system emitted as `sys-ids.kemkes.go.id/observation/{org}` (accept `/organization/{org}` on input, S7); device present and matching the authenticated device token | 10263 / 10001 / local 20006 |

CapabilityStatement: declares fhirVersion `4.0.1` (S21), the seven resources with their
supported interactions and search parameters, Bearer security scheme.

## Authorization matrix

| Principal | Organization/Location | Practitioner | Patient | Device | Encounter | Observation |
|---|---|---|---|---|---|---|
| admin | full | full | full | full (+ provision) | full | full |
| doctor | read | read | read if participant on patient's Encounter; create/update own encounter-scoped writes | read | create (own as participant), update own-visited | read for participated patients; no create (device writes) |
| patient | — (403) | — (403) | read own only | — (403) | read own | read where `subject` = own |
| device token | — | — | read assigned patient | — | read assigned open encounter | create only for assigned device+patient+open encounter; read own writes |

401 (no/invalid credentials) vs 403 (wrong principal for the object), both as
`OperationOutcome` per `fhir-security.md`.

## Error handling

- Every 4xx body is `OperationOutcome`: `severity: error`, `code ∈ {duplicate, format,
  value, not-found, forbidden, security, processing}`, `details.text` with
  `(RuleNumber: N)` where a rule fired, `expression` = element path.
- 406 when `Accept` is not JSON-compatible (R4 FHIR REST rule); media-type conflict
  handling per brief: accept `application/json` **and** `application/fhir+json` on input,
  always emit `application/fhir+json`.
- Search unknown parameter → 400 with local rule number; no match → empty searchset
  Bundle (`total: 0`), not 404.
- Device token scopes are enforced per-request against the token's assignment row;
  revoked/expired token → 401.
- Validation failure before persist ⇒ nothing written (processor-then-server).

## Search parameter set (fixed, minimal)

| Resource | Parameters |
|---|---|
| Patient | `identifier` (token `system\|value`), `name`, `birthdate`, `gender` (name+birthdate+gender mode per MPI; name min 3 chars) |
| Practitioner | `identifier`, `name` |
| Organization | `name` |
| Location | `name`, `organization` |
| Encounter | `subject`, `patient` (alias), `status`, `participant` (Practitioner id) |
| Observation | `subject`, `encounter`, `code`, `date` (period on `effectiveDateTime`) |
| Device | `identifier`, `patient` (assigned patient) |

All searches accept `_count` (≤100). Token syntax `system|value` as in R4.

## Testing

- **TDD throughout** (superpowers:test-driven-development): failing test → watch fail →
  minimal code → watch pass → commit. `python3 -m pytest tests -q` green at every commit.
- Unit: each rule function (accept + reject cases citing RuleNumber), id minting, JWT
  round-trip, authz matrix rows.
- Integration: FastAPI `TestClient` walking the nine-step scenario above, including
  every 401/403/400/409 path.
- Cross-check: fhir.resources-parsed fixtures round-trip (serialize→parse) so our
  stored JSON is valid R4 by an independent engine.
- Firmware: `arduino-cli compile --fqbn m5stack:esp32:m5stack_cores3 arduino/radar_json`
  must pass; hardware behavior documented as not run (no upload).
- Verification gate (superpowers:verification-before-completion) before any completion
  claim: run the full suite, the CLI seed against a temp db, and the compile.

## Risks and mitigations

| Risk | Mitigation |
|---|---|
| fhir.resources may coerce `"false"` instead of rejecting | Verify with a failing test first (S15); if it coerces, reject booleans/ints before parse in `parse.py` — the test pins the behavior either way |
| fhir.resources R4 model gaps on odd elements (extensions etc.) | Extensions: `extra="allow"` on extension-bearing containers only; parse failures fall back to structural hand-checks for that element — test-pinned |
| Encounter lifecycle rules could reject legitimate re-reads | Rules fire only on write paths; reads validate nothing |
| SQLite concurrent writes from device + doctor | Single-writer connection with `BEGIN IMMEDIATE`; test two sequential writers |
| Firmware compile environment drift (cores not installed) | Compile is a documented prerequisite step; CI-less repo records exact `arduino-cli` output in commit message |

## Later sub-project roadmap (for sequencing, not this spec)

1. Web UI (D4) — login, doctor worklist, patient record view.
2. Encounter/Condition/Procedure breadth — full Rawat Jalan resource set.
3. Profile sub-project — StructureDefinitions (Device profile per the 13-step
   checklist, SATUSEHAT-derived profiles) behind the Validator interface.
4. Bundle transaction + PATCH; `$match`; paging.
5. Organization hierarchy, Location wards, PractitionerRole, CareTeam assignment flows.
6. Device time sync, HR derived from radar pipeline instead of placeholder, SpO₂ code
   decision if the device grows it (S11 — documented local choice).
7. Webhook/worklist acknowledgment (post-D15 review state).

## Sources

- `docs/reference/claude/INDEX.md`, `VALIDITY-REVIEW.md` (S1–S29), `satusehat-observation.md`,
  `satusehat-encounter.md`, `satusehat-patient.md`, `satusehat-practitioner.md`,
  `satusehat-organization-location.md`, `satusehat-identifiers-and-master-data.md`,
  `satusehat-rest-api-and-validation.md`, `fhir-rest-api.md`, `fhir-security.md`,
  `fhir-observation.md`, `fhir-device.md`, `fhir-profiling.md`
- `docs/.superpowers/specs/2026-09-22-radar-json-fhir-dummy-design.md` (firmware/compute
  precedent), `arduino/radar_json/README.md`
