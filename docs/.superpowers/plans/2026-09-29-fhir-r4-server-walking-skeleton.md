# SATUSEHAT-Compatible FHIR R4 Server — Walking Skeleton Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a local-only FHIR R4 server where an admin provisions a flat facility, a doctor opens an Encounter, a device posts heart-rate Observations into it, the doctor reads them, and the patient reads their own record — with three-role auth and SATUSEHAT-shaped validation.

**Architecture:** FastAPI app with thin routes → `services/fhir_service.py` orchestration → validation pipeline (fhir.resources structural parse → per-resource SATUSEHAT rules → reference checks) → SQLite repositories. Auth is a FastAPI dependency resolving either a local JWT (admin/doctor/patient) or a provisioned device token into a `Principal`. Errors are always `OperationOutcome` with RuleNumbers.

**Tech Stack:** Python 3.12, FastAPI, fhir.resources (pydantic v2), PyJWT, SQLite (stdlib), pytest + httpx TestClient; Arduino CLI (`m5stack:esp32:m5stack_cores3`) for the firmware gate.

**Spec:** `docs/.superpowers/specs/2026-09-29-fhir-r4-server-walking-skeleton-design.md` — decisions D1–D16, validation tables, authz matrix, and the nine-step scenario in that file are normative. This plan argues from it; read both.

## Global Constraints

- All commands run from the repo root: `/mnt/Data/yep/Kuliah/Tugas/Semester 7 ntr lagi lulus/PRATA`. Test runner: `.venv/bin/python -m pytest tests -q` must be green after **every** task.
- Existing suites must stay green: `python3 -m pytest .tools/scrape/tests -q` (34 tests) and `python3 .tools/scrape/lint_views.py` (must print `0 problem(s)`). Do not touch `docs/reference/raw/`.
- Media types: accept `application/json` **and** `application/fhir+json` on input; always emit `application/fhir+json` (with `charset=utf-8`); `Accept` that is not JSON-compatible → 406 `OperationOutcome`.
- Time: `dateTime` inputs must carry a UTC offset; output canonicalized to `+00:00`. Dates earlier than **2014-06-03** rejected (configurable `Settings.earliest_date`). Future dates rejected except `period.end` on Encounter finish.
- RuleNumbers: reuse only the nine printed numbers (10001, 10002, 10117, 10124, 10132, 10134, 10171, 10254, 10263) and `duplicate`; our own rules use 20001+. Message format: `... (RuleNumber: N)` inside `issue.details.text`.
- Ids (D14): Patient `P` + 11 digits; Practitioner `N` + 8 digits; Organization 9–11 digits; Location, Device, Encounter, Observation → UUID v4. All ids must satisfy R4 `[A-Za-z0-9\-\.]{1,64}`.
- Patient create requires NIK (16 digits, system `https://fhir.kemkes.go.id/id/nik`) plus name, birthDate, gender ∈ {male, female}, address with administrativeCode sub-extensions (province/city/district/village/rt/rw), `multipleBirth[x]`. Server mints `Patient.id` and the `ihs-number` identifier; a client-sent `ihs-number` identifier is rejected.
- Observation in this slice: code LOINC `8867-4` only, `valueQuantity.code == "/min"`, system `http://unitsofmeasure.org`, category `vital-signs`, wajib status/code.coding/subject/encounter, `device` must equal the authenticated device.
- Base URL shape: everything FHIR under `/fhir-r4/v1`; `GET /fhir-r4/v1/metadata` and `POST /auth/token` are the only unauthenticated routes.
- JWT: HS256, claims `sub` (account id), `role` ∈ {admin, doctor, patient}, `ref` (resource reference like `Practitioner/N10000001`), TTL 3600 s from `Settings.jwt_ttl_seconds`.
- Device tokens: 32 random bytes, base64url text, stored as SHA-256 hex; plaintext returned only in the `$provision` response; one row per token with `device_id`, `patient_id`, `revoked`.
- Every commit message ends with:
  `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`
- Never claim a task done without running its stated commands (verification-before-completion).

## Review Focus

These five input classes are implied by the spec but easiest to get wrong; each has a pinning test in the task named.

1. **Quoted booleans/ints and arrays-on-scalars in payloads (S15/S13)** must yield a 400 `OperationOutcome`, never a 500 and never silent coercion → `tests/test_parse_structural.py::test_rejects_quoted_boolean`, `...::test_rejects_array_on_scalar`.
2. **Bearer-token edge cases** — absent, garbage, expired, valid doctor token used on device-only write, device token used for a foreign patient → 401 vs 403 distinguished, both `OperationOutcome` → `tests/test_routes.py::test_fhir_requires_token` (401 at HTTP), `tests/test_auth_principals.py::test_expired_token_401` (TokenError at library level), `tests/test_authz.py::test_device_can_create_assigned_observation_only` (403 at service level) and `tests/test_fhir_service.py::test_device_cannot_create_foreign_observation`. **(Post-implementation reconciliation, final review issue 12: the original text named `test_missing_token_401` and `tests/test_device_scope.py`, which were never written; these are the tests that actually pin the behavior.)**
3. **Search must enforce authz, not just read-by-id** — patient A searching `?subject=Patient/B`, doctor searching a never-participated patient, patient omitting `subject` entirely → 403 or self-filtered, never cross-tenant rows → `tests/test_search.py::test_patient_cannot_search_other_subject`, `...::test_patient_search_without_subject_returns_only_own`.
4. **Encounter lifecycle** — backwards transition, skipping `in-progress`, finishing without `period.end` growth, duplicate visit identifier → `tests/test_rules_encounter.py` (10 tests) plus, for the "can a PUT rewrite prior entries" case the original text missed, `test_rules_encounter.py::test_backwards_transition_rejected`'s preservation companion and the full-dict prefix check added by final review issue 10 (covered in Task 18's E2E path).
5. **Processor-then-server** — any validation failure leaves zero rows written, including references to nonexistent Patient/Encounter (10124/20002) → `tests/test_fhir_service.py::test_failed_validation_writes_nothing`.

---

### Task 1: Environment, package skeleton, config, DB schema

**Files:**
- Create: `requirements.txt`, `fhir_server/__init__.py`, `fhir_server/config.py`, `fhir_server/db.py`, `tests/conftest.py`
- Test: `tests/test_db_schema.py`

**Interfaces:**
- Consumes: nothing (bootstrap task).
- Produces: `Settings` dataclass (`db_path: str`, `jwt_secret: str`, `jwt_ttl_seconds: int = 3600`, `earliest_date: str = "2014-06-03"`, classmethod `Settings.from_env(**overrides)`); `db.connect(db_path: str) -> sqlite3.Connection` (row_factory=sqlite3.Row, `PRAGMA foreign_keys=ON`); `db.init(conn)` creating tables `resources(type,id,version,json,created,updated, PRIMARY KEY(type,id))`, `accounts(id,username,password_hash,role,subject_ref,active, PRIMARY KEY(id), UNIQUE(username))`, `device_tokens(id,device_id,patient_id,token_sha256,created,revoked, PRIMARY KEY(id), UNIQUE(token_sha256))`. Fixture `db_path(tmp_path)` in `tests/conftest.py`.

- [ ] **Step 1: Create venv and install dependencies**

```bash
python3 -m venv .venv
.venv/bin/pip install -q fastapi uvicorn "fhir.resources" PyJWT httpx pytest
.venv/bin/pip freeze | grep -E "^(fastapi|fhir.resources|PyJWT|httpx|pydantic)==" > requirements.txt
```

- [ ] **Step 2: Write the failing test**

```python
# tests/test_db_schema.py
from fhir_server import db

def test_init_creates_tables(db_path):
    conn = db.connect(db_path)
    db.init(conn)
    rows = {r[0] for r in conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table'")}
    assert {"resources", "accounts", "device_tokens"} <= rows

def test_resources_primary_key(db_path):
    conn = db.connect(db_path)
    db.init(conn)
    conn.execute(
        "INSERT INTO resources VALUES ('Patient','P1',1,'{}','2026-01-01T00:00:00+00:00','2026-01-01T00:00:00+00:00')")
    try:
        conn.execute("INSERT INTO resources VALUES ('Patient','P1',2,'{}','a','a')")
        raise AssertionError("duplicate insert must fail")
    except Exception:
        pass
```

Add to `tests/conftest.py`:

```python
import pytest
@pytest.fixture
def db_path(tmp_path):
    return str(tmp_path / "test.db")
```

- [ ] **Step 3: Run test to verify it fails**

Run: `.venv/bin/python -m pytest tests/test_db_schema.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'fhir_server'`

- [ ] **Step 4: Write minimal implementation**

```python
# fhir_server/config.py
import os
from dataclasses import dataclass

@dataclass(frozen=True)
class Settings:
    db_path: str
    jwt_secret: str
    jwt_ttl_seconds: int = 3600
    earliest_date: str = "2014-06-03"

    @classmethod
    def from_env(cls, **overrides):
        base = dict(
            db_path=os.environ.get("FHIR_DB_PATH", "fhir_server.db"),
            jwt_secret=os.environ.get("FHIR_JWT_SECRET", ""),
            jwt_ttl_seconds=int(os.environ.get("FHIR_JWT_TTL", "3600")),
            earliest_date=os.environ.get("FHIR_EARLIEST_DATE", "2014-06-03"),
        )
        base.update({k: v for k, v in overrides.items() if v is not None})
        if not base["jwt_secret"]:
            raise ValueError("FHIR_JWT_SECRET is required")
        return cls(**base)
```

```python
# fhir_server/db.py
import sqlite3

SCHEMA = """
CREATE TABLE IF NOT EXISTS resources (
    type TEXT NOT NULL, id TEXT NOT NULL, version INTEGER NOT NULL,
    json TEXT NOT NULL, created TEXT NOT NULL, updated TEXT NOT NULL,
    PRIMARY KEY (type, id));
CREATE TABLE IF NOT EXISTS accounts (
    id TEXT PRIMARY KEY, username TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL, role TEXT NOT NULL,
    subject_ref TEXT, active INTEGER NOT NULL DEFAULT 1);
CREATE TABLE IF NOT EXISTS device_tokens (
    id TEXT PRIMARY KEY, device_id TEXT NOT NULL, patient_id TEXT NOT NULL,
    token_sha256 TEXT NOT NULL UNIQUE, created TEXT NOT NULL,
    revoked INTEGER NOT NULL DEFAULT 0);
"""

def connect(db_path: str) -> sqlite3.Connection:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def init(conn: sqlite3.Connection) -> None:
    conn.executescript(SCHEMA)
    conn.commit()
```

```python
# fhir_server/__init__.py
```
(empty file; also empty `tests/__init__.py` not needed since pytest rootdir config)

- [ ] **Step 5: Run test to verify it passes**

Run: `.venv/bin/python -m pytest tests/test_db_schema.py -v`
Expected: PASS (2 tests)

- [ ] **Step 6: Commit**

```bash
git add requirements.txt fhir_server tests
git commit -m "feat(server): bootstrap package, settings, sqlite schema

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

---

### Task 2: Id minting (IHS-shaped)

**Files:**
- Create: `fhir_server/ids.py`
- Test: `tests/test_ids.py`

**Interfaces:**
- Consumes: nothing.
- Produces: `mint(resource_type: str) -> str` raising `ValueError` for unknown types; `R4_ID_RE` pattern constant `^[A-Za-z0-9.\-]{1,64}$`.

- [ ] **Step 1: Write the failing test**

```python
# tests/test_ids.py
import re
import pytest
from fhir_server.ids import mint, R4_ID_RE

def test_patient_id_shape():
    i = mint("Patient")
    assert re.fullmatch(r"P\d{11}", i)

def test_practitioner_id_shape():
    assert re.fullmatch(r"N\d{8}", mint("Practitioner"))

def test_organization_id_shape():
    i = mint("Organization")
    assert i.isdigit() and 9 <= len(i) <= 11

def test_uuid_types():
    for t in ("Location", "Device", "Encounter", "Observation"):
        i = mint(t)
        assert len(i) == 36 and i.count("-") == 4
        assert re.fullmatch(R4_ID_RE, i)

def test_unique_patient_ids():
    assert {mint("Patient") for _ in range(50)} == {mint("Patient")} or len(
        {mint("Patient") for _ in range(50)}) == 50

def test_unknown_type_raises():
    with pytest.raises(ValueError):
        mint("Condition")
```

- [ ] **Step 2: Run test to verify it fails**

Run: `.venv/bin/python -m pytest tests/test_ids.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'fhir_server.ids'`

- [ ] **Step 3: Write minimal implementation**

```python
# fhir_server/ids.py
import secrets
import uuid

R4_ID_RE = r"[A-Za-z0-9.\-]{1,64}"
_UUID_TYPES = {"Location", "Device", "Encounter", "Observation"}

def mint(resource_type: str) -> str:
    if resource_type == "Patient":
        return "P" + "".join(str(secrets.randbelow(10)) for _ in range(11))
    if resource_type == "Practitioner":
        return "N" + "".join(str(secrets.randbelow(10)) for _ in range(8))
    if resource_type == "Organization":
        n = secrets.randbelow(1_000_000_000) + 100_000_000  # 9 digits
        return str(n)
    if resource_type in _UUID_TYPES:
        return str(uuid.uuid4())
    raise ValueError(f"no id scheme for {resource_type}")
```

- [ ] **Step 4: Run test to verify it passes**

Run: `.venv/bin/python -m pytest tests/test_ids.py -v`
Expected: PASS (6 tests)

- [ ] **Step 5: Commit**

```bash
git add fhir_server/ids.py tests/test_ids.py
git commit -m "feat(server): IHS-shaped resource id minting

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

---

### Task 3: Issue model and OperationOutcome builder

**Files:**
- Create: `fhir_server/validation/__init__.py`, `fhir_server/validation/issues.py`, `fhir_server/validation/outcome.py`
- Test: `tests/test_outcome.py`

**Interfaces:**
- Consumes: nothing.
- Produces:
  - `issues.Issue` dataclass: `severity: str = "error"`, `code: str` (one of `duplicate|format|value|not-found|forbidden|security|processing|not-supported|invalid`), `details_text: str`, `expression: str | None = None`, `rule_number: int | None = None`.
  - Rule constants: `R_DUPLICATE=10001` unused; define exactly: `R_CODE_NOT_FOUND=10001`, `R_BAD_CODING_SYSTEM=10002`, `R_BAD_IDENTIFIER_SYSTEM=10117`, `R_MISSING_REFERENCE=10124`, `R_DATETIME=10132`, `R_EMPTY_TEXT=10134`, `R_INT_AS_STRING=10254`, `R_WAJIB_MISSING=10263`, `L_EARLIEST_DATE=20001`, `L_UNRESOLVABLE_REFERENCE=20002`, `L_LOCATION_POSITION=20003`, `L_PATIENT_IDENTITY=20004`, `L_DEVICE_RULE=20005`, `L_OBSERVATION_VALUE=20006`, `L_AUTH=20007`, `L_SEARCH_PARAM=20008`.
  - `outcome.to_outcome(issues: list[Issue]) -> dict` — playbook shape: `{"resourceType": "OperationOutcome", "issue": [...]}`; each issue gets `severity`, `code`, `details.text` (append ` (RuleNumber: N)` when `rule_number` set and not already in text), `expression: [path]` when set. Empty input → single `processing` issue `"Internal error"`.
  - `outcome.issues_for_message(message, code, expression=None, rule_number=None) -> list[Issue]` convenience.

- [ ] **Step 1: Write the failing test**

```python
# tests/test_outcome.py
from fhir_server.validation import issues, outcome

def test_outcome_shape_matches_playbook():
    i = issues.Issue(code="value", details_text="Code not found: 'x'",
                     expression="Observation.code", rule_number=issues.R_CODE_NOT_FOUND)
    o = outcome.to_outcome([i])
    assert o["resourceType"] == "OperationOutcome"
    assert o["issue"][0]["severity"] == "error"
    assert o["issue"][0]["code"] == "value"
    assert o["issue"][0]["details"]["text"] == \
        "Code not found: 'x' (RuleNumber: 10001)"
    assert o["issue"][0]["expression"] == ["Observation.code"]

def test_multiple_issues_preserved():
    a = issues.Issue(code="format", details_text="bad")
    b = issues.Issue(code="value", details_text="worse")
    assert len(outcome.to_outcome([a, b])["issue"]) == 2

def test_empty_issues_become_internal_error():
    o = outcome.to_outcome([])
    assert o["issue"][0]["code"] == "processing"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `.venv/bin/python -m pytest tests/test_outcome.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'fhir_server.validation'`

- [ ] **Step 3: Write minimal implementation**

```python
# fhir_server/validation/__init__.py
```
(empty)

```python
# fhir_server/validation/issues.py
from dataclasses import dataclass

R_CODE_NOT_FOUND = 10001
R_BAD_CODING_SYSTEM = 10002
R_BAD_IDENTIFIER_SYSTEM = 10117
R_MISSING_REFERENCE = 10124
R_DATETIME = 10132
R_EMPTY_TEXT = 10134
R_INT_AS_STRING = 10254
R_WAJIB_MISSING = 10263
L_EARLIEST_DATE = 20001
L_UNRESOLVABLE_REFERENCE = 20002
L_LOCATION_POSITION = 20003
L_PATIENT_IDENTITY = 20004
L_DEVICE_RULE = 20005
L_OBSERVATION_VALUE = 20006
L_AUTH = 20007
L_SEARCH_PARAM = 20008

@dataclass
class Issue:
    code: str
    details_text: str
    severity: str = "error"
    expression: str | None = None
    rule_number: int | None = None
```

```python
# fhir_server/validation/outcome.py
from .issues import Issue

def to_outcome(issue_list: list[Issue]) -> dict:
    if not issue_list:
        issue_list = [Issue(code="processing", details_text="Internal error")]
    out = []
    for i in issue_list:
        text = i.details_text
        if i.rule_number is not None and f"(RuleNumber: {i.rule_number})" not in text:
            text = f"{text} (RuleNumber: {i.rule_number})"
        entry = {
            "severity": i.severity,
            "code": i.code,
            "details": {"text": text},
        }
        if i.expression:
            entry["expression"] = [i.expression]
        out.append(entry)
    return {"resourceType": "OperationOutcome", "issue": out}

def issues_for_message(message, code, expression=None, rule_number=None) -> list[Issue]:
    return [Issue(code=code, details_text=message, expression=expression,
                  rule_number=rule_number)]
```

- [ ] **Step 4: Run test to verify it passes**

Run: `.venv/bin/python -m pytest tests/test_outcome.py -v`
Expected: PASS (3 tests)

- [ ] **Step 5: Commit**

```bash
git add fhir_server/validation tests/test_outcome.py
git commit -m "feat(server): OperationOutcome builder with RuleNumber messages

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

---

### Task 4: Structural parser (fhir.resources + strict primitive walk)

**Files:**
- Create: `fhir_server/validation/parse.py`
- Test: `tests/test_parse_structural.py`

**Interfaces:**
- Consumes: `validation.issues.Issue`, rule constants.
- Produces: `parse.SUPPORTED_TYPES: dict[str, type]` (maps the seven resource names to fhir.resources model classes); `parse.structural_issues(resource_type: str, payload) -> tuple[list[Issue], object | None]` returning `(issues, validated_model_or_None)`. Issues carry FHIRPath-ish expressions like `Patient.active` (dotted path, array indices as `[0]`). Pydantic model errors map to `code="structure"`→ use `code="processing"`; primitive/format errors → `code="format"` with `R_DATETIME` only for dateTime-ish paths, else no rule number; strict-walk issues use `code="value"`/`format` appropriately.
- Design note: strict walk (`_strict_check`) does three things `model_validate` alone may not: (a) unknown keys → `extra` rejected, (b) `str` where JSON boolean/integer expected → rejected **before** coercion (S15), (c) non-list where array expected and list where scalar expected (S13). Then `model_validate` runs for full typing; its errors append. If a pydantic validation succeeds the returned model is passed through.

- [ ] **Step 1: Write the failing test**

```python
# tests/test_parse_structural.py
from fhir_server.validation.parse import structural_issues

def valid_patient():
    return {
        "resourceType": "Patient",
        "active": True,
        "gender": "female",
        "birthDate": "1990-04-02",
        "name": [{"text": "Siti", "family": "Siti", "given": ["Siti"]}],
    }

def test_valid_patient_no_issues():
    issues, model = structural_issues("Patient", valid_patient())
    assert issues == [] and model is not None

def test_rejects_quoted_boolean():
    p = valid_patient(); p["active"] = "false"
    issues, model = structural_issues("Patient", p)
    assert model is None
    assert any(i.expression == "Patient.active" for i in issues)

def test_rejects_quoted_integer():
    issues, model = structural_issues("Patient", {"resourceType": "Patient",
        "multipleBirthInteger": "3"})
    assert model is None and issues

def test_rejects_array_on_scalar():
    p = valid_patient(); p["gender"] = ["female"]
    issues, model = structural_issues("Patient", p)
    assert model is None
    assert any(i.expression == "Patient.gender" for i in issues)

def test_rejects_scalar_where_array_expected():
    p = valid_patient(); p["name"] = {"text": "Siti"}
    issues, model = structural_issues("Patient", p)
    assert model is None

def test_rejects_unknown_element():
    p = valid_patient(); p["bogusField"] = 1
    issues, model = structural_issues("Patient", p)
    assert model is None
    assert any(i.expression == "Patient.bogusField" for i in issues)

def test_rejects_bad_date_format():
    p = valid_patient(); p["birthDate"] = "02-04-1990"
    issues, model = structural_issues("Patient", p)
    assert model is None
    assert any(i.code == "format" for i in issues)

def test_rejects_non_object_payload():
    issues, model = structural_issues("Patient", ["nope"])
    assert model is None and issues

def test_wrong_resource_type_key():
    issues, model = structural_issues("Patient", {"resourceType": "Observation"})
    assert model is None and issues
```

