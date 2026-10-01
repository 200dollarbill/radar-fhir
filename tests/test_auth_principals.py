import pytest
from fhir_server.auth import jwt as auth_jwt, passwords
from fhir_server.config import Settings


def settings(secret="test-secret-that-is-at-least-32-bytes-long"):
    return Settings(db_path=":memory:", jwt_secret=secret)


def test_password_roundtrip():
    h = passwords.hash_password("rahasia123")
    assert passwords.verify_password("rahasia123", h)
    assert not passwords.verify_password("wrong", h)
    assert h != passwords.hash_password("rahasia123")


def test_jwt_roundtrip():
    p = auth_jwt.Principal(kind="doctor", account_id="a1", role="doctor",
                           ref="Practitioner/N12345678")
    tok = auth_jwt.create_token(settings(), p)
    out = auth_jwt.verify_token(settings(), tok)
    assert out.kind == "doctor" and out.ref == "Practitioner/N12345678"


def test_expired_token_401():
    p = auth_jwt.Principal(kind="patient", account_id="a2", role="patient",
                           ref="Patient/P12345678901")
    s = settings()
    tok = auth_jwt.create_token(s, p, ttl_seconds=-1)
    with pytest.raises(auth_jwt.TokenError):
        auth_jwt.verify_token(s, tok)


def test_wrong_secret_rejected():
    p = auth_jwt.Principal(kind="admin", account_id="a3", role="admin", ref=None)
    tok = auth_jwt.create_token(settings("one-secret-that-is-at-least-32-bytes-long"), p)
    with pytest.raises(auth_jwt.TokenError):
        auth_jwt.verify_token(settings("two-secret-that-is-at-least-32-bytes-long"), tok)


def test_device_kind_not_mintable_as_jwt():
    with pytest.raises(ValueError):
        auth_jwt.create_token(settings(),
            auth_jwt.Principal(kind="device", device_id="d", patient_id="p"))
