import json
import os
import subprocess
import sys

import pytest
from fastapi.testclient import TestClient

from fhir_server.app import create_app
from fhir_server.config import Settings

E2E_SECRET = "e2e-secret-0123456789-0123456789abcdef"


@pytest.fixture
def scenario(db_path):
    # 1. seed via CLI
    env = dict(os.environ, FHIR_DB_PATH=db_path, FHIR_JWT_SECRET=E2E_SECRET,
               FHIR_ADMIN_PASSWORD="adm-pw")
    p = subprocess.run([sys.executable, "-m", "fhir_server", "seed", "--reset"],
                       capture_output=True, text=True, env=env, cwd=os.getcwd())
    assert p.returncode == 0, p.stderr
    summary = json.loads(p.stdout.strip().splitlines()[-1])
    app = create_app(Settings(db_path=db_path, jwt_secret=E2E_SECRET))
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
    # 3. re-provision to prove the route (seed already provisioned one)
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
    r = c.get(f"/fhir-r4/v1/Observation?subject=Patient/{s['patient_id']}",
              headers=doc)
    assert r.status_code == 200
    assert r.json()["total"] == 1
    r = c.get(f"/fhir-r4/v1/Observation/{obs_id}", headers=doc)
    assert r.status_code == 200
    # 8. finish the visit
    body_enc = c.get(f"/fhir-r4/v1/Encounter/{enc_id}", headers=doc).json()
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
    r = c.get("/fhir-r4/v1/Patient/P99999999999", headers=pat)
    assert r.status_code in (403, 404)
    # device cannot read Patient
    r = c.get(f"/fhir-r4/v1/Patient/{s['patient_id']}",
              headers={"Authorization": f"Bearer {device_token}"})
    assert r.status_code == 403
    # no anonymous access
    assert c.get("/fhir-r4/v1/Patient").status_code == 401
