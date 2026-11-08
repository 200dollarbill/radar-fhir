import json
import os
import re

import pytest
from fastapi.testclient import TestClient

from fhir_server.app import create_app
from fhir_server.config import Settings
from fhir_server.repositories import resources
from test_cli_seed import run_cli
from test_rules_observation import raw

SECRET = "cap-secret-0123456789-0123456789abcdef"


@pytest.fixture
def seeded(tmp_path):
    db = str(tmp_path / "cap.db")
    env = {"FHIR_DB_PATH": db, "FHIR_JWT_SECRET": SECRET,
           "FHIR_ADMIN_PASSWORD": "admin-pass-1"}
    p = run_cli(["seed", "--reset"], env)
    assert p.returncode == 0, p.stderr
    return {"db": db, "env": env, "seed": json.loads(p.stdout.splitlines()[-1])}


def card_of(seeded, label="S001"):
    p = run_cli(["capture-session", "--label", label], seeded["env"])
    assert p.returncode == 0, p.stderr
    return json.loads(p.stdout.strip().splitlines()[-1])


def count(seeded, type_):
    from fhir_server import db as db_mod
    return len(resources.list(db_mod.connect(seeded["db"]), type_))


def test_card_has_all_fields_and_references(seeded):
    card = card_of(seeded)
    assert set(card) == {"token", "patient", "encounter", "device", "org",
                         "label"}
    assert card["label"] == "S001"
    assert card["token"]
    assert re.fullmatch(r"Patient/\S+", card["patient"])
    assert re.fullmatch(r"Encounter/\S+", card["encounter"])
    assert card["device"] == f"Device/{seeded['seed']['device_id']}"
    assert card["org"] == seeded["seed"]["org_id"]


def test_card_can_post_a_raw_chunk(seeded):
    card = card_of(seeded)
    app = create_app(Settings(db_path=seeded["db"], jwt_secret=SECRET))
    body = raw(subject={"reference": card["patient"]},
               encounter={"reference": card["encounter"]},
               device={"reference": card["device"]},
               identifier=[{"system": "http://sys-ids.kemkes.go.id/observation/"
                                      + card["org"], "value": "cap-1-0"}])
    with TestClient(app) as c:
        r = c.post("/fhir-r4/v1/Observation", json=body,
                   headers={"Authorization": f"Bearer {card['token']}"})
        assert r.status_code == 201, r.text


def test_doctor_can_read_the_chunk(seeded):
    card = card_of(seeded)
    app = create_app(Settings(db_path=seeded["db"], jwt_secret=SECRET))
    body = raw(subject={"reference": card["patient"]},
               encounter={"reference": card["encounter"]},
               device={"reference": card["device"]},
               identifier=[{"system": "http://sys-ids.kemkes.go.id/observation/"
                                      + card["org"], "value": "cap-1-0"}])
    with TestClient(app) as c:
        r = c.post("/fhir-r4/v1/Observation", json=body,
                   headers={"Authorization": f"Bearer {card['token']}"})
        assert r.status_code == 201, r.text
        oid = r.json()["id"]
        t = c.post("/auth/token", json={"username": "doctor",
                                        "password": "doctor-pw"})
        got = c.get(f"/fhir-r4/v1/Observation/{oid}", headers={
            "Authorization": f"Bearer {t.json()['access_token']}"})
        assert got.status_code == 200, got.text


def test_two_sessions_get_different_patients(seeded):
    a = card_of(seeded, "A")
    b = card_of(seeded, "B")
    assert a["patient"] != b["patient"]
    assert a["encounter"] != b["encounter"]


def test_same_label_twice_succeeds(seeded):
    a = card_of(seeded, "S001")
    b = card_of(seeded, "S001")
    assert a["encounter"] != b["encounter"]


def test_unseeded_db_exits_1_with_message(tmp_path):
    env = {"FHIR_DB_PATH": str(tmp_path / "empty.db"),
           "FHIR_JWT_SECRET": SECRET}
    p = run_cli(["capture-session", "--label", "S001"], env)
    assert p.returncode == 1 and "seed" in p.stderr


@pytest.mark.parametrize("label", ["a b", "", "x" * 33])
def test_bad_label_rejected(seeded, label):
    before = (count(seeded, "Patient"), count(seeded, "Encounter"))
    p = run_cli(["capture-session", "--label", label], seeded["env"])
    assert p.returncode != 0
    assert before == (count(seeded, "Patient"), count(seeded, "Encounter"))
