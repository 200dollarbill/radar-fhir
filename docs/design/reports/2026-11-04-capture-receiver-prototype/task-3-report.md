# Task 3 report: capture-session CLI

Status: DONE. Commit 3d3644e "feat(server): capture-session command prints a session card".

## Implemented
`cmd_capture_session` in fhir_server/cli.py plus `capture-session --label` subparser. Label regex `^[A-Za-z0-9-]{1,32}$` (exit 2, nothing created). Takes first Organization/Location/Practitioner/Device; missing -> stderr `database not seeded: run "seed" first`, exit 1. Via FhirService with admin Principal: synthetic Patient (NIK "9900"+12 random digits, retry on 409, name "Sesi <label>", placeholder birthDate/gender/multipleBirthBoolean/address with administrativeCode), Encounter created arrived (1 history entry, identifier capture-<label>-<8 hex>, participant = Practitioner) then updated to in-progress with history extended, token via provision_device. Last stdout line is the JSON card.

## Tests (tests/test_cli_capture_session.py, 9 cases)
All brief cases; bad label parametrized over "a b", "", 33 chars.

## TDD
RED: `.venv/bin/python -m pytest tests/test_cli_capture_session.py -q` -> 6 failed, 3 passed; failure "argument cmd: invalid choice: 'capture-session'" (expected; the 3 bad-label cases passed already since argparse rejects any invalid command with nonzero exit).
GREEN: same command -> 9 passed. Full suite: 181 passed.

## Files
fhir_server/cli.py, tests/test_cli_capture_session.py

## Self-review
- Run on an unseeded path calls db init, so it creates an empty db file (harmless, then exits 1).
- Seeded Encounter/Patient times use current UTC truncated to seconds.
- Tests import run_cli/raw from sibling test modules (works under current pytest rootdir config).

## Concerns
None blocking. A failure between Patient and Encounter creation leaves an orphan Patient (no transaction).
