from datetime import datetime, timezone
import pytest
from python_receiver.models import PacketValidationError, RadarPacket

VALID = '{"epoch_id":11,"sample_idx":3,"t_host_unix":1789460288.97302,"fs":100,"crc_ok":true,"missed":0,"I":1.5295,"Q":1.5327,"ax":-0.677,"ay":0.738,"az":-0.168,"gx":0,"gy":0,"gz":0}'

def test_valid_line_parses_all_fields():
    packet = RadarPacket.from_json_line(VALID)
    assert packet.epoch_id == 11
    assert packet.sample_idx == 3
    assert packet.i_value == pytest.approx(1.5295)
    assert packet.q_value == pytest.approx(1.5327)
    assert packet.crc_ok is True

def test_invalid_json_is_rejected():
    with pytest.raises(PacketValidationError, match="invalid JSON"):
        RadarPacket.from_json_line("not-json")

def test_required_field_and_type_errors_are_rejected():
    with pytest.raises(PacketValidationError, match="missing field.*Q"):
        RadarPacket.from_json_line(VALID.replace(',"Q":1.5327', ''))
    with pytest.raises(PacketValidationError, match="fs"):
        RadarPacket.from_json_line(VALID.replace('"fs":100', '"fs":"100"'))

def test_packet_converts_to_local_observation():
    received = datetime(2026, 9, 22, 12, 0, 0, 123456, tzinfo=timezone.utc)
    observation = RadarPacket.from_json_line(VALID).to_observation(received)
    assert observation["resourceType"] == "Observation"
    assert observation["status"] == "final"
    assert observation["effectiveDateTime"] == "2026-09-22T12:00:00.123456Z"
    assert observation["category"][0]["coding"][0]["code"] == "vital-signs"
    assert {item["code"]["coding"][0]["code"] for item in observation["component"]} == {"radar-i", "radar-q", "accel-x", "accel-y", "accel-z", "gyro-x", "gyro-y", "gyro-z"}
    assert "subject" not in observation
    assert "device" not in observation

def test_bad_crc_does_not_convert_to_final_observation():
    with pytest.raises(PacketValidationError, match="crc_ok"):
        RadarPacket.from_json_line(VALID.replace('"crc_ok":true', '"crc_ok":false')).to_observation(datetime.now(timezone.utc))
