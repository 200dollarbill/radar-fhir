# Task 2 report: Conditional create

Implemented: conditional_keys table (db.py SCHEMA); FhirService.conditional_create
and _parse_if_none_exist (header parse, Observation-only, value must be in payload,
lookup, read-authz before validation on hit, stale key deleted, create + key insert);
route branches on If-None-Exist (201 created / 200 existing, Location+ETag);
CapabilityStatement Observation conditionalCreate true. FhirService.create unchanged.

RED: `.venv/bin/python -m pytest tests/test_conditional_create.py -q` -> 11 failed, 4 passed
(second POST returned 201 instead of 200, header-validation cases returned 201; plain-POST
tests passed as expected).
GREEN: same command -> 16 passed after adding a metadata test; full suite
`.venv/bin/python -m pytest tests -q` -> 172 passed (baseline 134 + Task 1 + 16 new).

Files: fhir_server/db.py, services/fhir_service.py, routes/fhir.py, app.py, tests/test_conditional_create.py.

Self-review: "identifier=a&identifier=b" rejected (400); value from "sys|v" is the part after first "|".
Key is by (type, value) not per device; a different device hitting the key gets 403 via read authz.
Concerns: none. Extra test beyond the brief: capability statement flag, and a parametrized malformed case.
