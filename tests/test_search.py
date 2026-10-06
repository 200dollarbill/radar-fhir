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
    s = FhirService(conn, Settings(db_path=db_path, jwt_secret="x" * 40))
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
    resources.put(conn, "Encounter", "e1", {
        "resourceType": "Encounter", "id": "e1", "status": "in-progress",
        "subject": {"reference": "Patient/P11111111111"},
        "participant": [{"individual": {"reference": "Practitioner/N12345678"}}]})
    resources.put(conn, "Device", "dev-1", {
        "resourceType": "Device", "id": "dev-1", "status": "active",
        "patient": {"reference": "Patient/P11111111111"}})
    return s


def test_doctor_patient_search_sees_only_participated(svc):
    b = svc.search(DOC, "Patient", {})
    assert b["total"] == 1
    assert b["entry"][0]["resource"]["id"] == "P11111111111"


def test_device_patient_search_param(svc):
    b = svc.search(ADMIN, "Device", {"patient": "Patient/P11111111111"})
    assert b["total"] == 1
    assert b["entry"][0]["resource"]["id"] == "dev-1"


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
    assert b["total"] <= 500
    assert len(b.get("entry", [])) <= 100
