import secrets
import uuid

R4_ID_RE = r"[A-Za-z0-9.\-]{1,64}"
_UUID_TYPES = {"Location", "Device", "Encounter", "Observation"}


def mint(resource_type: str) -> str:
    if resource_type == "Patient":
        return "P" + "".join(str(secrets.randbelow(10)) for _ in range(11))
    if resource_type == "Practitioner":
        return "N" + "".join(str(secrets.randbelow(10)) for _ in range(8))
    if resource_type == "Organization":
        return str(secrets.randbelow(1_000_000_000) + 100_000_000)
    if resource_type in _UUID_TYPES:
        return str(uuid.uuid4())
    raise ValueError(f"no id scheme for {resource_type}")
