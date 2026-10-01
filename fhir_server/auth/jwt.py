from dataclasses import dataclass
import time

import jwt as pyjwt


@dataclass(frozen=True)
class Principal:
    kind: str
    account_id: str | None = None
    role: str | None = None
    ref: str | None = None
    device_id: str | None = None
    patient_id: str | None = None


class TokenError(Exception):
    pass


_HUMAN_KINDS = {"admin", "doctor", "patient"}


def create_token(settings, principal: Principal,
                 ttl_seconds: int | None = None) -> str:
    if principal.kind not in _HUMAN_KINDS:
        raise ValueError("device principals do not use JWTs")
    now = int(time.time())
    ttl = ttl_seconds if ttl_seconds is not None else settings.jwt_ttl_seconds
    return pyjwt.encode(
        {"sub": principal.account_id, "role": principal.role,
         "ref": principal.ref, "iat": now, "exp": now + ttl},
        settings.jwt_secret, algorithm="HS256")


def verify_token(settings, token: str) -> Principal:
    try:
        claims = pyjwt.decode(token, settings.jwt_secret,
                              algorithms=["HS256"],
                              options={"require": ["exp"]})
    except pyjwt.PyJWTError as exc:
        raise TokenError(str(exc)) from exc
    role = claims.get("role")
    if role not in _HUMAN_KINDS:
        raise TokenError("bad role")
    return Principal(kind=role, account_id=claims.get("sub"),
                     role=role, ref=claims.get("ref"))
