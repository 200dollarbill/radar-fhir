from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from ..auth.passwords import hash_password
from ..authz import AuthzError
from ..repositories import accounts
from ..services.fhir_service import FhirError
from ..validation.issues import Issue
from ..validation.outcome import to_outcome
from .deps import get_principal

router = APIRouter(prefix="/fhir-r4/v1/admin", tags=["admin"])


def _err(exc):
    return JSONResponse(status_code=exc.status, content=to_outcome(exc.issues),
                        media_type="application/fhir+json")


@router.post("/accounts")
async def create_account(request: Request):
    try:
        principal = get_principal(request)
        if principal.kind != "admin":
            raise AuthzError("Only admins may manage accounts")
        body = await request.json()
        username, password = body.get("username"), body.get("password")
        role, ref = body.get("role"), body.get("ref")
        if not username or not password or role not in ("admin", "doctor",
                                                        "patient"):
            raise FhirError([Issue(code="value",
                                   details_text="username, password, role"
                                                " (admin|doctor|patient)"
                                                " required")], 400)
        accounts.create(request.app.state.conn, username,
                        hash_password(password), role, ref)
        return JSONResponse(status_code=201, content={"created": username},
                            media_type="application/fhir+json")
    except (FhirError, AuthzError) as exc:
        return _err(exc)


@router.get("/accounts")
async def list_accounts(request: Request):
    try:
        principal = get_principal(request)
        if principal.kind != "admin":
            raise AuthzError("Only admins may manage accounts")
        rows = accounts.list(request.app.state.conn)
        return JSONResponse(
            content=[{"username": r["username"], "role": r["role"],
                      "ref": r["subject_ref"]} for r in rows],
            media_type="application/fhir+json")
    except (FhirError, AuthzError) as exc:
        return _err(exc)
