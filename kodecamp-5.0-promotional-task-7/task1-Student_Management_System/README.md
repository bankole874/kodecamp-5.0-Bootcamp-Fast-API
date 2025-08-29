
# 🎓 Student Management System (FastAPI + SQLModel)

A simple **FastAPI backend** for managing students and their grades with **authentication, authorization, database, and request logging**.

---

## 🚀 Features
- **Student CRUD API**  
  - `name`, `age`, `email`, `grades`
- **Authentication & Authorization**  
  - JWT-based login (`/token` or `/login`)
  - Credentials stored in `users.json`
- **Routers** to keep `main.py` clean
- **Middleware** to log all requests
- **CORS enabled** for `http://localhost:3000` (frontend)

---

## ⚙️ Installation

```bash
pip install fastapi uvicorn sqlmodel passlib[bcrypt] python-jose[cryptography]
```

---

## 👤 User Management

### Create a new user

```bash
python create_user.py --username Hammed --password Pass123
```

<img width="835" height="619" alt="image" src="https://github.com/user-attachments/assets/71d1da80-a8f6-4fa0-9f55-74e06b65be21" />

This generates (or updates) `users.json`:

```json
{
  "Hammed": {
    "username": "Hammed",
    "hashed_password": "$2b$12$..."
  }
}
```

---

## ▶️ Running the App

```bash
uvicorn main:app --reload
```

By default, it runs on:

```
http://127.0.0.1:8000
```

Open API docs here:

```
http://127.0.0.1:8000/docs
```

---

## 🔑 Authentication

### 1. Login to get JWT token

* **POST** `/token`

  * Body → `x-www-form-urlencoded`

    * `username`: `Hammed`
    * `password`: `Pass123`

or use `/login` with **raw JSON**:

```json
{
  "username": "Hammed",
  "password": "Pass123"
}
```

Response:

```json
{
  "access_token": "your.jwt.token",
  "token_type": "bearer"
}
```

---

## 📌 CRUD API Endpoints

All **student routes require Authorization header**:

```
Authorization: Bearer <your-token>
```

### ➕ Create Student

```http
POST /students/
```

```json
{
  "name": "John Doe",
  "age": 20,
  "email": "john@example.com",
  "grades": "A"
}
```

### 📖 Get All Students

```http
GET /students/
```

### ✏️ Update Student

```http
PUT /students/{student_id}
```

### ❌ Delete Student

```http
DELETE /students/{student_id}
```

---

## 📝 Logging

All incoming requests are logged to `app.log` via custom middleware.

---

## 🌐 CORS

CORS is enabled for:

```
http://localhost:3000
```

(Useful when connecting to a frontend app)

---

## ✅ Next Steps

* Add more fields to `Student` model (e.g., subjects, GPA, etc.)
* Implement pagination for student list
* Add role-based access (admin vs. normal user)
