from fastapi.testclient import TestClient
from ..api import app

client = TestClient(app)


# Placeholder test atm
def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
