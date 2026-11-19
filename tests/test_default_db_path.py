from fhir_server.config import Settings
from test_cli_seed import run_cli


def test_settings_default_db_is_in_data(monkeypatch):
    monkeypatch.delenv("FHIR_DB_PATH", raising=False)
    assert Settings.from_env(jwt_secret="x" * 32).db_path == "data/fhir_server.db"


def test_init_db_default_creates_data_folder(tmp_path, monkeypatch):
    monkeypatch.delenv("FHIR_DB_PATH", raising=False)
    monkeypatch.chdir(tmp_path)
    p = run_cli(["init-db"], {"FHIR_JWT_SECRET": "x" * 32})
    assert p.returncode == 0, p.stderr
    assert "initialized data/fhir_server.db" in p.stdout
    assert (tmp_path / "data/fhir_server.db").is_file()