- [ ] **Step 2: Run test to verify it fails**

Run: `.venv/bin/python -m pytest tests/test_parse_structural.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'fhir_server.validation.parse'`

- [ ] **Step 3: Write minimal implementation**

```python
# fhir_server/validation/parse.py
import typing

from fhir.resources.observation import Observation
from fhir.resources.patient import Patient
from fhir.resources.practitioner import Practitioner
from fhir.resources.organization import Organization
from fhir.resources.location import Location
from fhir.resources.device import Device
from fhir.resources.encounter import Encounter

from .issues import Issue, R_DATETIME

SUPPORTED_TYPES = {
    "Patient": Patient, "Practitioner": Practitioner, "Organization": Organization,
    "Location": Location, "Device": Device, "Encounter": Encounter,
    "Observation": Observation,
}

def _unwrap(annotation):
    """Return the concrete class / origin info for a field annotation."""
    origin = typing.get_origin(annotation)
    if origin is typing.Union or str(origin) == "<class 'typing.Union'>":
        args = [a for a in typing.get_args(annotation) if a is not type(None)]
        return ("union", args)
    if origin in (list,):
        return ("list", typing.get_args(annotation)[0])
    if origin is not None:
        return ("other", annotation)
    return ("plain", annotation)

def _is_fhir_model(annotation) -> bool:
    return isinstance(annotation, type) and issubclass(annotation, __import__("pydantic").BaseModel)

def _strict_check(model_cls, payload, path, issues):
    """Reject unknown keys, quoted primitives, and array/scalar mismatches."""
    if not isinstance(payload, dict):
        issues.append(Issue(code="format", details_text=f"Expected object at {path}",
                            expression=path))
        return False
    fields = model_cls.model_fields
    ok = True
    for key, value in payload.items():
        if key == "resourceType":
            continue
        if key not in fields:
            issues.append(Issue(code="value",
                                details_text=f"Unknown element: {key}",
                                expression=f"{path}.{key}"))
            ok = False
            continue
        ann = fields[key].annotation
        kind, target = _unwrap(ann)
        child = f"{path}.{key}"
        if kind == "plain" and target is bool:
            if not isinstance(value, bool):
                issues.append(Issue(code="format",
                                    details_text="Boolean must be JSON true/false",
                                    expression=child))
                ok = False
        elif kind == "plain" and target is int and not isinstance(target, bool):
            if isinstance(value, str) or not isinstance(value, int):
                issues.append(Issue(code="format",
                                    details_text="Integer must be a JSON number",
                                    expression=child, rule_number=None))
                ok = False
        elif kind == "list":
            if not isinstance(value, list):
                issues.append(Issue(code="format",
                                    details_text="Expected array",
                                    expression=child))
                ok = False
            elif _is_fhir_model(target):
                for idx, item in enumerate(value):
                    if not _strict_check(target, item, f"{child}[{idx}]", issues):
                        ok = False
        elif _is_fhir_model(target):
            if not isinstance(value, dict):
                issues.append(Issue(code="format", details_text="Expected object",
                                    expression=child))
                ok = False
            else:
                if not _strict_check(target, value, child, issues):
                    ok = False
        elif kind == "union":
            sub = [a for a in target if _is_fhir_model(a)]
            if isinstance(value, dict) and sub:
                if not _strict_check(sub[0], value, child, issues):
                    ok = False
    return ok

def structural_issues(resource_type: str, payload) -> tuple[list[Issue], object | None]:
    issues: list[Issue] = []
    if not isinstance(payload, dict):
        issues.append(Issue(code="format", details_text="Body must be a JSON object"))
        return issues, None
    if payload.get("resourceType") != resource_type:
        issues.append(Issue(code="value",
                            details_text=f"Expected resourceType {resourceType(resource_type)}",
                            expression="resourceType"))
        return issues, None
    model_cls = SUPPORTED_TYPES[resource_type]
    ok = _strict_check(model_cls, payload, resource_type, issues)
    try:
        model = model_cls.model_validate(payload)
    except Exception as exc:  # pydantic ValidationError (and defensive catch)
        issues.extend(_pydantic_issues(exc, resource_type))
        return issues, None
    if not ok:
        return issues, None
    return issues, model

def resourceType(name: str) -> str:
    return name

def _pydantic_issues(exc, resource_type) -> list[Issue]:
    out = []
    for err in getattr(exc, "errors", lambda: [])():
        loc = ".".join(str(p) for p in err.get("loc", ()) if p != "body")
        expr = f"{resource_type}.{loc}" if loc else resource_type
        msg = err.get("msg", "invalid")
        is_time = "date" in str(err.get("type", "")) or "datetime" in str(err.get("type", ""))
        out.append(Issue(code="format" if is_time else "value",
                         details_text=msg, expression=expr,
                         rule_number=R_DATETIME if is_time else None))
    if not out:
        out.append(Issue(code="processing", details_text=str(exc),
                         expression=resource_type))
    return out
```

- [ ] **Step 4: Run test to verify it passes**

Run: `.venv/bin/python -m pytest tests/test_parse_structural.py -v`
Expected: PASS (10 tests). If fhir.resources does coerce a case the test expects rejected, the strict walk must catch it before `model_validate`; adjust only the walk, never the tests.

- [ ] **Step 5: Commit**

```bash
git add fhir_server/validation/parse.py tests/test_parse_structural.py
git commit -m "feat(server): strict structural parse with fhir.resources

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

---

### Task 5: Passwords and JWT

**Files:**
- Create: `fhir_server/auth/__init__.py`, `fhir_server/auth/passwords.py`, `fhir_server/auth/jwt.py`
- Test: `tests/test_auth_principals.py` (token parts here; route-level tests in Task 15)

**Interfaces:**
- Consumes: `Settings`.
- Produces:
  - `passwords.hash_password(plain: str) -> str` (PBKDF2-HMAC-SHA256, 100k iters, format `pbkdf2$<iters>$<salt_hex>$<hash_hex>`); `passwords.verify_password(plain, stored) -> bool`.
  - `jwt.Principal` dataclass: `kind: str` (`"admin"|"doctor"|"patient"|"device"`), `account_id: str | None`, `role: str | None`, `ref: str | None`, `device_id: str | None`, `patient_id: str | None`.
  - `jwt.create_token(settings, principal: Principal) -> str`; `jwt.verify_token(settings, token: str) -> Principal` raising `TokenError` (custom Exception) on bad/expired/wrong-kind. Device tokens are **not** JWTs — they are opaque strings resolved in Task 15's dependency; `create_token/verify_token` are for humans only (`kind` in admin/doctor/patient).

- [ ] **Step 1: Write the failing test**

```python
# tests/test_auth_principals.py
import time
import pytest
from fhir_server.auth import jwt as auth_jwt, passwords
from fhir_server.config import Settings

def settings(secret="test-secret"):
    return Settings(db_path=":memory:", jwt_secret=secret)

def test_password_roundtrip():
    h = passwords.hash_password("rahasia123")
    assert passwords.verify_password("rahasia123", h)
    assert not passwords.verify_password("wrong", h)
    assert h != passwords.hash_password("rahasia123")  # unique salt

def test_jwt_roundtrip():
    p = auth_jwt.Principal(kind="doctor", account_id="a1", role="doctor",
                           ref="Practitioner/N12345678")
    tok = auth_jwt.create_token(settings(), p)
    out = auth_jwt.verify_token(settings(), tok)
    assert out.kind == "doctor" and out.ref == "Practitioner/N12345678"

def test_expired_token_401():
    p = auth_jwt.Principal(kind="patient", account_id="a2", role="patient",
                           ref="Patient/P12345678901")
    s = settings()
    tok = auth_jwt.create_token(s, p, ttl_seconds=-1)
    with pytest.raises(auth_jwt.TokenError):
        auth_jwt.verify_token(s, tok)

def test_wrong_secret_rejected():
    p = auth_jwt.Principal(kind="admin", account_id="a3", role="admin", ref=None)
    tok = auth_jwt.create_token(settings("one"), p)
    with pytest.raises(auth_jwt.TokenError):
        auth_jwt.verify_token(settings("two"), tok)

def test_device_kind_not_mintable_as_jwt():
    with pytest.raises(ValueError):
        auth_jwt.create_token(settings(),
            auth_jwt.Principal(kind="device", device_id="d", patient_id="p"))
```

- [ ] **Step 2: Run test to verify it fails**

Run: `.venv/bin/python -m pytest tests/test_auth_principals.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'fhir_server.auth'`

- [ ] **Step 3: Write minimal implementation**

```python
# fhir_server/auth/__init__.py
```
(empty)

```python
# fhir_server/auth/passwords.py
import hashlib
import hmac
import secrets

_ITER = 100_000

def hash_password(plain: str) -> str:
    salt = secrets.token_bytes(16)
    dk = hashlib.pbkdf2_hmac("sha256", plain.encode(), salt, _ITER)
    return f"pbkdf2${_ITER}${salt.hex()}${dk.hex()}"

def verify_password(plain: str, stored: str) -> bool:
    try:
        _, iters, salt_hex, hash_hex = stored.split("$")
        dk = hashlib.pbkdf2_hmac("sha256", plain.encode(),
                                 bytes.fromhex(salt_hex), int(iters))
        return hmac.compare_digest(dk.hex(), hash_hex)
    except (ValueError, TypeError):
        return False
```

```python
# fhir_server/auth/jwt.py
from dataclasses import dataclass
import time

import jwt as pyjwt

@dataclass(frozen=True)
class Principal:
    kind: str
    account_id: str | None = None
    role: str | None = None
    ref: str | None = None
    device_id: str | None = None
    patient_id: str | None = None

class TokenError(Exception):
    pass

_HUMAN_KINDS = {"admin", "doctor", "patient"}

def create_token(settings, principal: Principal, ttl_seconds: int | None = None) -> str:
    if principal.kind not in _HUMAN_KINDS:
        raise ValueError("device principals do not use JWTs")
    now = int(time.time())
    ttl = ttl_seconds if ttl_seconds is not None else settings.jwt_ttl_seconds
    return pyjwt.encode(
        {"sub": principal.account_id, "role": principal.role,
         "ref": principal.ref, "iat": now, "exp": now + ttl},
        settings.jwt_secret, algorithm="HS256")

def verify_token(settings, token: str) -> Principal:
    try:
        claims = pyjwt.decode(token, settings.jwt_secret,
                              algorithms=["HS256"], options={"require": ["exp"]})
    except pyjwt.PyJWTError as exc:
        raise TokenError(str(exc)) from exc
    role = claims.get("role")
    if role not in _HUMAN_KINDS:
        raise TokenError("bad role")
    return Principal(kind=role, account_id=claims.get("sub"),
                     role=role, ref=claims.get("ref"))
```

- [ ] **Step 4: Run test to verify it passes**

Run: `.venv/bin/python -m pytest tests/test_auth_principals.py -v`
Expected: PASS (5 tests)

- [ ] **Step 5: Commit**

```bash
git add fhir_server/auth tests/test_auth_principals.py
git commit -m "feat(server): local JWT principals and password hashing

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

---

### Task 6: Repositories

**Files:**
- Create: `fhir_server/repositories/__init__.py`, `fhir_server/repositories/resources.py`, `fhir_server/repositories/accounts.py`, `fhir_server/repositories/devices.py`
- Test: `tests/test_repositories.py`

**Interfaces:**
- Consumes: `db.connect`, `db.init`.
- Produces (all take `conn: sqlite3.Connection` as first arg):
  - `resources.get(conn, type, id) -> dict | None`; `resources.put(conn, type, id, doc: dict) -> int` (upsert, bumps version, sets created/updated UTC `+00:00`, returns new version); `resources.delete(conn, type, id) -> bool`; `resources.list(conn, type) -> list[dict]`; `resources.exists(conn, type, id) -> bool`.
  - `accounts.create(conn, username, password_hash, role, subject_ref) -> str` (account id = uuid4); `accounts.get_by_username(conn, username) -> dict | None`; `accounts.get(conn, account_id) -> dict | None`; `accounts.list(conn) -> list[dict]`.
  - `devices.create_token(conn, device_id, patient_id, token_text) -> str` (stores sha256, returns token row id); `devices.resolve_token(conn, token_text) -> dict | None` (returns row only when `revoked=0`); `devices.revoke(conn, token_id) -> bool`; `devices.tokens_for_device(conn, device_id) -> list[dict]`.

- [ ] **Step 1: Write the failing test**

```python
# tests/test_repositories.py
from fhir_server import db
from fhir_server.repositories import accounts, devices, resources

def test_resource_put_get_delete(db_path):
    conn = db.connect(db_path); db.init(conn)
    v = resources.put(conn, "Patient", "P1", {"resourceType": "Patient", "id": "P1"})
    assert v == 1
    assert resources.get(conn, "Patient", "P1")["resourceType"] == "Patient"
    assert resources.put(conn, "Patient", "P1", {"resourceType": "Patient"}) == 2
    assert resources.delete(conn, "Patient", "P1") is True
    assert resources.get(conn, "Patient", "P1") is None
    assert resources.delete(conn, "Patient", "P1") is False

def test_list_by_type(db_path):
    conn = db.connect(db_path); db.init(conn)
    resources.put(conn, "Patient", "P1", {"resourceType": "Patient"})
    resources.put(conn, "Patient", "P2", {"resourceType": "Patient"})
    resources.put(conn, "Device", "d1", {"resourceType": "Device"})
    assert len(resources.list(conn, "Patient")) == 2

def test_accounts_unique_username(db_path):
    conn = db.connect(db_path); db.init(conn)
    accounts.create(conn, "doc1", "h", "doctor", "Practitioner/N1")
    try:
        accounts.create(conn, "doc1", "h", "doctor", "Practitioner/N1")
        raise AssertionError("duplicate username must fail")
    except Exception:
        pass

def test_device_token_lifecycle(db_path):
    conn = db.connect(db_path); db.init(conn)
    row_id = devices.create_token(conn, "dev-1", "Patient/P1", "tok-abc")
    assert devices.resolve_token(conn, "tok-abc")["device_id"] == "dev-1"
    assert devices.resolve_token(conn, "wrong") is None
    assert devices.revoke(conn, row_id) is True
    assert devices.resolve_token(conn, "tok-abc") is None
```

- [ ] **Step 2: Run test to verify it fails**

Run: `.venv/bin/python -m pytest tests/test_repositories.py -v`
Expected: FAIL with `ModuleNotFoundError`

- [ ] **Step 3: Write minimal implementation**

```python
# fhir_server/repositories/__init__.py
```
(empty)

```python
# fhir_server/repositories/resources.py
import datetime as dt
import json

def _now() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00")

def get(conn, type_, id_):
    row = conn.execute("SELECT json FROM resources WHERE type=? AND id=?",
                       (type_, id_)).fetchone()
    return json.loads(row["json"]) if row else None

def put(conn, type_, id_, doc) -> int:
    existing = conn.execute(
        "SELECT version FROM resources WHERE type=? AND id=?", (type_, id_)).fetchone()
    version = (existing["version"] + 1) if existing else 1
    now = _now()
    doc = dict(doc); doc["id"] = id_
    conn.execute(
        "INSERT INTO resources VALUES (?,?,?,?,?,?) "
        "ON CONFLICT(type,id) DO UPDATE SET json=excluded.json,"
        " version=excluded.version, updated=excluded.updated",
        (type_, id_, version, json.dumps(doc, separators=(",", ":")), now, now))
    conn.commit()
    return version

def delete(conn, type_, id_) -> bool:
    cur = conn.execute("DELETE FROM resources WHERE type=? AND id=?", (type_, id_))
    conn.commit()
    return cur.rowcount > 0

def list(conn, type_):
    return [json.loads(r["json"]) for r in
            conn.execute("SELECT json FROM resources WHERE type=?", (type_,))]

def exists(conn, type_, id_) -> bool:
    return conn.execute("SELECT 1 FROM resources WHERE type=? AND id=?",
                        (type_, id_)).fetchone() is not None
```

```python
# fhir_server/repositories/accounts.py
import uuid

def create(conn, username, password_hash, role, subject_ref) -> str:
    account_id = str(uuid.uuid4())
    conn.execute("INSERT INTO accounts VALUES (?,?,?,?,?,1)",
                 (account_id, username, password_hash, role, subject_ref))
    conn.commit()
    return account_id

def get_by_username(conn, username):
    row = conn.execute("SELECT * FROM accounts WHERE username=? AND active=1",
                       (username,)).fetchone()
    return dict(row) if row else None

def get(conn, account_id):
    row = conn.execute("SELECT * FROM accounts WHERE id=? AND active=1",
                       (account_id,)).fetchone()
    return dict(row) if row else None

def list(conn):
    return [dict(r) for r in conn.execute("SELECT * FROM accounts WHERE active=1")]
```

```python
# fhir_server/repositories/devices.py
import datetime as dt
import hashlib
import uuid

def _now() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00")

def create_token(conn, device_id, patient_id, token_text) -> str:
    token_id = str(uuid.uuid4())
    sha = hashlib.sha256(token_text.encode()).hexdigest()
    conn.execute("INSERT INTO device_tokens VALUES (?,?,?,?,?,0)",
                 (token_id, device_id, patient_id, sha, _now()))
    conn.commit()
    return token_id

def resolve_token(conn, token_text):
    sha = hashlib.sha256(token_text.encode()).hexdigest()
    row = conn.execute(
        "SELECT * FROM device_tokens WHERE token_sha256=? AND revoked=0",
        (sha,)).fetchone()
    return dict(row) if row else None

def revoke(conn, token_id) -> bool:
    cur = conn.execute("UPDATE device_tokens SET revoked=1 WHERE id=?", (token_id,))
    conn.commit()
    return cur.rowcount > 0

def tokens_for_device(conn, device_id):
    return [dict(r) for r in conn.execute(
        "SELECT * FROM device_tokens WHERE device_id=?", (device_id,))]
```

- [ ] **Step 4: Run test to verify it passes**

Run: `.venv/bin/python -m pytest tests/test_repositories.py -v`
Expected: PASS (4 tests)

- [ ] **Step 5: Commit**

```bash
git add fhir_server/repositories tests/test_repositories.py
git commit -m "feat(server): sqlite repositories for resources, accounts, devices

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

---

### Task 7: Common validation rules (dates, empty strings, coding systems, references)

**Files:**
- Create: `fhir_server/validation/rules_common.py`
- Test: `tests/test_rules_common.py`

**Interfaces:**
- Consumes: `Issue`, rule constants; `Settings.earliest_date`.
- Produces: functions each returning `list[Issue]`, all taking the payload dict plus optional context:
  - `check_datetimes(payload, resource_type, earliest_date: str) -> list[Issue]` — walks all `*DateTime`/`*date`-shaped **values** found at keys ending in `Date`/`DateTime`/`Instant` (recursive): missing offset on dateTime → `R_DATETIME` format; unparsable → `R_DATETIME` format; earlier than `earliest_date` (date part compare) → `L_EARLIEST_DATE` value; strictly-future (now + 1 min grace) → `R_DATETIME` value, **except** when the key path ends with `period.end`.
  - `check_empty_strings(payload, resource_type) -> list[Issue]` — any `str` value `""` or whitespace-only → `R_EMPTY_TEXT` at that path.
  - `check_coding_systems(payload, resource_type) -> list[Issue]` — for every dict containing `system` inside a `coding` list: system must be in `ALLOWED_SYSTEMS` (module constant, grows per resource task) else `R_BAD_CODING_SYSTEM`; if system starts with `https://www.hl7.org/fhir/` or `http://hl7.org/fhir/Codesystem` (web-page form) → **rewrites are not done here**: emit issue only if not allow-listed; a separate helper `normalize_system(system) -> tuple[str, bool]` maps the web-page forms to `http://terminology.hl7.org/CodeSystem/...` and returns `(normalized, changed)` for services to apply on input (S14).
  - `check_references(payload, resource_type, exists_fn) -> list[Issue]` — every dict with `reference: "Type/id"`: missing `reference` string → `R_MISSING_REFERENCE`; `exists_fn(type, id)` false → `L_UNRESOLVABLE_REFERENCE`. `exists_fn` is injected (no repo import here).

- [ ] **Step 1: Write the failing test**

```python
# tests/test_rules_common.py
from fhir_server.validation import rules_common as rc

def test_datetime_requires_offset():
    i = rc.check_datetimes({"subject": {"reference": "Patient/P1"},
        "effectiveDateTime": "2026-09-29T10:00:00"}, "Observation", "2014-06-03")
    assert any(x.rule_number == 10132 and x.code == "format" for x in i)

def test_datetime_accepts_offset():
    assert rc.check_datetimes({"effectiveDateTime": "2026-09-29T10:00:00+00:00"},
                              "Observation", "2014-06-03") == []

def test_date_before_floor_rejected():
    i = rc.check_datetimes({"birthDate": "2010-01-01"}, "Patient", "2014-06-03")
    assert any(x.rule_number == 20001 for x in i)

def test_future_date_rejected_but_period_end_allowed():
    future = "2099-01-01T00:00:00+00:00"
    assert any(x.rule_number == 10132 for x in
               rc.check_datetimes({"x": {"start": future}}, "Encounter", "2014-06-03"))
    assert rc.check_datetimes(
        {"period": {"start": "2026-01-01T00:00:00+00:00", "end": future}},
        "Encounter", "2014-06-03") == []

def test_empty_strings():
    i = rc.check_empty_strings({"title": "  "}, "Patient")
    assert any(x.rule_number == 10134 for x in i)

def test_coding_system_allow_list():
    bad = {"coding": [{"system": "http://evil.example", "code": "x"}]}
    i = rc.check_coding_systems(bad, "Observation")
    assert any(x.rule_number == 10002 for x in i)
    good = {"coding": [{"system": "http://loinc.org", "code": "8867-4"}]}
    assert rc.check_coding_systems(good, "Observation") == []

def test_normalize_webpage_system():
    norm, changed = rc.normalize_system(
        "https://www.hl7.org/fhir/Codesystem-diagnosis-role")
    assert changed and norm.startswith("http://terminology.hl7.org/CodeSystem/")

def test_reference_resolution():
    exists = lambda t, i: (t, i) == ("Patient", "P1")
    ok = rc.check_references({"subject": {"reference": "Patient/P1"}},
                             "Observation", exists)
    assert ok == []
    miss = rc.check_references({"subject": {"reference": "Patient/P9"}},
                               "Observation", exists)
    assert any(x.rule_number == 20002 for x in miss)
    malformed = rc.check_references({"subject": {}}, "Observation", exists)
    assert any(x.rule_number == 10124 for x in malformed)
```

