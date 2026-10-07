from fhir_server.validation import rules_common as rc


def test_datetime_requires_offset():
    i = rc.check_datetimes({"subject": {"reference": "Patient/P1"},
        "effectiveDateTime": "2026-09-29T10:00:00"}, "Observation", "2014-06-03")
    assert any(x.rule_number == 10132 and x.code == "format" for x in i)


def test_datetime_accepts_offset():
    assert rc.check_datetimes({"effectiveDateTime": "2026-09-29T10:00:00+00:00"},
                              "Observation", "2014-06-03") == []


def test_event_date_before_floor_rejected():
    # the S4 floor targets record event dates (period.start, effective[x])
    i = rc.check_datetimes({"period": {"start": "2010-01-01"}}, "Encounter",
                           "2014-06-03")
    assert any(x.rule_number == 20001 for x in i)


def test_birthdate_exempt_from_floor():
    # final review issue 11: demographic dates predate the floor
    assert rc.check_datetimes({"birthDate": "1990-02-14"}, "Patient",
                              "2014-06-03") == []
    # but a future birthDate is still impossible
    assert rc.check_datetimes({"birthDate": "2030-01-01"}, "Patient",
                              "2014-06-03")


def test_future_date_only_rejected():
    assert any(x.rule_number == 10132 for x in
               rc.check_datetimes({"birthDate": "2030-01-01"}, "Patient",
                                  "2014-06-03"))


def test_future_date_rejected_but_period_end_allowed():
    future = "2099-01-01T00:00:00+00:00"
    assert any(x.rule_number == 10132 for x in
               rc.check_datetimes({"x": {"start": future}}, "Encounter", "2014-06-03"))
    assert rc.check_datetimes(
        {"period": {"start": "2026-01-01T00:00:00+00:00", "end": future}},
        "Encounter", "2014-06-03") == []


def test_empty_strings():
    i = rc.check_empty_strings({"title": "  "}, "Patient")
    assert any(x.rule_number == 10134 for x in i)


def test_coding_system_allow_list():
    bad = {"coding": [{"system": "http://evil.example", "code": "x"}]}
    i = rc.check_coding_systems(bad, "Observation")
    assert any(x.rule_number == 10002 for x in i)
    good = {"coding": [{"system": "http://loinc.org", "code": "8867-4"}]}
    assert rc.check_coding_systems(good, "Observation") == []


def test_normalize_webpage_system():
    norm, changed = rc.normalize_system(
        "https://www.hl7.org/fhir/Codesystem-diagnosis-role")
    assert changed and norm.startswith("http://terminology.hl7.org/CodeSystem/")


def test_reference_resolution():
    exists = lambda t, i: (t, i) == ("Patient", "P1")
    ok = rc.check_references({"subject": {"reference": "Patient/P1"}},
                             "Observation", exists)
    assert ok == []
    miss = rc.check_references({"subject": {"reference": "Patient/P9"}},
                               "Observation", exists)
    assert any(x.rule_number == 20002 for x in miss)
    malformed = rc.check_references({"subject": {}}, "Observation", exists)
    assert any(x.rule_number == 10124 for x in malformed)


def test_canonicalize_datetimes_shifts_to_utc():
    payload = {"effectiveDateTime": "2026-09-29T17:00:00+07:00"}
    out = rc.canonicalize_datetimes(payload)
    assert out["effectiveDateTime"] == "2026-09-29T10:00:00+00:00"
