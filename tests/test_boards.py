import sqlite3

import pytest
from fastapi.testclient import TestClient

from fhir_server import db as db_mod
from fhir_server.app import create_app
from fhir_server.config import Settings
from fhir_server.repositories import boards
from fhir_server.routes.deps import get_principal
from test_cli_capture_session import SECRET, seeded  # noqa: F401  (fixture)
from test_rules_observation import raw

KEY_A = "a" * 64
KEY_B = "b" * 64


@pytest.fixture
def conn(tmp_path):
    c = db_mod.connect(str(tmp_path / "b.db"))
    db_mod.init(c)
    return c


def start(conn, serial="AB12CD34EF56", device_id="dev-1", patient="Patient/P1",
          encounter="Encounter/e1"):
    return boards.start_session(conn, serial=serial, device_id=device_id,
                                patient_ref=patient, encounter_ref=encounter,
                                practitioner_ref="Practitioner/N1", label="S001")


def test_register_get_and_find_by_key(conn):
    assert boards.register(conn, "AB12CD34EF56", "dev-1", KEY_A) is True
    row = boards.get(conn, "AB12CD34EF56")
    assert row["device_id"] == "dev-1"
    assert KEY_A not in str(row)  # only the hash is stored
    assert boards.by_key(conn, KEY_A)["serial"] == "AB12CD34EF56"
    assert boards.by_key(conn, KEY_B) is None


def test_reregister_replaces_the_key(conn):
    boards.register(conn, "AB12CD34EF56", "dev-1", KEY_A)
    assert boards.register(conn, "AB12CD34EF56", "dev-1", KEY_B) is False
    assert boards.by_key(conn, KEY_A) is None
    assert boards.by_key(conn, KEY_B)["serial"] == "AB12CD34EF56"


def test_one_open_session_per_board(conn):
    boards.register(conn, "AB12CD34EF56", "dev-1", KEY_A)
    first = start(conn)
    with pytest.raises(sqlite3.IntegrityError):
        start(conn, patient="Patient/P2")
    assert boards.open_session(conn, "AB12CD34EF56")["id"] == first
    assert boards.end_session(conn, first) is True
    assert boards.open_session(conn, "AB12CD34EF56") is None
    start(conn, patient="Patient/P2")  # free again
    assert len(boards.sessions(conn)) == 2
    assert len(boards.sessions(conn, open_only=True)) == 1


class _Req:
    def __init__(self, conn, token):
        self.headers = {"Authorization": f"Bearer {token}"}
        app_state = type("S", (), {"conn": conn,
                                   "settings": Settings(db_path=":memory:",
                                                        jwt_secret=SECRET)})
        self.app = type("A", (), {"state": app_state})


def test_board_key_principal_follows_the_open_session(conn):
    boards.register(conn, "AB12CD34EF56", "dev-1", KEY_A)
    p = get_principal(_Req(conn, KEY_A))
    assert (p.kind, p.device_id, p.patient_id) == ("device", "dev-1", None)
    sid = start(conn)
    assert get_principal(_Req(conn, KEY_A)).patient_id == "Patient/P1"
    boards.end_session(conn, sid)
    assert get_principal(_Req(conn, KEY_A)).patient_id is None


def test_board_key_without_session_cannot_upload(seeded):  # noqa: F811
    conn = db_mod.connect(seeded["db"])
    dev = seeded["seed"]["device_id"]
    boards.register(conn, "AB12CD34EF56", dev, KEY_A)
    app = create_app(Settings(db_path=seeded["db"], jwt_secret=SECRET))
    body = raw(subject={"reference": f"Patient/{seeded['seed']['patient_id']}"},
               device={"reference": f"Device/{dev}"},
               identifier=[{"system": "http://sys-ids.kemkes.go.id/observation/"
                                      + seeded["seed"]["org_id"], "value": "b-1-0"}])
    with TestClient(app) as c:
        r = c.post("/fhir-r4/v1/Observation", json=body,
                   headers={"Authorization": f"Bearer {KEY_A}"})
    assert r.status_code == 403, r.text
