import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    db_path: str
    jwt_secret: str
    jwt_ttl_seconds: int = 3600
    earliest_date: str = "2014-06-03"

    @classmethod
    def from_env(cls, **overrides):
        base = dict(
            db_path=os.environ.get("FHIR_DB_PATH", "fhir_server.db"),
            jwt_secret=os.environ.get("FHIR_JWT_SECRET", ""),
            jwt_ttl_seconds=int(os.environ.get("FHIR_JWT_TTL", "3600")),
            earliest_date=os.environ.get("FHIR_EARLIEST_DATE", "2014-06-03"),
        )
        base.update({k: v for k, v in overrides.items() if v is not None})
        if not base["jwt_secret"]:
            raise ValueError("FHIR_JWT_SECRET is required")
        return cls(**base)
