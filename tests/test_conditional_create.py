import json
import os
import subprocess
import sys

import pytest
from fastapi.testclient import TestClient

from fhir_server.app import create_app
from fhir_server.config import Settings
from fhir_server.repositories import resources
from fhir_server.validation.rules_observation import RAW_CODE, RAW_SYSTEM

SECRET = "cc-secret-0123456789-0123456789abcdef"
UCUM = "http://unitsofmeasure.org"
URL = "/fhir-r4/v1/Observation"
COMPONENTS = [("i-voltage", "V"), ("q-voltage", "V"),
              ("accel-x", "[g]"), ("accel-y", "[g]"), ("accel-z", "[g]"),
              ("gyro-x", "deg/s"), ("gyro-y", "deg/s"), ("gyro-z", "deg/s")]


def _comp(code, unit):
    return {"code": {"coding": [{"system": RAW_SYSTEM, "code": code}]},
            "valueSampledData": {
                "origin": {"value": 0, "unit": unit, "system": UCUM,
                           "code": unit},
                "period": 10, "dimensions": 1, "data": "1.65 1.66 1.67"}}


def _login(c, u, pw):
    r = c.post("/auth/token", json={"username": u, "password": pw})
    assert r.status_code == 200, r.text
    return {"Authorization": f"Bearer {r.json()['access_token']}"}


@pytest.fixture
def env(db_path):
    e = dict(os.environ, FHIR_DB_PATH=db_path, FHIR_JWT_SECRET=SECRET,
             FHIR_ADMIN_PASSWORD="adm-pw")
    p = subprocess.run([sys.executable, "-m", "fhir_server", "seed", "--reset"],
                       capture_output=True, text=True, env=e, cwd=os.getcwd())
    assert p.returncode == 0, p.stderr
    s = json.loads(p.stdout.strip().splitlines()[-1])
    app = create_app(Settings(db_path=db_path, jwt_secret=SECRET))
    with TestClient(app) as c:
        admin = _login(c, "admin", s["admin_password"])
        doc = _login(c, "doctor", s["doctor_password"])
        r = c.post("/fhir-r4/v1/Encounter", headers=doc, json={
            "resourceType": "Encounter",
            "identifier": [{"use": "official",
                            "system": "http://sys-ids.kemkes.go.id/encounter/"
                                      f"{s['org_id']}",
                            "value": "KUNJ-CC"}],
            "status": "arrived",
            "statusHistory": [{"status": "arrived", "period": {
                "start": "2026-09-29T10:00:00+00:00"}}],
            "class": {"system": "http://terminology.hl7.org/CodeSystem/v3-ActCode",
                      "code": "AMB", "display": "ambulatory"},
            "subject": {"reference": f"Patient/{s['patient_id']}"},
            "period": {"start": "2026-09-29T10:00:00+00:00"},
            "location": [{"location": {
                "reference": f"Location/{s['location_id']}"}}],
            "serviceProvider": {"reference": f"Organization/{s['org_id']}"},
        })
        assert r.status_code == 201, r.text
        enc = r.json()
        enc_id = enc["id"]
        enc["status"] = "in-progress"
        enc["statusHistory"] = [
            {"status": "arrived",
             "period": {"start": "2026-09-29T10:00:00+00:00"}},
            {"status": "in-progress",
             "period": {"start": "2026-09-29T10:05:00+00:00"}}]
        r = c.put(f"/fhir-r4/v1/Encounter/{enc_id}", headers=doc, json=enc)
        assert r.status_code == 200, r.text
        r = c.post(f"/fhir-r4/v1/Device/{s['device_id']}/$provision",
                   headers=admin, json={"patient": f"Patient/{s['patient_id']}"})
        dev_tok = {"Authorization": f"Bearer {r.json()['token']}"}
        # a second device assigned to the same patient
        resources.put(c.app.state.conn, "Device", "dev-other",
                      {"resourceType": "Device", "id": "dev-other",
                       "status": "active"})
        r = c.post("/fhir-r4/v1/Device/dev-other/$provision", headers=admin,
                   json={"patient": f"Patient/{s['patient_id']}"})
        assert r.status_code == 200, r.text
        other_tok = {"Authorization": f"Bearer {r.json()['token']}"}
        yield {"c": c, "s": s, "enc_id": enc_id, "dev": dev_tok,
               "other": other_tok, "admin": admin, "doc": doc}


def chunk(env, value="cap-1-0", device=None):
    s = env["s"]
    return {
        "resourceType": "Observation", "status": "final",
        "code": {"coding": [{"system": RAW_SYSTEM, "code": RAW_CODE,
                             "display": "Raw radar I/Q capture"}]},
        "subject": {"reference": f"Patient/{s['patient_id']}"},
        "encounter": {"reference": f"Encounter/{env['enc_id']}"},
        "effectiveDateTime": "2026-09-29T10:06:00+00:00",
        "device": {"reference": f"Device/{device or s['device_id']}"},
        "identifier": [{"system": "http://sys-ids.kemkes.go.id/observation/"
                                  f"{s['org_id']}", "value": value}],
        "component": [_comp(c, u) for c, u in COMPONENTS],
    }


