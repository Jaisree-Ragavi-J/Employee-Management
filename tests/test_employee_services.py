import pytest
from employee_services import *
from database import get_connection, init_db


# ---------------- FIX TEST DB ----------------
@pytest.fixture(scope="module", autouse=True)
def setup_db():
    init_db()
    yield


# ---------------- TEST CREATE ----------------
def test_create_employee():
    emp = create_employee("John", "john@test.com", "IT")

    assert emp["name"] == "John"
    assert emp["email"] == "john@test.com"
    assert emp["dept"] == "IT"
    assert "id" in emp


# ---------------- TEST GET ALL ----------------
def test_get_all():
    employees = get_all_employees()
    assert isinstance(employees, list)


# ---------------- TEST GET BY ID ----------------
def test_get_by_id():
    emp = create_employee("Alice", "alice@test.com", "HR")

    result = get_employee_by_id(emp["id"])

    assert result["name"] == "Alice"


# ---------------- TEST UPDATE ----------------
def test_update_employee():
    emp = create_employee("Bob", "bob@test.com", "Finance")

    updated = update_employee(emp["id"], {"dept": "IT"})

    assert updated["dept"] == "IT"


# ---------------- TEST DELETE ----------------
def test_delete_employee():
    emp = create_employee("Charlie", "charlie@test.com", "Ops")

    result = delete_employee(emp["id"])

    assert result is True


# ---------------- TEST SEARCH ----------------
def test_search_employee():
    create_employee("Ravi Kumar", "ravi@test.com", "IT")

    results = search_employee_by_name("Ravi")

    assert len(results) >= 1