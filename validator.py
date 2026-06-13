def validate_employee(data):
    if not data:
        return "Request body is missing"

    if not data.get("name"):
        return "Name is required"

    if not data.get("email"):
        return "Email is required"

    if "@" not in data["email"]:
        return "Invalid email format"

    return None