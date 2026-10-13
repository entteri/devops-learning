from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_info():
    response = client.get("/info")

    assert response.status_code == 200
    assert response.json()["name"] == "devops-learning"
    assert response.json()["version"] == "0.1.0"
    assert "environment" in response.json()