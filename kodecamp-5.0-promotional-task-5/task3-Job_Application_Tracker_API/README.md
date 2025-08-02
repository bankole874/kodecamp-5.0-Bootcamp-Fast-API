
# 📋 Job Application Tracker API

A simple RESTful API for managing job applications, built with **FastAPI**. Applications are saved to a JSON file and can be created, listed, and searched by status.

---

## 🚀 Features

- ✅ Add new job applications
- 📄 List all applications
- 🔍 Search by status (`pending`, `accepted`, `rejected`)
- 💾 Persistent storage in `applications.json`
- ⚠️ Input error handling with `try-except`

---

## 🛠️ Installation

1. **Clone the repository:**

```bash
git clone https://github.com/bankole874/kodecamp-5.0-Bootcamp-Fast-API.git
cd kodecamp-5.0-promotional-task-5/task3-Job_Application_Tracker_API/
````

2. **Create a virtual environment and activate it:**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**

```bash
pip install fastapi uvicorn
```

---

## ▶️ Run the API

```bash
uvicorn main:app --reload
```

The API will be available at:
🔗 `http://127.0.0.1:8000`

---

## 📬 API Endpoints

### ✅ POST `/applications/`

Create a new job application.

**JSON Body:**

```json
{
  "name": "Hammed Bankole",
  "company": "TeKnowledge",
  "position": "Technical Support Engineer",
  "status": "accepted"
}
```

---

### 📄 GET `/applications/`

Get all job applications.

---

### 🔍 GET `/applications/search?status=pending`

Search applications by status (`pending`, `accepted`, or `rejected`).

---

## 📦 Data Persistence

Applications are saved in `applications.json`. If the file doesn't exist, it will be created automatically.

---

## 🙋‍♂️ Author

**Hammed Bankole**
Feel free to reach out or contribute!