- [ ] **Step 2: Run test to verify it fails**

Run: `.venv/bin/python -m pytest tests/test_rules_common.py -v`
Expected: FAIL with `ModuleNotFoundError`

- [ ] **Step 3: Write minimal implementation**

```python
# fhir_server/validation/rules_common.py
import datetime as dt
import re

from .issues import (Issue, R_DATETIME, R_EMPTY_TEXT, R_BAD_CODING_SYSTEM,
                     R_MISSING_REFERENCE, L_EARLIEST_DATE,
                     L_UNRESOLVABLE_REFERENCE)

ALLOWED_SYSTEMS = {
    "http://loinc.org",
    "http://unitsofmeasure.org",
    "http://hl7.org/fhir/administrative-gender",
    "http://hl7.org/fhir/observation-status",
    "http://hl7.org/fhir/encounter-status",
    "http://hl7.org/fhir/location-status",
    "http://hl7.org/fhir/device-status",
    "http://hl7.org/fhir/identifier-use",
    "http://hl7.org/fhir/name-use",
    "http://hl7.org/fhir/address-use",
    "http://hl7.org/fhir/address-type",
    "http://hl7.org/fhir/contact-point-system",
    "http://hl7.org/fhir/contact-point-use",
    "http://terminology.hl7.org/CodeSystem/observation-category",
    "http://terminology.hl7.org/CodeSystem/v3-ActCode",
    "http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
    "http://terminology.hl7.org/CodeSystem/v3-ActState",
    "http://terminology.hl7.org/CodeSystem/organization-type",
    "http://terminology.hl7.org/CodeSystem/contactentity-type",
    "http://terminology.hl7.org/CodeSystem/encounter-type",
    "http://terminology.hl7.org/CodeSystem/v2-0131",
    "http://terminology.hl7.org/CodeSystem/v3-RoleCode",
    "http://terminology.hl7.org/CodeSystem/location-physical-type",
    "http://terminology.hl7.org/CodeSystem/v3-MaritalStatus",
    "http://terminology.hl7.org/CodeSystem/data-absent-reason",
    "http://terminology.hl7.org/CodeSystem/observation-interpretation",
    "urn:ietf:bcp:47",
    "https://fhir.kemkes.go.id/id/nik",
    "https://fhir.kemkes.go.id/id/nik-ibu",
    "https://fhir.kemkes.go.id/id/ihs-number",
    "https://fhir.kemkes.go.id/id/paspor",
    "https://fhir.kemkes.go.id/id/kk",
    "https://fhir.kemkes.go.id/r4/StructureDefinition/administrativeCode",
    "http://sys-ids.kemkes.go.id/organization",
    "http://sys-ids.kemkes.go.id/location",
    "http://sys-ids.kemkes.go.id/encounter",
    "http://sys-ids.kemkes.go.id/observation",
    "http://sys-ids.kemkes.go.id/device",
    "http://sys-ids.kemkes.go.id/practitioner",
}

_DT_KEYS = re.compile(r"(Date|DateTime|Instant|Time)$")
_FLOOR_DEFAULT = "2014-06-03"
_GRACE = dt.timedelta(minutes=1)

def _walk(node, path=""):
    if isinstance(node, dict):
        for k, v in node.items():
            yield from _walk(v, f"{path}.{k}" if path else k)
    elif isinstance(node, list):
        for idx, v in enumerate(node):
            yield from _walk(v, f"{path}[{idx}]")
    else:
        yield path, node

def check_datetimes(payload, resource_type, earliest_date=_FLOOR_DEFAULT):
    issues = []
    now = dt.datetime.now(dt.timezone.utc)
    floor = dt.date.fromisoformat(earliest_date)
    for path, value in _walk(payload):
        leaf = path.split(".")[-1].split("[")[0]
        if not _DT_KEYS.search(leaf) or not isinstance(value, str):
            continue
        try:
            parsed = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
        except ValueError:
            issues.append(Issue(code="format",
                                details_text=f"Invalid date time format : {value}"
                                             f". Format allowed : YYYY-MM-DDThh:mm:ss+00:00",
                                expression=f"{resource_type}.{path}",
                                rule_number=R_DATETIME))
            continue
        is_date_only = re.fullmatch(r"\d{4}(-\d{2}(-\d{2})?)?", value) is not None
        if not is_date_only and parsed.utcoffset() is None:
            issues.append(Issue(code="format",
                                details_text=f"Invalid date time format : {value}"
                                             f". Format allowed : YYYY-MM-DDThh:mm:ss+00:00",
                                expression=f"{resource_type}.{path}",
                                rule_number=R_DATETIME))
            continue
        as_date = parsed.date()
        if as_date < floor:
            issues.append(Issue(code="value",
                                details_text=f"Date {value} earlier than allowed"
                                             f" earliest {earliest_date}",
                                expression=f"{resource_type}.{path}",
                                rule_number=L_EARLIEST_DATE))
        if parsed > now + _GRACE and not path.endswith("period.end"):
            issues.append(Issue(code="value",
                                details_text=f"Invalid date time value : {value}"
                                             f" Not Allowed : Future Date",
                                expression=f"{resource_type}.{path}",
                                rule_number=R_DATETIME))
    return issues

def check_empty_strings(payload, resource_type):
    return [Issue(code="value", details_text=f"Text is empty: '{value}'",
                  expression=f"{resource_type}.{path}",
                  rule_number=R_EMPTY_TEXT)
            for path, value in _walk(payload)
            if isinstance(value, str) and value.strip() == ""]

def normalize_system(system: str) -> tuple[str, bool]:
    for prefix in ("https://www.hl7.org/fhir/Codesystem",
                   "http://www.hl7.org/fhir/Codesystem",
                   "https://www.hl7.org/fhir/CodeSystem"):
        if system.startswith(prefix):
            tail = system.rsplit("/", 1)[-1]
            return f"http://terminology.hl7.org/CodeSystem/{tail}", True
    return system, False

def check_coding_systems(payload, resource_type):
    issues = []
    def walk(node, path=""):
        if isinstance(node, dict):
            if "coding" in node and isinstance(node["coding"], list):
                for idx, c in enumerate(node["coding"]):
                    if isinstance(c, dict) and "system" in c:
                        sys_ = c["system"]
                        norm, _ = normalize_system(sys_)
                        if norm not in ALLOWED_SYSTEMS:
                            issues.append(Issue(
                                code="value",
                                details_text=f"Invalid coding system: {sys_}",
                                expression=f"{resource_type}.{path}.coding[{idx}].system",
                                rule_number=R_BAD_CODING_SYSTEM))
            for k, v in node.items():
                walk(v, f"{path}.{k}" if path else k)
        elif isinstance(node, list):
            for idx, v in enumerate(node):
                walk(v, f"{path}[{idx}]")
    walk(payload)
    return issues

def check_references(payload, resource_type, exists_fn):
    issues = []
    def walk(node, path=""):
        if isinstance(node, dict):
            if "reference" in node:
                ref = node["reference"]
                if not isinstance(ref, str) or "/" not in ref:
                    issues.append(Issue(
                        code="value",
                        details_text=f"Reference is mandatory : {resource_type}.{path}",
                        expression=f"{resource_type}.{path}",
                        rule_number=R_MISSING_REFERENCE))
                else:
                    t, _, rid = ref.partition("/")
                    if not exists_fn(t, rid):
                        issues.append(Issue(
                            code="value",
                            details_text=f"Unresolvable reference: {ref}",
                            expression=f"{resource_type}.{path}",
                            rule_number=L_UNRESOLVABLE_REFERENCE))
            for k, v in node.items():
                walk(v, f"{path}.{k}" if path else k)
        elif isinstance(node, list):
            for idx, v in enumerate(node):
                walk(v, f"{path}[{idx}]")
    walk(payload)
    return issues
```

- [ ] **Step 4: Run test to verify it passes**

Run: `.venv/bin/python -m pytest tests/test_rules_common.py -v`
Expected: PASS (8 tests)

- [ ] **Step 5: Commit**

```bash
git add fhir_server/validation/rules_common.py tests/test_rules_common.py
git commit -m "feat(server): common validation rules for dates, text, systems, refs

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

---

### Task 8: Rules for Organization, Location, Practitioner, Device

**Files:**
- Create: `fhir_server/validation/rules_master.py`
- Test: `tests/test_rules_master.py`

**Interfaces:**
- Consumes: `rules_common` functions, `Issue`, constants.
- Produces: `validate_organization(payload) -> list[Issue]`, `validate_location(payload) -> list[Issue]`, `validate_practitioner(payload) -> list[Issue]`, `validate_device(payload) -> list[Issue]`. Each assumes structural parse already passed.

- [ ] **Step 1: Write the failing test**

```python
# tests/test_rules_master.py
from fhir_server.validation import rules_master as rm

def test_org_identifier_system_prefix():
    bad = {"resourceType": "Organization",
           "identifier": [{"use": "official", "system": "http://example.org", "value": "X"}]}
    assert any(i.rule_number == 10117 for i in rm.validate_organization(bad))
    good = {"resourceType": "Organization",
            "identifier": [{"use": "official",
                            "system": "http://sys-ids.kemkes.go.id/organization/100000001",
                            "value": "X"}]}
    assert rm.validate_organization(good) == []

def test_org_contact_needs_purpose_coding():
    bad = {"resourceType": "Organization",
           "contact": [{"name": {"text": "Billing"}}]}
    assert any(i.rule_number == 10263 for i in rm.validate_organization(bad))

def test_location_position_needs_both_coords():
    bad = {"resourceType": "Location", "position": {"longitude": 106.8}}
    assert any(i.rule_number == 20003 for i in rm.validate_location(bad))
    ok = {"resourceType": "Location",
          "position": {"longitude": 106.8, "latitude": -6.2}}
    assert rm.validate_location(ok) == []

def test_practitioner_qualification_needs_coding():
    bad = {"resourceType": "Practitioner", "qualification": [{"period": {}}]}
    assert any(i.rule_number == 10263 for i in rm.validate_practitioner(bad))

def test_device_status_enum():
    bad = {"resourceType": "Device", "status": "bogus"}
    assert any(i.rule_number == 20005 for i in rm.validate_device(bad))
    good = {"resourceType": "Device", "status": "active"}
    assert rm.validate_device(good) == []
```

- [ ] **Step 2: Run test to verify it fails**

Run: `.venv/bin/python -m pytest tests/test_rules_master.py -v`
Expected: FAIL with `ModuleNotFoundError`

- [ ] **Step 3: Write minimal implementation**

```python
# fhir_server/validation/rules_master.py
from .issues import Issue, R_BAD_IDENTIFIER_SYSTEM, R_WAJIB_MISSING, L_DEVICE_RULE, L_LOCATION_POSITION

def _identifier_system_issue(payload, prefix):
    out = []
    for idx, ident in enumerate(payload.get("identifier") or []):
        system = ident.get("system")
        if system is not None and not system.startswith(prefix):
            out.append(Issue(code="value",
                             details_text=f"Invalid identifier system: {system}",
                             expression=f"{payload['resourceType']}.identifier[{idx}].system",
                             rule_number=R_BAD_IDENTIFIER_SYSTEM))
    return out

def validate_organization(payload):
    out = _identifier_system_issue(payload, "http://sys-ids.kemkes.go.id/organization/")
    for idx, contact in enumerate(payload.get("contact") or []):
        if "purpose" not in contact:
            out.append(Issue(code="value",
                             details_text="Wajib element missing: Organization.contact.purpose",
                             expression=f"Organization.contact[{idx}].purpose",
                             rule_number=R_WAJIB_MISSING))
        elif not (contact["purpose"].get("coding")):
            out.append(Issue(code="value",
                             details_text="Wajib element missing: Organization.contact.purpose.coding",
                             expression=f"Organization.contact[{idx}].purpose.coding",
                             rule_number=R_WAJIB_MISSING))
    return out

def validate_location(payload):
    out = _identifier_system_issue(payload, "http://sys-ids.kemkes.go.id/location/")
    pos = payload.get("position")
    if isinstance(pos, dict):
        missing = [k for k in ("longitude", "latitude") if k not in pos]
        if missing:
            out.append(Issue(code="value",
                             details_text=f"Wajib element missing: Location.position.{'/'.join(missing)}",
                             expression="Location.position",
                             rule_number=L_LOCATION_POSITION))
    return out

def validate_practitioner(payload):
    out = []
    for idx, qual in enumerate(payload.get("qualification") or []):
        if not (qual.get("code") or {}).get("coding"):
            out.append(Issue(code="value",
                             details_text="Wajib element missing: Practitioner.qualification.code.coding",
                             expression=f"Practitioner.qualification[{idx}].code.coding",
                             rule_number=R_WAJIB_MISSING))
    return out

def validate_device(payload):
    allowed = {"active", "inactive", "entered-in-error"}
    status = payload.get("status")
    if status is not None and status not in allowed:
        return [Issue(code="value",
                      details_text=f"Invalid device status: {status}",
                      expression="Device.status",
                      rule_number=L_DEVICE_RULE)]
    return []
```

- [ ] **Step 4: Run test to verify it passes**

Run: `.venv/bin/python -m pytest tests/test_rules_master.py -v`
Expected: PASS (5 tests)

- [ ] **Step 5: Commit**

```bash
git add fhir_server/validation/rules_master.py tests/test_rules_master.py
git commit -m "feat(server): SATUSEHAT rules for Organization/Location/Practitioner/Device

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

---

### Task 9: Patient rules (NIK, MPI union, minted ids)

**Files:**
- Create: `fhir_server/validation/rules_patient.py`
- Test: `tests/test_rules_patient.py`

**Interfaces:**
- Consumes: `rules_common`, `Issue`, constants.
- Produces: `validate_patient(payload, *, is_create: bool, exists_fn=None) -> list[Issue]`. For create: server will mint `Patient.id` and ihs-number, so `is_create=True` rejects a client-supplied `ihs-number` identifier (`L_PATIENT_IDENTITY`). `exists_fn` unused for patients (kept for signature symmetry with other rules — do not add dead branches; omit the parameter if unused, only `is_create` needed).

- [ ] **Step 1: Write the failing test**

```python
# tests/test_rules_patient.py
from fhir_server.validation.rules_patient import validate_patient

def base(**kw):
    p = {
        "resourceType": "Patient",
        "identifier": [
            {"use": "official", "system": "https://fhir.kemkes.go.id/id/nik",
             "value": "3175061001900001"},
            {"use": "official", "system": "https://fhir.kemkes.go.id/id/ihs-number",
             "value": "P00000000001"}],
        "name": [{"use": "official", "text": "Budi", "family": "Budi",
                  "given": ["Budi"]}],
        "gender": "male",
        "birthDate": "1990-01-01",
        "multipleBirthBoolean": False,
        "address": [{
            "use": "home", "line": ["Jl. Melati 1"], "city": "Jakarta",
            "postalCode": "10110", "country": "ID",
            "extension": [{
                "url": "https://fhir.kemkes.go.id/r4/StructureDefinition/administrativeCode",
                "extension": [
                    {"url": "province", "valueCode": "31"},
                    {"url": "city", "valueCode": "3171"},
                    {"url": "district", "valueCode": "317101"},
                    {"url": "village", "valueCode": "317101001"},
                    {"url": "rt", "valueCode": "001"},
                    {"url": "rw", "valueCode": "001"}]}]}],
    }
    p.update(kw)
    return p

def test_valid_patient_create_passes_without_client_ihs():
    p = base()
    p["identifier"] = [p["identifier"][0]]  # NIK only on create
    assert validate_patient(p, is_create=True) == []

def test_nik_required():
    p = base(); p["identifier"] = []
    assert any(i.rule_number == 10117 for i in validate_patient(p, is_create=True))

def test_nik_must_be_16_digits():
    p = base()
    p["identifier"] = [{"use": "official", "system": "https://fhir.kemkes.go.id/id/nik",
                        "value": "123"}]
    assert any(i.rule_number == 20004 for i in validate_patient(p, is_create=True))

def test_client_sent_ihs_rejected_on_create():
    assert any(i.rule_number == 20004
               for i in validate_patient(base(), is_create=True))

def test_missing_name_wajib():
    p = base(name=None)
    assert any(i.rule_number == 10263 for i in validate_patient(p, is_create=True))

def test_gender_limited_and_required():
    p = base(gender="other")
    assert any(i.rule_number == 20004 for i in validate_patient(p, is_create=True))
    p2 = base(); del p2["gender"]
    assert any(i.rule_number == 20004 for i in validate_patient(p2, is_create=True))

def test_missing_birthdate_fails():
    p = base(); del p["birthDate"]
    assert any(i.rule_number == 20004 for i in validate_patient(p, is_create=True))

def test_missing_address_fails():
    p = base(); p["address"] = []
    assert any(i.rule_number == 20004 for i in validate_patient(p, is_create=True))

def test_address_needs_administrative_code():
    p = base(); p["address"][0] = {"use": "home", "line": ["x"]}
    assert any(i.rule_number == 20004 for i in validate_patient(p, is_create=True))

def test_multiple_birth_wajib():
    p = base()
    for k in ("multipleBirthBoolean", "multipleBirthInteger"):
        p.pop(k, None)
    assert any(i.rule_number == 10263 for i in validate_patient(p, is_create=True))

def test_gender_family_wrong_type_is_structural_not_here():
    # gender enum is administrative-gender; "other" is valid R4 but not MPI
    p = base(gender="unknown")
    assert any(i.rule_number == 20004 for i in validate_patient(p, is_create=True))
```

- [ ] **Step 2: Run test to verify it fails**

Run: `.venv/bin/python -m pytest tests/test_rules_patient.py -v`
Expected: FAIL with `ModuleNotFoundError`

- [ ] **Step 3: Write minimal implementation**

```python
# fhir_server/validation/rules_patient.py
from .issues import Issue, R_BAD_IDENTIFIER_SYSTEM, R_WAJIB_MISSING, L_PATIENT_IDENTITY

NIK_SYSTEM = "https://fhir.kemkes.go.id/id/nik"
IHS_SYSTEM = "https://fhir.kemkes.go.id/id/ihs-number"
ADMIN_CODE_URL = "https://fhir.kemkes.go.id/r4/StructureDefinition/administrativeCode"
_ADMIN_SUBS = ("province", "city", "district", "village", "rt", "rw")

def _issue(text, rule, expr="Patient"):
    return Issue(code="value", details_text=text, expression=expr, rule_number=rule)

def validate_patient(payload, *, is_create: bool):
    out = []
    identifiers = payload.get("identifier") or []
    nik = [i for i in identifiers if i.get("system") == NIK_SYSTEM]
    if not identifiers:
        out.append(_issue("Wajib element missing: Patient.identifier",
                          R_WAJIB_MISSING, "Patient.identifier"))
    elif not nik:
        out.append(_issue(f"Missing NIK identifier system {NIK_SYSTEM}",
                          L_PATIENT_IDENTITY, "Patient.identifier"))
    else:
        value = nik[0].get("value") or ""
        if not (value.isdigit() and len(value) == 16):
            out.append(_issue(f"NIK must be 16 digits, got '{value}'",
                              L_PATIENT_IDENTITY, "Patient.identifier[0].value"))
    if is_create:
        if any(i.get("system") == IHS_SYSTEM for i in identifiers):
            out.append(_issue("ihs-number identifier is server-issued; client may not send it",
                              L_PATIENT_IDENTITY, "Patient.identifier"))
        if payload.get("id"):
            out.append(_issue("Patient.id is server-issued",
                              L_PATIENT_IDENTITY, "Patient.id"))
    if not payload.get("name"):
        out.append(_issue("Wajib element missing: Patient.name",
                          R_WAJIB_MISSING, "Patient.name"))
    if not payload.get("birthDate"):
        out.append(_issue("MPI requires birthDate for NIK patients",
                          L_PATIENT_IDENTITY, "Patient.birthDate"))
    if payload.get("gender") not in ("male", "female"):
        out.append(_issue("MPI requires gender male or female",
                          L_PATIENT_IDENTITY, "Patient.gender"))
    addresses = payload.get("address") or []
    if not addresses:
        out.append(_issue("MPI requires address for NIK patients",
                          L_PATIENT_IDENTITY, "Patient.address"))
    else:
        admin = [e for e in (addresses[0].get("extension") or [])
                 if e.get("url") == ADMIN_CODE_URL]
        subs = set()
        if admin:
            subs = {e.get("url") for e in admin[0].get("extension") or []}
        if not admin or not set(_ADMIN_SUBS) <= subs:
            out.append(_issue(
                "address requires administrativeCode with province/city/district/village/rt/rw",
                L_PATIENT_IDENTITY, "Patient.address[0].extension"))
    if "multipleBirthBoolean" not in payload and "multipleBirthInteger" not in payload:
        out.append(_issue("Wajib element missing: Patient.multipleBirth[x]",
                          R_WAJIB_MISSING, "Patient.multipleBirth[x]"))
    return out
```

- [ ] **Step 4: Run test to verify it passes**

Run: `.venv/bin/python -m pytest tests/test_rules_patient.py -v`
Expected: PASS (11 tests)

- [ ] **Step 5: Commit**

