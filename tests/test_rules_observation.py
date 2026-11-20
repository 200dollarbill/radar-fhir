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


# ---- raw radar capture chunks ----
from fhir_server.validation.rules_observation import RAW_SYSTEM, RAW_CODE

UCUM = "http://unitsofmeasure.org"
RAW_COMPONENTS = [("i-voltage", "V"), ("q-voltage", "V"),
                  ("accel-x", "[g]"), ("accel-y", "[g]"), ("accel-z", "[g]"),
                  ("gyro-x", "deg/s"), ("gyro-y", "deg/s"), ("gyro-z", "deg/s")]


def comp(code, unit, data="1.65 1.66 1.67", period=10):
    return {"code": {"coding": [{"system": RAW_SYSTEM, "code": code}]},
            "valueSampledData": {
                "origin": {"value": 0, "unit": unit, "system": UCUM, "code": unit},
                "period": period, "dimensions": 1, "data": data}}


def raw(**kw):
    p = {
        "resourceType": "Observation",
        "status": "final",
        "code": {"coding": [{"system": RAW_SYSTEM, "code": RAW_CODE,
                             "display": "Raw radar I/Q capture"}]},
        "subject": {"reference": PAT},
        "encounter": {"reference": ENC},
        "effectiveDateTime": NOW,
        "device": {"reference": DEV},
        "identifier": [{"system": f"http://sys-ids.kemkes.go.id/observation/{ORG}",
                        "value": "cap-1-0"}],
        "component": [comp(c, u) for c, u in RAW_COMPONENTS],
    }
    p.update(kw)
    return p


def raw_data(data, **kw):
    return raw(component=[comp(c, u, data=data) for c, u in RAW_COMPONENTS], **kw)


def errs(p, **extra):
    return validate_observation(p, **{**kw(), **extra})


def has_obs_issue(issues):
    return bool(issues) and any(i.expression.startswith("Observation") for i in issues)


def test_raw_capture_valid():
    assert errs(raw()) == []


def test_raw_accepts_error_tokens():
    assert errs(raw_data("1.65 E -0.5")) == []
    assert errs(raw_data("L U 2")) == []


def test_raw_requires_i_and_q():
    p = raw(component=[comp(c, u) for c, u in RAW_COMPONENTS if c != "q-voltage"])
    assert has_obs_issue(errs(p))


def test_raw_rejects_unknown_component_code():
    comps = [comp(c, u) for c, u in RAW_COMPONENTS] + [comp("bogus", "V")]
    assert has_obs_issue(errs(raw(component=comps)))


def test_raw_rejects_duplicate_component_code():
    comps = [comp(c, u) for c, u in RAW_COMPONENTS] + [comp("accel-x", "[g]")]
    assert has_obs_issue(errs(raw(component=comps)))


def test_raw_rejects_top_level_value():
    p = raw(valueQuantity={"value": 72, "system": UCUM, "code": "/min"})
    assert has_obs_issue(errs(p))


def test_raw_rejects_non_sampled_component():
    comps = [comp(c, u) for c, u in RAW_COMPONENTS]
    comps[2] = {"code": comps[2]["code"],
                "valueQuantity": {"value": 1, "system": UCUM, "code": "[g]"}}
    assert has_obs_issue(errs(raw(component=comps)))


def test_raw_rejects_dimensions_not_one():
    comps = [comp(c, u) for c, u in RAW_COMPONENTS]
    comps[0]["valueSampledData"]["dimensions"] = 2
    assert has_obs_issue(errs(raw(component=comps)))


def test_raw_rejects_period_zero():
    p = raw(component=[comp(c, u, period=0) for c, u in RAW_COMPONENTS])
    assert has_obs_issue(errs(p))


def test_raw_rejects_mismatched_period():
    comps = [comp(c, u) for c, u in RAW_COMPONENTS]
    comps[3]["valueSampledData"]["period"] = 20
    assert has_obs_issue(errs(raw(component=comps)))


def test_raw_rejects_mismatched_sample_count():
    comps = [comp(c, u) for c, u in RAW_COMPONENTS]
    comps[4]["valueSampledData"]["data"] = "1 2"
    assert has_obs_issue(errs(raw(component=comps)))


def test_raw_rejects_bad_token():
    assert has_obs_issue(errs(raw_data("1.65 abc")))


def test_raw_rejects_nan_token():
    assert has_obs_issue(errs(raw_data("1.65 NaN")))


def test_raw_accepts_exponent_token():
    assert errs(raw_data("1e-7")) == []
    assert errs(raw_data("1.5E+3 -2e5")) == []


def test_raw_rejects_over_1000_samples():
    assert has_obs_issue(errs(raw_data(" ".join(["1"] * 1001))))


def test_raw_accepts_exactly_1000_samples():
    assert errs(raw_data(" ".join(["1"] * 1000))) == []


def test_raw_rejects_empty_data():
    assert has_obs_issue(errs(raw_data("")))


def test_raw_requires_exactly_one_identifier():
    assert has_obs_issue(errs(raw(identifier=[])))
    ident = {"system": f"http://sys-ids.kemkes.go.id/observation/{ORG}", "value": "a"}
    assert has_obs_issue(errs(raw(identifier=[ident, dict(ident, value="b")])))


def test_raw_requires_identifier_value():
    p = raw(identifier=[{"system": f"http://sys-ids.kemkes.go.id/observation/{ORG}"}])
    assert has_obs_issue(errs(p))


def test_raw_keeps_device_rule():
    p = raw(device={"reference": "Device/other"})
    assert any(i.rule_number == 20005 for i in errs(p))


def test_raw_keeps_finished_encounter_rule():
    enc = {"status": "finished", "subject": {"reference": PAT}}
    issues = errs(raw(), encounter_getter=lambda ref: enc)
    assert any(i.rule_number == 20005 and i.expression == "Observation.encounter"
               for i in issues)


def test_heart_rate_code_still_required_for_other_codes():
    p = valid()
    p["code"] = {"coding": [{"system": "http://loinc.org", "code": "29463-7"}]}
    assert any(i.rule_number == 10001 for i in errs(p))
