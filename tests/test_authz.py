import pytest
from fhir_server import db
from fhir_server.auth.jwt import Principal
from fhir_server.authz import (AuthzError, check, filter_search,
                               participates_in_patient)
from fhir_server.repositories import resources

ADMIN = Principal(kind="admin", account_id="a", role="admin", ref=None)
DOC = Principal(kind="doctor", account_id="d", role="doctor",
                ref="Practitioner/N12345678")
PAT = Principal(kind="patient", account_id="p", role="patient",
                ref="Patient/P11111111111")
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
    with pytest.raises(AuthzError):
        check(DOC, "create", "Organization", conn=conn)
    with pytest.raises(AuthzError):
        check(PAT, "create", "Patient", conn=conn)
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
        check(PAT, "read", "Practitioner",
              {"resourceType": "Practitioner"}, conn=conn)


def test_patient_search_autoscopes_to_self(db_path):
    conn = make_conn(db_path)
    out = filter_search(PAT, "Observation", {}, conn)
    assert out["subject"] == "Patient/P11111111111"
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
    assert not participates_in_patient(conn, "Practitioner/N99999999",
                                       "P11111111111")
