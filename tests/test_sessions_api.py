import pytest
from fastapi.testclient import TestClient

from fhir_server import db as db_mod
from fhir_server.app import create_app
from fhir_server.config import Settings
from fhir_server.repositories import boards
from fhir_server.repositories import resources as res
from test_cli_capture_session import SECRET, seeded  # noqa: F401  (fixture)
from test_rules_observation import raw

BOARD = "AB12CD34EF56"
KEY_A = "a" * 64
KEY_B = "b" * 64


@pytest.fixture
def api(seeded):  # noqa: F811
    app = create_app(Settings(db_path=seeded["db"], jwt_secret=SECRET))
    with TestClient(app) as c:
        c.seed = seeded["seed"]
        c.conn = app.state.conn
        yield c


def login(c, user, pw):
    r = c.post("/auth/token", json={"username": user, "password": pw})
    assert r.status_code == 200, r.text
    return {"Authorization": f"Bearer {r.json()['access_token']}"}


@pytest.fixture
def admin(api):
    return login(api, "admin", "admin-pass-1")


@pytest.fixture
def doctor(api):
    return login(api, "doctor", "doctor-pw")


def board_key(key):
    return {"Authorization": f"Bearer {key}"}


def register(api, admin, serial=BOARD, key=KEY_A):
    return api.post("/api/boards", json={"id": serial, "key": key}, headers=admin)


def new_patient(api, admin, label="S001"):
    r = api.post("/api/patients", json={"label": label}, headers=admin)
    assert r.status_code == 201, r.text
    return r.json()["patient"]


def open_session(api, who, patient, serial=BOARD, label="S001", **extra):
    return api.post("/api/sessions", headers=who,
                    json={"board": serial, "patient": patient, "label": label, **extra})


def chunk_for(card, value="b-1-0"):
    return raw(subject={"reference": card["patient"]},
               encounter={"reference": card["encounter"]},
               device={"reference": card["device"]},
               identifier=[{"system": "http://sys-ids.kemkes.go.id/observation/"
                                      + card["org"], "value": value}])


def test_admin_registers_then_rekeys_a_board(api, admin):
    r = register(api, admin)
    assert r.status_code == 201, r.text
    device = r.json()["device"]
    dev = res.get(api.conn, "Device", device.split("/")[1])
    assert dev["serialNumber"] == BOARD
    assert {"system": "urn:prata:board", "value": BOARD} in dev["identifier"]
    r = register(api, admin, key=KEY_B)
    assert r.status_code == 200 and r.json()["device"] == device
    assert boards.by_key(api.conn, KEY_A) is None


@pytest.mark.parametrize("body", [
    {"id": "ab12cd34ef56", "key": KEY_A},          # lower case id
    {"id": "AB12CD34EF5", "key": KEY_A},           # too short
    {"id": BOARD, "key": "A" * 64},                # key must be lower hex
    {"id": BOARD, "key": "a" * 63},
    {"id": "SIM-1234567", "key": KEY_A},
])
def test_register_rejects_bad_ids_and_keys(api, admin, body):
    assert api.post("/api/boards", json=body, headers=admin).status_code == 400


def test_simulated_board_ids_are_accepted(api, admin):
    assert register(api, admin, serial="SIM-0A1B2C3D").status_code == 201


def test_only_admins_register_boards_and_create_patients(api, doctor):
    assert register(api, doctor).status_code == 403
    assert api.post("/api/patients", json={"label": "S1"}, headers=doctor).status_code == 403
    assert api.post("/api/boards", json={"id": BOARD, "key": KEY_A}).status_code == 401


def test_admin_creates_a_test_patient(api, admin):
    r = api.post("/api/patients", json={"label": "S001"}, headers=admin)
    assert r.status_code == 201
    assert r.json()["name"] == "Sesi S001"
    assert api.post("/api/patients", json={"label": "bad label!"},
                    headers=admin).status_code == 400


def test_session_gives_the_board_its_card_and_upload_works(api, admin):
    register(api, admin)
    patient = new_patient(api, admin)
    r = open_session(api, admin, patient)
    assert r.status_code == 201, r.text
    sess = r.json()
    enc = res.get(api.conn, "Encounter", sess["encounter"].split("/")[1])
    assert enc["status"] == "in-progress"
    doc_ref = f"Practitioner/{api.seed['practitioner_id']}"
    assert any(p["individual"]["reference"] == doc_ref for p in enc["participant"])

    r = api.post("/api/board/session", json={"id": BOARD}, headers=board_key(KEY_A))
    assert r.status_code == 200, r.text
    card = r.json()
    assert set(card) == {"board", "device", "patient", "patientName", "encounter",
                         "org", "label", "session"}
    assert card["patient"] == patient and card["label"] == "S001"
    assert card["patientName"] == "Sesi S001"
    r = api.post("/fhir-r4/v1/Observation", json=chunk_for(card), headers=board_key(KEY_A))
    assert r.status_code == 201, r.text


