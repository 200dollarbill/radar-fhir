from .issues import Issue


def to_outcome(issue_list: list[Issue]) -> dict:
    if not issue_list:
        issue_list = [Issue(code="processing", details_text="Internal error")]
    out = []
    for i in issue_list:
        text = i.details_text
        if i.rule_number is not None and f"(RuleNumber: {i.rule_number})" not in text:
            text = f"{text} (RuleNumber: {i.rule_number})"
        entry = {
            "severity": i.severity,
            "code": i.code,
            "details": {"text": text},
        }
        if i.expression:
            entry["expression"] = [i.expression]
        out.append(entry)
    return {"resourceType": "OperationOutcome", "issue": out}


def issues_for_message(message, code, expression=None, rule_number=None) -> list[Issue]:
    return [Issue(code=code, details_text=message, expression=expression,
                  rule_number=rule_number)]
