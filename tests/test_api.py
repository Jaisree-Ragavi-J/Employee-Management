import pytest
from app import app
from database import init_db
import json


# ---------------- FIX DB SAFETY ----------------
@pytest.fixture(autouse=True)
def setup_db():
    init_db()
    yield


# ---------------- CLIENT FIXTURE ----------------
@pytest.fixture
def client():
    app.config["TESTING"] = True
    return app.test_client()


# ---------------- HOME ----------------
def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Employee Management API Running" in response.data


# ---------------- CREATE ----------------
def test_create_employee_api(client):
    response = client.post(
        "/employees",
        json={
            "name": "API",
            "email": "api@gmail.com",
            "dept": "IT"
        }
    )

    assert response.status_code == 201

    data = response.get_json()
    assert data["name"] == "API"


# ---------------- GET ALL ----------------
def test_get_all_api(client):
    response = client.get("/employees")

    assert response.status_code == 200
    assert isinstance(response.get_json(), list)