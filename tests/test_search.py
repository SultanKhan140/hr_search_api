from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_search_with_filters():
    response = client.get("/search?status=Active")
    assert response.status_code == 200
