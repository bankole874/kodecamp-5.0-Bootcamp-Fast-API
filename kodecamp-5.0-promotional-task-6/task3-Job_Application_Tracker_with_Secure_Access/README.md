# Job Application Tracker API

A simple **FastAPI** project for securely tracking job applications per user. Each user can only view and manage their own applications.

---

## Features
- **User Authentication**: Basic Auth for secure access.
- **Add Applications**: `POST /applications/` — Add a new job application.
- **View Applications**: `GET /applications/` — Retrieve only the logged-in user's job applications.
- **Persistent Storage**: Data stored in `applications.json` (per-user isolation).

---

## Usage

### Authentication
This project uses **Basic Auth**. Default demo users:
- `alice / password1`
- `bob / password2`

### Endpoints

#### ➤ Add Application
**POST** `/applications/`
```json
{
  "job_title": "Backend Developer",
  "company": "TechCorp",
  "date_applied": "2025-08-21",
  "status": "Interview Scheduled"
}
```

#### ➤ View Applications
**GET** `/applications/`
- Returns only the authenticated user’s job applications.

---

## File Storage
Applications are stored in `applications.json`:
```json
{
  "alice": [
    {
      "job_title": "Backend Developer",
      "company": "TechCorp",
      "date_applied": "2025-08-21",
      "status": "Interview Scheduled"
    }
  ],
  "bob": []
}
```
