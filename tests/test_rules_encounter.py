from fhir_server.validation.rules_encounter import validate_encounter

ORG = "100000001"
NOW = "2026-09-29T10:00:00+00:00"


def created(**kw):
    p = {
        "resourceType": "Encounter",
        "identifier": [{"use": "official",
                        "system": f"http://sys-ids.kemkes.go.id/encounter/{ORG}",
                        "value": "K-001"}],
        "status": "arrived",
        "statusHistory": [{"status": "arrived", "period": {"start": NOW}}],
        "class": {"system": "http://terminology.hl7.org/CodeSystem/v3-ActCode",
                  "code": "AMB", "display": "ambulatory"},
        "subject": {"reference": "Patient/P12345678901"},
        "period": {"start": NOW},
        "location": [{"location": {"reference": "Location/abc"}}],
        "serviceProvider": {"reference": f"Organization/{ORG}"},
    }
    p.update(kw)
    return p


def test_valid_create_passes():
    assert validate_encounter(created(), existing=None, org_id=ORG) == []


def test_identifier_system_must_match_org():
    p = created()
    p["identifier"][0]["system"] = "http://sys-ids.kemkes.go.id/encounter/999"
    assert any(i.rule_number == 10117 for i in
               validate_encounter(p, existing=None, org_id=ORG))


def test_create_must_be_arrived():
    p = created(status="in-progress")
    assert any(i.rule_number == 10263 for i in
               validate_encounter(p, existing=None, org_id=ORG))


def test_missing_service_provider():
    p = created(); del p["serviceProvider"]
    assert any(i.rule_number == 10263 for i in
               validate_encounter(p, existing=None, org_id=ORG))


def test_duplicate_identifier():
    i = validate_encounter(created(), existing=None, org_id=ORG,
                           duplicate_fn=lambda v: v == "K-001")
    assert any(x.code == "duplicate" for x in i)


def test_forward_transition_arrived_to_in_progress():
    existing = created()
    new = created(status="in-progress",
                  statusHistory=[{"status": "arrived", "period": {"start": NOW}},
                                 {"status": "in-progress",
                                  "period": {"start": NOW}}])
    assert validate_encounter(new, existing=existing, org_id=ORG) == []


def test_backwards_transition_rejected():
    existing = created(status="in-progress",
                       statusHistory=[{"status": "arrived",
                                       "period": {"start": NOW}},
                                      {"status": "in-progress",
                                       "period": {"start": NOW}}])
    new = created()  # back to arrived
    assert validate_encounter(new, existing=existing, org_id=ORG)


def test_skip_to_finished_rejected():
    existing = created()
    new = created(status="finished",
                  statusHistory=[
                      {"status": "arrived", "period": {"start": NOW}},
                      {"status": "finished",
                       "period": {"start": NOW, "end": NOW}}])
    assert validate_encounter(new, existing=existing, org_id=ORG)


def test_finished_needs_history_entry_and_period_end():
    existing = created(status="in-progress",
                       statusHistory=[{"status": "arrived",
                                       "period": {"start": NOW}},
                                      {"status": "in-progress",
                                       "period": {"start": NOW}}])
    ok = created(status="finished",
                 statusHistory=[
                     {"status": "arrived", "period": {"start": NOW}},
                     {"status": "in-progress", "period": {"start": NOW}},
                     {"status": "finished",
                      "period": {"start": NOW, "end": NOW}}])
    ok["period"] = {"start": NOW, "end": NOW}
    assert validate_encounter(ok, existing=existing, org_id=ORG) == []
    no_end = created(status="finished",
                     statusHistory=[
                         {"status": "arrived", "period": {"start": NOW}},
                         {"status": "in-progress", "period": {"start": NOW}},
                         {"status": "finished",
                          "period": {"start": NOW, "end": NOW}}])
    no_end["period"] = {"start": NOW}  # top-level period.end missing
    assert validate_encounter(no_end, existing=existing, org_id=ORG)


def test_wrong_org_service_provider_rejected():
    p = created(serviceProvider={"reference": "Organization/999"})
    assert validate_encounter(p, existing=None, org_id=ORG)
