from app import app
from database import init_db

# 🔥 ADD THIS
init_db()


def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200


def test_create_employee_api():
    client = app.test_client()

    response = client.post("/employees", json={
        "name": "API",
        "email": "api@gmail.com",
        "dept": "IT"
    })

    assert response.status_code == 201


def test_get_all_api():
    client = app.test_client()
    response = client.get("/employees")

    assert response.status_code == 200