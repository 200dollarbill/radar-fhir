from fhir_server.validation import rules_master as rm


def test_org_identifier_system_prefix():
    bad = {"resourceType": "Organization",
           "identifier": [{"use": "official", "system": "http://example.org", "value": "X"}]}
    assert any(i.rule_number == 10117 for i in rm.validate_organization(bad))
    good = {"resourceType": "Organization",
            "identifier": [{"use": "official",
                            "system": "http://sys-ids.kemkes.go.id/organization/100000001",
                            "value": "X"}]}
    assert rm.validate_organization(good) == []


def test_org_contact_needs_purpose_coding():
    bad = {"resourceType": "Organization",
           "contact": [{"name": {"text": "Billing"}}]}
    assert any(i.rule_number == 10263 for i in rm.validate_organization(bad))


def test_location_position_needs_both_coords():
    bad = {"resourceType": "Location", "position": {"longitude": 106.8}}
    assert any(i.rule_number == 20003 for i in rm.validate_location(bad))
    ok = {"resourceType": "Location",
          "position": {"longitude": 106.8, "latitude": -6.2}}
    assert rm.validate_location(ok) == []


def test_practitioner_qualification_needs_coding():
    bad = {"resourceType": "Practitioner", "qualification": [{"period": {}}]}
    assert any(i.rule_number == 10263 for i in rm.validate_practitioner(bad))


def test_device_status_enum():
    bad = {"resourceType": "Device", "status": "bogus"}
    assert any(i.rule_number == 20005 for i in rm.validate_device(bad))
    good = {"resourceType": "Device", "status": "active"}
    assert rm.validate_device(good) == []
