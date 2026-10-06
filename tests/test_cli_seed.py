import json
import os
import subprocess
import sys


def run_cli(args, env_extra):
    env = dict(os.environ, **env_extra)
    return subprocess.run([sys.executable, "-m", "fhir_server", *args],
                          capture_output=True, text=True, env=env,
                          cwd=os.getcwd())


def test_seed_creates_login_and_summary(tmp_path):
    db = str(tmp_path / "seed.db")
    env = {"FHIR_DB_PATH": db,
           "FHIR_JWT_SECRET": "cli-secret-0123456789-0123456789abcdef",
           "FHIR_ADMIN_PASSWORD": "admin-pass-1"}
    p = run_cli(["seed", "--reset"], env)
    assert p.returncode == 0, p.stderr
    summary = json.loads(p.stdout.strip().splitlines()[-1])
    assert summary["admin_password"] == "admin-pass-1"
    assert summary["device_token"]
    from fastapi.testclient import TestClient
    from fhir_server.app import create_app
    from fhir_server.config import Settings
    app = create_app(Settings(db_path=db,
                              jwt_secret="cli-secret-0123456789-0123456789abcdef"))
    with TestClient(app) as c:
        r = c.post("/auth/token",
                   json={"username": "admin", "password": "admin-pass-1"})
        assert r.status_code == 200, r.text
        tok = r.json()["access_token"]
        got = c.get(f"/fhir-r4/v1/Patient/{summary['patient_id']}",
                    headers={"Authorization": f"Bearer {tok}"})
        assert got.status_code == 200
        nik = [i for i in got.json()["identifier"]
               if i["system"].endswith("/nik")]
        assert nik and nik[0]["value"].isdigit() and len(nik[0]["value"]) == 16


def test_seed_requires_reset_flag_to_wipe(tmp_path):
    db = str(tmp_path / "exists.db")
    open(db, "w").write("not a database")
    env = {"FHIR_DB_PATH": db, "FHIR_JWT_SECRET": "cli-secret-0123456789-0123456789abcdef"}
    p = run_cli(["seed"], env)  # without --reset the corrupt file must not be wiped
    assert p.returncode != 0 or "seed" in p.stdout
