"""Parse the literal HTTP body out of ingest.h and prove it is the same
JSON contract device_client speaks. Catches C++ string divergences that the
arduino-cli compile gate cannot see."""
import json
import pathlib
import re

INGEST = pathlib.Path("arduino/radar_json/ingest.h")

MACROS = {
    "PATIENT_REF": "Patient/P11111111111",
    "ENCOUNTER_REF": "Encounter/e1",
    "DEVICE_REF": "Device/dev-1",
    "ORG_IHS": "100000001",
}
SUBSTITUTIONS = {
    "utcNowIso()": "2026-09-29T10:06:00+00:00",
    "String(bpm, 1)": "72.0",
}

TOKEN = re.compile(
    r'"((?:[^"\\]|\\.)*)"'                      # C++ string literal
    r"|(utcNowIso\(\)|String\(bpm, 1\))"         # function-like tokens
    r"|(" + "|".join(MACROS) + ")"               # config macros
)


def firmware_body() -> str:
    text = INGEST.read_text()
    expr = text[text.index("String body ="):text.index("HTTPClient http;")]
    parts = []
    for m in TOKEN.finditer(expr):
        if m.group(1) is not None:
            parts.append(m.group(1).replace('\\"', '"'))
        elif m.group(2) is not None:
            parts.append(SUBSTITUTIONS[m.group(2)])
        else:
            parts.append(MACROS[m.group(3)])
    return "".join(parts)


def test_firmware_body_is_valid_json():
    doc = json.loads(firmware_body())  # raises on stray braces (was the bug)
    assert doc["resourceType"] == "Observation"
    assert doc["status"] == "final"


def test_firmware_body_matches_python_wire_contract():
    from device_client.client import build_observation
    fw = json.loads(firmware_body())
    py = build_observation(
        patient=MACROS["PATIENT_REF"], encounter=MACROS["ENCOUNTER_REF"],
        device=MACROS["DEVICE_REF"], bpm=72.0,
        effective_datetime=SUBSTITUTIONS["utcNowIso()"])
    assert set(fw) == set(py), (set(fw) ^ set(py))
    for key in ("subject", "encounter", "device", "code", "category",
                "valueQuantity", "identifier", "effectiveDateTime"):
        if key == "identifier":
            # server mints the local value's system form; compare shape only
            assert isinstance(fw[key], list) and isinstance(py[key], list)
            assert fw[key][0]["value"] == py[key][0]["value"]
        else:
            assert fw[key] == py[key], key


def test_firmware_code_is_heart_rate():
    doc = json.loads(firmware_body())
    assert doc["code"]["coding"][0]["code"] == "8867-4"
    assert doc["valueQuantity"]["code"] == "/min"
    assert doc["valueQuantity"]["value"] == 72.0
