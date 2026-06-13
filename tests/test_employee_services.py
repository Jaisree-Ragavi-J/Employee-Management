from employee_services import *
from database import init_db


# Runs before all tests
def setup_module():
    init_db()


def test_create_and_get():
    emp = create_employee("Test", "test@gmail.com", "IT")
    assert emp["name"] == "Test"

    fetched = get_employee_by_id(emp["id"])
    assert fetched is not None


def test_update():
    emp = create_employee("Old", "old@gmail.com", "HR")

    updated = update_employee(emp["id"], {
        "name": "New",
        "email": "new@gmail.com",
        "dept": "IT"
    })

    assert updated["name"] == "New"


def test_delete():
    emp = create_employee("Delete", "del@gmail.com", "IT")

    result = delete_employee(emp["id"])
    assert result is True