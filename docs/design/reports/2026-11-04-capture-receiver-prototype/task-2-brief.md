### Task 2: Conditional create

**Files:**
- Modify: `fhir_server/db.py`, `fhir_server/services/fhir_service.py`, `fhir_server/routes/fhir.py`, `fhir_server/app.py` (CapabilityStatement)
- Test: `tests/test_conditional_create.py`

**Interfaces:**
- Consumes: raw rule from Task 1.
- Produces: `FhirService.conditional_create(principal, resource_type, payload, if_none_exist: str) -> tuple[str, dict, bool]` returning `(id, doc, created)`. Table `conditional_keys(type TEXT, identifier_value TEXT, resource_id TEXT, PRIMARY KEY (type, identifier_value))`. Route status `201` when created, `200` otherwise. `FhirService.create` is unchanged.

- [ ] **Step 1: Write failing tests** in `tests/test_conditional_create.py`, using the `client` pattern from `tests/test_routes.py`: seed an org, patient, in-progress Encounter and device token.

```python
def test_first_post_201_second_200_same_id():
def test_second_post_stores_no_new_row():  # count of Observation rows stays 1
def test_system_pipe_value_form_matches_value_only_key():
    # header "identifier=<sys>|v" after a post with "identifier=v" -> 200
def test_retry_after_encounter_finished_returns_200():  # Review Focus 2
def test_other_device_gets_403_not_the_record():
def test_header_param_other_than_identifier_400():
def test_malformed_header_400():       # "identifier" and "identifier="
def test_header_value_not_in_payload_400():  # cannot poison another chunk's key
def test_non_observation_type_400():
def test_invalid_payload_400_records_no_key():  # corrected retry then gets 201
def test_key_of_deleted_resource_creates_again():  # admin DELETE, then POST -> 201
def test_plain_post_may_reuse_identifier():  # two plain POSTs "radar-1" -> both 201
def test_plain_post_ignores_conditional_keys():  # conditional then plain, same value -> 201
```

- [ ] **Step 2: Run to verify failure**

Run: `.venv/bin/python -m pytest tests/test_conditional_create.py -q`
Expected: FAIL. The second POST returns `201`.

- [ ] **Step 3: Implement.** Add the table to `SCHEMA`. It is `IF NOT EXISTS`, so existing databases gain it at `init`.

`conditional_create` order:
1. Parse the header. Accept exactly one `identifier=` parameter, taking the part after `|` when present. Otherwise raise `FhirError` with `400`.
2. Reject any type other than Observation with `400`.
3. Require the value to equal a `payload.identifier[].value`, otherwise `400`.
4. Look up the key. On a hit with a live resource, run `authz.check(principal, "read", ...)` and return `(id, doc, False)`. This comes **before** validation so Review Focus 2 holds.
5. On a hit with a deleted resource, delete the key and continue.
6. Call `self.create(...)`, insert the key, return `(id, doc, True)`.

In the `create` route, read the payload first, then branch on `request.headers.get("If-None-Exist")`. Everything after the `await` runs without yielding on the single event loop, so two retries cannot interleave.

Set `conditionalCreate: true` on the Observation entry of the CapabilityStatement.

- [ ] **Step 4: Run to verify pass**

Run: `.venv/bin/python -m pytest tests -q`
Expected: all pass.

- [ ] **Step 5: Commit**

```bash
git add fhir_server/db.py fhir_server/services/fhir_service.py fhir_server/routes/fhir.py fhir_server/app.py tests/test_conditional_create.py
git commit -m "feat(server): conditional create for Observation retries"
```

---

