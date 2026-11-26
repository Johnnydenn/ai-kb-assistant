"""Tests for the health endpoint."""

from fastapi.testclient import TestClient

from kb_assistant import __version__
from kb_assistant.app import app

client = TestClient(app)


def test_health_returns_200() -> None:
    """The health endpoint responds successfully."""
    response = client.get("/health")
    assert response.status_code == 200


def test_health_status_is_ok() -> None:
    """The health payload reports an ok status."""
    response = client.get("/health")
    assert response.json()["status"] == "ok"


def test_health_version_matches_package() -> None:
    """The health payload reports the package version."""
    response = client.get("/health")
    assert response.json()["version"] == __version__
