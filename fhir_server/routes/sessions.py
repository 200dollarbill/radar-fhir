"""Dashboard and board API (not FHIR): boards, test patients, sessions.

Errors use the same OperationOutcome body as the FHIR routes."""
import functools

from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from ..authz import AuthzError
from ..services.fhir_service import FhirError
from ..services.sessions import SessionService
from ..validation.issues import Issue
from ..validation.outcome import to_outcome
from .deps import get_principal

router = APIRouter(prefix="/api", tags=["sessions"])


def _out(payload, status=200):
    return JSONResponse(status_code=status, content=payload)


def _err(exc):
    return JSONResponse(status_code=exc.status, content=to_outcome(exc.issues),
                        media_type="application/fhir+json")


async def _body(request):
    try:
        body = await request.json()
    except Exception:
        body = None
    if not isinstance(body, dict):
        raise FhirError([Issue(code="format",
                               details_text="Body must be a JSON object")], 400)
    return body


def _svc(request):
    return SessionService(request.app.state.conn, request.app.state.settings)


def _handle(fn):
    @functools.wraps(fn)  # keeps the signature FastAPI reads for parameters
    async def wrapper(*args, **kw):
        try:
            return await fn(*args, **kw)
        except (FhirError, AuthzError) as exc:
            return _err(exc)
    return wrapper


@router.post("/board/session")
@_handle
async def board_session(request: Request):
    header = request.headers.get("Authorization", "")
    key = header.removeprefix("Bearer ").strip() if header.startswith("Bearer ") else ""
    body = await _body(request)
    return _out(_svc(request).board_session(key, str(body.get("id") or "")))


@router.get("/boards")
@_handle
async def list_boards(request: Request):
    return _out(_svc(request).list_boards(get_principal(request)))


@router.post("/boards")
@_handle
async def register_board(request: Request):
    principal = get_principal(request)
    body = await _body(request)
    created, dev_id = _svc(request).register_board(principal, body.get("id"),
                                                   body.get("key"))
    return _out({"id": body.get("id"), "device": f"Device/{dev_id}",
                 "created": created}, 201 if created else 200)


@router.post("/patients")
@_handle
async def create_patient(request: Request):
    principal = get_principal(request)
    body = await _body(request)
    return _out(_svc(request).create_test_patient(principal, body.get("label")), 201)


@router.get("/sessions")
@_handle
async def list_sessions(request: Request):
    open_only = request.query_params.get("open") in ("1", "true")
    return _out(_svc(request).list_sessions(get_principal(request), open_only))


@router.post("/sessions")
@_handle
async def open_session(request: Request):
    principal = get_principal(request)
    body = await _body(request)
    return _out(_svc(request).open_session(
        principal, body.get("board"), body.get("patient"), body.get("label"),
        body.get("practitioner")), 201)


@router.post("/sessions/{session_id}/end")
@_handle
async def end_session(request: Request, session_id: str):
    return _out(_svc(request).end_session(get_principal(request), session_id))
