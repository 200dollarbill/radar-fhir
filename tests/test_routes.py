import pytest
from fastapi.testclient import TestClient

from fhir_server.app import create_app
from fhir_server.auth.passwords import hash_password
from fhir_server.config import Settings
from fhir_server.repositories import accounts, devices, resources


@pytest.fixture
def client(db_path):
    settings = Settings(db_path=db_path,
                        jwt_secret="route-secret-0123456789-0123456789abcdef")
    app = create_app(settings)
    with TestClient(app) as c:
        yield c


def admin_token(c):
    conn = c.app.state.conn
    accounts.create(conn, "admin", hash_password("admin-pw"), "admin", None)
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
    assert r.status_code == 201
    assert r.headers["content-type"].startswith("application/fhir+json")
    assert r.headers["location"].startswith("/fhir-r4/v1/Organization/")


def test_bad_accept_406(client):
    tok = admin_token(client)
    r = client.get("/fhir-r4/v1/Patient/x",
                   headers={**hdr(tok), "Accept": "application/xml"})
    assert r.status_code == 406


def test_wrong_content_type_415(client):
    tok = admin_token(client)
    r = client.post("/fhir-r4/v1/Organization",
                    headers={**hdr(tok), "Content-Type": "application/xml"},
                    content=b"<x/>")
    assert r.status_code == 415


def test_device_provision_and_use(client):
    tok = admin_token(client)
    conn = client.app.state.conn
    resources.put(conn, "Device", "dev-1",
                  {"resourceType": "Device", "id": "dev-1", "status": "active"})
    resources.put(conn, "Patient", "P11111111111",
                  {"resourceType": "Patient", "id": "P11111111111"})
    r = client.post("/fhir-r4/v1/Device/dev-1/$provision", headers=hdr(tok),
                    json={"patient": "Patient/P11111111111"})
    assert r.status_code == 200, r.text
    device_tok = r.json()["token"]
    r2 = client.get("/fhir-r4/v1/Patient/P11111111111", headers=hdr(device_tok))
    assert r2.status_code == 403  # device cannot read Patient
    assert devices.resolve_token(conn, device_tok)["patient_id"] == \
        "Patient/P11111111111"


def test_account_admin_flow(client):
    tok = admin_token(client)
    # the Practitioner resource must exist before an account can reference it
    resources.put(client.app.state.conn, "Practitioner", "N12345678",
                  {"resourceType": "Practitioner", "id": "N12345678"})
    r = client.post("/fhir-r4/v1/admin/accounts", headers=hdr(tok),
                    json={"username": "doc1", "password": "pw",
                          "role": "doctor", "ref": "Practitioner/N12345678"})
    assert r.status_code == 201
    r2 = client.post("/auth/token", json={"username": "doc1", "password": "pw"})
    assert r2.status_code == 200
    r3 = client.post("/fhir-r4/v1/admin/accounts",
                     headers=hdr(r2.json()["access_token"]),
                     json={"username": "x", "password": "y",
                           "role": "admin", "ref": None})
    assert r3.status_code == 403


def test_auth_non_dict_body_is_not_500(client):
    r = client.post("/auth/token", json=[1, 2, 3])
    assert r.status_code == 401
    assert r.json()["resourceType"] == "OperationOutcome"


def test_admin_accounts_non_dict_body_400(client):
    tok = admin_token(client)
    r = client.post("/fhir-r4/v1/admin/accounts", headers=hdr(tok),
                    json=["not", "a", "dict"])
    assert r.status_code == 400
    assert r.json()["resourceType"] == "OperationOutcome"


def test_duplicate_account_409(client):
    tok = admin_token(client)
    payload = {"username": "dup", "password": "pw", "role": "doctor",
               "ref": None}
    assert client.post("/fhir-r4/v1/admin/accounts",
                       headers=hdr(tok), json=payload).status_code == 201
    r = client.post("/fhir-r4/v1/admin/accounts", headers=hdr(tok),
                    json=payload)
    assert r.status_code == 409
    assert r.json()["resourceType"] == "OperationOutcome"


def test_delete_honours_accept_406(client):
    tok = admin_token(client)
    r = client.delete("/fhir-r4/v1/Patient/nope",
                      headers={**hdr(tok), "Accept": "application/xml"})
    assert r.status_code == 406


def test_account_ref_must_exist(client):
    tok = admin_token(client)
    r = client.post("/fhir-r4/v1/admin/accounts", headers=hdr(tok),
                    json={"username": "doc-bad", "password": "pw",
                          "role": "doctor", "ref": "Practitioner/NOPE"})
    assert r.status_code == 400
    assert r.json()["resourceType"] == "OperationOutcome"
