import pytest
from fastapi.testclient import TestClient

from app.main import app

@pytest.fixture
def client():
    """Create a test client for the FastAPI application."""
    return TestClient(app)

def test_info_returns_200(client):
    """Info endpoint should return HTTP 200."""
    response = client.get("/info")
    assert response.status_code == 200

def test_info_response_content(client):
    """Info endpoint should return the expected static JSON."""
    response = client.get("/info")
    data = response.json()
    
    assert data["message"] == "Welcome to FastAPI on Kubernetes!"
    assert data["author"] == "Yusdanis"
    assert data["app_name"] == "FastAPIApp"
    assert data["version"] == "1.0.0"
