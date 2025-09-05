
# 📌 Job Application Tracker (FastAPI + SQLModel)

A simple **Job Application Tracker API** built with **FastAPI** and **SQLModel**.  
It allows users to track job applications, search by status, and ensures **per-user isolation** with authentication.  
All requests require a **User-Agent header**.

---

<img width="895" height="855" alt="image" src="https://github.com/user-attachments/assets/9c2e4ec8-e305-42bc-b09c-a5c5656e2fd9" />

---

## 🚀 Features
- Add new job applications
- List all job applications for the authenticated user
- Search job applications by status (e.g., `pending`, `offer`, `rejected`)
- Authentication via **Bearer Token**
- Each user only sees their own applications
- Middleware enforces `User-Agent` header
- Error handling for invalid requests

---

## 🛠️ Tech Stack
- [FastAPI](https://fastapi.tiangolo.com/) (API framework)
- [SQLModel](https://sqlmodel.tiangolo.com/) (ORM + SQLAlchemy + Pydantic)
- [SQLite](https://www.sqlite.org/) (database)
- [Uvicorn](https://www.uvicorn.org/) (ASGI server)

---

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/bankole874/kodecamp-5.0-Bootcamp-Fast-API
   cd kodecamp-5.0-Bootcamp-Fast-API/kodecamp-5.0-promotional-task-7/task3-Job_Application_Tracker

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux / macOS
   ```

3. Install dependencies:

   ```bash
   pip install fastapi==0.111.0 sqlmodel==0.0.22 uvicorn[standard]==0.30.0
   ```

4. Run the server:

   ```bash
   uvicorn main:app --reload
   ```

The API will be available at 👉 `http://127.0.0.1:8000`

---

## 🔑 Authentication

For demo purposes, tokens are **hard-coded** in `deps.py`:

```python
TOKENS = {
    "token-user-1": 1,
    "token-user-2": 2,
}
```

➡️ Use either `token-user-1` or `token-user-2` as a **Bearer token**.

Example header:

```
Authorization: Bearer token-user-1
User-Agent: postman
```

---

## 📖 API Endpoints

### 1️⃣ Add a new job application

`POST /applications/`

Request body:

```json
{
  "company": "Kodecamp",
  "position": "Backend Engineer",
  "status": "pending",
  "date_applied": "2025-08-29"
}
```

Response:

```json
{
  "id": 1
  "company": "Kodecamp",
  "position": "Backend Engineer",
  "status": "pending",
  "date_applied": "2025-08-29"
}
```

---

### 2️⃣ List all applications

`GET /applications/`

Response:

```json
[
  {
    "id": 1
    "company": "Kodecamp",
    "position": "Backend Engineer",
    "status": "pending",
    "date_applied": "2025-08-29"
  }
]
```

---

### 3️⃣ Search applications by status

`GET /applications/search?status=pending`

Response:

```json
[
  {
    "id": 1
    "company": "Kodecamp",
    "position": "Backend Engineer",
    "status": "pending",
    "date_applied": "2025-08-29"
  }
]
```

---

### 4️⃣ Middleware check

If you send a request **without `User-Agent` header**, you’ll get:

```json
{
  "detail": "User-Agent header is required."
}
```

---

## 🧪 Testing with Postman

* Set `Authorization: Bearer token-user-1`
* Set `User-Agent: postman`
* Use the endpoints above

👉 You can also explore the API in **Swagger UI**:
`http://127.0.0.1:8000/docs`

---

## 📌 Notes

* Replace the demo token-based auth in `deps.py` with a real authentication system (OAuth2/JWT) for production use.
* You can easily extend `/applications/search` with more filters (company, date ranges, etc.).
* SQLite is used for simplicity; switch to PostgreSQL/MySQL in production.


