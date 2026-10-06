import pytest
from fhir_server import db
from fhir_server.auth.jwt import Principal
from fhir_server.config import Settings
from fhir_server.repositories import resources
from fhir_server.services.fhir_service import FhirService, FhirError

ADMIN = Principal(kind="admin", role="admin", account_id="a")
DEV = Principal(kind="device", device_id="dev-1",
                patient_id="Patient/P11111111111")


@pytest.fixture
def svc(db_path):
    conn = db.connect(db_path); db.init(conn)
    settings = Settings(db_path=db_path, jwt_secret="x" * 40)
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
                               "period": {"start": "2026-01-10T10:00:00+00:00"}}],
            "class": {"system": "http://terminology.hl7.org/CodeSystem/v3-ActCode",
                      "code": "AMB"},
            "subject": {"reference": "Patient/PDoesNotExist"},
            "period": {"start": "2026-01-10T10:00:00+00:00"},
            "location": [{"location": {"reference": "Location/loc-1"}}],
            "serviceProvider": {"reference": "Organization/100000001"}})
    assert e.value.status == 400


def test_read_missing_404(svc):
    with pytest.raises(FhirError) as e:
        svc.read(ADMIN, "Patient", "P404")
    assert e.value.status == 404


def test_update_bumps_version(svc):
    svc.create(ADMIN, "Organization", org_payload())
    orgs = resources.list(svc.conn, "Organization")
    target = [o for o in orgs if o["name"] == "Klinik Satu"][0]
    payload = dict(target); payload["name"] = "Klinik Dua"
    _, doc, ver = svc.update(ADMIN, "Organization", target["id"], payload)
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


def test_create_canonicalizes_offsets_to_utc(svc):
    payload = {
        "resourceType": "Encounter",
        "identifier": [{"use": "official",
                        "system": "http://sys-ids.kemkes.go.id/encounter/100000001",
                        "value": "K-UTC"}],
        "status": "arrived",
        "statusHistory": [{"status": "arrived",
                           "period": {"start": "2026-01-10T17:00:00+07:00"}}],
        "class": {"system": "http://terminology.hl7.org/CodeSystem/v3-ActCode",
                  "code": "AMB"},
        "subject": {"reference": "Patient/P11111111111"},
        "period": {"start": "2026-01-10T17:00:00+07:00"},
        "location": [{"location": {"reference": "Location/loc-1"}}],
        "serviceProvider": {"reference": "Organization/100000001"}}
    _, doc, _ = svc.create(ADMIN, "Encounter", payload)
    assert doc["period"]["start"] == "2026-01-10T10:00:00+00:00"
