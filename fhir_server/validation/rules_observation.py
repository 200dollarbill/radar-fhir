import re

from .issues import (Issue, R_WAJIB_MISSING, R_CODE_NOT_FOUND,
                     R_BAD_IDENTIFIER_SYSTEM, L_OBSERVATION_VALUE,
                     L_DEVICE_RULE)


def _wajib(text, expr):
    return Issue(code="value", details_text=f"Wajib element missing: {text}",
                 expression=expr, rule_number=R_WAJIB_MISSING)


RAW_SYSTEM = "urn:prata:radar-signal"
RAW_CODE = "raw-capture"
RAW_MAX_SAMPLES = 1000
RAW_COMPONENT_CODES = {"i-voltage", "q-voltage", "accel-x", "accel-y", "accel-z",
                       "gyro-x", "gyro-y", "gyro-z"}
_TOKEN_RE = re.compile(r"^-?\d+(\.\d+)?([eE][+-]?\d+)?$")
_ERROR_TOKENS = {"E", "L", "U"}


def _raw_issue(text, expr):
    return Issue(code="value", details_text=text, expression=expr,
                 rule_number=L_OBSERVATION_VALUE)


def _heart_rate_rules(payload, c0):
    out = []
    if c0 is not None and (c0.get("system") != "http://loinc.org"
                           or c0.get("code") != "8867-4"):
        out.append(Issue(code="value",
                         details_text=f"Code not found: '{c0.get('code')}' in system:"
                                      " http://loinc.org (heart-rate slice)",
                         expression="Observation.code.coding[0]",
                         rule_number=R_CODE_NOT_FOUND))
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
    return out


def _raw_capture_rules(payload):
    out = []
    if "valueQuantity" in payload or any(
            k.startswith("value") for k in payload):
        out.append(_raw_issue("Raw capture chunk must not carry a top-level value[x]",
                              "Observation.value"))
    idents = payload.get("identifier") or []
    if len(idents) != 1:
        out.append(_raw_issue("Raw capture chunk needs exactly one identifier",
                              "Observation.identifier"))
    for idx, ident in enumerate(idents):
        if not ident.get("value"):
            out.append(_raw_issue("identifier.value is required",
                                  f"Observation.identifier[{idx}].value"))
    seen = set()
    periods = set()
    counts = set()
    comps = payload.get("component") or []
    for idx, comp in enumerate(comps):
        base = f"Observation.component[{idx}]"
        ccodings = (comp.get("code") or {}).get("coding") or []
        cc = ccodings[0] if ccodings else {}
        code = cc.get("code")
        if cc.get("system") != RAW_SYSTEM or code not in RAW_COMPONENT_CODES:
            out.append(_raw_issue(f"Unknown raw component code: '{code}'",
                                  f"{base}.code"))
        elif code in seen:
            out.append(_raw_issue(f"Duplicate raw component code: '{code}'",
                                  f"{base}.code"))
        else:
            seen.add(code)
        sd = comp.get("valueSampledData")
        if not isinstance(sd, dict):
            out.append(_raw_issue("Raw component must use valueSampledData",
                                  f"{base}.valueSampledData"))
            continue
        if sd.get("dimensions") != 1 or isinstance(sd.get("dimensions"), bool):
            out.append(_raw_issue("valueSampledData.dimensions must be 1",
                                  f"{base}.valueSampledData.dimensions"))
        period = sd.get("period")
        if isinstance(period, bool) or not isinstance(period, (int, float)) or period <= 0:
            out.append(_raw_issue("valueSampledData.period must be > 0",
                                  f"{base}.valueSampledData.period"))
        else:
            periods.add(period)
        data = sd.get("data")
        tokens = data.split() if isinstance(data, str) else []
        if not tokens:
            out.append(_raw_issue("valueSampledData.data must not be empty",
                                  f"{base}.valueSampledData.data"))
            continue
        counts.add(len(tokens))
        if len(tokens) > RAW_MAX_SAMPLES:
            out.append(_raw_issue(f"At most {RAW_MAX_SAMPLES} samples per chunk",
                                  f"{base}.valueSampledData.data"))
        bad = next((t for t in tokens
                    if t not in _ERROR_TOKENS and not _TOKEN_RE.match(t)), None)
        if bad is not None:
            out.append(_raw_issue(f"Invalid data token: '{bad}'",
                                  f"{base}.valueSampledData.data"))
    for need in ("i-voltage", "q-voltage"):
        if need not in seen:
            out.append(_raw_issue(f"Raw capture requires component '{need}'",
                                  "Observation.component"))
    if len(periods) > 1:
        out.append(_raw_issue("All components must share one period",
                              "Observation.component"))
    if len(counts) > 1:
        out.append(_raw_issue("All components must have the same sample count",
                              "Observation.component"))
    return out


def validate_observation(payload, *, org_id, device_ref, assigned_patient,
                         encounter_getter=None):
    out = []
    if not payload.get("status"):
        out.append(_wajib("Observation.status", "Observation.status"))
    codings = (payload.get("code") or {}).get("coding") or []
    c0 = codings[0] if codings else None
    if c0 is None:
        out.append(_wajib("Observation.code.coding", "Observation.code.coding"))
    if (c0 or {}).get("system") == RAW_SYSTEM and c0.get("code") == RAW_CODE:
        out.extend(_raw_capture_rules(payload))
    else:
        out.extend(_heart_rate_rules(payload, c0))
    if not (payload.get("subject") or {}).get("reference"):
        out.append(_wajib("Observation.subject", "Observation.subject"))
    if not (payload.get("encounter") or {}).get("reference"):
        out.append(_wajib("Observation.encounter", "Observation.encounter"))
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
    enc_ref = (payload.get("encounter") or {}).get("reference")
    if (assigned_patient is not None and enc_ref and encounter_getter is not None):
        enc = encounter_getter(enc_ref)
        if enc is not None:
            if enc.get("status") != "in-progress":
                out.append(Issue(
                    code="value",
                    details_text="Device may only write into an in-progress"
                                 f" Encounter (status={enc.get('status')})",
                    expression="Observation.encounter",
                    rule_number=L_DEVICE_RULE))
            enc_subj = (enc.get("subject") or {}).get("reference")
            if enc_subj != assigned_patient:
                out.append(Issue(
                    code="value",
                    details_text="Encounter subject does not match the device"
                                 f" assignment ({assigned_patient})",
                    expression="Observation.encounter",
                    rule_number=L_DEVICE_RULE))
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
