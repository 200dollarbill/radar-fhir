### Task 3: `capture-session` CLI

**Files:**
- Modify: `fhir_server/cli.py`
- Test: `tests/test_cli_capture_session.py`

**Interfaces:**
- Produces: `python -m fhir_server capture-session --label S001`. The last stdout line is JSON `{"token","patient":"Patient/<id>","encounter":"Encounter/<id>","device":"Device/<id>","org","label"}`.

- [ ] **Step 1: Write failing tests**, using `run_cli` as in `tests/test_cli_seed.py`.

```python
def test_card_has_all_fields_and_references():
def test_card_can_post_a_raw_chunk():  # valid raw chunk with this token -> 201
def test_doctor_can_read_the_chunk():  # seeded doctor reads the Observation -> 200
def test_two_sessions_get_different_patients():
def test_same_label_twice_succeeds():
def test_unseeded_db_exits_1_with_message():
    assert p.returncode == 1 and "seed" in p.stderr
def test_bad_label_rejected():  # "a b", "" -> nonzero exit, nothing created
```

- [ ] **Step 2: Run to verify failure**

Run: `.venv/bin/python -m pytest tests/test_cli_capture_session.py -q`
Expected: FAIL with an argparse error (invalid choice).

- [ ] **Step 3: Implement `cmd_capture_session(args)`.** Label must match `^[A-Za-z0-9-]{1,32}$`.

Take the first Organization, Location, Practitioner and Device from `resources.list`. If any is missing, print `database not seeded: run "seed" first` to stderr and exit 1.

Use `FhirService(conn, Settings.from_env(db_path=args.db))` with `Principal(kind="admin")`:
- **Patient:** NIK `"9900"` + 12 random digits, which is not a real province code and so marks it synthetic. Retry on collision. Name text `Sesi <label>`, and `birthDate`, `gender`, `multipleBirthBoolean` and `address` with `administrativeCode` copied in shape from `cmd_seed`. The validator requires these fields, and their values are placeholders.
- **Encounter:** create as `arrived` with one history entry, identifier value `capture-<label>-<8 hex>`, and `participant` naming the Practitioner. Then `update` to `in-progress` with the history extended.
- **Token:** `provision_device`.

- [ ] **Step 4: Run to verify pass**

Run: `.venv/bin/python -m pytest tests -q`
Expected: all pass.

- [ ] **Step 5: Commit**

```bash
git add fhir_server/cli.py tests/test_cli_capture_session.py
git commit -m "feat(server): capture-session command prints a session card"
```

---