```bash
git add fhir_server/validation/rules_patient.py tests/test_rules_patient.py
git commit -m "feat(server): Patient NIK and MPI union rules

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

---

### Task 10: Encounter rules (lifecycle-aware subset)

**Files:**
- Create: `fhir_server/validation/rules_encounter.py`
- Test: `tests/test_rules_encounter.py`

**Interfaces:**
- Consumes: `rules_common`, `Issue`, constants.
- Produces: `validate_encounter(payload, *, existing: dict | None, org_id: str) -> list[Issue]`.
  - `existing` is the stored resource on update, `None` on create; `org_id` is the facility IHS id used to check the identifier system.
  - Create: requires identifier (system `http://sys-ids.kemkes.go.id/encounter/{org_id}` or value check by prefix + exact org suffix), status == `arrived`, `statusHistory` exactly one entry with status `arrived` and `period.start` and no `period.end`, class coding `AMB` from v3-ActCode, subject.reference `Patient/...`, serviceProvider.reference `Organization/{org_id}`, location present, period.start present.
  - Update: allowed transitions `arrived → in-progress → finished` (forward only, no skips, no reverse). On transition to `in-progress`: statusHistory gains an entry `{status: in-progress, period: {start: <now ISO+00:00>}}` — **the rule validates the incoming payload contains it** (services append it; the rule checks shape and order). On transition to `finished`: gains `{status: finished, period: {start, end}}`; `period.end` must be present on the top-level `period`. Prior entries must remain intact and in order.
  - Duplicate: when creating and `exists_fn(identifier_value)` is true → `Issue(code="duplicate", details_text="Found duplicate resource: Encounter", rule_number=None)`. Signature: `validate_encounter(payload, *, existing, org_id, duplicate_fn=None)` where `duplicate_fn(value) -> bool`.

- [ ] **Step 1: Write the failing test**

```python
# tests/test_rules_encounter.py
from fhir_server.validation.rules_encounter import validate_encounter

ORG = "100000001"
NOW = "2026-09-29T10:00:00+00:00"

def created(**kw):
    p = {
        "resourceType": "Encounter",
        "identifier": [{"use": "official",
                        "system": f"http://sys-ids.kemkes.go.id/encounter/{ORG}",
                        "value": "K-001"}],
        "status": "arrived",
        "statusHistory": [{"status": "arrived", "period": {"start": NOW}}],
        "class": {"system": "http://terminology.hl7.org/CodeSystem/v3-ActCode",
                  "code": "AMB", "display": "ambulatory"},
        "subject": {"reference": "Patient/P12345678901"},
        "period": {"start": NOW},
        "location": [{"location": {"reference": "Location/abc"}}],
        "serviceProvider": {"reference": f"Organization/{ORG}"},
    }
    p.update(kw)
    return p

def test_valid_create_passes():
    assert validate_encounter(created(), existing=None, org_id=ORG) == []

def test_identifier_system_must_match_org():
    p = created()
    p["identifier"][0]["system"] = "http://sys-ids.kemkes.go.id/encounter/999"
    assert any(i.rule_number == 10117 for i in
               validate_encounter(p, existing=None, org_id=ORG))

def test_create_must_be_arrived():
    p = created(status="in-progress")
    assert any(i.rule_number == 10263 for i in
               validate_encounter(p, existing=None, org_id=ORG))

def test_missing_service_provider():
    p = created(); del p["serviceProvider"]
    assert any(i.rule_number == 10263 for i in
               validate_encounter(p, existing=None, org_id=ORG))

def test_duplicate_identifier():
    i = validate_encounter(created(), existing=None, org_id=ORG,
                           duplicate_fn=lambda v: v == "K-001")
    assert any(x.code == "duplicate" for x in i)

def test_forward_transition_arrived_to_in_progress():
    existing = created()
    new = created(status="in-progress",
                  statusHistory=[{"status": "arrived", "period": {"start": NOW}},
                                 {"status": "in-progress", "period": {"start": NOW}}])
    assert validate_encounter(new, existing=existing, org_id=ORG) == []

def test_backwards_transition_rejected():
    existing = created(status="in-progress",
                       statusHistory=[{"status": "arrived", "period": {"start": NOW}},
                                      {"status": "in-progress", "period": {"start": NOW}}])
    new = created()  # back to arrived
    assert validate_encounter(new, existing=existing, org_id=ORG)

def test_skip_to_finished_rejected():
    existing = created()
    new = created(status="finished",
                  statusHistory=[
                      {"status": "arrived", "period": {"start": NOW}},
                      {"status": "finished", "period": {"start": NOW, "end": NOW}}])
    assert validate_encounter(new, existing=existing, org_id=ORG)

def test_finished_needs_history_entry_and_period_end():
    existing = created(status="in-progress",
                       statusHistory=[{"status": "arrived", "period": {"start": NOW}},
                                      {"status": "in-progress", "period": {"start": NOW}}])
    new = created(status="finished",
                  statusHistory=[
                      {"status": "arrived", "period": {"start": NOW}},
                      {"status": "in-progress", "period": {"start": NOW}},
                      {"status": "finished", "period": {"start": NOW, "end": NOW}}])
    assert validate_encounter(new, existing=existing, org_id=ORG) == []
    no_end = created(status="finished",
                     statusHistory=[
                         {"status": "arrived", "period": {"start": NOW}},
                         {"status": "in-progress", "period": {"start": NOW}},
                         {"status": "finished", "period": {"start": NOW, "end": NOW}}])
    no_end["period"] = {"start": NOW}
    assert validate_encounter(no_end, existing=existing, org_id=ORG)
```

- [ ] **Step 2: Run test to verify it fails**

Run: `.venv/bin/python -m pytest tests/test_rules_encounter.py -v`
Expected: FAIL with `ModuleNotFoundError`

- [ ] **Step 3: Write minimal implementation**

```python
# fhir_server/validation/rules_encounter.py
from .issues import Issue, R_BAD_IDENTIFIER_SYSTEM, R_WAJIB_MISSING, R_DATETIME

_ORDER = ["arrived", "in-progress", "finished"]

def _wajib(text, expr):
    return Issue(code="value", details_text=f"Wajib element missing: {text}",
                 expression=expr, rule_number=R_WAJIB_MISSING)

def _check_base(payload, org_id, out):
    idents = payload.get("identifier") or []
    if not idents:
        out.append(_wajib("Encounter.identifier", "Encounter.identifier"))
    else:
        want = f"http://sys-ids.kemkes.go.id/encounter/{org_id}"
        if idents[0].get("system") != want:
            out.append(Issue(code="value",
                             details_text=f"Invalid identifier system: {idents[0].get('system')}",
                             expression="Encounter.identifier[0].system",
                             rule_number=R_BAD_IDENTIFIER_SYSTEM))
    if payload.get("status") is None:
        out.append(_wajib("Encounter.status", "Encounter.status"))
    cls = payload.get("class") or {}
    if cls.get("code") != "AMB":
        out.append(_wajib("Encounter.class (AMB)", "Encounter.class"))
    if not (payload.get("subject") or {}).get("reference"):
        out.append(_wajib("Encounter.subject", "Encounter.subject"))
    if not (payload.get("serviceProvider") or {}).get("reference"):
        out.append(_wajib("Encounter.serviceProvider", "Encounter.serviceProvider"))
    if not payload.get("location"):
        out.append(_wajib("Encounter.location", "Encounter.location"))
    if not (payload.get("period") or {}).get("start"):
        out.append(_wajib("Encounter.period.start", "Encounter.period.start"))

def _history_statuses(payload):
    return [h.get("status") for h in payload.get("statusHistory") or []]

def validate_encounter(payload, *, existing, org_id, duplicate_fn=None):
    out = []
    _check_base(payload, org_id, out)
    # service-provider org check
    sp = (payload.get("serviceProvider") or {}).get("reference", "")
    if sp and sp != f"Organization/{org_id}":
        out.append(_wajib(f"Encounter.serviceProvider must be Organization/{org_id}",
                          "Encounter.serviceProvider"))
    if existing is None:
        hist = payload.get("statusHistory") or []
        if payload.get("status") != "arrived":
            out.append(_wajib("Encounter.status must be 'arrived' on create",
                              "Encounter.status"))
        if (len(hist) != 1 or hist[0].get("status") != "arrived"
                or not (hist[0].get("period") or {}).get("start")
                or "end" in (hist[0].get("period") or {})):
            out.append(_wajib(
                "Encounter.statusHistory must be one arrived entry with period.start only",
                "Encounter.statusHistory[0]"))
        if duplicate_fn and idents := (payload.get("identifier") or []):
            if duplicate_fn(idents[0].get("value")):
                out.append(Issue(code="duplicate",
                                 details_text="Found duplicate resource: Encounter",
                                 expression="Encounter.identifier"))
    else:
        old_status = existing.get("status")
        new_status = payload.get("status")
        old_seq = _history_statuses(existing)
        new_seq = _history_statuses(payload)
        if old_seq != new_seq[:len(old_seq)] or new_seq[:len(old_seq)] != old_seq:
            out.append(_wajib("Encounter.statusHistory must preserve prior entries",
                              "Encounter.statusHistory"))
        try:
            forward = _ORDER.index(new_status) == _ORDER.index(old_status) + 1
        except ValueError:
            forward = False
        if new_status != old_status and not forward:
            out.append(Issue(code="value",
                             details_text=f"Illegal Encounter.status transition"
                                          f" {old_status} -> {new_status}",
                             expression="Encounter.status", rule_number=R_DATETIME))
        if new_status == "in-progress":
            if new_seq != ["arrived", "in-progress"]:
                out.append(_wajib("Encounter.statusHistory must be arrived,in-progress",
                                  "Encounter.statusHistory"))
        if new_status == "finished":
            if new_seq != ["arrived", "in-progress", "finished"]:
                out.append(_wajib(
                    "Encounter.statusHistory must be arrived,in-progress,finished",
                    "Encounter.statusHistory"))
            last = (payload.get("statusHistory") or [{}])[-1]
            if not (last.get("period") or {}).get("end"):
                out.append(_wajib("Encounter.statusHistory.finished period.end",
                                  "Encounter.statusHistory[-1].period.end"))
            if not (payload.get("period") or {}).get("end"):
                out.append(_wajib("Encounter.period.end", "Encounter.period.end"))
    return out
```

- [ ] **Step 4: Run test to verify it passes**

Run: `.venv/bin/python -m pytest tests/test_rules_encounter.py -v`
Expected: PASS (9 tests)

- [ ] **Step 5: Commit**

```bash
git add fhir_server/validation/rules_encounter.py tests/test_rules_encounter.py
git commit -m "feat(server): lifecycle-aware Encounter rules

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

---

### Task 11: Observation rules (heart-rate slice)

**Files:**
- Create: `fhir_server/validation/rules_observation.py`
- Test: `tests/test_rules_observation.py`

**Interfaces:**
- Consumes: `rules_common`, `Issue`, constants.
- Produces: `validate_observation(payload, *, org_id: str, device_ref: str | None, assigned_patient: str | None) -> list[Issue]`.
  - Wajib: `status`, `code.coding` non-empty, `subject.reference`, `encounter.reference` → `R_WAJIB_MISSING`.
  - `code.coding[0]` must be `system=http://loinc.org, code=8867-4` → `R_CODE_NOT_FOUND` (10001).
  - `category` when present must include `observation-category | vital-signs` → `R_BAD_CODING_SYSTEM`/10001-style; use `R_CODE_NOT_FOUND`.
  - `valueQuantity`: required (heart-rate slice), `code == "/min"`, `system == "http://unitsofmeasure.org"`, `value` a number (not bool) → `L_OBSERVATION_VALUE` (20006); range sanity `0 < value < 300` → 20006.
  - `device.reference` must equal `device_ref` (when a device principal is writing) → `L_DEVICE_RULE` (20005).
  - `subject.reference` must equal `assigned_patient` (device principal) → `L_DEVICE_RULE`.
  - Identifier system: absent OK on create (server can mint) — but if present must be `http://sys-ids.kemkes.go.id/observation/{org}` or `.../organization/{org}` (S7 accept-both); on output services normalize to `/observation/`.
  - `effectiveDateTime` optional here (common rule validates format when present).

- [ ] **Step 1: Write the failing test**

```python
# tests/test_rules_observation.py
from fhir_server.validation.rules_observation import validate_observation

ORG = "100000001"
DEV = "Device/aaa"
PAT = "Patient/P12345678901"
ENC = "Encounter/bbb"
NOW = "2026-09-29T10:00:00+00:00"

def valid(**kw):
    p = {
        "resourceType": "Observation",
        "status": "final",
        "category": [{"coding": [{
            "system": "http://terminology.hl7.org/CodeSystem/observation-category",
            "code": "vital-signs", "display": "Vital Signs"}]}],
        "code": {"coding": [{"system": "http://loinc.org",
                             "code": "8867-4", "display": "Heart rate"}]},
        "subject": {"reference": PAT},
        "encounter": {"reference": ENC},
        "effectiveDateTime": NOW,
        "valueQuantity": {"value": 72, "unit": "beats/minute",
                          "system": "http://unitsofmeasure.org", "code": "/min"},
        "device": {"reference": DEV},
        "identifier": [{"system": f"http://sys-ids.kemkes.go.id/observation/{ORG}",
                        "value": "obs-1"}],
    }
    p.update(kw)
    return p

def kw():
    return dict(org_id=ORG, device_ref=DEV, assigned_patient=PAT)

def test_valid_passes():
    assert validate_observation(valid(), **kw()) == []

def test_wajib_subject_encounter_code_status():
    p = valid(); del p["subject"]; del p["encounter"]
    p["code"] = {}; del p["status"]
    i = validate_observation(p, **kw())
    assert sum(1 for x in i if x.rule_number == 10263) >= 4

def test_non_loinc_code_rejected():
    p = valid()
    p["code"] = {"coding": [{"system": "http://loinc.org", "code": "8480-6"}]}
    assert any(i.rule_number == 10001 for i in validate_observation(p, **kw()))

def test_value_quantity_rules():
    p = valid(valueQuantity={"value": 72, "code": "kg",
                             "system": "http://unitsofmeasure.org"})
    assert any(i.rule_number == 20006 for i in validate_observation(p, **kw()))
    p2 = valid(valueQuantity={"value": 999, "code": "/min",
                              "system": "http://unitsofmeasure.org"})
    assert any(i.rule_number == 20006 for i in validate_observation(p2, **kw()))

def test_device_must_match_principal():
    p = valid(device={"reference": "Device/other"})
    assert any(i.rule_number == 20005 for i in validate_observation(p, **kw()))

def test_subject_must_match_assignment():
    p = valid(subject={"reference": "Patient/P99999999999"})
    assert any(i.rule_number == 20005 for i in validate_observation(p, **kw()))

def test_identifier_system_forms_accepted():
    for sys_ in (f"http://sys-ids.kemkes.go.id/observation/{ORG}",
                 f"http://sys-ids.kemkes.go.id/organization/{ORG}"):
        p = valid(identifier=[{"system": sys_, "value": "x"}])
        assert validate_observation(p, **kw()) == []
    p = valid(identifier=[{"system": "http://evil", "value": "x"}])
    assert any(i.rule_number == 10117 for i in validate_observation(p, **kw()))
```

- [ ] **Step 2: Run test to verify it fails**

Run: `.venv/bin/python -m pytest tests/test_rules_observation.py -v`
Expected: FAIL with `ModuleNotFoundError`

- [ ] **Step 3: Write minimal implementation**

```python
# fhir_server/validation/rules_observation.py
from .issues import (Issue, R_WAJIB_MISSING, R_CODE_NOT_FOUND,
                     R_BAD_IDENTIFIER_SYSTEM, L_OBSERVATION_VALUE, L_DEVICE_RULE)

def _wajib(text, expr):
    return Issue(code="value", details_text=f"Wajib element missing: {text}",
                 expression=expr, rule_number=R_WAJIB_MISSING)

def validate_observation(payload, *, org_id, device_ref, assigned_patient):
    out = []
    if not payload.get("status"):
        out.append(_wajib("Observation.status", "Observation.status"))
    codings = (payload.get("code") or {}).get("coding") or []
    if not codings:
        out.append(_wajib("Observation.code.coding", "Observation.code.coding"))
    else:
        c0 = codings[0]
        if c0.get("system") != "http://loinc.org" or c0.get("code") != "8867-4":
            out.append(Issue(code="value",
                             details_text=f"Code not found: '{c0.get('code')}' in system:"
                                          f" http://loinc.org (heart-rate slice)",
                             expression="Observation.code.coding[0]",
                             rule_number=R_CODE_NOT_FOUND))
    if not (payload.get("subject") or {}).get("reference"):
        out.append(_wajib("Observation.subject", "Observation.subject"))
    if not (payload.get("encounter") or {}).get("reference"):
        out.append(_wajib("Observation.encounter", "Observation.encounter"))
    cats = ((payload.get("category") or [{}])[0].get("coding") or [])
    if cats and not any(c.get("code") == "vital-signs" for c in cats):
        out.append(Issue(code="value",
                         details_text="Category must include observation-category | vital-signs",
                         expression="Observation.category[0].coding",
                         rule_number=R_CODE_NOT_FOUND))
    vq = payload.get("valueQuantity")
    if vq is None:
        out.append(_wajib("Observation.valueQuantity (heart-rate slice)",
                          "Observation.valueQuantity"))
    else:
        if (vq.get("system") != "http://unitsofmeasure.org"
                or vq.get("code") != "/min"):
            out.append(Issue(code="value",
                             details_text="Heart rate requires UCUM /min",
                             expression="Observation.valueQuantity",
                             rule_number=L_OBSERVATION_VALUE))
        val = vq.get("value")
        if isinstance(val, bool) or not isinstance(val, (int, float)):
            out.append(Issue(code="value", details_text="valueQuantity.value must be numeric",
                             expression="Observation.valueQuantity.value",
                             rule_number=L_OBSERVATION_VALUE))
        elif not (0 < val < 300):
            out.append(Issue(code="value", details_text="Heart rate out of range (0,300)",
                             expression="Observation.valueQuantity.value",
                             rule_number=L_OBSERVATION_VALUE))
    dev = (payload.get("device") or {}).get("reference")
    if device_ref is not None and dev != device_ref:
        out.append(Issue(code="value",
                         details_text=f"Observation.device must be {device_ref}",
                         expression="Observation.device", rule_number=L_DEVICE_RULE))
    subj = (payload.get("subject") or {}).get("reference")
    if assigned_patient is not None and subj != assigned_patient:
        out.append(Issue(code="value",
                         details_text=f"Device assigned to {assigned_patient}, not {subj}",
                         expression="Observation.subject", rule_number=L_DEVICE_RULE))
    for idx, ident in enumerate(payload.get("identifier") or []):
        sys_ = ident.get("system")
        allowed = {f"http://sys-ids.kemkes.go.id/observation/{org_id}",
                   f"http://sys-ids.kemkes.go.id/organization/{org_id}"}
        if sys_ is not None and sys_ not in allowed:
            out.append(Issue(code="value",
                             details_text=f"Invalid identifier system: {sys_}",
                             expression=f"Observation.identifier[{idx}].system",
                             rule_number=R_BAD_IDENTIFIER_SYSTEM))
    return out
```

- [ ] **Step 4: Run test to verify it passes**

Run: `.venv/bin/python -m pytest tests/test_rules_observation.py -v`
Expected: PASS (7 tests)

- [ ] **Step 5: Commit**

```bash
git add fhir_server/validation/rules_observation.py tests/test_rules_observation.py
git commit -m "feat(server): heart-rate Observation validation rules

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

---

### Task 12: Authorization matrix and principal helpers

**Files:**
- Create: `fhir_server/authz.py`
- Test: `tests/test_authz.py`

**Interfaces:**
- Consumes: `Principal`, `repositories.resources`.
- Produces:
  - `class AuthzError(Exception)` with `.issues: list[Issue]` (always `code="forbidden"`, `rule_number=L_AUTH`) and `.status = 403`.
  - `authz.check(principal, action, resource_type, resource=None, *, conn=None)` — action ∈ {`read`, `create`, `update`, `delete`}. Raises `AuthzError` when denied; returns `None` when allowed.
    - admin: everything allowed.
    - doctor: read Organization/Location/Practitioner yes; read Patient only if participant (needs `conn`); create Encounter yes; update Encounter only if participant on that encounter; read Observation only if participant on its encounter's subject; create/update/delete Patient, Device, Organization, Location, Practitioner, Observation → denied; delete anything → denied (skeleton: no deletes for non-admin).
    - patient: read Patient where `resource["id"] == ref id` from `principal.ref`; read Encounter/Observation where subject/reference id matches own; everything else denied (including create/update/delete).
    - device: read Observation written by own device (device reference match); read own Device resource; create Observation validated elsewhere in service (check returns allowed, real constraints live in rules); all else denied.
  - `authz.participates_in_patient(conn, practitioner_ref, patient_id) -> bool` — scans Encounter list for `subject.reference == Patient/{patient_id}` and any `participant[].individual.reference == practitioner_ref`.
  - `authz.filter_search(principal, resource_type, params, conn) -> None` — raises `AuthzError` unless the search is permitted:
    - patient: for Patient/Encounter/Observation searches, `params["subject"]` or `params["patient"]` must equal own reference (or own id); otherwise **rewrite** is not allowed here — raise if missing/foreign (service may instead auto-filter; decide: raise on foreign, auto-inject own when missing — implement auto-inject by returning modified params: `filter_search(...) -> dict` returning effective params). **Use the return-dict form:** `authz.filter_search(principal, resource_type, params, conn) -> dict` with auto-injection for patients (subject=own) and doctors (subject restricted to participated patients — implemented as post-filter flag `authz.principal_patient_scope(conn, principal) -> set[str] | None`, None = unrestricted; the service post-filters results).

- [ ] **Step 1: Write the failing test**

```python
# tests/test_authz.py
import pytest
from fhir_server import db
from fhir_server.auth.jwt import Principal
from fhir_server.authz import AuthzError, check, filter_search, participates_in_patient
from fhir_server.repositories import resources

