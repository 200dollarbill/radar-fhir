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
