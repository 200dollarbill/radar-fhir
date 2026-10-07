"""Structural validation: fhir.resources (pydantic v2) parse plus a strict
pre-walk that rejects what pydantic may coerce instead of rejecting (S15
quoted booleans, S13 array-on-scalar)."""
import re
import typing

import pydantic
from fhir.resources.R4B.device import Device
from fhir.resources.R4B.encounter import Encounter
from fhir.resources.R4B.location import Location
from fhir.resources.R4B.observation import Observation
from fhir.resources.R4B.organization import Organization
from fhir.resources.R4B.patient import Patient
from fhir.resources.R4B.practitioner import Practitioner

from .issues import Issue, R_DATETIME

SUPPORTED_TYPES = {
    "Patient": Patient, "Practitioner": Practitioner, "Organization": Organization,
    "Location": Location, "Device": Device, "Encounter": Encounter,
    "Observation": Observation,
}

_DATE_RE = re.compile(r"^\d{4}(-\d{2}(-\d{2})?)?$")
_DATETIME_RE = re.compile(
    r"^\d{4}-\d{2}-\d{2}(T\d{2}:\d{2}:\d{2}(\.\d+)?(Z|[+-]\d{2}:\d{2})?)?$")


def _is_model(annotation) -> bool:
    return (isinstance(annotation, type)
            and issubclass(annotation, pydantic.BaseModel))


def _as_model(annotation):
    """Return the pydantic model for a field annotation, resolving the lazy
    abc.*Type proxies fhir.resources uses for nested elements
    (e.g. abc.QuantityType -> Quantity). None when not a model at all."""
    if annotation is None:
        return None
    if _is_model(annotation):
        return annotation
    getter = getattr(annotation, "get_model_klass", None)
    if getter is None:
        return None
    try:
        klass = getter()
    except Exception:
        return None
    return klass if _is_model(klass) else None


def _unwrap(annotation):
    """Classify a field annotation: ('model', cls), ('list', item),
    ('opt', inner) or ('primitive', annotation)."""
    origin = typing.get_origin(annotation)
    if origin is typing.Union or origin is getattr(types := __import__("types"), "UnionType", None):
        args = [a for a in typing.get_args(annotation) if a is not type(None)]
        return _unwrap(args[0]) if len(args) == 1 else ("any", args)
    if origin is list:
        return ("list", typing.get_args(annotation)[0])
    if origin is not None:
        return ("any", annotation)
    resolved = _as_model(annotation)
    if resolved is not None:
        return ("model", resolved)
    return ("primitive", annotation)


def _check_date_value(value, child, issues):
    if not isinstance(value, str):
        issues.append(Issue(code="format", details_text="Date must be a string",
                            expression=child, rule_number=R_DATETIME))
        return False
    if not _DATE_RE.match(value):
        issues.append(Issue(code="format",
                            details_text=f"Invalid date format : {value}",
                            expression=child, rule_number=R_DATETIME))
        return False
    return True


def _check_datetime_value(value, child, issues):
    if not isinstance(value, str):
        issues.append(Issue(code="format", details_text="DateTime must be a string",
                            expression=child, rule_number=R_DATETIME))
        return False
    if not _DATETIME_RE.match(value):
        issues.append(Issue(code="format",
                            details_text=f"Invalid date time format : {value}"
                                         f". Format allowed : YYYY-MM-DDThh:mm:ss+00:00",
                            expression=child, rule_number=R_DATETIME))
        return False
    return True


def _check_primitive(name, annotation, value, child, issues):
    """Strict primitive checks before pydantic gets a chance to coerce."""
    ok = True
    ann = str(annotation)
    if "bool" in ann and "Literal" not in ann:
        if not isinstance(value, bool):
            issues.append(Issue(code="format",
                                details_text="Boolean must be JSON true/false",
                                expression=child))
            return False
    if ("int" in ann or "positiveInt" in ann or "unsignedInt" in ann) \
            and "bool" not in ann and "str" not in ann:
        if isinstance(value, str) or not isinstance(value, int):
            issues.append(Issue(code="format",
                                details_text="Integer must be a JSON number",
                                expression=child))
            return False
    if "float" in ann or "decimal" in ann or "Numeric" in ann:
        if isinstance(value, str) or isinstance(value, bool) \
                or not isinstance(value, (int, float)):
            issues.append(Issue(code="format",
                                details_text="Decimal must be a JSON number",
                                expression=child))
            return False
    lower = name.lower()
    if lower.endswith("datetime") or lower.endswith("instant"):
        ok = _check_datetime_value(value, child, issues) and ok
    elif lower.endswith("date"):
        ok = _check_date_value(value, child, issues) and ok
    return ok


