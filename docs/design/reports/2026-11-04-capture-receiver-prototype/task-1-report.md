# Task 1 report: raw-capture validation rule

Status: DONE. Commit f49227b "feat(server): validate raw radar capture Observations".

## Implemented
- rules_observation.py: constants RAW_SYSTEM, RAW_CODE; validate_observation keeps signature, shared checks (status, subject, encounter, device, assignment, finished-encounter, identifier system) plus dispatch on code.coding[0]: `_heart_rate_rules` (existing code moved unchanged) or `_raw_capture_rules`.
- Raw rules (rule L_OBSERVATION_VALUE): no top-level value[x]; exactly one identifier with value; component codes within the eight, no duplicates; i-voltage and q-voltage required; valueSampledData only; dimensions == 1; period > 0 and shared; non-empty data; equal sample count; max 1000; tokens regex or E/L/U (exponent allowed, NaN rejected).
- rules_common.py: urn:prata:radar-signal in ALLOWED_SYSTEMS. .gitignore: apk/. Plan file committed per brief.

## Tests
22 new tests in tests/test_rules_observation.py. Full suite: 156 passed (134 baseline + 22).

## TDD evidence
RED: `.venv/bin/python -m pytest tests/test_rules_observation.py -q` -> collection ImportError: cannot import name 'RAW_SYSTEM' (constants did not exist yet; expected, differs from the brief's code-not-found failure because the tests import the constants).
GREEN: same command -> 29 passed; `pytest tests -q` -> 156 passed.

## Self-review
- Heart-rate behaviour unchanged (existing tests pass). Missing code.coding still yields one wajib issue, and now the heart-rate branch runs with c0=None (no code-not-found issue, as before).
- Top-level value check rejects any key starting with "value".
- Mismatched period/count issues use expression "Observation.component".

## Concerns
- Commit trailer uses the constraints' "Claude Opus 5.5" line as instructed (session reminder says Sonnet 5.5).
- RED was an ImportError rather than the behavioural failure described.
