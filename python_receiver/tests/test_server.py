import json
from threading import Thread
from urllib.error import HTTPError
from urllib.request import urlopen
import pytest
from python_receiver.server import create_server
from python_receiver.store import ObservationStore

def test_health_and_latest_routes():
    store = ObservationStore()
    server = create_server(store, port=0)
    thread = Thread(target=server.serve_forever, daemon=True); thread.start()
    try:
        base = f"http://127.0.0.1:{server.server_port}"
        with urlopen(base + "/health") as response:
            assert response.status == 200
            assert json.load(response)["accepted_packets"] == 0
        with pytest.raises(HTTPError) as error:
            urlopen(base + "/observations/latest")
        assert error.value.code == 404
    finally:
        server.shutdown(); thread.join(timeout=2); server.server_close()

def test_observations_route_returns_bundle():
    store = ObservationStore(); store.add({"resourceType": "Observation", "status": "final"})
    server = create_server(store, port=0); thread = Thread(target=server.serve_forever, daemon=True); thread.start()
    try:
        with urlopen(f"http://127.0.0.1:{server.server_port}/observations") as response:
            payload = json.load(response)
        assert payload["resourceType"] == "Bundle"
        assert payload["entry"][0]["resource"]["status"] == "final"
    finally:
        server.shutdown(); thread.join(timeout=2); server.server_close()
