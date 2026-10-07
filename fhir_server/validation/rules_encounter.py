from .issues import Issue, R_BAD_IDENTIFIER_SYSTEM, R_WAJIB_MISSING

_ORDER = ["arrived", "in-progress", "finished"]


def _wajib(text, expr):
    return Issue(code="value", details_text=f"Wajib element missing: {text}",
                 expression=expr, rule_number=R_WAJIB_MISSING)


def _check_base(payload, org_id, out):
    idents = payload.get("identifier") or []
    if not idents:
        out.append(_wajib("Encounter.identifier", "Encounter.identifier"))
    else:
        want = f"http://sys-ids.kemkes.go.id/encounter/{org_id}"
        if idents[0].get("system") != want:
            out.append(Issue(
                code="value",
                details_text=f"Invalid identifier system:"
                             f" {idents[0].get('system')}",
                expression="Encounter.identifier[0].system",
                rule_number=R_BAD_IDENTIFIER_SYSTEM))
    if payload.get("status") is None:
        out.append(_wajib("Encounter.status", "Encounter.status"))
    cls = payload.get("class") or {}
    if cls.get("code") != "AMB":
        out.append(_wajib("Encounter.class (AMB)", "Encounter.class"))
    if not (payload.get("subject") or {}).get("reference"):
        out.append(_wajib("Encounter.subject", "Encounter.subject"))
    if not (payload.get("serviceProvider") or {}).get("reference"):
        out.append(_wajib("Encounter.serviceProvider", "Encounter.serviceProvider"))
    if not payload.get("location"):
        out.append(_wajib("Encounter.location", "Encounter.location"))
    if not (payload.get("period") or {}).get("start"):
        out.append(_wajib("Encounter.period.start", "Encounter.period.start"))


def _history_statuses(payload):
    return [h.get("status") for h in payload.get("statusHistory") or []]


def validate_encounter(payload, *, existing, org_id, duplicate_fn=None):
    out = []
    _check_base(payload, org_id, out)
    sp = (payload.get("serviceProvider") or {}).get("reference", "")
    if sp and sp != f"Organization/{org_id}":
        out.append(_wajib(f"Encounter.serviceProvider must be Organization/{org_id}",
                          "Encounter.serviceProvider"))
    if existing is None:
        hist = payload.get("statusHistory") or []
        if payload.get("status") != "arrived":
            out.append(_wajib("Encounter.status must be 'arrived' on create",
                              "Encounter.status"))
        if (len(hist) != 1 or hist[0].get("status") != "arrived"
                or not (hist[0].get("period") or {}).get("start")
                or "end" in (hist[0].get("period") or {})):
            out.append(_wajib(
                "Encounter.statusHistory must be one arrived entry"
                " with period.start only",
                "Encounter.statusHistory[0]"))
        if duplicate_fn:
            idents = payload.get("identifier") or []
            if idents and duplicate_fn(idents[0].get("value")):
                out.append(Issue(code="duplicate",
                                 details_text="Found duplicate resource: Encounter",
                                 expression="Encounter.identifier"))
    else:
        old_status = existing.get("status")
        new_status = payload.get("status")
        old_seq = _history_statuses(existing)
        new_seq = _history_statuses(payload)
        new_hist = payload.get("statusHistory") or []
        old_hist = existing.get("statusHistory") or []
        if new_seq[:len(old_seq)] != old_seq or \
                new_hist[:len(old_hist)] != old_hist:
            out.append(_wajib(
                "Encounter.statusHistory prior entries must be preserved"
                " byte-for-byte", "Encounter.statusHistory"))
        try:
            forward = _ORDER.index(new_status) == _ORDER.index(old_status) + 1
        except ValueError:
            forward = False
        if new_status != old_status and not forward:
            out.append(Issue(
                code="value",
                details_text=f"Illegal Encounter.status transition"
                             f" {old_status} -> {new_status}",
                expression="Encounter.status", rule_number=R_WAJIB_MISSING))
        if new_status == "in-progress" and new_seq != ["arrived", "in-progress"]:
            out.append(_wajib("Encounter.statusHistory must be arrived,in-progress",
                              "Encounter.statusHistory"))
        if new_status == "finished":
            if new_seq != ["arrived", "in-progress", "finished"]:
                out.append(_wajib(
                    "Encounter.statusHistory must be arrived,in-progress,finished",
                    "Encounter.statusHistory"))
            last = (payload.get("statusHistory") or [{}])[-1]
            if not (last.get("period") or {}).get("end"):
                out.append(_wajib("Encounter.statusHistory.finished period.end",
                                  "Encounter.statusHistory[-1].period.end"))
            if not (payload.get("period") or {}).get("end"):
                out.append(_wajib("Encounter.period.end", "Encounter.period.end"))
    return out
