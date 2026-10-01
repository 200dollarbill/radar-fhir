from fhir_server.validation import issues, outcome

def test_outcome_shape_matches_playbook():
    i = issues.Issue(code="value", details_text="Code not found: 'x'",
                     expression="Observation.code", rule_number=issues.R_CODE_NOT_FOUND)
    o = outcome.to_outcome([i])
    assert o["resourceType"] == "OperationOutcome"
    assert o["issue"][0]["severity"] == "error"
    assert o["issue"][0]["code"] == "value"
    assert o["issue"][0]["details"]["text"] == \
        "Code not found: 'x' (RuleNumber: 10001)"
    assert o["issue"][0]["expression"] == ["Observation.code"]

def test_multiple_issues_preserved():
    a = issues.Issue(code="format", details_text="bad")
    b = issues.Issue(code="value", details_text="worse")
    assert len(outcome.to_outcome([a, b])["issue"]) == 2

def test_empty_issues_become_internal_error():
    o = outcome.to_outcome([])
    assert o["issue"][0]["code"] == "processing"
