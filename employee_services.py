from database import get_connection


def create_employee(name, email, dept):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO employees (name, email, dept) VALUES (?, ?, ?)",
        (name, email, dept)
    )

    conn.commit()
    emp_id = cursor.lastrowid
    conn.close()

    return {
        "id": emp_id,
        "name": name,
        "email": email,
        "dept": dept
    }


def get_all_employees():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    conn.close()

    return [
        {"id": r[0], "name": r[1], "email": r[2], "dept": r[3]}
        for r in rows
    ]


def get_employee_by_id(emp_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM employees WHERE id=?", (emp_id,))
    row = cursor.fetchone()
    conn.close()

    if not row:
        return None

    return {"id": row[0], "name": row[1], "email": row[2], "dept": row[3]}


def update_employee(emp_id, data):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM employees WHERE id=?", (emp_id,))
    if not cursor.fetchone():
        conn.close()
        return None

    cursor.execute(
        "UPDATE employees SET name=?, email=?, dept=? WHERE id=?",
        (
            data.get("name"),
            data.get("email"),
            data.get("dept"),
            emp_id
        )
    )

    conn.commit()
    conn.close()

    return get_employee_by_id(emp_id)


def delete_employee(emp_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM employees WHERE id=?", (emp_id,))
    conn.commit()

    deleted = cursor.rowcount
    conn.close()

    return deleted > 0


def search_employee_by_name(name):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM employees WHERE name LIKE ?",
        ('%' + name + '%',)
    )

    rows = cursor.fetchall()
    conn.close()

    return [
        {"id": r[0], "name": r[1], "email": r[2], "dept": r[3]}
        for r in rows
    ]