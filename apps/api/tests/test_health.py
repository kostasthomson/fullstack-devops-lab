from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root_endpoint() -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "API is running"
    assert "environment" in response.json()


def test_health_endpoint() -> None:
    response = client.get("/health")
    assert response.status_code in (200, 503)
    assert response.json()["status"] in ("ok", "degraded")
    assert isinstance(response.json()["database_connected"], bool)