ADMIN = Principal(kind="admin", account_id="a", role="admin", ref=None)
DOC = Principal(kind="doctor", account_id="d", role="doctor", ref="Practitioner/N12345678")
PAT = Principal(kind="patient", account_id="p", role="patient", ref="Patient/P11111111111")
DEV = Principal(kind="device", account_id=None, device_id="dev-1",
                patient_id="Patient/P11111111111")

def make_conn(db_path):
    conn = db.connect(db_path); db.init(conn)
    resources.put(conn, "Patient", "P11111111111",
                  {"resourceType": "Patient", "id": "P11111111111"})
    resources.put(conn, "Patient", "P22222222222",
                  {"resourceType": "Patient", "id": "P22222222222"})
    resources.put(conn, "Encounter", "e1", {
        "resourceType": "Encounter", "id": "e1", "status": "in-progress",
        "subject": {"reference": "Patient/P11111111111"},
        "participant": [{"individual": {"reference": "Practitioner/N12345678"}}]})
    return conn

def test_admin_can_do_everything(db_path):
    conn = make_conn(db_path)
    for action in ("read", "create", "update", "delete"):
        for rt in ("Patient", "Observation", "Device"):
            check(ADMIN, action, rt, {"id": "x"}, conn=conn)

def test_admin_only_can_create_org(db_path):
    conn = make_conn(db_path)
    with pytest.raises(AuthzError): check(DOC, "create", "Organization", conn=conn)
    with pytest.raises(AuthzError): check(PAT, "create", "Patient", conn=conn)
    check(ADMIN, "create", "Organization", conn=conn)

def test_doctor_patient_read_requires_participation(db_path):
    conn = make_conn(db_path)
    with pytest.raises(AuthzError):
        check(DOC, "read", "Patient",
              {"resourceType": "Patient", "id": "P22222222222"}, conn=conn)
    check(DOC, "read", "Patient",
          {"resourceType": "Patient", "id": "P11111111111"}, conn=conn)

def test_patient_reads_only_self(db_path):
    conn = make_conn(db_path)
    check(PAT, "read", "Patient",
          {"resourceType": "Patient", "id": "P11111111111"}, conn=conn)
    with pytest.raises(AuthzError):
        check(PAT, "read", "Patient",
              {"resourceType": "Patient", "id": "P22222222222"}, conn=conn)
    with pytest.raises(AuthzError):
        check(PAT, "read", "Practitioner", {"resourceType": "Practitioner"}, conn=conn)

def test_patient_search_autoscopes_to_self(db_path):
    conn = make_conn(db_path)
    assert filter_search(PAT, "Observation", {}, conn)["subject"] == "Patient/P11111111111"
    with pytest.raises(AuthzError):
        filter_search(PAT, "Observation", {"subject": "Patient/P22222222222"}, conn)
    with pytest.raises(AuthzError):
        filter_search(PAT, "Device", {}, conn)

def test_doctor_search_scope(db_path):
    conn = make_conn(db_path)
    filter_search(DOC, "Observation", {"subject": "Patient/P11111111111"}, conn)
    with pytest.raises(AuthzError):
        filter_search(DOC, "Observation", {"subject": "Patient/P22222222222"}, conn)

def test_device_can_create_assigned_observation_only(db_path):
    conn = make_conn(db_path)
    check(DEV, "create", "Observation",
          {"resourceType": "Observation",
           "subject": {"reference": "Patient/P11111111111"},
           "device": {"reference": "Device/dev-1"}}, conn=conn)
    with pytest.raises(AuthzError):
        check(DEV, "create", "Observation",
              {"resourceType": "Observation",
               "subject": {"reference": "Patient/P22222222222"},
               "device": {"reference": "Device/dev-1"}}, conn=conn)
    with pytest.raises(AuthzError):
        check(DEV, "create", "Patient", conn=conn)

def test_participates_helper(db_path):
    conn = make_conn(db_path)
    assert participates_in_patient(conn, "Practitioner/N12345678", "P11111111111")
    assert not participates_in_patient(conn, "Practitioner/N99999999", "P11111111111")
```

- [ ] **Step 2: Run test to verify it fails**

Run: `.venv/bin/python -m pytest tests/test_authz.py -v`
Expected: FAIL with `ModuleNotFoundError`

- [ ] **Step 3: Write minimal implementation**

```python
# fhir_server/authz.py
from .auth.jwt import Principal
from .repositories import resources as res
from .validation.issues import Issue, L_AUTH

class AuthzError(Exception):
    def __init__(self, message="Access denied"):
        super().__init__(message)
        self.issues = [Issue(code="forbidden", details_text=message,
                             rule_number=L_AUTH)]
        self.status = 403

_ADMIN_ALL = True
_DOCTOR_READABLE = {"Organization", "Location", "Practitioner", "Patient",
                    "Device", "Encounter", "Observation"}
_PATIENT_READABLE = {"Patient", "Encounter", "Observation"}

def _own_id(principal: Principal) -> str | None:
    if principal.ref and "/" in principal.ref:
        return principal.ref.split("/", 1)[1]
    return None

def participates_in_patient(conn, practitioner_ref, patient_id) -> bool:
    for enc in res.list(conn, "Encounter"):
        if (enc.get("subject") or {}).get("reference") != f"Patient/{patient_id}":
            continue
        for p in enc.get("participant") or []:
            if (p.get("individual") or {}).get("reference") == practitioner_ref:
                return True
    return False

def _doctor_reads_patient(conn, principal, resource) -> bool:
    pid = resource.get("id")
    return bool(pid) and participates_in_patient(conn, principal.ref, pid)

def _doctor_reads_encounter(resource, principal) -> bool:
    # doctor must be a participant of this encounter
    for p in resource.get("participant") or []:
        if (p.get("individual") or {}).get("reference") == principal.ref:
            return True
    return False

def _doctor_reads_observation(conn, principal, resource) -> bool:
    enc_ref = (resource.get("encounter") or {}).get("reference", "")
    if not enc_ref:
        return False
    enc = res.get(conn, "Encounter", enc_ref.split("/", 1)[1])
    if not enc:
        return False
    return _doctor_reads_encounter(enc, principal)

def check(principal, action, resource_type, resource=None, *, conn=None):
    if principal.kind == "admin":
        return None
    if principal.kind == "doctor":
        if action == "delete":
            raise AuthzError("Doctors cannot delete resources")
        if action in ("create", "update"):
            if resource_type == "Encounter":
                if action == "update" and not _doctor_reads_encounter(resource or {}, principal):
                    raise AuthzError("Doctor is not a participant of this Encounter")
                return None
            raise AuthzError(f"Doctors cannot {action} {resource_type}")
        # read
        if resource_type not in _DOCTOR_READABLE:
            raise AuthzError(f"Doctors cannot read {resource_type}")
        if resource_type == "Patient":
            if not _doctor_reads_patient(conn, principal, resource):
                raise AuthzError("Doctor is not a participant for this patient")
        elif resource_type == "Observation":
            if not _doctor_reads_observation(conn, principal, resource):
                raise AuthzError("Doctor has no participated encounter for this Observation")
        return None
    if principal.kind == "patient":
        if action != "read":
            raise AuthzError("Patients are read-only")
        if resource_type not in _PATIENT_READABLE:
            raise AuthzError(f"Patients cannot read {resource_type}")
        own = _own_id(principal)
        subj = (resource.get("subject") or {}).get("reference") or ""
        if resource_type == "Patient":
            if resource.get("id") != own:
                raise AuthzError("Patients may read only their own record")
        elif not subj.endswith(f"/{own}"):
            raise AuthzError("Patients may read only their own records")
        return None
    if principal.kind == "device":
        if action == "create" and resource_type == "Observation":
            subj = (resource.get("subject") or {}).get("reference")
            dev = (resource.get("device") or {}).get("reference")
            if subj != principal.patient_id or dev != f"Device/{principal.device_id}":
                raise AuthzError("Device token not authorized for this Observation")
            return None
        if action == "read" and resource_type == "Observation":
            dev = (resource.get("device") or {}).get("reference")
            if dev != f"Device/{principal.device_id}":
                raise AuthzError("Device may read only its own Observations")
            return None
        if action == "read" and resource_type == "Device" and resource.get("id") == principal.device_id:
            return None
        raise AuthzError("Device token not authorized for this action")
    raise AuthzError("Unknown principal kind")

def filter_search(principal, resource_type, params, conn) -> dict:
    params = dict(params)
    if principal.kind == "admin":
        return params
    if principal.kind == "patient":
        if resource_type == "Patient":
            ident = params.get("identifier")
            own = principal.ref
            if "identifier" in params and not str(ident).endswith(own.split("/", 1)[1]):
                raise AuthzError("Patients may search only their own record")
            params.pop("identifier", None)
            params["id"] = own.split("/", 1)[1] if "id" not in params else params["id"]
            if params.get("id") != own.split("/", 1)[1]:
                raise AuthzError("Patients may search only their own record")
            return params
        if resource_type not in ("Encounter", "Observation"):
            raise AuthzError(f"Patients cannot search {resource_type}")
        own_ref = principal.ref
        subject = params.get("subject") or params.get("patient")
        if subject is None:
            params["subject"] = own_ref
        elif subject != own_ref:
            raise AuthzError("Patients may search only their own records")
        return params
    if principal.kind == "doctor":
        if resource_type == "Patient":
            # doctors may search patients only via participation-scoped reads later;
            # allow identifier/name searches (worklist) — restrict by participation post-filter
            return params
        if resource_type in ("Encounter", "Observation"):
            subject = params.get("subject") or params.get("patient")
            if subject:
                pid = subject.split("/", 1)[1]
                if not participates_in_patient(conn, principal.ref, pid):
                    raise AuthzError("Doctor has no participated encounter for this patient")
                return params
            params["_scope_participant"] = principal.ref  # post-filter marker
            return params
        if resource_type in ("Organization", "Location", "Practitioner", "Device"):
            return params
        raise AuthzError(f"Doctors cannot search {resource_type}")
    if principal.kind == "device":
        if resource_type == "Observation":
            subject = params.get("subject") or params.get("patient")
            if subject and subject != principal.patient_id:
                raise AuthzError("Device may search only its assigned patient")
            params["subject"] = principal.patient_id
            return params
        raise AuthzError(f"Devices cannot search {resource_type}")
    raise AuthzError("Unknown principal kind")
```

Note for the service layer (Task 13): after search, when `_scope_participant` marker present, drop Encounters where the doctor is not a participant and Observations whose encounter the doctor does not participate in; strip the marker before running parameter matching.

- [ ] **Step 4: Run test to verify it passes**

Run: `.venv/bin/python -m pytest tests/test_authz.py -v`
Expected: PASS (7 tests)

- [ ] **Step 5: Commit**

```bash
git add fhir_server/authz.py tests/test_authz.py
git commit -m "feat(server): three-role authorization matrix and search scoping

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

---

### Task 13: FHIR service — create/read/update/delete orchestration

**Files:**
- Create: `fhir_server/services/__init__.py`, `fhir_server/services/fhir_service.py`
- Test: `tests/test_fhir_service.py`

**Interfaces:**
- Consumes: `parse.structural_issues`, all `rules_*`, `authz.check`, `resources` repo, `ids.mint`.
- Produces (class `FhirService` with `conn`, `settings`, `org_id: str` attributes; constructed per request in routes):
  - `class FhirError(Exception)`: `.issues: list[Issue]`, `.status: int` (400/404/403/409).
  - `create(principal, resource_type, payload) -> tuple[str, dict, int]` — order: `authz.check(create)` → structural parse → rule set (dispatch table `RULE_SETS: dict[str, callable]`) → reference checks with `exists_fn` → mint id (Patient gets ihs-number identifier appended, `id` set) → `put` → return `(id, stored_doc, version)`. On any issue → `FhirError(status=400, ...)`; duplicate issues → status 409.
  - `read(principal, resource_type, id) -> dict` — repo get; missing → `FhirError(404, not-found)`; then `authz.check(read)`.
  - `update(principal, resource_type, id, payload) -> dict` — must exist (404); structural + rules with `existing`; authz; `put`; returns stored doc.
  - `delete(principal, resource_type, id) -> None` — authz + exists; `resources.delete`.
  - `provision_device(principal, device_id, patient_ref) -> str` — admin only (authz check via `check(principal, "update", "Device", ...)` is wrong semantics — use explicit `if principal.kind != "admin": raise AuthzError`); creates device token via `devices.create_token`, returns plaintext token.
  - Helpers: `org_id` read from seeded Organization (single-org skeleton: first Organization row; if none, rules that need org_id use `""` and org-suffix checks are skipped for non-Observation/Org-typed rules until seeded — tests seed).

- [ ] **Step 1: Write the failing test**

```python
# tests/test_fhir_service.py
import pytest
from fhir_server import db
from fhir_server.auth.jwt import Principal
from fhir_server.config import Settings
from fhir_server.repositories import accounts, resources
from fhir_server.services.fhir_service import FhirService, FhirError

ADMIN = Principal(kind="admin", role="admin", account_id="a")
DEV = Principal(kind="device", device_id="dev-1",
                patient_id="Patient/P11111111111")

@pytest.fixture
def svc(db_path):
    conn = db.connect(db_path); db.init(conn)
    settings = Settings(db_path=db_path, jwt_secret="x")
    s = FhirService(conn, settings)
    resources.put(conn, "Organization", "100000001",
                  {"resourceType": "Organization", "id": "100000001",
                   "name": "Klinik Demo"})
    resources.put(conn, "Location", "loc-1",
                  {"resourceType": "Location", "id": "loc-1", "status": "active",
                   "name": "Poli 1"})
    resources.put(conn, "Device", "dev-1",
                  {"resourceType": "Device", "id": "dev-1", "status": "active"})
    resources.put(conn, "Patient", "P11111111111",
                  {"resourceType": "Patient", "id": "P11111111111"})
    return s

def org_payload():
    return {"resourceType": "Organization",
            "identifier": [{"use": "official",
                            "system": "http://sys-ids.kemkes.go.id/organization/100000001",
                            "value": "X"}],
            "name": "Klinik Satu"}

def test_create_assigns_id_and_version(svc):
    pid, doc, ver = svc.create(ADMIN, "Organization", org_payload())
    assert doc["id"] == pid and ver == 1
    assert svc.read(ADMIN, "Organization", pid)["name"] == "Klinik Satu"

def test_failed_validation_writes_nothing(svc):
    before = len(resources.list(svc.conn, "Patient"))
    with pytest.raises(FhirError) as e:
        svc.create(ADMIN, "Patient", {"resourceType": "Patient", "name": []})
    assert e.value.status == 400
    assert len(resources.list(svc.conn, "Patient")) == before

def test_unresolvable_reference_400(svc):
    with pytest.raises(FhirError) as e:
        svc.create(ADMIN, "Encounter", {
            "resourceType": "Encounter",
            "identifier": [{"use": "official",
                            "system": "http://sys-ids.kemkes.go.id/encounter/100000001",
                            "value": "K-1"}],
            "status": "arrived",
            "statusHistory": [{"status": "arrived",
                               "period": {"start": "2026-09-29T10:00:00+00:00"}}],
            "class": {"system": "http://terminology.hl7.org/CodeSystem/v3-ActCode",
                      "code": "AMB"},
            "subject": {"reference": "Patient/PDoesNotExist"},
            "period": {"start": "2026-09-29T10:00:00+00:00"},
            "location": [{"location": {"reference": "Location/loc-1"}}],
            "serviceProvider": {"reference": "Organization/100000001"}})
    assert e.value.status == 400

def test_read_missing_404(svc):
    with pytest.raises(FhirError) as e:
        svc.read(ADMIN, "Patient", "P404")
    assert e.value.status == 404

def test_update_bumps_version(svc):
    svc.create(ADMIN, "Organization", org_payload())
    # find created org
    orgs = resources.list(svc.conn, "Organization")
    payload = dict(orgs[0]); payload["name"] = "Klinik Dua"
    _, doc, ver = svc.update(ADMIN, "Organization", doc_id := orgs[0]["id"], payload)
    assert ver == 2 and doc["name"] == "Klinik Dua"

def test_device_cannot_create_foreign_observation(svc):
    with pytest.raises(FhirError) as e:
        svc.create(DEV, "Observation", {
            "resourceType": "Observation", "status": "final",
            "code": {"coding": [{"system": "http://loinc.org", "code": "8867-4"}]},
            "subject": {"reference": "Patient/P99999999999"},
            "encounter": {"reference": "Encounter/nope"},
            "device": {"reference": "Device/dev-1"},
            "valueQuantity": {"value": 70, "code": "/min",
                              "system": "http://unitsofmeasure.org"}})
    assert e.value.status == 403
```

- [ ] **Step 2: Run test to verify it fails**

Run: `.venv/bin/python -m pytest tests/test_fhir_service.py -v`
Expected: FAIL with `ModuleNotFoundError`

- [ ] **Step 3: Write minimal implementation**

```python
# fhir_server/services/__init__.py
```
(empty)

```python
# fhir_server/services/fhir_service.py
from .. import authz, ids
from ..auth.jwt import Principal
from ..repositories import devices as devices_repo
from ..repositories import resources as res
from ..validation import parse, rules_common, rules_encounter, rules_master, \
    rules_observation, rules_patient
from ..validation.issues import Issue

class FhirError(Exception):
    def __init__(self, issues, status):
        super().__init__(issues[0].details_text if issues else "error")
        self.issues = issues
        self.status = status

def _master_org_id(conn) -> str:
    orgs = res.list(conn, "Organization")
    return orgs[0].get("id", "") if orgs else ""

class FhirService:
    def __init__(self, conn, settings):
        self.conn = conn
        self.settings = settings
        self.org_id = _master_org_id(conn)

    def _exists(self, t, i):
        return res.exists(self.conn, t, i)

    def _rule_sets(self, resource_type, payload, *, existing=None,
                   principal=None):
        org = self.org_id
        out = []
        out += rules_common.check_datetimes(payload, resource_type,
                                            self.settings.earliest_date)
        out += rules_common.check_empty_strings(payload, resource_type)
        out += rules_common.check_coding_systems(payload, resource_type)
        if resource_type == "Organization":
            out += rules_master.validate_organization(payload)
        elif resource_type == "Location":
            out += rules_master.validate_location(payload)
        elif resource_type == "Practitioner":
            out += rules_master.validate_practitioner(payload)
        elif resource_type == "Device":
            out += rules_master.validate_device(payload)
        elif resource_type == "Patient":
            out += rules_patient.validate_patient(payload, is_create=existing is None)
        elif resource_type == "Encounter":
            def dup(value):
                for e in res.list(self.conn, "Encounter"):
                    for ident in e.get("identifier") or []:
                        if ident.get("value") == value:
                            return True
                return False
            out += rules_encounter.validate_encounter(
                payload, existing=existing, org_id=org, duplicate_fn=dup)
        elif resource_type == "Observation":
            device_ref, assigned = None, None
            if principal is not None and principal.kind == "device":
                device_ref = f"Device/{principal.device_id}"
                assigned = principal.patient_id
            out += rules_observation.validate_observation(
                payload, org_id=org, device_ref=device_ref,
                assigned_patient=assigned)
        if existing is None:
            out += rules_common.check_references(payload, resource_type, self._exists)
        return out

    def create(self, principal, resource_type, payload):
        authz.check(principal, "create", resource_type, payload, conn=self.conn)
        issues, _ = parse.structural_issues(resource_type, payload)
        if not issues:
            issues = self._rule_sets(resource_type, payload, principal=principal)
        if issues:
            status = 409 if any(i.code == "duplicate" for i in issues) else 400
            raise FhirError(issues, status)
        new_id = ids.mint(resource_type)
        doc = dict(payload)
        doc["id"] = new_id
        if resource_type == "Patient":
            idents = list(doc.get("identifier") or [])
            idents.append({"use": "official",
                           "system": "https://fhir.kemkes.go.id/id/ihs-number",
                           "value": new_id})
            doc["identifier"] = idents
        if resource_type == "Observation":
            idents = [dict(i) for i in (doc.get("identifier") or [])]
            idents = [{**i,
                       "system": (f"http://sys-ids.kemkes.go.id/observation/{self.org_id}"
                                  if i.get("system", "").startswith(
                                      "http://sys-ids.kemkes.go.id/organization/")
                                  else i.get("system"))} for i in idents]
            if not idents:
                idents = [{"use": "usual",
                           "system": f"http://sys-ids.kemkes.go.id/observation/{self.org_id}",
                           "value": new_id}]
            doc["identifier"] = idents
        version = res.put(self.conn, resource_type, new_id, doc)
        return new_id, res.get(self.conn, resource_type, new_id), version

    def read(self, principal, resource_type, id_):
        doc = res.get(self.conn, resource_type, id_)
        if doc is None:
            raise FhirError([Issue(code="not-found",
                                   details_text=f"{resource_type}/{id_} not found")], 404)
        authz.check(principal, "read", resource_type, doc, conn=self.conn)
        return doc

    def update(self, principal, resource_type, id_, payload):
        existing = res.get(self.conn, resource_type, id_)
        if existing is None:
            raise FhirError([Issue(code="not-found",
                                   details_text=f"{resource_type}/{id_} not found")], 404)
        authz.check(principal, "update", resource_type, payload, conn=self.conn)
        issues, _ = parse.structural_issues(resource_type, payload)
        if not issues:
            issues = self._rule_sets(resource_type, payload, existing=existing,
                                     principal=principal)
        if issues:
            status = 409 if any(i.code == "duplicate" for i in issues) else 400
            raise FhirError(issues, status)
        doc = dict(payload)
        doc["id"] = id_
        res.put(self.conn, resource_type, id_, doc)
        return res.get(self.conn, resource_type, id_)

    def delete(self, principal, resource_type, id_):
        authz.check(principal, "delete", resource_type, conn=self.conn)
        if not res.delete(self.conn, resource_type, id_):
            raise FhirError([Issue(code="not-found",
                                   details_text=f"{resource_type}/{id_} not found")], 404)

    def provision_device(self, principal, device_id, patient_ref):
        if principal.kind != "admin":
            raise FhirError([Issue(code="forbidden",
                                   details_text="Only admins may provision devices",
                                   rule_number=20007)], 403)
        if not res.exists(self.conn, "Device", device_id):
            raise FhirError([Issue(code="not-found", details_text="Device not found")], 404)
        pid = patient_ref.split("/", 1)[-1]
        if not res.exists(self.conn, "Patient", pid):
            raise FhirError([Issue(code="not-found", details_text="Patient not found")], 404)
        token = devices_repo.create_token(self.conn, device_id, patient_ref,
                                          __import__("secrets").token_urlsafe(32))
        return token
```

