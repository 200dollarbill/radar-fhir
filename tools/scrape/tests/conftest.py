import socket
import pytest


def _online():
    try:
        socket.create_connection(("hl7.org", 443), timeout=3).close()
        return True
    except OSError:
        return False


def pytest_configure(config):
    config.addinivalue_line("markers", "network: needs internet")


def pytest_collection_modifyitems(config, items):
    if _online():
        return
    skip = pytest.mark.skip(reason="offline")
    for item in items:
        if "network" in item.keywords:
            item.add_marker(skip)
