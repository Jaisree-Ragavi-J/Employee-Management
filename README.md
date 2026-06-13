# 🚀 Employee Management API

A Flask-based Employee Management System that provides RESTful APIs to manage employee records with full CRUD functionality, search capability, validation, and automated testing.

---

## 📌 Features

* ✅ Create Employee
* ✅ Get All Employees
* ✅ Get Employee by ID
* ✅ Update Employee
* ✅ Delete Employee
* ✅ Search Employee by Name
* ✅ Input Validation
* ✅ Error Handling
* ✅ API Documentation (`/docs`)
* ✅ Automated Testing using Pytest
* ✅ CI Pipeline using GitHub Actions

---

## 🛠️ Tech Stack

* **Backend:** Flask (Python)
* **Database:** SQLite
* **Testing:** Pytest
* **CI/CD:** GitHub Actions
* **Deployment:** Render

---

## 📁 Project Structure

```
EMPLOYEE-MANAGEMENT/
│
├── app.py
├── database.py
├── employee_services.py
├── validator.py
├── requirements.txt
├── .gitignore
│
├── tests/
│   ├── conftest.py
│   ├── test_api.py
│   └── test_employee_services.py
│
└── .github/workflows/ci.yml
```

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```
git clone https://github.com/<your-username>/Employee-Management.git
cd Employee-Management
```

---

### 2. Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3. Install Dependencies

```
pip install -r requirements.txt
```

---

### 4. Run Application

```
python app.py
```

---

## 🌐 API Endpoints

| Method | Endpoint                | Description        |
| ------ | ----------------------- | ------------------ |
| POST   | /employees              | Create employee    |
| GET    | /employees              | Get all employees  |
| GET    | /employees/{id}         | Get employee by ID |
| PUT    | /employees/{id}         | Update employee    |
| DELETE | /employees/{id}         | Delete employee    |
| GET    | /employees/search?name= | Search by name     |

---

## 📄 API Documentation

```
/docs
```

---

## 🧪 Running Tests

```
pytest
```

---

## 🚀 Deployment

The application is deployed on **Render** and supports production-ready execution using Gunicorn.

---

## 🧠 DevOps Highlights

* CI pipeline configured using GitHub Actions
* Automated testing on each push
* Modular project structure
* Database initialization handled for tests
* Clean code and validation layer implemented

---

## 📌 Future Improvements

* Add Docker support
* Use PostgreSQL for production
* Add authentication
* Integrate Swagger UI

---

## 👩‍💻 Author

**Jaisree Ragavi**

---

## ⭐ Acknowledgement

Developed as part of a DevOps trainee assignment focusing on backend development, testing, and deployment practices.
