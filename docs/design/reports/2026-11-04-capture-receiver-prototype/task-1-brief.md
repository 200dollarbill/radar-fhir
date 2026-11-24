### Task 1: Raw-capture validation rule

**Files:**
- Modify: `fhir_server/validation/rules_observation.py`, `fhir_server/validation/rules_common.py`, `.gitignore`
- Test: `tests/test_rules_observation.py`

**Interfaces:**
- Produces: `validate_observation` keeps its signature and dispatches on `code.coding[0]`. Constants `RAW_SYSTEM = "urn:prata:radar-signal"`, `RAW_CODE = "raw-capture"`.

- [ ] **Step 1: Write failing tests** in `tests/test_rules_observation.py`.

Add a helper `raw(**kw)` returning a valid chunk with all eight components of three samples, plus:

```python
def test_raw_capture_valid(): assert errs(raw()) == []
def test_raw_accepts_error_tokens():  # data "1.65 E -0.5"
def test_raw_requires_i_and_q():      # drop q-voltage -> issue
def test_raw_rejects_unknown_component_code():
def test_raw_rejects_duplicate_component_code():
def test_raw_rejects_top_level_value():   # valueQuantity present -> issue
def test_raw_rejects_non_sampled_component():  # valueQuantity in a component
def test_raw_rejects_dimensions_not_one():
def test_raw_rejects_period_zero():
def test_raw_rejects_mismatched_period():
def test_raw_rejects_mismatched_sample_count():
def test_raw_rejects_bad_token():     # data "1.65 abc"
def test_raw_rejects_nan_token():     # data "1.65 NaN"
def test_raw_accepts_exponent_token():  # data "1e-7"
def test_raw_rejects_over_1000_samples():  # 1001 tokens
def test_raw_accepts_exactly_1000_samples():
def test_raw_rejects_empty_data():
def test_raw_requires_exactly_one_identifier():  # 0 and 2 -> issue
def test_raw_requires_identifier_value():
def test_raw_keeps_device_rule():     # wrong device_ref -> issue, as heart rate
def test_raw_keeps_finished_encounter_rule():
def test_heart_rate_code_still_required_for_other_codes():  # LOINC other than 8867-4 still rejected
```

Each reject test asserts at least one issue whose `expression` starts with `Observation`.

- [ ] **Step 2: Run to verify failure**

Run: `.venv/bin/python -m pytest tests/test_rules_observation.py -q`
Expected: new tests FAIL with a code-not-found issue on valid raw payloads. Existing tests pass.

- [ ] **Step 3: Implement.** Split `validate_observation` into shared checks (status, subject, encounter, device, assignment, identifier system) and two branches: `_heart_rate_rules` (existing code, category and `valueQuantity` checks unchanged) and `_raw_capture_rules`. Use `L_OBSERVATION_VALUE` as the rule number. Data tokens match `^-?\d+(\.\d+)?([eE][+-]?\d+)?$` or are exactly `E`, `L`, `U`. JavaScript can write very small numbers like `1e-7`, so the exponent form must pass.

Add `"urn:prata:radar-signal"` to `ALLOWED_SYSTEMS`. Add `apk/` to `.gitignore`.

- [ ] **Step 4: Run to verify pass**

Run: `.venv/bin/python -m pytest tests -q`
Expected: all pass, including the original 134.

- [ ] **Step 5: Commit**

```bash
git add fhir_server/validation/rules_observation.py fhir_server/validation/rules_common.py tests/test_rules_observation.py .gitignore docs/.superpowers/plans/2026-11-04-capture-receiver-prototype.md
git commit -m "feat(server): validate raw radar capture Observations"
```

---

