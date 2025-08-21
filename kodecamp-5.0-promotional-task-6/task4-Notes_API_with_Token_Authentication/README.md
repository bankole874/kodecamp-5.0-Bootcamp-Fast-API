# 📝 Notes API with JWT Authentication

A simple **FastAPI** project for managing notes with **JWT-based authentication**.
Each user can log in, receive a token, and create/view their own notes. Notes are stored in a JSON file per user.

---

## 🚀 Features

* **User Authentication** using JWT (JSON Web Tokens)
* **Secure Endpoints** with Bearer token
* **Notes Management**

  * Add notes (`POST /notes/`)
  * View personal notes (`GET /notes/`)
* **Per-user storage**: Notes saved in `<username>_notes.json`

---

## ▶️ Running the App

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

By default, the app will run at:

```
http://127.0.0.1:8000
```

Interactive API docs available at:

* Swagger UI → `http://127.0.0.1:8000/docs`
* ReDoc → `http://127.0.0.1:8000/redoc`

---

## 🔑 Authentication Flow

1. **Login to get JWT Token**

   * Endpoint: `POST /login/`
   * Request (form-data):

     ```
     username=alice
     password=password123
     ```
   * Response:

     ```json
     {
       "access_token": "<JWT_TOKEN>",
       "token_type": "bearer"
     }
     ```

2. **Use Token in Authorization Header**
   Example:

   ```
   Authorization: Bearer <JWT_TOKEN>
   ```

---

## 📌 Endpoints

### 1. Login

**POST** `/login/`
Authenticate and receive JWT token.

---

### 2. Add Note

**POST** `/notes/`
Requires token.

**Body (JSON):**

```json
{
  "title": "Shopping List",
  "content": "Eggs, Milk, Bread"
}
```

**Response:**

```json
{
  "msg": "Note added",
  "note": {
    "title": "Shopping List",
    "content": "Eggs, Milk, Bread",
    "date": "2025-08-20T12:34:56.789123"
  }
}
```

---

### 3. Get Notes

**GET** `/notes/`
Requires token.

**Response:**

```json
[
  {
    "title": "Shopping List",
    "content": "Eggs, Milk, Bread",
    "date": "2025-08-20T12:34:56.789123"
  }
]
```

---

## 👥 Default Users

The project comes with some predefined users (stored in `fake_users_db` inside `main.py`):

| Username | Password    |
| -------- | ----------- |
| alice    | password123 |
| bob      | secret456   |
