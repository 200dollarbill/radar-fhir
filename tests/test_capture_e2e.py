"""Chunk round trip: simulated lines -> real JS parser/chunker/builder -> real server."""
import json
import subprocess
from pathlib import Path

from fastapi.testclient import TestClient

from fhir_server.app import create_app
from fhir_server.config import Settings
from test_cli_capture_session import SECRET, card_of, seeded  # noqa: F401

FIXTURE = Path(__file__).resolve().parent.parent / "receiver/tests/fixtures/make_chunk.mjs"
CODE_TO_CHANNEL = {"i-voltage": "I", "q-voltage": "Q", "accel-x": "ax",
                   "accel-y": "ay", "accel-z": "az", "gyro-x": "gx",
                   "gyro-y": "gy", "gyro-z": "gz"}


def test_chunk_round_trip(seeded):  # noqa: F811
    card = card_of(seeded)
    # No skip: a missing node must fail this test, not hide the contract.
    p = subprocess.run(["node", str(FIXTURE), json.dumps(card)],
                       capture_output=True, text=True)
    assert p.returncode == 0, p.stderr
    made = json.loads(p.stdout)
    obs, identifier, expected = made["observation"], made["identifier"], made["expected"]
    assert any("E" in v for v in expected["I"]), "fixture must include a gap"

    app = create_app(Settings(db_path=seeded["db"], jwt_secret=SECRET))
    auth = {"Authorization": f"Bearer {card['token']}"}

    def post():
        return c.post("/fhir-r4/v1/Observation", json=obs,
                      headers={**auth, "If-None-Exist": f"identifier={identifier}"})

    with TestClient(app) as c:
        r1 = post()
        assert r1.status_code == 201, r1.text
        r2 = post()
        assert r2.status_code == 200, r2.text
        assert r2.json()["id"] == r1.json()["id"]
        stored = c.get(f"/fhir-r4/v1/Observation/{r1.json()['id']}",
                       headers=auth).json()
    assert len(stored["component"]) == 8
    for comp in stored["component"]:
        channel = CODE_TO_CHANNEL[comp["code"]["coding"][0]["code"]]
        got = comp["valueSampledData"]["data"].split(" ")
        assert got == expected[channel], channel
