"""set-password: change an account's password without re-seeding (which wipes the db)."""
from fastapi.testclient import TestClient

from fhir_server.app import create_app
from fhir_server.config import Settings
from test_cli_capture_session import SECRET, seeded  # noqa: F401  (fixture)
from test_cli_seed import run_cli


def can_login(db, user, pw):
    app = create_app(Settings(db_path=db, jwt_secret=SECRET))
    with TestClient(app) as c:
        return c.post("/auth/token", json={"username": user, "password": pw}).status_code == 200


def test_sets_the_password_from_an_env_variable(seeded):  # noqa: F811
    env = {**seeded["env"], "NEW_PW": "fresh-admin-pass"}
    p = run_cli(["set-password", "--username", "admin", "--from-env", "NEW_PW"], env)
    assert p.returncode == 0, p.stderr
    assert "fresh-admin-pass" not in p.stdout + p.stderr  # never echoes the password
    assert can_login(seeded["db"], "admin", "fresh-admin-pass")
    assert not can_login(seeded["db"], "admin", "admin-pass-1")


def test_unknown_user_and_missing_variable_fail_cleanly(seeded):  # noqa: F811
    p = run_cli(["set-password", "--username", "nobody", "--from-env", "FHIR_ADMIN_PASSWORD"], seeded["env"])
    assert p.returncode == 1 and "no active account" in p.stderr
    env = {k: v for k, v in seeded["env"].items()}
    p = run_cli(["set-password", "--username", "admin", "--from-env", "UNSET_VAR_XYZ"], env)
    assert p.returncode == 2 and "UNSET_VAR_XYZ" in p.stderr
    assert can_login(seeded["db"], "admin", "admin-pass-1")  # unchanged
