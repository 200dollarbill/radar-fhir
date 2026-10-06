import pytest
from fastapi.testclient import TestClient

from fhir_server.app import create_app
from fhir_server.config import Settings
from fhir_server.repositories import devices, resources
from device_client import client as dc

ORG = "100000001"


@pytest.fixture
def env(db_path):
    settings = Settings(db_path=db_path,
                        jwt_secret="dc-secret-0123456789-0123456789abcdef")
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
            {"status": "arrived",
             "period": {"start": "2026-09-29T10:00:00+00:00"}},
            {"status": "in-progress",
             "period": {"start": "2026-09-29T10:05:00+00:00"}}],
        "class": {"system": "http://terminology.hl7.org/CodeSystem/v3-ActCode",
                  "code": "AMB"},
        "period": {"start": "2026-09-29T10:00:00+00:00"},
        "location": [{"location": {"reference": "Location/L1"}}],
        "serviceProvider": {"reference": f"Organization/{ORG}"}})
    resources.put(conn, "Device", "dev-1",
                  {"resourceType": "Device", "id": "dev-1", "status": "active"})
    devices.create_token(conn, "dev-1", "Patient/P11111111111",
                         "device-secret-token")
    c = TestClient(app)
    return {"client": c, "token": "device-secret-token", "conn": conn}


def _post_fn(c):
    def post_fn(url, **kw):
        path = url.replace("http://test", "")
        r = c.post(path, **kw)
        return type("R", (), {"status_code": r.status_code,
                              "json": lambda self: r.json()})()
    return post_fn


def test_submit_success(env):
    status, body = dc.submit_heart_rate(
        "http://test", env["token"], patient="Patient/P11111111111",
        encounter="Encounter/e1", device="Device/dev-1", bpm=72,
        effective_datetime="2026-09-29T10:06:00+00:00",
        post_fn=_post_fn(env["client"]))
    assert status == 201
    assert body["resourceType"] == "Observation"
    assert body["valueQuantity"]["value"] == 72


def test_submit_wrong_encounter_rejected(env):
    status, body = dc.submit_heart_rate(
        "http://test", env["token"], patient="Patient/P11111111111",
        encounter="Encounter/ghost", device="Device/dev-1", bpm=72,
        effective_datetime="2026-09-29T10:06:00+00:00",
        post_fn=_post_fn(env["client"]))
    assert status == 400
    assert body["resourceType"] == "OperationOutcome"
