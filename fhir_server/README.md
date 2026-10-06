# PRATA FHIR R4 server (walking skeleton)

A standalone, local-only **FHIR R4 (4.0.1)** server shaped like SATUSEHAT:
three roles (admin / doctor / patient), provisioned device tokens for direct
Observation ingest, SATUSEHAT-style `OperationOutcome` errors with RuleNumbers.

Design authority: `docs/.superpowers/specs/2026-09-29-fhir-r4-server-walking-skeleton-design.md`
Implementation plan: `docs/.superpowers/plans/2026-09-29-fhir-r4-server-walking-skeleton.md`

**This server never calls the hosted SATUSEHAT platform. No API keys, no
registration, no outbound FHIR calls — ever.** Everything runs against a local
SQLite file.

## Run

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
FHIR_ADMIN_PASSWORD=<choose> .venv/bin/python -m fhir_server seed --reset
FHIR_JWT_SECRET=<choose> .venv/bin/python -m fhir_server serve --port 8000
```

`seed --reset` wipes and rebuilds the DB, then prints a JSON summary on its
**last stdout line**: `admin_password`, `doctor_password`, `patient_password`,
`device_token`, `org_id`, `location_id`, `practitioner_id`, `patient_id`,
`device_id`. (Passwords come from `FHIR_ADMIN_PASSWORD` / `FHIR_DOCTOR_PASSWORD`
/ `FHIR_PATIENT_PASSWORD`, or are generated and printed once.)

If `FHIR_JWT_SECRET` is unset, `seed`/`serve` generate one and append it to
`.env` (process-local fallback if that file cannot be written).

## Endpoints

| Method + path | Auth | Purpose |
|---|---|---|
| `POST /auth/token` | none | `{username, password}` → `{access_token, token_type, expires_in}` |
| `GET /fhir-r4/v1/metadata` | none | CapabilityStatement (fhirVersion 4.0.1) |
| `POST /fhir-r4/v1/{Type}` | Bearer | create (201 + Location + ETag) |
| `GET /fhir-r4/v1/{Type}/{id}` | Bearer | read (200 + ETag) |
| `PUT /fhir-r4/v1/{Type}/{id}` | Bearer | full update (200 + ETag) |
| `DELETE /fhir-r4/v1/{Type}/{id}` | Bearer | delete (204; admin only) |
| `GET /fhir-r4/v1/{Type}?param=…` | Bearer | search → `Bundle` `searchset` |
| `POST /fhir-r4/v1/Device/{id}/$provision` | admin Bearer | mint a device token (returns plaintext once) |
| `POST /fhir-r4/v1/admin/accounts` / `GET …` | admin Bearer | manage accounts |

Supported types: `Organization, Location, Practitioner, Patient, Device,
Encounter, Observation` (heart-rate slice, LOINC 8867-4). Search parameters per
type are listed in the spec and in `/metadata`.

Input accepts `application/json` and `application/fhir+json`; output is always
`application/fhir+json`. Non-JSON `Accept` → 406; non-JSON `Content-Type` on a
write → 415; both as `OperationOutcome`.

## Roles

- **admin** — everything, including `$provision` and account management.
- **doctor** — creates/updates `Encounter` (auto-added as participant), reads
  only patients they participate with and their encounters/observations.
- **patient** — read-only on their own `Patient`, `Encounter`, `Observation`.
- **device token** — creates `Observations` only for its assigned
  patient + a `subject`/`encounter` that matches the assignment; reads only its
  own writes.

## Device ingest contract

The Python double `device_client/client.py::submit_heart_rate` and the ESP32
firmware `arduino/radar_json/ingest.h` speak the identical contract: a
heart-rate `Observation` POSTed to `/fhir-r4/v1/Observation` with the
provisioned `Bearer` token. See `arduino/radar_json/README.md` for firmware
config (config.h is gitignored; **do not upload** until GPIO wiring is
confirmed).

## The nine-step flow (curl sketch)

```bash
B=http://127.0.0.1:8000
ADM=$(curl -s $B/auth/token -d '{"username":"admin","password":"<seed>"}' | jq -r .access_token)
TOK=$(curl -s -H "Authorization: Bearer $ADM" -X POST \
      $B/fhir-r4/v1/Device/<device_id>/$provision \
      -H 'Content-Type: application/json' \
      -d '{"patient":"Patient/<patient_id>"}' | jq -r .token)
DOC=$(curl -s $B/auth/token -d '{"username":"doctor","password":"<seed>"}' | jq -r .access_token)
# doctor: POST Encounter (arrived) → PUT in-progress → device POSTs →
# doctor GET Observation?subject=… → PUT Encounter finished
# patient: GET /fhir-r4/v1/Patient/<id> with their own token
```

Full scripted version: `tests/test_scenario_e2e.py`.

## Tests

```bash
.venv/bin/python -m pytest tests -q          # server suite
python3 -m pytest .tools/scrape/tests -q     # reference-compilation suite (34)
python3 .tools/scrape/lint_views.py          # must print "0 problem(s)"
/home/pingwalk/.local/bin/arduino-cli compile --fqbn m5stack:esp32:m5stack_cores3 arduino/radar_json
```

Validation is layered: fhir.resources (R4B models) structural parse →
per-resource SATUSEHAT rules → reference existence → persist
(processor-then-server: a failed request writes nothing).
