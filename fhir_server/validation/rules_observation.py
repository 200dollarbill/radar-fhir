from .issues import (Issue, R_WAJIB_MISSING, R_CODE_NOT_FOUND,
                     R_BAD_IDENTIFIER_SYSTEM, L_OBSERVATION_VALUE,
                     L_DEVICE_RULE)


def _wajib(text, expr):
    return Issue(code="value", details_text=f"Wajib element missing: {text}",
                 expression=expr, rule_number=R_WAJIB_MISSING)


def validate_observation(payload, *, org_id, device_ref, assigned_patient):
    out = []
    if not payload.get("status"):
        out.append(_wajib("Observation.status", "Observation.status"))
    codings = (payload.get("code") or {}).get("coding") or []
    if not codings:
        out.append(_wajib("Observation.code.coding", "Observation.code.coding"))
    else:
        c0 = codings[0]
        if c0.get("system") != "http://loinc.org" or c0.get("code") != "8867-4":
            out.append(Issue(code="value",
                             details_text=f"Code not found: '{c0.get('code')}' in system:"
                                          " http://loinc.org (heart-rate slice)",
                             expression="Observation.code.coding[0]",
                             rule_number=R_CODE_NOT_FOUND))
    if not (payload.get("subject") or {}).get("reference"):
        out.append(_wajib("Observation.subject", "Observation.subject"))
    if not (payload.get("encounter") or {}).get("reference"):
        out.append(_wajib("Observation.encounter", "Observation.encounter"))
    categories = payload.get("category") or []
    cat_codings = categories[0].get("coding") or [] if categories else []
    if cat_codings and not any(
            c.get("system") == "http://terminology.hl7.org/CodeSystem/observation-category"
            and c.get("code") == "vital-signs" for c in cat_codings):
        out.append(Issue(code="value",
                         details_text="Category must include observation-category | vital-signs",
                         expression="Observation.category[0].coding",
                         rule_number=R_CODE_NOT_FOUND))
    vq = payload.get("valueQuantity")
    if vq is None:
        out.append(_wajib("Observation.valueQuantity (heart-rate slice)",
                          "Observation.valueQuantity"))
    else:
        if (vq.get("system") != "http://unitsofmeasure.org"
                or vq.get("code") != "/min"):
            out.append(Issue(code="value",
                             details_text="Heart rate requires UCUM /min",
                             expression="Observation.valueQuantity",
                             rule_number=L_OBSERVATION_VALUE))
        val = vq.get("value")
        if isinstance(val, bool) or not isinstance(val, (int, float)):
            out.append(Issue(code="value",
                             details_text="valueQuantity.value must be numeric",
                             expression="Observation.valueQuantity.value",
                             rule_number=L_OBSERVATION_VALUE))
        elif not 0 < val < 300:
            out.append(Issue(code="value",
                             details_text="Heart rate out of range (0,300)",
                             expression="Observation.valueQuantity.value",
                             rule_number=L_OBSERVATION_VALUE))
    dev = (payload.get("device") or {}).get("reference")
    if device_ref is not None and dev != device_ref:
        out.append(Issue(code="value",
                         details_text=f"Observation.device must be {device_ref}",
                         expression="Observation.device", rule_number=L_DEVICE_RULE))
    subj = (payload.get("subject") or {}).get("reference")
    if assigned_patient is not None and subj != assigned_patient:
        out.append(Issue(code="value",
                         details_text=f"Device assigned to {assigned_patient}, not {subj}",
                         expression="Observation.subject", rule_number=L_DEVICE_RULE))
    for idx, ident in enumerate(payload.get("identifier") or []):
        system = ident.get("system")
        allowed = {f"http://sys-ids.kemkes.go.id/observation/{org_id}",
                   f"http://sys-ids.kemkes.go.id/organization/{org_id}"}
        if system is not None and system not in allowed:
            out.append(Issue(code="value",
                             details_text=f"Invalid identifier system: {system}",
                             expression=f"Observation.identifier[{idx}].system",
                             rule_number=R_BAD_IDENTIFIER_SYSTEM))
    return out
