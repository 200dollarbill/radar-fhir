import json
from urllib.parse import parse_qsl

from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from ..auth import jwt as auth_jwt
from ..auth.passwords import verify_password
from ..repositories import accounts
from ..validation.issues import Issue
from ..validation.outcome import to_outcome

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/token")
async def token(request: Request):
    body = await _read_body(request)
    if not isinstance(body, dict):
        body = {}
    acct = accounts.get_by_username(request.app.state.conn,
                                    str(body.get("username") or ""))
    if not acct or not verify_password(str(body.get("password") or ""),
                                       acct["password_hash"]):
        return JSONResponse(status_code=401,
                            content=to_outcome([Issue(
                                code="security",
                                details_text="Authentication failed",
                                rule_number=20007)]),
                            media_type="application/fhir+json")
    principal = auth_jwt.Principal(kind=acct["role"], account_id=acct["id"],
                                   role=acct["role"], ref=acct["subject_ref"])
    settings = request.app.state.settings
    return {"access_token": auth_jwt.create_token(settings, principal),
            "token_type": "Bearer",
            "expires_in": settings.jwt_ttl_seconds}


async def _read_body(request: Request):
    ct = request.headers.get("content-type", "")
    raw = await request.body()
    if "application/x-www-form-urlencoded" in ct:
        return dict(parse_qsl(raw.decode()))
    try:
        return json.loads(raw) if raw else {}
    except (ValueError, UnicodeDecodeError):
        return {}
