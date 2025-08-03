
# 📝 Notes App API (with File System Support)

A FastAPI-based RESTful API to create, read, update, and delete notes saved as `.txt` files using the local file system.

---

## 🚀 Features

- 📄 Create new notes (saved as `.txt`)
- 📖 Read existing notes by title
- ✏️ Update note content
- 🗑️ Delete notes
- 🔐 Filename sanitization
- ⚙️ Uses the `os` module and error handling
- 🧪 Easy to test and extend
- 🛠️ Git branch-ready for feature development

---

## 📁 Directory Structure

```

notes\_app/
├── main.py
├── notes/              # Where notes are saved as .txt files
└── README.md

````

---

## 📦 Requirements

- Python 3.8+
- FastAPI
- Uvicorn

Install dependencies:

```bash
pip install fastapi uvicorn
````

---

## ▶️ How to Run

Start the FastAPI server with:

```bash
uvicorn main:app --reload
```

API will be available at:
[http://127.0.0.1:8000](http://127.0.0.1:8000)

Postman UI:
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

<img width="1619" height="548" alt="image" src="https://github.com/user-attachments/assets/1e60c5b2-ecd3-4e43-b951-5835df76af25" />

---

## 📬 API Endpoints

### 🔹 Create Note

**POST** `/notes/`

**Body:**

```json
{
  "title": "shopping",
  "content": "Buy milk and eggs"
}
```

---

### 🔹 Read Note

**GET** `/notes/{title}`

**Response:**

```json
{
  "title": "shopping",
  "content": "Buy milk and eggs"
}
```

---

### 🔹 Update Note

**POST** `/notes/{title}`

**Body:**

```json
{
  "title": "shopping",
  "content": "Buy milk, eggs, and bread"
}
```

---

### 🔹 Delete Note

**DELETE** `/notes/{title}`

---

## ⚠️ Notes

* Notes are stored in the `notes/` folder.
* Titles with `/` are sanitized to avoid path traversal.
* Files are saved with `.txt` extension.