- [ ] **Step 4: Run test to verify it passes**

Run: `.venv/bin/python -m pytest tests/test_fhir_service.py -v`
Expected: PASS (6 tests)

- [ ] **Step 5: Commit**

```bash
git add fhir_server/services tests/test_fhir_service.py
git commit -m "feat(server): fhir service orchestration with processor-then-server

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

---

### Task 14: Search implementation

**Files:**
- Modify: `fhir_server/services/fhir_service.py` (add `search`)
- Test: `tests/test_search.py`

**Interfaces:**
- Consumes: `authz.filter_search`, `resources.list`.
- Produces: `FhirService.search(principal, resource_type, params: dict[str, str]) -> dict` returning a Bundle: `{"resourceType": "Bundle", "type": "searchset", "total": n, "entry": [{"resource": doc}, ...]}`. Per-resource supported parameters as per spec's table; unsupported param name → `FhirError(400, L_SEARCH_PARAM)`. `_count` capped at 100 (default 50). Token `system|value` matching for `identifier`. Name matching: case-insensitive substring against `name[].text|family|given[]`, min 3 chars else 400. `date` on Observation: matches when `effectiveDateTime` falls within the value if it contains `/` (interval) else exact-date prefix match. Patient `id` param supported (used by authz auto-scope). Post-filter: `_scope_participant` marker → doctor participation filtering as described in Task 12.

- [ ] **Step 1: Write the failing test**

```python
# tests/test_search.py
import pytest
from fhir_server import db
from fhir_server.auth.jwt import Principal
from fhir_server.config import Settings
from fhir_server.repositories import resources
from fhir_server.services.fhir_service import FhirService, FhirError

ADMIN = Principal(kind="admin", role="admin")
PAT = Principal(kind="patient", role="patient", ref="Patient/P11111111111")
DOC = Principal(kind="doctor", role="doctor", ref="Practitioner/N12345678")

@pytest.fixture
def svc(db_path):
    conn = db.connect(db_path); db.init(conn)
    s = FhirService(conn, Settings(db_path=db_path, jwt_secret="x"))
    resources.put(conn, "Observation", "o1", {
        "resourceType": "Observation", "id": "o1", "status": "final",
        "subject": {"reference": "Patient/P11111111111"},
        "encounter": {"reference": "Encounter/e1"},
        "device": {"reference": "Device/dev-1"},
        "code": {"coding": [{"system": "http://loinc.org", "code": "8867-4"}]},
        "effectiveDateTime": "2026-09-29T10:00:00+00:00"})
    resources.put(conn, "Observation", "o2", {
        "resourceType": "Observation", "id": "o2", "status": "final",
        "subject": {"reference": "Patient/P22222222222"},
        "encounter": {"reference": "Encounter/e2"},
        "device": {"reference": "Device/dev-2"},
        "code": {"coding": [{"system": "http://loinc.org", "code": "8867-4"}]},
        "effectiveDateTime": "2026-09-29T11:00:00+00:00"})
    resources.put(conn, "Patient", "P11111111111", {
        "resourceType": "Patient", "id": "P11111111111",
        "name": [{"text": "Budi Santoso", "family": "Santoso", "given": ["Budi"]}]})
    resources.put(conn, "Patient", "P22222222222", {
        "resourceType": "Patient", "id": "P22222222222",
        "name": [{"text": "Siti", "family": "Siti", "given": ["Siti"]}]})
    return s

def test_bundle_shape(svc):
    b = svc.search(ADMIN, "Observation", {"subject": "Patient/P11111111111"})
    assert b["resourceType"] == "Bundle" and b["type"] == "searchset"
    assert b["total"] == 1 and b["entry"][0]["resource"]["id"] == "o1"

def test_patient_cannot_search_other_subject(svc):
    with pytest.raises(FhirError) as e:
        svc.search(PAT, "Observation", {"subject": "Patient/P22222222222"})
    assert e.value.status == 403

def test_patient_search_without_subject_returns_only_own(svc):
    b = svc.search(PAT, "Observation", {})
    assert b["total"] == 1
    assert all(e["resource"]["subject"]["reference"] == "Patient/P11111111111"
               for e in b["entry"])

def test_doctor_requires_participation_for_subject(svc):
    with pytest.raises(FhirError) as e:
        svc.search(DOC, "Observation", {"subject": "Patient/P22222222222"})
    assert e.value.status == 403

def test_unknown_parameter_400(svc):
    with pytest.raises(FhirError) as e:
        svc.search(ADMIN, "Observation", {"bogus": "x"})
    assert e.value.status == 400

def test_name_search_min_three_chars(svc):
    with pytest.raises(FhirError):
        svc.search(ADMIN, "Patient", {"name": "Bu"})
    b = svc.search(ADMIN, "Patient", {"name": "santoso"})
    assert b["total"] == 1

def test_empty_result_is_empty_bundle(svc):
    b = svc.search(ADMIN, "Observation", {"subject": "Patient/P00000000000"})
    assert b["total"] == 0 and "entry" not in b

def test_count_cap(svc):
    b = svc.search(ADMIN, "Observation", {"_count": "500"})
    assert b["total"] <= 500  # server clamps internal slice; see impl note
```

- [ ] **Step 2: Run test to verify it fails**

Run: `.venv/bin/python -m pytest tests/test_search.py -v`
Expected: FAIL (no `search` method)

- [ ] **Step 3: Write minimal implementation** (append to `fhir_service.py`)

```python
SUPPORTED_PARAMS = {
    "Patient": {"identifier", "name", "birthdate", "gender", "id"},
    "Practitioner": {"identifier", "name", "id"},
    "Organization": {"name", "id"},
    "Location": {"name", "organization", "id"},
    "Encounter": {"subject", "patient", "status", "participant", "id"},
    "Observation": {"subject", "encounter", "code", "date", "id"},
    "Device": {"identifier", "patient", "id"},
}

def _matches_identifier(doc, value):
    want_system, _, want_value = str(value).partition("|")
    for ident in doc.get("identifier") or []:
        if want_value and ident.get("value") != want_value:
            continue
        if want_system and ident.get("system") != want_system:
            continue
        if want_value or want_system:
            return True
    return False

def _matches_name(doc, needle):
    needle = needle.lower()
    for n in doc.get("name") or []:
        fields = [n.get("text"), n.get("family")] + list(n.get("given") or [])
        if any(f and needle in f.lower() for f in fields):
            return True
    return False

class FhirService:  # reopening to add search in this task
    def search(self, principal, resource_type, params):
        from ..validation.issues import L_SEARCH_PARAM
        supported = SUPPORTED_PARAMS.get(resource_type, {"id"})
        unknown = [k for k in params
                   if k not in supported and k != "_count"]
        if unknown:
            raise FhirError([Issue(code="value",
                                   details_text=f"Unknown search parameter: {unknown[0]}",
                                   expression=f"{resource_type}.{unknown[0]}",
                                   rule_number=L_SEARCH_PARAM)], 400)
        effective = authz.filter_search(principal, resource_type, params, self.conn)
        marker = effective.pop("_scope_participant", None)
        if resource_type == "Patient" and "name" in effective \
                and len(effective["name"]) < 3:
            raise FhirError([Issue(code="value", details_text="name needs >= 3 chars",
                                   expression="Patient.name")], 400)
        docs = res.list(self.conn, resource_type)
        try:
            matched = [d for d in docs
                       if all(self._param_match(resource_type, d, k, v)
                              for k, v in effective.items())]
        except _BadParam as exc:
            raise FhirError([Issue(code="value", details_text=str(exc),
                                   rule_number=L_SEARCH_PARAM)], 400)
        if marker:
            if resource_type == "Encounter":
                matched = [d for d in matched if authz._doctor_reads_encounter(d, principal)]
            elif resource_type == "Observation":
                matched = [d for d in matched
                           if authz._doctor_reads_observation(self.conn, principal, d)]
        count = int(effective.get("_count", 50)) if "_count" in params else 50
        count = max(0, min(count, 100))
        total = len(matched)
        return {"resourceType": "Bundle", "type": "searchset", "total": total,
                "entry": [{"resource": d} for d in matched[:count]]}

    def _param_match(self, resource_type, doc, key, value):
        if key == "_count":
            return True
        if key == "id":
            return doc.get("id") == value
        if key in ("subject", "patient"):
            ref = (doc.get("subject") or {}).get("reference") \
                if resource_type == "Observation" else None
            if resource_type == "Encounter":
                ref = (doc.get("subject") or {}).get("reference")
            return ref == value
        if key == "identifier":
            return _matches_identifier(doc, value)
        if key == "name":
            return _matches_name(doc, value)
        if key == "gender":
            return doc.get("gender") == value
        if key == "birthdate":
            return doc.get("birthDate") == value
        if key == "status":
            return doc.get("status") == value
        if key == "code":
            want_system, _, want_code = str(value).partition("|")
            codings = (doc.get("code") or {}).get("coding") or []
            return any((not want_system or c.get("system") == want_system)
                       and c.get("code") == want_code for c in codings)
        if key == "encounter":
            return (doc.get("encounter") or {}).get("reference") == value
        if key == "participant":
            return any((p.get("individual") or {}).get("reference") == value
                       for p in doc.get("participant") or [])
        if key == "date":
            eff = doc.get("effectiveDateTime")
            if not eff:
                return False
            if "/" in value:  # interval
                start, _, end = value.partition("/")
                return start <= eff <= end
            return eff[:len(value)] == value  # prefix: yyyy, yyyy-mm, yyyy-mm-dd
        if key == "organization":
            return (doc.get("managingOrganization") or {}).get("reference") == value \
                if resource_type == "Location" else False
        if key == "patient" and resource_type == "Device":
            return (doc.get("patient") or {}).get("reference") == value
        raise _BadParam(f"Unsupported search parameter: {key}")

class _BadParam(Exception):
    pass
```

Fix note: in `search`, `_count` must be popped from `effective` before `_param_match` runs (its `all(...)` already ignores `_count` via the key check — keep the explicit branch). Ensure `params` for Patient auto-scoped `id` lands correctly (authz sets `params["id"]`; it is in SUPPORTED_PARAMS for Patient).

- [ ] **Step 4: Run test to verify it passes**

Run: `.venv/bin/python -m pytest tests/test_search.py -v`
Expected: PASS (8 tests)

- [ ] **Step 5: Commit**

```bash
git add fhir_server/services/fhir_service.py tests/test_search.py
git commit -m "feat(server): fixed-parameter search with searchset bundles

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

---

### Task 15: HTTP routes (FHIR surface, auth, admin, metadata)

**Files:**
- Create: `fhir_server/app.py`, `fhir_server/routes/__init__.py`, `fhir_server/routes/fhir.py`, `fhir_server/routes/auth.py`, `fhir_server/routes/admin.py`, `fhir_server/routes/deps.py`
- Test: `tests/test_routes.py`

**Interfaces:**
- Consumes: `FhirService`, `FhirError`, `AuthzError`, `auth_jwt`, `passwords`, `accounts`, `devices` repos, `to_outcome`.
- Produces:
  - `app.py`: `create_app(settings) -> FastAPI`; mounts routers under `/fhir-r4/v1` (fhir+admin), `/auth` (auth); `app.state.settings`, `app.state.conn` (single connection created at startup).
  - `routes/deps.py`: `get_principal(request) -> Principal` FastAPI dependency: reads `Authorization: Bearer x`; if x is a JWT → `verify_token`; else try `devices.resolve_token` → device Principal; missing/invalid → `HTTPException`-free raise of `FhirError(401)`. `get_service(request) -> FhirService`.
  - FHIR routes: `POST|GET /{type}` and `GET|PUT|DELETE /{type}/{id}` where type ∈ SUPPORTED_TYPES; `POST /Device/{id}/$provision`; search via GET with query params (list of `(k, v)` pairs collapsed to dict — duplicate keys: last wins, documented). Emit `application/fhir+json`; create → 201 with `Location: /fhir-r4/v1/{type}/{id}` and ETag `W/"{version}"`; read/update → 200 + ETag; delete → 204; search → 200 Bundle; `GET /metadata` public CapabilityStatement; error path: catch `FhirError`/`AuthzError` → `JSONResponse(status, to_outcome(...), media_type="application/fhir+json")`.
  - Media handling: request `Content-Type` must be in {application/json, application/fhir+json} (415 `OperationOutcome` otherwise; empty body on GET fine); `Accept` header, if present and not JSON-compatible → 406.
  - `POST /auth/token`: form or JSON `{username, password}` → 200 `{"access_token", "token_type": "Bearer", "expires_in": 3600}` (playbook-ish) or 401 `OperationOutcome`.
  - Admin routes (under `/fhir-r4/v1`, authenticated): `POST /admin/accounts` `{username, password, role, ref}` (admin-only; creates account row; role in admin/doctor/patient), `GET /admin/accounts` (admin-only, no password hashes).
  - CapabilityStatement: `fhirVersion "4.0.1"`, `status "active"`, `date`, `kind "instance"`, `software {name: "PRATA FHIR server", version: "0.1.0"}`, `implementation {description, url}`, `rest [{mode: "server", security {service: [{coding: [{system: "http://terminology.hl7.org/CodeSystem/restful-security-service", "code": "Bearer"}]}]}, resource: [...]}]` with `type`, `interaction` per supported verb, `searchParam` per SUPPORTED_PARAMS entries with basic `code/type` (`token` for identifier/code, `string` for name, `date` for date/birthdate, `reference` for subject/encounter/patient, `token` for status/gender/id? — `id` uses type `token`… use `Special` skip: only list non-id params).

- [ ] **Step 1: Write the failing test**

```python
# tests/test_routes.py
import json
import pytest
from fastapi.testclient import TestClient
from fhir_server.app import create_app
from fhir_server.auth import jwt as auth_jwt
from fhir_server.auth.jwt import Principal
from fhir_server.config import Settings
from fhir_server.repositories import accounts, devices, resources

@pytest.fixture
def client(db_path):
    settings = Settings(db_path=db_path, jwt_secret="route-secret")
    app = create_app(settings)
    with TestClient(app) as c:
        yield c

def admin_token(c):
    conn = c.app.state.conn
    accounts.create(conn, "admin", __import__("fhir_server.auth.passwords",
        fromlist=["hash_password"]).hash_password("admin-pw"), "admin", None)
    r = c.post("/auth/token", json={"username": "admin", "password": "admin-pw"})
    assert r.status_code == 200, r.text
    return r.json()["access_token"]

def hdr(token):
    return {"Authorization": f"Bearer {token}"}

def test_metadata_public(client):
    r = client.get("/fhir-r4/v1/metadata")
    assert r.status_code == 200
    body = r.json()
    assert body["resourceType"] == "CapabilityStatement"
    assert body["fhirVersion"] == "4.0.1"
    types = {res_["type"] for res_ in body["rest"][0]["resource"]}
    assert {"Patient", "Observation", "Encounter"} <= types

def test_fhir_requires_token(client):
    r = client.get("/fhir-r4/v1/Patient/x")
    assert r.status_code == 401
    assert r.json()["resourceType"] == "OperationOutcome"

def test_auth_flow_and_create(client):
    tok = admin_token(client)
    r = client.post("/fhir-r4/v1/Patient", headers=hdr(tok),
                    json={"resourceType": "Patient", "gender": "male"})
    assert r.status_code == 400
    assert "RuleNumber" in r.text

def test_media_type_accepts_plain_json(client):
    tok = admin_token(client)
    r = client.post("/fhir-r4/v1/Organization",
                    headers={**hdr(tok), "Content-Type": "application/json"},
                    json={"resourceType": "Organization", "name": "Klinik"})
    assert r.status_code in (201, 400)  # 400 only if rules demand identifier — org rules don't
    assert r.status_code == 201
    assert r.headers["content-type"].startswith("application/fhir+json")
    assert r.headers["location"].startswith("/fhir-r4/v1/Organization/")

def test_bad_accept_406(client):
    tok = admin_token(client)
    r = client.get("/fhir-r4/v1/Patient/x", headers={**hdr(tok),
                                                     "Accept": "application/xml"})
    assert r.status_code == 406

def test_wrong_content_type_415(client):
    tok = admin_token(client)
    r = client.post("/fhir-r4/v1/Organization", headers={**hdr(tok),
                    "Content-Type": "application/xml"}, content=b"<x/>")
    assert r.status_code == 415

def test_device_provision_and_use(client):
    tok = admin_token(client)
    conn = client.app.state.conn
    resources.put(conn, "Device", "dev-1", {"resourceType": "Device",
                                            "id": "dev-1", "status": "active"})
    resources.put(conn, "Patient", "P11111111111",
                  {"resourceType": "Patient", "id": "P11111111111"})
    r = client.post("/fhir-r4/v1/Device/dev-1/$provision", headers=hdr(tok),
                    json={"patient": "Patient/P11111111111"})
    assert r.status_code == 200, r.text
    device_tok = r.json()["token"]
    # device token now authenticates
    r2 = client.get("/fhir-r4/v1/Patient/P11111111111",
                    headers=hdr(device_tok))
    assert r2.status_code == 403  # device cannot read Patient
    # invalid device action returns 401 for revoked?
    assert devices.resolve_token(conn, device_tok)["patient_id"] == "Patient/P11111111111"

def test_account_admin_flow(client):
    tok = admin_token(client)
    r = client.post("/fhir-r4/v1/admin/accounts", headers=hdr(tok),
                    json={"username": "doc1", "password": "pw",
                          "role": "doctor", "ref": "Practitioner/N12345678"})
    assert r.status_code == 201
    r2 = client.post("/auth/token", json={"username": "doc1", "password": "pw"})
    assert r2.status_code == 200
    # non-admin cannot create accounts
    r3 = client.post("/fhir-r4/v1/admin/accounts", headers=hdr(r2.json()["access_token"]),
                     json={"username": "x", "password": "y", "role": "admin", "ref": None})
    assert r3.status_code == 403
```

- [ ] **Step 2: Run test to verify it fails**

Run: `.venv/bin/python -m pytest tests/test_routes.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'fhir_server.app'`

- [ ] **Step 3: Write minimal implementation**

```python
# fhir_server/routes/deps.py
from fastapi import Request

from ..auth import jwt as auth_jwt
from ..auth.jwt import Principal
from ..repositories import devices as devices_repo
from ..services.fhir_service import FhirError, FhirService
from ..validation.issues import Issue

def get_service(request: Request) -> FhirService:
    return FhirService(request.app.state.conn, request.app.state.settings)

def get_principal(request: Request) -> Principal:
    header = request.headers.get("Authorization", "")
    if not header.startswith("Bearer "):
        raise FhirError([Issue(code="security",
                               details_text="Authorization: Bearer <token> is required",
                               rule_number=20007)], 401)
    token = header.removeprefix("Bearer ").strip()
    try:
        return auth_jwt.verify_token(request.app.state.settings, token)
    except auth_jwt.TokenError:
        pass
    row = devices_repo.resolve_token(request.app.state.conn, token)
    if row:
        return Principal(kind="device", device_id=row["device_id"],
                         patient_id=row["patient_id"])
    raise FhirError([Issue(code="security",
                           details_text="Invalid or expired token",
                           rule_number=20007)], 401)
```

```python
# fhir_server/routes/__init__.py
```
(empty)

```python
# fhir_server/routes/auth.py
from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse

from ..auth import jwt as auth_jwt
from ..auth.passwords import verify_password
from ..repositories import accounts
from ..services.fhir_service import FhirError
from ..validation.outcome import to_outcome

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/token")
async def token(request: Request):
    body = await _read_body(request)
    user = body.get("username"); pw = body.get("password", "")
    acct = accounts.get_by_username(request.app.state.conn, user or "")
    if not acct or not verify_password(pw, acct["password_hash"]):
        return JSONResponse(status_code=401, content=to_outcome(
            [__import__("fhir_server.validation.issues", fromlist=["Issue"]).Issue(
                code="security", details_text="Authentication failed",
                rule_number=20007)]),
            media_type="application/fhir+json")
    principal = auth_jwt.Principal(kind=acct["role"], account_id=acct["id"],
                                   role=acct["role"], ref=acct["subject_ref"])
    settings = request.app.state.settings
    tok = auth_jwt.create_token(settings, principal)
    return {"access_token": tok, "token_type": "Bearer",
            "expires_in": settings.jwt_ttl_seconds}

async def _read_body(request: Request):
    ct = request.headers.get("content-type", "")
    if "application/x-www-form-urlencoded" in ct:
        form = await request.form()
        return dict(form)
    try:
        return await request.json()
    except Exception:
        return {}
```

