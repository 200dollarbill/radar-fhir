from fastapi import Request

from ..auth import jwt as auth_jwt
from ..auth.jwt import Principal
from ..repositories import accounts as accounts_repo
from ..repositories import boards as boards_repo
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
        principal = auth_jwt.verify_token(request.app.state.settings, token)
    except auth_jwt.TokenError:
        principal = None
    if principal is not None:
        # A login token outlives a disable-account by up to its lifetime;
        # checking the account on every request cuts it off at once.
        if principal.account_id and not accounts_repo.get(
                request.app.state.conn, principal.account_id):
            raise FhirError([Issue(code="security",
                                   details_text="Account disabled",
                                   rule_number=20007)], 401)
        return principal
    row = devices_repo.resolve_token(request.app.state.conn, token)
    if row:
        return Principal(kind="device", device_id=row["device_id"],
                         patient_id=row["patient_id"])
    board = boards_repo.by_key(request.app.state.conn, token)
    if board:
        # The board may write only into its open session (spec B5); with none,
        # patient_id stays None and the device rules refuse every write.
        sess = boards_repo.open_session(request.app.state.conn, board["serial"])
        return Principal(kind="device", device_id=board["device_id"],
                         patient_id=sess["patient_ref"] if sess else None)
    raise FhirError([Issue(code="security",
                           details_text="Invalid or expired token",
                           rule_number=20007)], 401)
