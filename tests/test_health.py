import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def client():
    """Create a test client for the FastAPI application."""
    return TestClient(app)


def test_health_returns_200(client):
    """Health endpoint should return HTTP 200."""
    response = client.get("/health")
    assert response.status_code == 200


def test_health_response_has_required_fields(client):
    """Health response must include status, hostname, and timestamp."""
    data = client.get("/health").json()
    assert "status" in data
    assert "hostname" in data
    assert "timestamp" in data


def test_health_status_is_healthy(client):
    """Status field should be 'healthy'."""
    data = client.get("/health").json()
    assert data["status"] == "healthy"


def test_health_hostname_is_not_empty(client):
    """Hostname should never be empty."""
    data = client.get("/health").json()
    assert len(data["hostname"]) > 0


def test_health_timestamp_is_iso_format(client):
    """Timestamp should be a valid ISO 8601 string."""
    from datetime import datetime

    data = client.get("/health").json()
    # Will raise ValueError if not valid ISO format
    datetime.fromisoformat(data["timestamp"])