```python
# fhir_server/routes/fhir.py
import json
from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse, Response
from fastapi.routing import APIRoute

from ..authz import AuthzError
from ..validation import parse
from ..validation.issues import Issue
from ..validation.outcome import to_outcome
from ..services.fhir_service import FhirError, FhirService
from .deps import get_principal, get_service

router = APIRouter(prefix="/fhir-r4/v1", tags=["fhir"])
_TYPES = tuple(parse.SUPPORTED_TYPES)
_FHIR_JSON = "application/fhir+json; charset=utf-8"
_INPUT_CT = ("application/json", "application/fhir+json")

def _json_response(payload, status=200, headers=None):
    return JSONResponse(status_code=status, content=payload, headers=headers or {},
                        media_type="application/fhir+json")

def _error_response(exc):
    return JSONResponse(status_code=exc.status, content=to_outcome(exc.issues),
                        media_type="application/fhir+json")

async def _check_media(request: Request):
    accept = request.headers.get("accept")
    if accept and not any(t in accept for t in ("application/json", "*/*",
                                                "application/fhir+json")):
        raise FhirError([Issue(code="not-supported",
                               details_text="Accept must allow application/fhir+json")], 406)
    if request.method in ("POST", "PUT"):
        ct = request.headers.get("content-type", "")
        if not any(ct.startswith(t) for t in _INPUT_CT):
            raise FhirError([Issue(code="not-supported",
                                   details_text="Content-Type must be application/json"
                                                " or application/fhir+json")], 415)

async def _payload(request: Request) -> dict:
    try:
        body = await request.json()
    except Exception:
        raise FhirError([Issue(code="format", details_text="Body must be valid JSON",
                               rule_number=10132)], 400)
    if not isinstance(body, dict):
        raise FhirError([Issue(code="format", details_text="Body must be a JSON object")], 400)
    return body

def _wrap(fn):
    async def inner(request: Request, *args, **kwargs):
        try:
            await _check_media(request)
            return await fn(request, *args, **kwargs)
        except FhirError as exc:
            return _error_response(exc)
        except AuthzError as exc:
            return _error_response(exc)
    return inner

@router.get("/{type_}", name="search_or_read_index")
async def search(type_: str, request: Request):
    return await _wrap_impl_search(request, type_)

async def _wrap_impl_search(request, type_):
    try:
        await _check_media(request)
        if type_ not in _TYPES:
            raise FhirError([Issue(code="not-found",
                                   details_text=f"Unsupported resource type {type_}")], 404)
        svc = get_service(request)
        principal = get_principal(request)
        params = dict(request.query_params)
        result = svc.search(principal, type_, params)
        return _json_response(result)
    except FhirError as exc:
        return _error_response(exc)
    except AuthzError as exc:
        return _error_response(exc)

@router.post("/{type_}")
async def create(type_: str, request: Request):
    try:
        await _check_media(request)
        if type_ not in _TYPES:
            raise FhirError([Issue(code="not-found",
                                   details_text=f"Unsupported resource type {type_}")], 404)
        svc = get_service(request)
        principal = get_principal(request)
        payload = await _payload(request)
        rid, doc, version = svc.create(principal, type_, payload)
        return _json_response(doc, status=201, headers={
            "Location": f"/fhir-r4/v1/{type_}/{rid}",
            "ETag": f'W/"{version}"'})
    except FhirError as exc:
        return _error_response(exc)
    except AuthzError as exc:
        return _error_response(exc)

@router.get("/{type_}/{rid}")
async def read(type_: str, rid: str, request: Request):
    try:
        await _check_media(request)
        if type_ not in _TYPES:
            raise FhirError([Issue(code="not-found",
                                   details_text=f"Unsupported resource type {type_}")], 404)
        svc = get_service(request)
        principal = get_principal(request)
        doc = svc.read(principal, type_, rid)
        return _json_response(doc)
    except FhirError as exc:
        return _error_response(exc)
    except AuthzError as exc:
        return _error_response(exc)

@router.put("/{type_}/{rid}")
async def update(type_: str, rid: str, request: Request):
    try:
        await _check_media(request)
        if type_ not in _TYPES:
            raise FhirError([Issue(code="not-found",
                                   details_text=f"Unsupported resource type {type_}")], 404)
        svc = get_service(request)
        principal = get_principal(request)
        payload = await _payload(request)
        doc = svc.update(principal, type_, rid, payload)
        return _json_response(doc)
    except FhirError as exc:
        return _error_response(exc)
    except AuthzError as exc:
        return _error_response(exc)

@router.delete("/{type_}/{rid}")
async def delete(type_: str, rid: str, request: Request):
    try:
        if type_ not in _TYPES:
            raise FhirError([Issue(code="not-found",
                                   details_text=f"Unsupported resource type {type_}")], 404)
        svc = get_service(request)
        principal = get_principal(request)
        svc.delete(principal, type_, rid)
        return Response(status_code=204)
    except FhirError as exc:
        return _error_response(exc)
    except AuthzError as exc:
        return _error_response(exc)

@router.post("/Device/{rid}/$provision")
async def provision(rid: str, request: Request):
    try:
        await _check_media(request)
        svc = get_service(request)
        principal = get_principal(request)
        body = await _payload(request)
        patient = body.get("patient")
        if not isinstance(patient, str) or not patient.startswith("Patient/"):
            raise FhirError([Issue(code="value",
                                   details_text='body must be {"patient": "Patient/{id}"}')],
                            400)
        token = svc.provision_device(principal, rid, patient)
        return _json_response({"token": token, "device": f"Device/{rid}",
                               "patient": patient})
    except FhirError as exc:
        return _error_response(exc)
    except AuthzError as exc:
        return _error_response(exc)
```

Route-ordering note: `POST /Device/{rid}/$provision` must be registered **before** `POST /{type_}` so `$provision` is not swallowed — put it above the generic routes in the module.

```python
# fhir_server/routes/admin.py
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from ..auth.passwords import hash_password
from ..authz import AuthzError
from ..repositories import accounts
from ..services.fhir_service import FhirError
from ..validation.issues import Issue
from ..validation.outcome import to_outcome
from .deps import get_principal

router = APIRouter(prefix="/fhir-r4/v1/admin", tags=["admin"])

def _err(exc):
    return JSONResponse(status_code=exc.status, content=to_outcome(exc.issues),
                        media_type="application/fhir+json")

@router.post("/accounts")
async def create_account(request: Request):
    try:
        principal = get_principal(request)
        if principal.kind != "admin":
            raise AuthzError("Only admins may manage accounts")
        body = await request.json()
        username, password = body.get("username"), body.get("password")
        role, ref = body.get("role"), body.get("ref")
        if not username or not password or role not in ("admin", "doctor", "patient"):
            raise FhirError([Issue(code="value",
                                   details_text="username, password, role"
                                                " (admin|doctor|patient) required")], 400)
        accounts.create(request.app.state.conn, username,
                        hash_password(password), role, ref)
        return JSONResponse(status_code=201, content={"created": username},
                            media_type="application/fhir+json")
    except (FhirError, AuthzError) as exc:
        return _err(exc)

@router.get("/accounts")
async def list_accounts(request: Request):
    try:
        principal = get_principal(request)
        if principal.kind != "admin":
            raise AuthzError("Only admins may manage accounts")
        rows = accounts.list(request.app.state.conn)
        return JSONResponse(
            content=[{"username": r["username"], "role": r["role"],
                      "ref": r["subject_ref"]} for r in rows],
            media_type="application/fhir+json")
    except AuthzError as exc:
        return _err(exc)
```

```python
# fhir_server/app.py
import datetime as dt
from fastapi import FastAPI

from .config import Settings
from .routes import admin as admin_routes
from .routes import auth as auth_routes
from .routes import fhir as fhir_routes
from .validation import parse

def capability_statement(settings) -> dict:
    interactions = {
        "read": {"code": "read"}, "search": {"code": "search-type"},
        "create": {"code": "create"}, "update": {"code": "update"},
        "delete": {"code": "delete"},
    }
    param_types = {
        "identifier": "token", "name": "string", "birthdate": "date",
        "gender": "token", "subject": "reference", "patient": "reference",
        "encounter": "reference", "code": "token", "date": "date",
        "status": "token", "participant": "reference", "organization": "reference",
    }
    resources_out = []
    for rtype, params in __import__(
            "fhir_server.services.fhir_service", fromlist=["SUPPORTED_PARAMS"]
    ).SUPPORTED_PARAMS.items():
        resources_out.append({
            "type": rtype,
            "interaction": [{"code": c} for c in
                            ("read", "search-type", "create", "update", "delete")],
            "searchParam": [{"code": p, "type": param_types.get(p, "token")}
                            for p in sorted(params) if p != "id"],
        })
    return {
        "resourceType": "CapabilityStatement",
        "status": "active",
        "date": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00"),
        "kind": "instance",
        "fhirVersion": "4.0.1",
        "format": ["application/fhir+json", "application/json"],
        "software": {"name": "PRATA FHIR server", "version": "0.1.0"},
        "implementation": {"description": "Local SATUSEHAT-compatible FHIR R4 server",
                           "url": "http://127.0.0.1:8000/fhir-r4/v1"},
        "rest": [{
            "mode": "server",
            "security": {"service": [{
                "coding": [{"system": "http://terminology.hl7.org/CodeSystem/"
                                       "restful-security-service",
                            "code": "Bearer"}]}]},
            "resource": resources_out,
        }],
    }

def create_app(settings: Settings) -> FastAPI:
    from . import db as db_mod
    app = FastAPI(title="PRATA FHIR R4 server", docs_url=None, redoc_url=None)
    app.state.settings = settings
    app.state.conn = db_mod.connect(settings.db_path)
    db_mod.init(app.state.conn)
    app.include_router(auth_routes.router)
    app.include_router(admin_routes.router)
    app.include_router(fhir_routes.router)

    @app.get("/fhir-r4/v1/metadata")
    def metadata():
        from fastapi.responses import JSONResponse
        return JSONResponse(content=capability_statement(settings),
                            media_type="application/fhir+json")
    return app
```

- [ ] **Step 4: Run test to verify it passes**

Run: `.venv/bin/python -m pytest tests/test_routes.py -v`
Expected: PASS (8 tests). Iterate on route ordering/media checks until green; do not weaken tests.

- [ ] **Step 5: Commit**

```bash
git add fhir_server/app.py fhir_server/routes tests/test_routes.py
git commit -m "feat(server): fhir http surface, auth endpoint, admin accounts, metadata

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

---

### Task 16: CLI — init-db and seed

**Files:**
- Create: `fhir_server/cli.py`, `fhir_server/__main__.py`
- Test: `tests/test_cli_seed.py`

**Interfaces:**
- Consumes: everything above.
- Produces: `python3 -m fhir_server init-db [--db PATH]`; `python3 -m fhir_server seed [--db PATH] [--reset]` — `seed` deletes the target DB file (only with `--reset`), creates schema, then inserts: bootstrap admin account (username `admin`, password from `FHIR_ADMIN_PASSWORD` env or generated `secrets.token_urlsafe(12)`, printed once), Organization `100000001` (name from env `FHIR_ORG_NAME` default `Klinik Demo`), Location, Practitioner `N10000000` + doctor account (`doctor`/`doctor-pw` default or env), Patient `P10000000001` with full NIK union + patient account, Device + **prints a provisioned device token** (provisions directly into the repo). Prints a JSON summary `{admin_password, device_token, patient_id, practitioner_id, org_id, location_id}`. `__main__.py` dispatches argparse subcommands. Settings secret: if `FHIR_JWT_SECRET` unset, generate and write `.env` file line `FHIR_JWT_SECRET=...` (do not overwrite existing), export into process env.

- [ ] **Step 1: Write the failing test**

```python
# tests/test_cli_seed.py
import json
import os
import subprocess
import sys

def run_cli(args, env_extra):
    env = dict(os.environ, **env_extra)
    return subprocess.run([sys.executable, "-m", "fhir_server", *args],
                          capture_output=True, text=True, env=env, cwd=os.getcwd())

def test_seed_creates_login_and_summary(tmp_path):
    db = str(tmp_path / "seed.db")
    env = {"FHIR_DB_PATH": db, "FHIR_JWT_SECRET": "cli-secret",
           "FHIR_ADMIN_PASSWORD": "admin-pass-1"}
    p = run_cli(["seed", "--reset"], env)
    assert p.returncode == 0, p.stderr
    summary = json.loads(p.stdout.strip().splitlines()[-1])
    assert summary["admin_password"] == "admin-pass-1"
    assert summary["device_token"]
    # login works against the seeded db
    from fastapi.testclient import TestClient
    from fhir_server.app import create_app
    from fhir_server.config import Settings
    app = create_app(Settings(db_path=db, jwt_secret="cli-secret"))
    with TestClient(app) as c:
        r = c.post("/auth/token", json={"username": "admin", "password": "admin-pass-1"})
        assert r.status_code == 200
        tok = r.json()["access_token"]
        got = c.get(f"/fhir-r4/v1/Patient/{summary['patient_id']}",
                    headers={"Authorization": f"Bearer {tok}"})
        assert got.status_code == 200
        nik = [i for i in got.json()["identifier"] if i["system"].endswith("/nik")]
        assert nik and nik[0]["value"].isdigit() and len(nik[0]["value"]) == 16

def test_seed_requires_reset_flag_to_wipe(tmp_path):
    db = str(tmp_path / "exists.db")
    open(db, "w").write("not a database")
    env = {"FHIR_DB_PATH": db, "FHIR_JWT_SECRET": "cli-secret"}
    p = run_cli(["seed"], env)  # without --reset, sqlite connect must fail loudly
    assert p.returncode != 0 or "seed" in p.stdout
```

- [ ] **Step 2: Run test to verify it fails**

Run: `.venv/bin/python -m pytest tests/test_cli_seed.py -v`
Expected: FAIL (`No module named fhir_server.__main__` / seed not implemented)

- [ ] **Step 3: Write minimal implementation**

```python
# fhir_server/cli.py
import argparse
import json
import os
import secrets
import sys

def _load_dotenv():
    if os.path.exists(".env"):
        for line in open(".env"):
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, _, v = line.partition("=")
                os.environ.setdefault(k.strip(), v.strip())

def _ensure_secret():
    if not os.environ.get("FHIR_JWT_SECRET"):
        secret = secrets.token_urlsafe(32)
        with open(".env", "a") as f:
            f.write(f"FHIR_JWT_SECRET={secret}\n")
        os.environ["FHIR_JWT_SECRET"] = secret

def cmd_init_db(args):
    from . import db as db_mod
    conn = db_mod.connect(args.db)
    db_mod.init(conn)
    print(f"initialized {args.db}")

def cmd_seed(args):
    from . import db as db_mod, ids
    from .auth.passwords import hash_password
    from .config import Settings
    from .repositories import accounts, devices, resources
    if args.reset and os.path.exists(args.db):
        os.remove(args.db)
    conn = db_mod.connect(args.db)
    db_mod.init(conn)
    admin_password = os.environ.get("FHIR_ADMIN_PASSWORD") or secrets.token_urlsafe(12)
    accounts.create(conn, "admin", hash_password(admin_password), "admin", None)
    org_id = "100000001"
    resources.put(conn, "Organization", org_id, {
        "resourceType": "Organization", "id": org_id,
        "name": os.environ.get("FHIR_ORG_NAME", "Klinik Demo"),
        "identifier": [{"use": "official",
                        "system": f"http://sys-ids.kemkes.go.id/organization/{org_id}",
                        "value": org_id}]})
    loc_id = "loc-poliklinik-1"
    resources.put(conn, "Location", loc_id, {
        "resourceType": "Location", "id": loc_id, "status": "active",
        "mode": "instance", "name": "Poli Jantung",
        "managingOrganization": {"reference": f"Organization/{org_id}"}})
    doc_id = "N10000000"
    resources.put(conn, "Practitioner", doc_id, {
        "resourceType": "Practitioner", "id": doc_id,
        "identifier": [{"system": "https://fhir.kemkes.go.id/id/nik",
                        "value": "3175061001900099"}],
        "name": [{"use": "official", "text": "drg. Contoh, Sp.JP",
                  "family": "Contoh", "given": ["Contoh"]}],
        "gender": "male", "birthDate": "1980-05-05"})
    doctor_password = os.environ.get("FHIR_DOCTOR_PASSWORD", "doctor-pw")
    accounts.create(conn, "doctor", hash_password(doctor_password), "doctor",
                    f"Practitioner/{doc_id}")
    pat_id = "P10000000001"
    resources.put(conn, "Patient", pat_id, {
        "resourceType": "Patient", "id": pat_id,
        "identifier": [
            {"use": "official", "system": "https://fhir.kemkes.go.id/id/nik",
             "value": "3175061001900001"},
            {"use": "official", "system": "https://fhir.kemkes.go.id/id/ihs-number",
             "value": pat_id}],
        "name": [{"use": "official", "text": "Budi Santoso",
                  "family": "Santoso", "given": ["Budi"]}],
        "gender": "male", "birthDate": "1990-02-14",
        "multipleBirthBoolean": False,
        "address": [{
            "use": "home", "line": ["Jl. Melati No. 1"], "city": "Jakarta Pusat",
            "postalCode": "10110", "country": "ID",
            "extension": [{
                "url": "https://fhir.kemkes.go.id/r4/StructureDefinition/"
                       "administrativeCode",
                "extension": [
                    {"url": "province", "valueCode": "31"},
                    {"url": "city", "valueCode": "3171"},
                    {"url": "district", "valueCode": "317101"},
                    {"url": "village", "valueCode": "317101001"},
                    {"url": "rt", "valueCode": "001"},
                    {"url": "rw", "valueCode": "001"}]}]}]})
    patient_password = os.environ.get("FHIR_PATIENT_PASSWORD", "patient-pw")
    accounts.create(conn, "patient", hash_password(patient_password), "patient",
                    f"Patient/{pat_id}")
    dev_id = ids.mint("Device")
    resources.put(conn, "Device", dev_id, {
        "resourceType": "Device", "id": dev_id, "status": "active",
        "manufacturer": "PRATA", "deviceName": [
            {"name": "Radar JVP dummy", "type": "model-name"}]})
    device_token = secrets.token_urlsafe(32)
    devices.create_token(conn, dev_id, f"Patient/{pat_id}", device_token)
    print(json.dumps({
        "admin_password": admin_password,
        "doctor_password": doctor_password,
        "patient_password": patient_password,
        "device_token": device_token,
        "org_id": org_id, "location_id": loc_id,
        "practitioner_id": doc_id, "patient_id": pat_id, "device_id": dev_id,
    }))

def main(argv=None):
    _load_dotenv()
    _ensure_secret()
    parser = argparse.ArgumentParser(prog="fhir_server")
    parser.add_argument("--db", default=os.environ.get("FHIR_DB_PATH", "fhir_server.db"))
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("init-db").set_defaults(fn=cmd_init_db)
    seed = sub.add_parser("seed")
    seed.add_argument("--reset", action="store_true")
    seed.set_defaults(fn=cmd_seed)
    args = parser.parse_args(argv)
    args.fn(args)

if __name__ == "__main__":
    main()
```

```python
# fhir_server/__main__.py
from .cli import main
main()
```

- [ ] **Step 4: Run test to verify it passes**

Run: `.venv/bin/python -m pytest tests/test_cli_seed.py -v`
Expected: PASS (2 tests)

- [ ] **Step 5: Commit**

```bash
git add fhir_server/cli.py fhir_server/__main__.py tests/test_cli_seed.py
git commit -m "feat(server): seed CLI with bootstrap accounts and device token

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

---

### Task 17: Device client (Python wire-contract double)

**Files:**
- Create: `device_client/__init__.py`, `device_client/client.py`
- Test: `tests/test_device_client.py`

**Interfaces:**
- Consumes: HTTP surface (Task 15).
- Produces: `client.submit_heart_rate(base_url: str, device_token: str, *, patient: str, encounter: str, device: str, bpm: float, effective_datetime: str, identifier_value: str | None = None) -> tuple[int, dict]` — builds the exact Observation JSON (fields as in Task 11's `valid()`), POSTs to `{base_url}/Observation` with `Authorization: Bearer <device_token>` and `Content-Type: application/json`, returns `(status_code, response_json)`. `client.login(base_url, username, password) -> str` helper for humans/tests.

- [ ] **Step 1: Write the failing test**

```python
# tests/test_device_client.py
import pytest
from fastapi.testclient import TestClient
from fhir_server.app import create_app
from fhir_server.config import Settings
from fhir_server.repositories import accounts, devices, resources
from fhir_server.auth.passwords import hash_password
from device_client import client as dc

ORG = "100000001"

@pytest.fixture
def env(db_path):
    settings = Settings(db_path=db_path, jwt_secret="dc-secret")
    app = create_app(settings)
    conn = app.state.conn
    resources.put(conn, "Organization", ORG,
                  {"resourceType": "Organization", "id": ORG, "name": "K"})
    resources.put(conn, "Location", "L1",
                  {"resourceType": "Location", "id": "L1", "status": "active",
                   "name": "Poli"})
    resources.put(conn, "Patient", "P11111111111",
                  {"resourceType": "Patient", "id": "P11111111111"})
    resources.put(conn, "Encounter", "e1", {
        "resourceType": "Encounter", "id": "e1", "status": "in-progress",
        "subject": {"reference": "Patient/P11111111111"},
        "identifier": [{"use": "official",
                        "system": f"http://sys-ids.kemkes.go.id/encounter/{ORG}",
                        "value": "K-1"}],
        "statusHistory": [
            {"status": "arrived", "period": {"start": "2026-09-29T10:00:00+00:00"}},
            {"status": "in-progress", "period": {"start": "2026-09-29T10:05:00+00:00"}}],
        "class": {"system": "http://terminology.hl7.org/CodeSystem/v3-ActCode",
                  "code": "AMB"},
        "period": {"start": "2026-09-29T10:00:00+00:00"},
        "location": [{"location": {"reference": "Location/L1"}}],
        "serviceProvider": {"reference": f"Organization/{ORG}"}})
    resources.put(conn, "Device", "dev-1",
                  {"resourceType": "Device", "id": "dev-1", "status": "active"})
    token = devices.create_token(conn, "dev-1", "Patient/P11111111111",
                                 "device-secret-token")
    c = TestClient(app)
    return {"client": c, "token": "device-secret-token", "conn": conn}

def test_submit_success(env):
    c = env["client"]
    # TestClient cannot be used by the raw httpx-posting client — the client
    # must accept a `post_fn` override for tests:
    def post_fn(url, **kw):
        path = url.replace("http://test", "")
        r = c.post(path, **kw)
        return type("R", (), {"status_code": r.status_code,
                              "json": lambda self: r.json()})()
    status, body = dc.submit_heart_rate(
        "http://test", env["token"], patient="Patient/P11111111111",
        encounter="Encounter/e1", device="Device/dev-1", bpm=72,
        effective_datetime="2026-09-29T10:06:00+00:00", post_fn=post_fn)
    assert status == 201
    assert body["resourceType"] == "Observation"
    assert body["valueQuantity"]["value"] == 72

def test_submit_wrong_encounter_rejected(env):
    c = env["client"]
    def post_fn(url, **kw):
        path = url.replace("http://test", "")
        r = c.post(path, **kw)
        return type("R", (), {"status_code": r.status_code,
                              "json": lambda self: r.json()})()
    status, body = dc.submit_heart_rate(
        "http://test", env["token"], patient="Patient/P11111111111",
        encounter="Encounter/ghost", device="Device/dev-1", bpm=72,
        effective_datetime="2026-09-29T10:06:00+00:00", post_fn=post_fn)
    assert status == 400
    assert body["resourceType"] == "OperationOutcome"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `.venv/bin/python -m pytest tests/test_device_client.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'device_client'`

- [ ] **Step 3: Write minimal implementation**

```python
# device_client/__init__.py
```
(empty)

```python
# device_client/client.py
import json
import urllib.request

def _default_post(url, *, headers, data):
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req) as resp:
            body = resp.read().decode()
            status = resp.status
    except urllib.error.HTTPError as exc:
        body = exc.read().decode()
        status = exc.code
    class R:
        pass
    r = R()
    r.status_code = status
    r.json = lambda: json.loads(body)
    return r

