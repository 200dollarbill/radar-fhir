from fastapi import Request

from ..auth import jwt as auth_jwt
from ..auth.jwt import Principal
from ..repositories import devices as devices_repo
from ..services.fhir_service import FhirError, FhirService
from ..validation.issues import Issue


def get_service(request: Request) -> FhirService:
    return FhirService(request.app.state.conn, request.app.state.settings)


def get_principal(request: Request) -> Principal:
    header = request.headers.get("Authorization", "")
    if not header.startswith("Bearer "):
        raise FhirError([Issue(code="security",
                               details_text="Authorization: Bearer <token>"
                                            " is required",
                               rule_number=20007)], 401)
    token = header.removeprefix("Bearer ").strip()
    try:
        return auth_jwt.verify_token(request.app.state.settings, token)
    except auth_jwt.TokenError:
        pass
    row = devices_repo.resolve_token(request.app.state.conn, token)
    if row:
        return Principal(kind="device", device_id=row["device_id"],
                         patient_id=row["patient_id"])
    raise FhirError([Issue(code="security",
                           details_text="Invalid or expired token",
                           rule_number=20007)], 401)
