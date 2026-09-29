import re
import pytest
from fhir_server.ids import mint, R4_ID_RE

def test_patient_id_shape():
    assert re.fullmatch(r"P\d{11}", mint("Patient"))

def test_practitioner_id_shape():
    assert re.fullmatch(r"N\d{8}", mint("Practitioner"))

def test_organization_id_shape():
    i = mint("Organization")
    assert i.isdigit() and 9 <= len(i) <= 11

def test_uuid_types():
    for t in ("Location", "Device", "Encounter", "Observation"):
        i = mint(t)
        assert len(i) == 36 and i.count("-") == 4
        assert re.fullmatch(R4_ID_RE, i)

def test_unique_patient_ids():
    assert len({mint("Patient") for _ in range(50)}) == 50

def test_unknown_type_raises():
    with pytest.raises(ValueError):
        mint("Condition")