def test_a_busy_board_cannot_get_a_second_session(api, admin):
    register(api, admin)
    first = open_session(api, admin, new_patient(api, admin, "S1")).json()
    r = open_session(api, admin, new_patient(api, admin, "S2"), label="S2")
    assert r.status_code == 409
    assert boards.open_session(api.conn, BOARD)["id"] == first["id"]


def test_unregistered_board_cannot_open_a_session(api, admin):
    assert open_session(api, admin, new_patient(api, admin)).status_code == 404


def test_board_session_errors(api, admin):
    register(api, admin)
    ok = {"id": BOARD}
    assert api.post("/api/board/session", json=ok, headers=board_key(KEY_B)).status_code == 401
    assert api.post("/api/board/session", json={"id": "FFFFFFFFFFFF"},
                    headers=board_key(KEY_A)).status_code == 401
    assert api.post("/api/board/session", json=ok).status_code == 401
    r = api.post("/api/board/session", json=ok, headers=board_key(KEY_A))
    assert r.status_code == 404
    assert "no open session" in r.text.lower()


def test_ending_a_session_finishes_the_visit_and_stops_uploads(api, admin):
    register(api, admin)
    sess = open_session(api, admin, new_patient(api, admin)).json()
    card = api.post("/api/board/session", json={"id": BOARD}, headers=board_key(KEY_A)).json()
    r = api.post(f"/api/sessions/{sess['id']}/end", headers=admin)
    assert r.status_code == 200, r.text
    enc = res.get(api.conn, "Encounter", sess["encounter"].split("/")[1])
    assert enc["status"] == "finished" and enc["period"]["end"]
    assert api.post("/api/board/session", json={"id": BOARD},
                    headers=board_key(KEY_A)).status_code == 404
    r = api.post("/fhir-r4/v1/Observation", json=chunk_for(card, "b-2-0"),
                 headers=board_key(KEY_A))
    assert r.status_code == 403
    assert api.post(f"/api/sessions/{sess['id']}/end", headers=admin).status_code == 409


def test_doctor_opens_sessions_only_for_their_patients(api, admin, doctor):
    register(api, admin)
    patient = new_patient(api, admin)
    # not yet a participant
    assert open_session(api, doctor, patient).status_code == 403
    # an admin-opened session with this doctor makes them a participant
    first = open_session(api, admin, patient).json()
    api.post(f"/api/sessions/{first['id']}/end", headers=admin)
    r = open_session(api, doctor, patient, label="S001-b")
    assert r.status_code == 201, r.text
    assert r.json()["practitioner"] == f"Practitioner/{api.seed['practitioner_id']}"
    assert api.post(f"/api/sessions/{r.json()['id']}/end", headers=doctor).status_code == 200


def test_doctor_sees_and_ends_only_their_own_sessions(api, admin, doctor):
    register(api, admin)
    register(api, admin, serial="SIM-00000001", key=KEY_B)
    mine = open_session(api, admin, new_patient(api, admin, "S1"), label="S1").json()
    other = boards.start_session(
        api.conn, serial="SIM-00000001",
        device_id=boards.get(api.conn, "SIM-00000001")["device_id"],
        patient_ref="Patient/x", encounter_ref="Encounter/y",
        practitioner_ref="Practitioner/someone-else", label="S2")
    listed = api.get("/api/sessions", headers=doctor).json()
    assert [s["id"] for s in listed] == [mine["id"]]
    assert len(api.get("/api/sessions", headers=admin).json()) == 2
    assert api.post(f"/api/sessions/{other}/end", headers=doctor).status_code == 403


def test_open_filter_and_board_list(api, admin, doctor):
    register(api, admin)
    sess = open_session(api, admin, new_patient(api, admin)).json()
    boards_out = api.get("/api/boards", headers=doctor).json()
    assert boards_out[0]["id"] == BOARD
    assert boards_out[0]["session"]["id"] == sess["id"]
    api.post(f"/api/sessions/{sess['id']}/end", headers=admin)
    assert api.get("/api/sessions?open=1", headers=admin).json() == []
    ended = api.get("/api/sessions", headers=admin).json()[0]
    assert ended["ended"] and ended["patientName"] == "Sesi S001"
    assert api.get("/api/boards", headers=admin).json()[0]["session"] is None


def test_board_key_cannot_use_the_dashboard_api(api, admin):
    register(api, admin)
    assert api.get("/api/sessions", headers=board_key(KEY_A)).status_code == 403
    assert api.get("/api/boards", headers=board_key(KEY_A)).status_code == 403