def _strict_check(model_cls, payload, path, issues, *, root=False):
    if not isinstance(payload, dict):
        issues.append(Issue(code="format", details_text=f"Expected object at {path}",
                            expression=path))
        return False
    fields = model_cls.model_fields
    alias_to_name = {f.alias: n for n, f in fields.items() if f.alias}
    ok = True
    for key, value in payload.items():
        if key == "resourceType":
            continue
        if key.startswith("_"):
            continue  # primitive-extension companion key; pydantic handles it
        real = key if key in fields else alias_to_name.get(key)
        if real is None:
            if root:
                issues.append(Issue(code="value",
                                    details_text=f"Unknown element: {key}",
                                    expression=f"{path}.{key}"))
                ok = False
            # Nested unknown keys are extension URLs and sub-extensions:
            # leave them to pydantic (extension containers allow extras).
            continue
        child = f"{path}.{key}"
        kind, target = _unwrap(fields[real].annotation)
        if kind == "list":
            target = _as_model(target) or target
            if not isinstance(value, list):
                issues.append(Issue(code="format", details_text="Expected array",
                                    expression=child))
                ok = False
            elif _is_model(target):
                for idx, item in enumerate(value):
                    if not _strict_check(target, item, f"{child}[{idx}]", issues):
                        ok = False
        elif kind == "model":
            if not isinstance(value, dict):
                issues.append(Issue(code="format", details_text="Expected object",
                                    expression=child))
                ok = False
            elif not _strict_check(target, value, child, issues):
                ok = False
        elif kind == "any" and isinstance(target, (list, tuple)):
            # heterogeneous unions: check list-on-scalar and models if present
            if not isinstance(value, (list, dict)) or (
                    isinstance(value, list) and not any(
                        _is_model(a) or typing.get_origin(a) is list
                        for a in target)):
                issues.append(Issue(code="format",
                                    details_text=f"Unexpected value shape for {key}",
                                    expression=child))
                ok = False
            elif isinstance(value, dict):
                model_targets = [m for m in (_as_model(a) for a in target)
                                 if m is not None]
                if model_targets and not _strict_check(
                        model_targets[0], value, child, issues):
                    ok = False
        else:
            # primitive (possibly Optional): list on a scalar slot is S13
            if isinstance(value, list):
                issues.append(Issue(code="format", details_text="Expected scalar",
                                    expression=child))
                ok = False
            elif value is not None and not _check_primitive(
                    key, target, value, child, issues):
                ok = False
    return ok


def structural_issues(resource_type: str,
                      payload) -> tuple[list[Issue], object | None]:
    issues: list[Issue] = []
    if not isinstance(payload, dict):
        issues.append(Issue(code="format", details_text="Body must be a JSON object"))
        return issues, None
    if payload.get("resourceType") != resource_type:
        issues.append(Issue(code="value",
                            details_text=f"Expected resourceType {resource_type}",
                            expression="resourceType"))
        return issues, None
    model_cls = SUPPORTED_TYPES[resource_type]
    ok = _strict_check(model_cls, payload, resource_type, issues, root=True)
    try:
        model_cls.model_validate(payload)
    except Exception as exc:
        issues.extend(_pydantic_issues(exc, resource_type))
        return issues, None
    if not ok:
        return issues, None
    return issues, model_cls.model_validate(payload)


def _pydantic_issues(exc, resource_type) -> list[Issue]:
    out = []
    for err in getattr(exc, "errors", lambda: [])():
        loc = ".".join(str(p) for p in err.get("loc", ()) if p != "body")
        expr = f"{resource_type}.{loc}" if loc else resource_type
        msg = err.get("msg", "invalid")
        err_type = str(err.get("type", ""))
        is_time = "date" in err_type or "datetime" in err_type
        out.append(Issue(code="format" if is_time else "value",
                         details_text=msg, expression=expr,
                         rule_number=R_DATETIME if is_time else None))
    if not out:
        out.append(Issue(code="processing", details_text=str(exc),
                         expression=resource_type))
    return out
