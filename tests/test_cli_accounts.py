"""add-account, list-accounts, disable-account: the owner creates every login on the laptop."""
import re

import pytest
from fastapi.testclient import TestClient

from fhir_server import cli
from fhir_server import db as db_mod
from fhir_server.app import create_app
from fhir_server.config import Settings
from fhir_server.repositories import accounts, resources
from test_cli_capture_session import SECRET, count, seeded  # noqa: F401  (fixture)
from test_cli_seed import run_cli
from test_cli_set_password import can_login

NIK = "https://fhir.kemkes.go.id/id/nik"


def add(seeded, *args, env_extra=None):  # noqa: F811
    env = {**seeded["env"], "NEW_PW": "ana-pass-123", **(env_extra or {})}
    return run_cli(["add-account", *args, "--from-env", "NEW_PW"], env)


def all_accounts(db):
    return accounts.list_all(db_mod.connect(db))


def test_add_doctor_creates_practitioner_and_login(seeded):  # noqa: F811
    p = add(seeded, "--role", "doctor", "--username", "dr_ana", "--name", "Ana Putri")
    assert p.returncode == 0, p.stderr
    assert "ana-pass-123" not in p.stdout + p.stderr
    assert can_login(seeded["db"], "dr_ana", "ana-pass-123")
    acct = next(a for a in all_accounts(seeded["db"]) if a["username"] == "dr_ana")
    assert acct["subject_ref"].startswith("Practitioner/")
    prac = resources.get(db_mod.connect(seeded["db"]), "Practitioner",
                         acct["subject_ref"].split("/", 1)[1])
    nik = next(i["value"] for i in prac["identifier"] if i["system"] == NIK)
    assert re.fullmatch(r"9900\d{12}", nik)
    assert prac["name"][0]["text"] == "Ana Putri"
    assert p.stdout.strip() == f"created doctor dr_ana ({acct['subject_ref']})"


def test_add_admin_and_patient(seeded):  # noqa: F811
    p = add(seeded, "--role", "admin", "--username", "admin2")
    assert p.returncode == 0, p.stderr
    assert p.stdout.strip() == "created admin admin2"
    ref = f"Patient/{seeded['seed']['patient_id']}"
    p = add(seeded, "--role", "patient", "--username", "pat2", "--ref", ref)
    assert p.returncode == 0, p.stderr
    assert p.stdout.strip() == f"created patient pat2 ({ref})"
    assert can_login(seeded["db"], "admin2", "ana-pass-123")
    assert can_login(seeded["db"], "pat2", "ana-pass-123")


@pytest.mark.parametrize("args, code, text", [
    (["--role", "doctor", "--username", "doctor", "--name", "X"], 1, "already exists"),
    (["--role", "patient", "--username", "pat3", "--ref", "Patient/nope"], 1, "no Patient/nope"),
    (["--role", "patient", "--username", "pat3"], 2, "--ref"),
    (["--role", "doctor", "--username", "dr_x"], 2, "--name"),
    (["--role", "admin", "--username", "adm3", "--name", "X"], 2, "--name"),
    (["--role", "admin", "--username", "has space"], 2, "username"),
])
def test_refusals_write_nothing(seeded, args, code, text):  # noqa: F811
    before = (len(all_accounts(seeded["db"])), count(seeded, "Practitioner"))
    p = add(seeded, *args)
    assert p.returncode == code, (p.stdout, p.stderr)
    assert text in p.stderr
    assert (len(all_accounts(seeded["db"])), count(seeded, "Practitioner")) == before


def test_unset_password_variable_writes_nothing(seeded):  # noqa: F811
    before = len(all_accounts(seeded["db"]))
    p = run_cli(["add-account", "--role", "admin", "--username", "adm4",
                 "--from-env", "UNSET_XYZ"], seeded["env"])
    assert p.returncode == 2 and "UNSET_XYZ" in p.stderr
    assert len(all_accounts(seeded["db"])) == before


def test_interactive_passwords_must_match(seeded, monkeypatch, capsys):  # noqa: F811
    monkeypatch.setenv("FHIR_JWT_SECRET", SECRET)
    answers = iter(["a1b2c3", "zzzzzz"])
    monkeypatch.setattr("getpass.getpass", lambda prompt="": next(answers))
    before = len(all_accounts(seeded["db"]))
    with pytest.raises(SystemExit) as exc:
        cli.main(["--db", seeded["db"], "add-account", "--role", "admin", "--username", "adm5"])
    assert exc.value.code == 2
    assert "passwords do not match" in capsys.readouterr().err
    assert len(all_accounts(seeded["db"])) == before


def test_list_accounts_shows_role_ref_and_active(seeded):  # noqa: F811
    p = run_cli(["list-accounts"], seeded["env"])
    assert p.returncode == 0, p.stderr
    lines = p.stdout.splitlines()
    assert lines[0] == "username\trole\tref\tactive"
    assert "doctor\tdoctor\tPractitioner/N10000000\tyes" in lines
    assert "admin\tadmin\t-\tyes" in lines


def test_disabled_account_loses_login_and_live_token(seeded):  # noqa: F811
    app = create_app(Settings(db_path=seeded["db"], jwt_secret=SECRET))
    with TestClient(app) as c:
        r = c.post("/auth/token", json={"username": "doctor", "password": "doctor-pw"})
        assert r.status_code == 200
        token = r.json()["access_token"]
        auth = {"Authorization": f"Bearer {token}"}
        assert c.get("/api/sessions", headers=auth).status_code == 200

        p = run_cli(["disable-account", "--username", "doctor"], seeded["env"])
        assert p.returncode == 0, p.stderr
        assert p.stdout.strip() == "disabled doctor"

        r = c.get("/api/sessions", headers=auth)
        assert r.status_code == 401
        assert "Account disabled" in r.text
        r = c.post("/auth/token", json={"username": "doctor", "password": "doctor-pw"})
        assert r.status_code == 401
    p = run_cli(["list-accounts"], seeded["env"])
    assert "doctor\tdoctor\tPractitioner/N10000000\tno" in p.stdout.splitlines()
    p = run_cli(["disable-account", "--username", "nobody"], seeded["env"])
    assert p.returncode == 1 and "no account named nobody" in p.stderr


def test_disabled_username_cannot_be_reused(seeded):  # noqa: F811
    assert run_cli(["disable-account", "--username", "doctor"], seeded["env"]).returncode == 0
    p = add(seeded, "--role", "doctor", "--username", "doctor", "--name", "X")
    assert p.returncode == 1 and "already exists" in p.stderr
