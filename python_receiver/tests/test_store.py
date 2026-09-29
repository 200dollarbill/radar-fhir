from python_receiver.store import ObservationStore
from python_receiver.receiver import SerialReceiver

VALID = '{"epoch_id":11,"sample_idx":3,"t_host_unix":1789460288.97302,"fs":100,"crc_ok":true,"missed":0,"I":1.5295,"Q":1.5327,"ax":-0.677,"ay":0.738,"az":-0.168,"gx":0,"gy":0,"gz":0}'

def test_store_evicts_oldest_observation():
    store = ObservationStore(max_size=2)
    store.add({"id": "one"}); store.add({"id": "two"}); store.add({"id": "three"})
    assert [item["id"] for item in store.recent()] == ["two", "three"]
    assert store.latest()["id"] == "three"

def test_receiver_counts_valid_and_invalid_lines():
    store = ObservationStore()
    receiver = SerialReceiver("dummy", 115200, store)
    assert receiver.process_line(VALID) is True
    assert receiver.process_line("broken") is False
    health = store.snapshot_health()
    assert health["accepted_packets"] == 1
    assert health["invalid_packets"] == 1
