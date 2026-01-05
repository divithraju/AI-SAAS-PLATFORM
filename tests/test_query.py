from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_query_validation():
    res = client.post("/query", json={"question": ""})
    assert res.status_code == 400
