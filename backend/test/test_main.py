from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_welcome():
    response = client.get("/")
    assert app is not None
    assert response.status_code == 200
    assert response.json() == {"message": "API RESTfull Home Page"}


def test_not_found():
    response = client.get("/non-existent-route")
    assert response.status_code == 404
    assert response.json() != {"message": "API RESTfull Home Page"}
