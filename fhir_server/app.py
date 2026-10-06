import datetime as dt

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from .config import Settings
from .routes import admin as admin_routes
from .routes import auth as auth_routes
from .routes import fhir as fhir_routes
from .services.fhir_service import SUPPORTED_PARAMS


def capability_statement(settings) -> dict:
    param_types = {
        "identifier": "token", "name": "string", "birthdate": "date",
        "gender": "token", "subject": "reference", "patient": "reference",
        "encounter": "reference", "code": "token", "date": "date",
        "status": "token", "participant": "reference",
        "organization": "reference",
    }
    resources_out = [{
        "type": rtype,
        "interaction": [{"code": c} for c in
                        ("read", "search-type", "create", "update", "delete")],
        "searchParam": [{"code": p, "type": param_types.get(p, "token")}
                        for p in sorted(params) if p != "id"],
    } for rtype, params in SUPPORTED_PARAMS.items()]
    return {
        "resourceType": "CapabilityStatement",
        "status": "active",
        "date": dt.datetime.now(dt.timezone.utc).strftime(
            "%Y-%m-%dT%H:%M:%S+00:00"),
        "kind": "instance",
        "fhirVersion": "4.0.1",
        "format": ["application/fhir+json", "application/json"],
        "software": {"name": "PRATA FHIR server", "version": "0.1.0"},
        "implementation": {
            "description": "Local SATUSEHAT-compatible FHIR R4 server",
            "url": "http://127.0.0.1:8000/fhir-r4/v1"},
        "rest": [{
            "mode": "server",
            "security": {"service": [{
                "coding": [{
                    "system": "http://terminology.hl7.org/CodeSystem/"
                              "restful-security-service",
                    "code": "Bearer"}]}]},
            "resource": resources_out,
        }],
    }


def create_app(settings: Settings) -> FastAPI:
    from . import db as db_mod
    app = FastAPI(title="PRATA FHIR R4 server", docs_url=None, redoc_url=None)
    app.state.settings = settings
    app.state.conn = db_mod.connect(settings.db_path)
    db_mod.init(app.state.conn)
    app.include_router(auth_routes.router)
    app.include_router(admin_routes.router)

    # Registered before the FHIR router: GET /fhir-r4/v1/metadata must not be
    # swallowed by GET /fhir-r4/v1/{type_} (pre-flight ordering ruling).
    @app.get("/fhir-r4/v1/metadata")
    def metadata():
        return JSONResponse(content=capability_statement(settings),
                            media_type="application/fhir+json")

    app.include_router(fhir_routes.router)
    return app