def post(env, body, who="dev", header=None):
    h = dict(env[who])
    if header is not None:
        h["If-None-Exist"] = header
    return env["c"].post(URL, headers=h, json=body)


def count(env):
    return len(resources.list(env["c"].app.state.conn, "Observation"))


def test_first_post_201_second_200_same_id(env):
    r1 = post(env, chunk(env), header="identifier=cap-1-0")
    r2 = post(env, chunk(env), header="identifier=cap-1-0")
    assert r1.status_code == 201, r1.text
    assert r2.status_code == 200, r2.text
    assert r1.json()["id"] == r2.json()["id"]


def test_second_post_stores_no_new_row(env):
    post(env, chunk(env), header="identifier=cap-1-0")
    post(env, chunk(env), header="identifier=cap-1-0")
    assert count(env) == 1


def test_system_pipe_value_form_matches_value_only_key(env):
    post(env, chunk(env), header="identifier=cap-1-0")
    sysv = "http://sys-ids.kemkes.go.id/observation/" + env["s"]["org_id"]
    r = post(env, chunk(env), header=f"identifier={sysv}|cap-1-0")
    assert r.status_code == 200, r.text


def test_retry_after_encounter_finished_returns_200(env):
    r1 = post(env, chunk(env), header="identifier=cap-1-0")
    assert r1.status_code == 201
    c, doc = env["c"], env["doc"]
    e = c.get(f"/fhir-r4/v1/Encounter/{env['enc_id']}", headers=doc).json()
    e["status"] = "finished"
    e["statusHistory"] = e["statusHistory"] + [
        {"status": "finished",
         "period": {"start": "2026-09-29T10:05:00+00:00",
                    "end": "2026-09-29T11:00:00+00:00"}}]
    e["period"]["end"] = "2026-09-29T11:00:00+00:00"
    assert c.put(f"/fhir-r4/v1/Encounter/{env['enc_id']}", headers=doc,
                 json=e).status_code == 200
    r2 = post(env, chunk(env), header="identifier=cap-1-0")
    assert r2.status_code == 200, r2.text
    assert r2.json()["id"] == r1.json()["id"]


def test_other_device_gets_403_not_the_record(env):
    post(env, chunk(env), header="identifier=cap-1-0")
    r = post(env, chunk(env, device="dev-other"), who="other",
             header="identifier=cap-1-0")
    assert r.status_code == 403, r.text
    assert r.json()["resourceType"] == "OperationOutcome"
    assert "component" not in r.text


def test_header_param_other_than_identifier_400(env):
    r = post(env, chunk(env), header="code=cap-1-0")
    assert r.status_code == 400


@pytest.mark.parametrize("h", ["identifier", "identifier=", "identifier=a&identifier=b"])
def test_malformed_header_400(env, h):
    r = post(env, chunk(env), header=h)
    assert r.status_code == 400
    assert r.json()["resourceType"] == "OperationOutcome"


def test_header_value_not_in_payload_400(env):
    r = post(env, chunk(env, value="cap-1-0"), header="identifier=cap-9-9")
    assert r.status_code == 400
    assert count(env) == 0


def test_non_observation_type_400(env):
    r = env["c"].post("/fhir-r4/v1/Organization",
                      headers={**env["admin"], "If-None-Exist": "identifier=x"},
                      json={"resourceType": "Organization", "name": "K",
                            "identifier": [{"value": "x"}]})
    assert r.status_code == 400


def test_invalid_payload_400_records_no_key(env):
    bad = chunk(env)
    bad["component"] = bad["component"][1:]  # drops i-voltage
    r = post(env, bad, header="identifier=cap-1-0")
    assert r.status_code == 400
    r = post(env, chunk(env), header="identifier=cap-1-0")
    assert r.status_code == 201, r.text


def test_key_of_deleted_resource_creates_again(env):
    r1 = post(env, chunk(env), header="identifier=cap-1-0")
    d = env["c"].delete(f"{URL}/{r1.json()['id']}", headers=env["admin"])
    assert d.status_code == 204
    r2 = post(env, chunk(env), header="identifier=cap-1-0")
    assert r2.status_code == 201, r2.text
    assert r2.json()["id"] != r1.json()["id"]


def test_plain_post_may_reuse_identifier(env):
    assert post(env, chunk(env, value="radar-1")).status_code == 201
    assert post(env, chunk(env, value="radar-1")).status_code == 201


def test_plain_post_ignores_conditional_keys(env):
    assert post(env, chunk(env, value="radar-1"),
                header="identifier=radar-1").status_code == 201
    assert post(env, chunk(env, value="radar-1")).status_code == 201
    assert count(env) == 2


def test_capability_statement_advertises_conditional_create(env):
    body = env["c"].get("/fhir-r4/v1/metadata").json()
    obs = [r for r in body["rest"][0]["resource"] if r["type"] == "Observation"][0]
    assert obs["conditionalCreate"] is True
