from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse, Response

from ..authz import AuthzError
from ..repositories import resources as res
from ..services.fhir_service import FhirError
from ..validation import parse
from ..validation.issues import Issue
from ..validation.outcome import to_outcome
from .deps import get_principal, get_service

router = APIRouter(prefix="/fhir-r4/v1", tags=["fhir"])
_TYPES = tuple(parse.SUPPORTED_TYPES)
_INPUT_CT = ("application/json", "application/fhir+json")
_ACCEPT_OK = ("application/json", "application/fhir+json", "*/*")


def _json(payload, status=200, headers=None):
    return JSONResponse(status_code=status, content=payload,
                        headers=headers or {},
                        media_type="application/fhir+json")


def _error(exc):
    return JSONResponse(status_code=exc.status, content=to_outcome(exc.issues),
                        media_type="application/fhir+json")


def _check_media(request: Request):
    accept = request.headers.get("accept")
    if accept and not any(t in accept for t in _ACCEPT_OK):
        raise FhirError([Issue(code="not-supported",
                               details_text="Accept must allow"
                                            " application/fhir+json")], 406)
    if request.method in ("POST", "PUT"):
        ct = request.headers.get("content-type", "")
        if not any(ct.startswith(t) for t in _INPUT_CT):
            raise FhirError([Issue(code="not-supported",
                                   details_text="Content-Type must be"
                                                " application/json or"
                                                " application/fhir+json")], 415)


async def _payload(request: Request) -> dict:
    try:
        body = await request.json()
    except Exception:
        raise FhirError([Issue(code="format",
                               details_text="Body must be valid JSON",
                               rule_number=10132)], 400)
    if not isinstance(body, dict):
        raise FhirError([Issue(code="format",
                               details_text="Body must be a JSON object")], 400)
    return body


def _check_type(type_):
    if type_ not in _TYPES:
        raise FhirError([Issue(code="not-found",
                               details_text=f"Unsupported resource type"
                                            f" {type_}")], 404)


@router.post("/Device/{rid}/$provision")
async def provision(rid: str, request: Request):
    try:
        _check_media(request)
        svc, principal = get_service(request), get_principal(request)
        body = await _payload(request)
        patient = body.get("patient")
        if not isinstance(patient, str) or not patient.startswith("Patient/"):
            raise FhirError([Issue(code="value",
                                   details_text='body must be'
                                               ' {"patient": "Patient/{id}"}')],
                            400)
        token = svc.provision_device(principal, rid, patient)
        return _json({"token": token, "device": f"Device/{rid}",
                      "patient": patient})
    except (FhirError, AuthzError) as exc:
        return _error(exc)


@router.get("/{type_}")
async def search(type_: str, request: Request):
    try:
        _check_media(request)
        _check_type(type_)
        svc, principal = get_service(request), get_principal(request)
        return _json(svc.search(principal, type_, dict(request.query_params)))
    except (FhirError, AuthzError) as exc:
        return _error(exc)


@router.post("/{type_}")
async def create(type_: str, request: Request):
    try:
        _check_media(request)
        _check_type(type_)
        svc, principal = get_service(request), get_principal(request)
        rid, doc, version = svc.create(principal, type_,
                                       await _payload(request))
        return _json(doc, status=201, headers={
            "Location": f"/fhir-r4/v1/{type_}/{rid}",
            "ETag": f'W/"{version}"'})
    except (FhirError, AuthzError) as exc:
        return _error(exc)


@router.get("/{type_}/{rid}")
async def read(type_: str, rid: str, request: Request):
    try:
        _check_media(request)
        _check_type(type_)
        svc, principal = get_service(request), get_principal(request)
        doc = svc.read(principal, type_, rid)
        headers = {}
        version = res.get_version(svc.conn, type_, rid)
        if version is not None:
            headers["ETag"] = f'W/"{version}"'
        return _json(doc, headers=headers)
    except (FhirError, AuthzError) as exc:
        return _error(exc)


@router.put("/{type_}/{rid}")
async def update(type_: str, rid: str, request: Request):
    try:
        _check_media(request)
        _check_type(type_)
        svc, principal = get_service(request), get_principal(request)
        _, doc, version = svc.update(principal, type_, rid,
                                     await _payload(request))
        return _json(doc, headers={"ETag": f'W/"{version}"'})
    except (FhirError, AuthzError) as exc:
        return _error(exc)


@router.delete("/{type_}/{rid}")
async def delete(type_: str, rid: str, request: Request):
    try:
        _check_type(type_)
        svc, principal = get_service(request), get_principal(request)
        svc.delete(principal, type_, rid)
        return Response(status_code=204)
    except (FhirError, AuthzError) as exc:
        return _error(exc)