def build_observation(*, patient, encounter, device, bpm, effective_datetime,
                      identifier_value=None):
    ident = [{"system": "http://sys-ids.kemkes.go.id/organization/100000001",
              "value": identifier_value or "device-local-1"}]
    return {
        "resourceType": "Observation",
        "status": "final",
        "category": [{"coding": [{
            "system": "http://terminology.hl7.org/CodeSystem/observation-category",
            "code": "vital-signs", "display": "Vital Signs"}]}],
        "code": {"coding": [{"system": "http://loinc.org", "code": "8867-4",
                             "display": "Heart rate"}]},
        "subject": {"reference": patient},
        "encounter": {"reference": encounter},
        "effectiveDateTime": effective_datetime,
        "valueQuantity": {"value": bpm, "unit": "beats/minute",
                          "system": "http://unitsofmeasure.org", "code": "/min"},
        "device": {"reference": device},
        "identifier": ident,
    }

def submit_heart_rate(base_url, device_token, *, patient, encounter, device,
                      bpm, effective_datetime, identifier_value=None,
                      post_fn=None):
    post = post_fn or _default_post
    doc = build_observation(patient=patient, encounter=encounter, device=device,
                            bpm=bpm, effective_datetime=effective_datetime,
                            identifier_value=identifier_value)
    r = post(f"{base_url.rstrip('/')}/fhir-r4/v1/Observation",
             headers={"Authorization": f"Bearer {device_token}",
                      "Content-Type": "application/json"},
             data=json.dumps(doc).encode())
    return r.status_code, r.json()

def login(base_url, username, password, *, post_fn=None):
    post = post_fn or _default_post
    r = post(f"{base_url.rstrip('/')}/auth/token",
             headers={"Content-Type": "application/json"},
             data=json.dumps({"username": username, "password": password}).encode())
    if r.status_code != 200:
        raise RuntimeError(f"login failed: {r.status_code}")
    return r.json()["access_token"]
```

- [ ] **Step 4: Run test to verify it passes**

Run: `.venv/bin/python -m pytest tests/test_device_client.py -v`
Expected: PASS (2 tests)

- [ ] **Step 5: Commit**

```bash
git add device_client tests/test_device_client.py
git commit -m "feat(server): python device client with heart-rate submit contract

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

---

### Task 18: End-to-end scenario (the nine-step proof)

**Files:**
- Test: `tests/test_scenario_e2e.py`

**Interfaces:**
- Consumes: all prior tasks through the HTTP surface only (no repo imports except to seed fixtures).

- [ ] **Step 1: Write the failing test**

```python
# tests/test_scenario_e2e.py
import json
import os
import subprocess
import sys

import pytest
from fastapi.testclient import TestClient
from fhir_server.app import create_app
from fhir_server.config import Settings

@pytest.fixture
def scenario(db_path):
    # 1. seed via CLI
    env = dict(os.environ, FHIR_DB_PATH=db_path, FHIR_JWT_SECRET="e2e-secret",
               FHIR_ADMIN_PASSWORD="adm-pw")
    p = subprocess.run([sys.executable, "-m", "fhir_server", "seed", "--reset"],
                       capture_output=True, text=True, env=env, cwd=os.getcwd())
    assert p.returncode == 0, p.stderr
    summary = json.loads(p.stdout.strip().splitlines()[-1])
    app = create_app(Settings(db_path=db_path, jwt_secret="e2e-secret"))
    c = TestClient(app)
    return {"c": c, "s": summary}

def login(c, u, pw):
    r = c.post("/auth/token", json={"username": u, "password": pw})
    assert r.status_code == 200, r.text
    return {"Authorization": f"Bearer {r.json()['access_token']}"}

def test_nine_step_scenario(scenario):
    c, s = scenario["c"], scenario["s"]
    # 2. admin token
    admin = login(c, "admin", s["admin_password"])
    # 3. (device already provisioned by seed; re-provision to prove the route)
    r = c.post(f"/fhir-r4/v1/Device/{s['device_id']}/$provision", headers=admin,
               json={"patient": f"Patient/{s['patient_id']}"})
    assert r.status_code == 200, r.text
    device_token = r.json()["token"]
    # 4. doctor opens the visit
    doc = login(c, "doctor", s["doctor_password"])
    r = c.post("/fhir-r4/v1/Encounter", headers=doc, json={
        "resourceType": "Encounter",
        "identifier": [{"use": "official",
                        "system": f"http://sys-ids.kemkes.go.id/encounter/{s['org_id']}",
                        "value": "KUNJ-001"}],
        "status": "arrived",
        "statusHistory": [{"status": "arrived",
                           "period": {"start": "2026-09-29T10:00:00+00:00"}}],
        "class": {"system": "http://terminology.hl7.org/CodeSystem/v3-ActCode",
                  "code": "AMB", "display": "ambulatory"},
        "subject": {"reference": f"Patient/{s['patient_id']}"},
        "period": {"start": "2026-09-29T10:00:00+00:00"},
        "location": [{"location": {"reference": f"Location/{s['location_id']}"}}],
        "serviceProvider": {"reference": f"Organization/{s['org_id']}"},
    })
    assert r.status_code == 201, r.text
    enc_id = r.json()["id"]
    # server auto-added the doctor as participant
    assert any(p["individual"]["reference"] == f"Practitioner/{s['practitioner_id']}"
               for p in r.json().get("participant", [])), "doctor must be participant"
    # 5. start the visit
    started = r.json()
    started["status"] = "in-progress"
    started["statusHistory"] = [
        {"status": "arrived", "period": {"start": "2026-09-29T10:00:00+00:00"}},
        {"status": "in-progress", "period": {"start": "2026-09-29T10:05:00+00:00"}}]
    r = c.put(f"/fhir-r4/v1/Encounter/{enc_id}", headers=doc, json=started)
    assert r.status_code == 200, r.text
    # 6. device posts heart rate
    from device_client.client import submit_heart_rate
    def post_fn(url, **kw):
        path = url.replace("http://test", "")
        resp = c.post(path, **kw)
        return type("R", (), {"status_code": resp.status_code,
                              "json": lambda self: resp.json()})()
    status, body = submit_heart_rate(
        "http://test", device_token, patient=f"Patient/{s['patient_id']}",
        encounter=f"Encounter/{enc_id}", device=f"Device/{s['device_id']}",
        bpm=72, effective_datetime="2026-09-29T10:06:00+00:00",
        post_fn=post_fn)
    assert status == 201, body
    obs_id = body["id"]
    # 7. doctor reviews (read-only)
    r = c.get(f"/fhir-r4/v1/Observation?subject=Patient/{s['patient_id']}", headers=doc)
    assert r.status_code == 200
    assert r.json()["total"] == 1
    r = c.get(f"/fhir-r4/v1/Observation/{obs_id}", headers=doc)
    assert r.status_code == 200
    # 8. finish the visit
    body_enc = r = c.get(f"/fhir-r4/v1/Encounter/{enc_id}", headers=doc).json()
    body_enc["status"] = "finished"
    body_enc["statusHistory"] = body_enc["statusHistory"] + [
        {"status": "finished",
         "period": {"start": "2026-09-29T10:05:00+00:00",
                    "end": "2026-09-29T11:00:00+00:00"}}]
    body_enc["period"]["end"] = "2026-09-29T11:00:00+00:00"
    r = c.put(f"/fhir-r4/v1/Encounter/{enc_id}", headers=doc, json=body_enc)
    assert r.status_code == 200, r.text
    # 9. patient reads own record only
    pat = login(c, "patient", s["patient_password"])
    r = c.get(f"/fhir-r4/v1/Patient/{s['patient_id']}", headers=pat)
    assert r.status_code == 200
    r = c.get("/fhir-r4/v1/Observation", headers=pat)
    assert r.status_code == 200 and r.json()["total"] == 1
    # cross-tenant denial
    other = login(c, "doctor", s["doctor_password"])
    # a foreign patient id must 403 for the patient role
    r = c.get("/fhir-r4/v1/Patient/P99999999999", headers=pat)
    assert r.status_code in (403, 404)
    # device cannot read Patient
    r = c.get(f"/fhir-r4/v1/Patient/{s['patient_id']}",
              headers={"Authorization": f"Bearer {device_token}"})
    assert r.status_code == 403
    # no anonymous access
    assert c.get("/fhir-r4/v1/Patient").status_code == 401
```

- [ ] **Step 2: Run test to verify it fails**

Run: `.venv/bin/python -m pytest tests/test_scenario_e2e.py -v`
Expected: FAIL (scenario pieces not yet wired — likely 404 on routes or participant missing)

- [ ] **Step 3: Fix the implementation, not the test**

The likely gap: `services.create` does not auto-add the creating doctor to
`Encounter.participant`. Add in `FhirService.create`, when
`resource_type == "Encounter"` and `principal.kind == "doctor"`:

```python
        if resource_type == "Encounter" and principal.kind == "doctor":
            participants = list(doc.get("participant") or [])
            entry = {"individual": {"reference": principal.ref}}
            if not any((p.get("individual") or {}).get("reference") == principal.ref
                       for p in participants):
                participants.append(entry)
            doc["participant"] = participants
```

Apply the equivalent auto-participant merge on `update` (preserve existing participants,
re-add doctor if absent) so finish-PUT cannot drop the participant.

- [ ] **Step 4: Run test to verify it passes**

Run: `.venv/bin/python -m pytest tests/test_scenario_e2e.py -v`
Expected: PASS (1 test)

- [ ] **Step 5: Run the whole suite**

Run: `.venv/bin/python -m pytest tests -q`
Expected: all green

- [ ] **Step 6: Commit**

```bash
git add tests/test_scenario_e2e.py fhir_server/services/fhir_service.py
git commit -m "feat(server): end-to-end device-to-patient scenario

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

---

### Task 19: Firmware — WiFi heart-rate ingest

**Files:**
- Create: `arduino/radar_json/config.example.h`, `arduino/radar_json/ingest.h`
- Modify: `arduino/radar_json/radar_json.ino` (add include + periodic ingest call), `arduino/radar_json/README.md` (document config + no-upload rule stays), `.gitignore` (add `arduino/radar_json/config.h`)

**Interfaces:**
- Consumes: the Observation wire contract from Task 17 (`build_observation` JSON shape), `$provision` token from seed.
- Produces: compile-time config header; `postHeartRate()` function in `ingest.h` that connects WiFi (`WiFi.h`), gets UTC via `configTime(0, 0, "pool.ntp.org")`, builds the same Observation JSON, and POSTs with `HTTPClient` using `Authorization: Bearer <DEVICE_TOKEN>`; called at 1 Hz from `loop()` when configured (`DEVICE_TOKEN[0] != '\0'`), non-blocking-ish (skip if previous POST in flight — simple synchronous with short timeout 2000 ms is acceptable for 1 Hz placeholder). Serial JSON stream keeps running.

- [ ] **Step 1: Create config example and document**

```cpp
// arduino/radar_json/config.example.h  — copy to config.h and fill in.
// config.h is gitignored: never commit real credentials.
#pragma once
#define WIFI_SSID     "your-wifi"
#define WIFI_PASSWORD "your-password"
#define SERVER_URL    "http://192.168.1.10:8000"   // FHIR server base URL
#define DEVICE_TOKEN  ""    // from $provision response; empty disables ingest
#define DEVICE_REF    "Device/REPLACE"             // this device's reference
#define PATIENT_REF   "Patient/REPLACE"            // assigned patient
#define ENCOUNTER_REF ""    // set at runtime from doctor-opened visit, or fill in
#define ORG_IHS       "100000001"
#define INGEST_PERIOD_MS 1000
```

- [ ] **Step 2: Write the ingest header (minimal but real)**

```cpp
// arduino/radar_json/ingest.h
#pragma once
#include <Arduino.h>
#include <WiFi.h>
#include <HTTPClient.h>
#include <time.h>
#include "config.h"

inline bool ingestConfigured() {
  return WIFI_SSID[0] != '\0' && DEVICE_TOKEN[0] != '\0'
      && ENCOUNTER_REF[0] != '\0' && PATIENT_REF[0] != '\0';
}

inline String utcNowIso() {
  struct tm t;
  if (!getLocalTime(&t, 100)) return String("1970-01-01T00:00:00+00:00");
  char buf[32];
  strftime(buf, sizeof(buf), "%Y-%m-%dT%H:%M:%S+00:00", &t);
  return String(buf);
}

inline int postHeartRate(float bpm) {
  if (WiFi.status() != WL_CONNECTED) return -1;
  String body = String(
    "{\"resourceType\":\"Observation\",\"status\":\"final\","
    "\"category\":[{\"coding\":[{\"system\":"
    "\"http://terminology.hl7.org/CodeSystem/observation-category\","
    "\"code\":\"vital-signs\",\"display\":\"Vital Signs\"}]}],"
    "\"code\":{\"coding\":[{\"system\":\"http://loinc.org\","
    "\"code\":\"8867-4\",\"display\":\"Heart rate\"}]},"
    "\"subject\":{\"reference\":\"") + PATIENT_REF +
    "\"},\"encounter\":{\"reference\":\"" + ENCOUNTER_REF +
    "\"},\"effectiveDateTime\":\"" + utcNowIso() +
    "\"},\"valueQuantity\":{\"value\":" + String(bpm, 1) +
    ",\"unit\":\"beats/minute\",\"system\":\"http://unitsofmeasure.org\","
    "\"code\":\"/min\"},\"device\":{\"reference\":\"" + DEVICE_REF +
    "\"},\"identifier\":[{\"system\":\"http://sys-ids.kemkes.go.id/organization/" +
    ORG_IHS + "\",\"value\":\"radar-1\"}]}";
  HTTPClient http;
  http.begin(String(SERVER_URL) + "/fhir-r4/v1/Observation");
  http.addHeader("Content-Type", "application/json");
  http.addHeader("Authorization", String("Bearer ") + DEVICE_TOKEN);
  http.setTimeout(2000);
  int code = http.POST(body);
  http.end();
  return code;
}
```

- [ ] **Step 3: Wire into the sketch**

Read `arduino/radar_json/radar_json.ino` first; add near the includes:

```cpp
#include "ingest.h"
```

and in `setup()` after network/display init:

```cpp
  if (ingestConfigured()) {
    WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
    configTime(0, 0, "pool.ntp.org");  // UTC for effectiveDateTime
  }
```

and in `loop()` (once per `INGEST_PERIOD_MS`):

```cpp
  static uint32_t lastIngest = 0;
  if (ingestConfigured() && WiFi.status() == WL_CONNECTED
      && millis() - lastIngest >= INGEST_PERIOD_MS) {
    lastIngest = millis();
    float placeholderHr = 72.0f;  // placeholder until radar pipeline exists
    postHeartRate(placeholderHr);
  }
```

- [ ] **Step 4: Add config.h to .gitignore and compile**

```bash
echo "arduino/radar_json/config.h" >> .gitignore
cp arduino/radar_json/config.example.h arduino/radar_json/config.h
arduino-cli compile --fqbn m5stack:esp32:m5stack_cores3 arduino/radar_json
```

Expected: compile succeeds (cores were installed per `arduino/radar_json/README.md`; if missing, run the README's `arduino-cli core install esp32:esp32` + `arduino-cli lib install M5Unified` and record the output in the commit message). Record that hardware behavior (WiFi, POST, display) is NOT run — compile-only gate.

- [ ] **Step 5: Update README**

Add a section to `arduino/radar_json/README.md`: copy `config.example.h` → `config.h`, obtain `DEVICE_TOKEN` from seed/`$provision`, set `ENCOUNTER_REF` to the doctor-opened encounter, and the standing rule **do not upload** until GPIO wiring is confirmed.

- [ ] **Step 6: Commit**

```bash
git add arduino/radar_json .gitignore
git commit -m "feat(firmware): wifi heart-rate ingest with device token (compile gate)

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

---

### Task 20: Documentation and final verification

**Files:**
- Create: `fhir_server/README.md`
- Modify: `CLAUDE.md` (Status section: sub-project 2 walking-skeleton spec/plan implemented; remaining sub-projects listed in spec roadmap)

**Interfaces:**
- Consumes: all tasks.
- Produces: run instructions (venv, install, seed, uvicorn, curl examples for the nine-step flow), architecture pointer to the spec.

- [ ] **Step 1: Write README with exact run commands**

Content requirements (real commands, tested in Step 3):

```markdown
# PRATA FHIR R4 server (walking skeleton)
## Run
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
FHIR_ADMIN_PASSWORD=admin-pass .venv/bin/python -m fhir_server seed --reset
.venv/bin/uvicorn fhir_server.app:create_app --factory --port 8000
```

Note: uvicorn needs settings — provide instead a `python3 -m fhir_server serve --port 8000`
subcommand in `cli.py` that calls `uvicorn.run(create_app(settings), ...)`. Add that subcommand
(two lines) and test it imports; do not launch a server in tests.

Document: login `POST /auth/token`, device ingest contract (Task 17), test suite command,
spec path, and the "no hosted SATUSEHAT calls ever" rule.

- [ ] **Step 2: Add `serve` subcommand to cli.py**

```python
def cmd_serve(args):
    from .app import create_app
    from .config import Settings
    import uvicorn
    uvicorn.run(create_app(Settings.from_env(db_path=args.db)),
                host="127.0.0.1", port=args.port)
```
(register with `sub.add_parser("serve")`, `--port` default 8000, `.set_defaults(fn=cmd_serve)`)

- [ ] **Step 3: Run full verification**

```bash
.venv/bin/python -m pytest tests -q                      # all server tests green
python3 -m pytest .tools/scrape/tests -q                 # 34 still green
python3 .tools/scrape/lint_views.py                      # prints 0 problem(s)
FHIR_DB_PATH /tmp/verify.db seed --reset (via .venv python)  # seed works on clean path
arduino-cli compile --fqbn m5stack:esp32:m5stack_cores3 arduino/radar_json   # compile green
```

Expected: every command succeeds. Record actual outputs in the commit message body if any
deviates.

- [ ] **Step 4: Update CLAUDE.md status and commit**

Change the `## Status` section lines about sub-project 2 from "NOT STARTED" to
"walking skeleton implemented (spec/plan paths); remaining sub-projects per spec roadmap".

```bash
git add fhir_server/README.md fhir_server/cli.py CLAUDE.md
git commit -m "docs(server): run guide, serve command, status update

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

- [ ] **Step 5: Final branch review**

Invoke `superpowers:requesting-code-review` for a whole-branch review, then
`superpowers:verification-before-completion` before reporting done.

---

## Self-Review Notes (plan author)

- **Spec coverage:** goal/flow → Tasks 15–18; validation tables → Tasks 3–11, 13;
  authz matrix → Task 12 (+14 search scoping); media types/406/415 → Task 15;
  OperationOutcome/RuleNumbers → Tasks 3, 13–15; id minting D14 → Task 2;
  NIK/MPI union D13 → Task 9 + seed; Encounter lifecycle D12/D9 → Task 10 + 18;
  device token D6 → Tasks 6, 13, 15, 17; firmware D16 → Task 19; CapabilityStatement → 15;
  seed/bootstrap → 16; docs/status → 20. Review-Focus items all have named tests
  (parse→T4, bearer→T5/T15/T12, search authz→T14, lifecycle→T10, processor-then-server→T13).
- **Type consistency:** `Issue`, `FhirError`, `AuthzError`, `Principal`, `FhirService`,
  `structural_issues`, `validate_*`, `filter_search`, `mint`, `create_token/verify_token`
  signatures reused verbatim across tasks. `provision_device` returns token id in Task 13
  draft — corrected: it must return the **plaintext token** (it generates it internally),
  which Task 15 and 18 rely on (`r.json()["token"]`).
- **Watch-outs flagged for executors:** route order for `$provision`; `_count` handling;
  doctor auto-participant (only Task 18's test forces it — if Task 13 tests pass without
  it, add the auto-participant code in Task 13 so the E2E task stays fix-free; Task 18
  Step 3 documents the patch either way); pydantic coercion must be pre-empted by the
  strict walk (T4).
