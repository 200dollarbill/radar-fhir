"""Validation and conversion for the board's newline-delimited packets."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
import json
import math
from numbers import Real
from typing import Any


class PacketValidationError(ValueError):
    """Raised when a serial packet cannot be safely interpreted."""


_FIELDS = ("epoch_id", "sample_idx", "t_host_unix", "fs", "crc_ok", "missed",
           "I", "Q", "ax", "ay", "az", "gx", "gy", "gz")
_INT_FIELDS = {"epoch_id", "sample_idx", "fs", "missed"}
_NUM_FIELDS = {"t_host_unix", "I", "Q", "ax", "ay", "az", "gx", "gy", "gz"}


def _number(value: Any, field: str) -> float:
    if isinstance(value, bool) or not isinstance(value, Real) or not math.isfinite(float(value)):
        raise PacketValidationError(f"field {field} must be a finite number")
    return float(value)


@dataclass(frozen=True)
class RadarPacket:
    epoch_id: int
    sample_idx: int
    t_host_unix: float
    fs: int
    crc_ok: bool
    missed: int
    i_value: float
    q_value: float
    ax: float
    ay: float
    az: float
    gx: float
    gy: float
    gz: float

    @classmethod
    def from_json_line(cls, line: str) -> "RadarPacket":
        try:
            payload = json.loads(line.strip())
        except json.JSONDecodeError as exc:
            raise PacketValidationError("invalid JSON") from exc
        if not isinstance(payload, dict):
            raise PacketValidationError("packet must be a JSON object")
        for field in _FIELDS:
            if field not in payload:
                raise PacketValidationError(f"missing field {field}")
        for field in _INT_FIELDS:
            value = payload[field]
            if isinstance(value, bool) or not isinstance(value, int):
                raise PacketValidationError(f"field {field} must be an integer")
        if not isinstance(payload["crc_ok"], bool):
            raise PacketValidationError("field crc_ok must be boolean")
        values = {field: _number(payload[field], field) for field in _NUM_FIELDS}
        return cls(
            epoch_id=payload["epoch_id"], sample_idx=payload["sample_idx"],
            t_host_unix=values["t_host_unix"], fs=payload["fs"],
            crc_ok=payload["crc_ok"], missed=payload["missed"],
            i_value=values["I"], q_value=values["Q"], ax=values["ax"],
            ay=values["ay"], az=values["az"], gx=values["gx"],
            gy=values["gy"], gz=values["gz"],
        )

    def to_observation(self, received_at: datetime) -> dict[str, Any]:
        if not self.crc_ok:
            raise PacketValidationError("crc_ok is false")
        timestamp = received_at.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")
        components = (
            ("radar-i", "Radar I", self.i_value, "V"),
            ("radar-q", "Radar Q", self.q_value, "V"),
            ("accel-x", "Accelerometer X", self.ax, "g"),
            ("accel-y", "Accelerometer Y", self.ay, "g"),
            ("accel-z", "Accelerometer Z", self.az, "g"),
            ("gyro-x", "Gyroscope X", self.gx, "deg/s"),
            ("gyro-y", "Gyroscope Y", self.gy, "deg/s"),
            ("gyro-z", "Gyroscope Z", self.gz, "deg/s"),
        )
        return {
            "resourceType": "Observation",
            "status": "final",
            "category": [{"coding": [{
                "system": "http://terminology.hl7.org/CodeSystem/observation-category",
                "code": "vital-signs", "display": "Vital Signs",
            }]}],
            "code": {"coding": [{
                "system": "urn:prata:radar-dummy", "code": "radar-iq", "display": "Radar I/Q sample",
            }]},
            "effectiveDateTime": timestamp,
            "component": [{
                "code": {"coding": [{"system": "urn:prata:radar-dummy", "code": code, "display": display}]},
                "valueQuantity": {"value": value, "unit": unit},
            } for code, display, value, unit in components],
        }
