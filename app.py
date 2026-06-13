from flask import Flask, request, jsonify
from employee_services import *
from validator import validate_employee
from database import init_db

app = Flask(__name__)


@app.route("/")
def home():
    return "Employee Management API Running"


@app.route("/docs")
def docs():
    base_url = "http://127.0.0.1:5000"

    return jsonify({
        "create_employee": f"POST {base_url}/employees",
        "get_all": f"GET {base_url}/employees",
        "get_by_id": f"GET {base_url}/employees/1",
        "update": f"PUT {base_url}/employees/1",
        "delete": f"DELETE {base_url}/employees/1",
        "search": f"GET {base_url}/employees/search?name=rag"
    })


@app.route("/employees", methods=["POST"])
def create():
    data = request.get_json()

    error = validate_employee(data)
    if error:
        return jsonify({"error": error}), 400

    result = create_employee(
        data.get("name"),
        data.get("email"),
        data.get("dept")
    )

    return jsonify(result), 201


@app.route("/employees", methods=["GET"])
def get_all():
    return jsonify(get_all_employees()), 200


@app.route("/employees/<int:emp_id>", methods=["GET"])
def get_by_id(emp_id):
    emp = get_employee_by_id(emp_id)

    if not emp:
        return jsonify({"error": "Employee not found"}), 404

    return jsonify(emp), 200


@app.route("/employees/<int:emp_id>", methods=["PUT"])
def update(emp_id):
    data = request.get_json()

    emp = update_employee(emp_id, data)

    if not emp:
        return jsonify({"error": "Employee not found"}), 404

    return jsonify(emp), 200


@app.route("/employees/<int:emp_id>", methods=["DELETE"])
def delete(emp_id):
    success = delete_employee(emp_id)

    if not success:
        return jsonify({"error": "Employee not found"}), 404

    return jsonify({"message": "Deleted successfully"}), 200


@app.route("/employees/search", methods=["GET"])
def search():
    name = request.args.get("name")

    if not name:
        return jsonify({"error": "Name query parameter required"}), 400

    result = search_employee_by_name(name)
    return jsonify(result), 200


if __name__ == "__main__":
    init_db()
    app.run(debug=True)