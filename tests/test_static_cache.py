"""The website files must be re-checked on every load: a stale cached module whose
exports changed stops the whole page (2026-11-18: old serial.js lacked serialSend,
so app.js never ran, the top bar stayed empty and Connect board did nothing)."""
import pytest
from fastapi.testclient import TestClient

from fhir_server.app import create_app
from fhir_server.config import Settings


@pytest.fixture
def client(tmp_path):
    app = create_app(Settings(db_path=str(tmp_path / "s.db"),
                              jwt_secret="static-secret-0123456789abcdef"))
    with TestClient(app) as c:
        yield c


@pytest.mark.parametrize("path", ["/capture/", "/capture/app.js", "/capture/src/serial.js",
                                  "/capture/sessions.html", "/capture/site.css"])
def test_site_files_must_be_revalidated(client, path):
    r = client.get(path)
    assert r.status_code == 200
    assert r.headers["cache-control"] == "no-cache"


def test_not_modified_answers_keep_the_header(client):
    first = client.get("/capture/app.js")
    r = client.get("/capture/app.js", headers={"If-None-Match": first.headers["etag"]})
    assert r.status_code == 304
    assert r.headers["cache-control"] == "no-cache"

