# 🎓 Secure Student Portal API

A **FastAPI** project that allows students to securely **register, log in, and view their grades**.  
Passwords are securely hashed, and data is stored in `students.json`.

<img width="829" height="453" alt="image" src="https://github.com/user-attachments/assets/30d124d2-2c1e-458c-b524-fb378171b1ab" />

---

## 🚀 Features
- ✅ Student registration (`/register/`)
- ✅ Login with **HTTP Basic Auth** (`/login/`)
- ✅ Fetch grades (requires authentication) (`/grades/`)
- ✅ Password hashing using SHA-256
- ✅ Persistent storage in `students.json`
- ✅ Error handling with `try-except`

---

## 📦 Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/student-portal-api.git
cd student-portal-api
````

### 2. Create and activate a virtual environment

```bash
python -m venv venv
venv\Scripts\activate       # On Windows
```

### 3. Install dependencies

```bash
pip install fastapi uvicorn pydantic
```

---

## ▶️ Running the API

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

API will be live at:
👉 `http://127.0.0.1:8000`

---

## 🔑 API Endpoints

### 1. Register a student

**POST** `/register/`
**Body (JSON):**

```json
{
  "username": "alice",
  "password": "mypassword",
  "grades": [95, 88, 92]
}
```

**Response:**

```json
{ "message": "Student registered successfully" }
```

---

### 2. Login

**POST** `/login/`
**Auth:** Basic Auth (username & password)

**Response:**

```json
{ "message": "Welcome, alice!" }
```

---

### 3. Get Grades

**GET** `/grades/`
**Auth:** Basic Auth

**Response:**

```json
{
  "username": "alice",
  "grades": [95, 88, 92]
}
```

---

## 🧪 Testing with Postman

1. Open Postman and create a new request.
2. For **Register**:

   * Method: `POST`
   * URL: `http://127.0.0.1:8000/register/`
   * Body → `raw → JSON`
   * Paste student details.
3. For **Login**:

   * Method: `POST`
   * URL: `http://127.0.0.1:8000/login/`
   * Authorization → `Basic Auth` → enter username & password.
4. For **Get Grades**:

   * Method: `GET`
   * URL: `http://127.0.0.1:8000/grades/`
   * Authorization → `Basic Auth`.

---

## ⚡ Example cURL Commands

### Register

```bash
curl -X POST "http://127.0.0.1:8000/register/" \
-H "Content-Type: application/json" \
-d '{"username":"alice","password":"mypassword","grades":[90,85,92]}'
```

### Login

```bash
curl -u alice:mypassword -X POST "http://127.0.0.1:8000/login/"
```

### Get Grades

```bash
curl -u alice:mypassword "http://127.0.0.1:8000/grades/"
```
