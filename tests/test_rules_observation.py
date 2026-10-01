from fhir_server.validation.rules_observation import validate_observation

ORG = "100000001"
DEV = "Device/aaa"
PAT = "Patient/P12345678901"
ENC = "Encounter/bbb"
NOW = "2026-09-29T10:00:00+00:00"


def valid(**kw):
    p = {
        "resourceType": "Observation",
        "status": "final",
        "category": [{"coding": [{
            "system": "http://terminology.hl7.org/CodeSystem/observation-category",
            "code": "vital-signs", "display": "Vital Signs"}]}],
        "code": {"coding": [{"system": "http://loinc.org",
                             "code": "8867-4", "display": "Heart rate"}]},
        "subject": {"reference": PAT},
        "encounter": {"reference": ENC},
        "effectiveDateTime": NOW,
        "valueQuantity": {"value": 72, "unit": "beats/minute",
                          "system": "http://unitsofmeasure.org", "code": "/min"},
        "device": {"reference": DEV},
        "identifier": [{"system": f"http://sys-ids.kemkes.go.id/observation/{ORG}",
                        "value": "obs-1"}],
    }
    p.update(kw)
    return p


def kw():
    return dict(org_id=ORG, device_ref=DEV, assigned_patient=PAT)


def test_valid_passes():
    assert validate_observation(valid(), **kw()) == []


def test_wajib_subject_encounter_code_status():
    p = valid(); del p["subject"]; del p["encounter"]
    p["code"] = {}; del p["status"]
    i = validate_observation(p, **kw())
    assert sum(1 for x in i if x.rule_number == 10263) >= 4


def test_non_loinc_code_rejected():
    p = valid()
    p["code"] = {"coding": [{"system": "http://loinc.org", "code": "8480-6"}]}
    assert any(i.rule_number == 10001 for i in validate_observation(p, **kw()))


def test_value_quantity_rules():
    p = valid(valueQuantity={"value": 72, "code": "kg",
                             "system": "http://unitsofmeasure.org"})
    assert any(i.rule_number == 20006 for i in validate_observation(p, **kw()))
    p2 = valid(valueQuantity={"value": 999, "code": "/min",
                              "system": "http://unitsofmeasure.org"})
    assert any(i.rule_number == 20006 for i in validate_observation(p2, **kw()))


def test_device_must_match_principal():
    p = valid(device={"reference": "Device/other"})
    assert any(i.rule_number == 20005 for i in validate_observation(p, **kw()))


def test_subject_must_match_assignment():
    p = valid(subject={"reference": "Patient/P99999999999"})
    assert any(i.rule_number == 20005 for i in validate_observation(p, **kw()))


def test_identifier_system_forms_accepted():
    for sys_ in (f"http://sys-ids.kemkes.go.id/observation/{ORG}",
                 f"http://sys-ids.kemkes.go.id/organization/{ORG}"):
        p = valid(identifier=[{"system": sys_, "value": "x"}])
        assert validate_observation(p, **kw()) == []
    p = valid(identifier=[{"system": "http://evil", "value": "x"}])
    assert any(i.rule_number == 10117 for i in validate_observation(p, **kw()))
