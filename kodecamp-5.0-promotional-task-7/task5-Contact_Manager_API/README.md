# Contact Manager API (Modular)

A **Contact Management System** built with **FastAPI**, **SQLModel**, and **JWT authentication**. The project is modularized to keep `main.py` clean and maintainable.

---

<img width="901" height="611" alt="image" src="https://github.com/user-attachments/assets/e94dbda0-98a4-473f-a9e8-0b5951133339" />

---

## 🚀 Features
- **User Authentication**
  - Register new users
  - Login with email & password
  - JWT-based authentication
- **Contacts Management (per user)**
  - Create a new contact
  - List user’s contacts
  - Update a contact
  - Delete a contact
- **Security**
  - Password hashing with `passlib`
  - JWT tokens with `python-jose`
- **Middleware**
  - Logs client IP address for each request
- **CORS enabled** (for frontend integration)

---

## ⚙️ Installation & Setup

### 1. Clone repository
```bash
git clone https://github.com/bankole874/kodecamp-5.0-Bootcamp-Fast-API.git
cd kodecamp-5.0-Bootcamp-Fast-API/kodecamp-5.0-promotional-task-7/task5-Contact_Manager_API/

```

### 2. Create virtual environment & install dependencies
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 3. Run the app
```bash
uvicorn app.main:app --reload
```
Server will be available at 👉 `http://127.0.0.1:8000`

---

## 🧪 Testing with Postman

### 1. Register a new user
- **POST** `http://127.0.0.1:8000/users/`
- Body (JSON):
```json
{
  "email": "you@example.com",
  "password": "secret",
  "full_name": "Your Name"
}
```

### 2. Login and get JWT token
- **POST** `http://127.0.0.1:8000/token`
- Body (form-data):
  - username: `you@example.com`
  - password: `secret`
- Response contains `access_token`.

### 3. Create a contact
- **POST** `http://127.0.0.1:8000/contacts/`
- Headers: `Authorization: Bearer <token>`
- Body (JSON):
```json
{
  "name": "Alice",
  "email": "alice@example.com",
  "phone": "1234567890"
}
```

### 4. List contacts
- **GET** `http://127.0.0.1:8000/contacts/`
- Headers: `Authorization: Bearer <token>`

### 5. Update a contact
- **PUT** `http://127.0.0.1:8000/contacts/{id}`
- Headers: `Authorization: Bearer <token>`
- Body (JSON):
```json
{
  "phone": "9876543210"
}
```

### 6. Delete a contact
- **DELETE** `http://127.0.0.1:8000/contacts/{id}`
- Headers: `Authorization: Bearer <token>`

---

## 🔐 Demo User
At startup, a demo user is created automatically:
- **Email**: `demo@example.com`
- **Password**: `demopassword`

---

## 📌 Notes
- For production:
  - Use **PostgreSQL** or another RDBMS (instead of SQLite)
  - Configure **Alembic migrations**
  - Use a secure `SECRET_KEY` from environment variables
  - Restrict **CORS origins**
  - Run behind HTTPS

