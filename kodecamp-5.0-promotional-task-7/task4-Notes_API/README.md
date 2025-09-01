
# 📝 Notes API (FastAPI + SQLModel)

A simple **Notes Management API** built with **FastAPI** and **SQLModel**, featuring:

- Full CRUD (create, read, delete) for notes.
- Database persistence with SQLite.
- Automatic JSON backup of all notes.
- Middleware to count and log all incoming requests.
- CORS enabled for multiple frontends.

---

## 🚀 Features
- **Note Model**: `id`, `title`, `content`, `created_at`
- **Endpoints**:
  - `POST /notes/` — create note
  - `GET /notes/` — list all notes
  - `GET /notes/{id}` — get a single note
  - `DELETE /notes/{id}` — delete note
- **Middleware**:
  - Logs the total number of requests made.
- **Backup**:
  - Saves a snapshot of all notes in `notes.json` whenever notes are created or deleted.
- **CORS**:
  - Allowed origins:  
    - `http://localhost:3000`  
    - `http://127.0.0.1:5500`

---

## ⚙️ Setup & Installation

### 1. Clone repo
```bash
git clone https://github.com/yourusername/notes-api.git
cd notes-api
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the server

```bash
uvicorn app.main:app --reload
```

Server will start at:

* API: [http://127.0.0.1:8000](http://127.0.0.1:8000)
* Docs (Swagger): [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🧪 Testing with Postman

1. Open Postman and create a new **Collection**.
2. Add requests for the following:

* **Create Note**

  * Method: `POST`
  * URL: `http://127.0.0.1:8000/notes/`
  * Body (JSON):

    ```json
    { "title": "My first note", "content": "Hello, Mr. Bassey 😊" }
    ```

* **List Notes**

  * Method: `GET`
  * URL: `http://127.0.0.1:8000/notes/`

* **Get Note by ID**

  * Method: `GET`
  * URL: `http://127.0.0.1:8000/notes/1`

* **Delete Note**

  * Method: `DELETE`
  * URL: `http://127.0.0.1:8000/notes/1`

3. Check the `notes.json` file after creating or deleting notes.

4. Watch the terminal logs for request counts:

   ```
   INFO - Total requests so far: 1
   INFO - Total requests so far: 2
   ```

---

## 📦 Example JSON Backup (`notes.json`)

```json
[
    {
        "title": "My first note",
        "content": "Hello, Mr. Bassey 😊",
        "id": 1,
        "created_at": "2025-09-01T05:54:56.099075"
    }
]
```

---

## ✅ Future Improvements

* Add **update note** (`PUT /notes/{id}`).
* Support **pagination** for large note collections.
* Add **authentication** (JWT, OAuth2) for multi-user support.
* Deploy to **Docker** or **cloud platforms**.

---

## 🛠️ Tech Stack

* [FastAPI](https://fastapi.tiangolo.com/) — modern, fast Python web framework
* [SQLModel](https://sqlmodel.tiangolo.com/) — SQLAlchemy + Pydantic hybrid
* [SQLite](https://www.sqlite.org/) — lightweight database
* [Postman](https://www.postman.com/) — API testing
