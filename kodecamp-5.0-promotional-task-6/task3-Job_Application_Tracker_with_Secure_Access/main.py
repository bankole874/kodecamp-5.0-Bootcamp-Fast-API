# Task 3: Job Application Tracker with Secure Access
# Goal: Build an API where each user can only see their own job applications.
# Features:
# JobApplication class: job title, company, date applied, status
# Authenticated users can:
# POST /applications/ — add
# GET /applications/ — view only their applications
# Store per-user data in applications.json
# Use dependency to get current logged-in user and filter results

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel
from typing import List
from datetime import date
import secrets
import json
import os

app = FastAPI(title="Job Application Tracker")
security = HTTPBasic()

DATA_FILE = "applications.json"

# In-memory user store for demo purposes (replace with DB in real use)
USERS = {
    "alice": "password1",
    "bob": "password2",
}

# Pydantic model for applications
class JobApplication(BaseModel):
    job_title: str
    company: str
    date_applied: date
    status: str


# --- Helpers for persistence ---
def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2, default=str)


# --- Authentication Dependency ---
def get_current_user(credentials: HTTPBasicCredentials = Depends(security)):
    username = credentials.username
    password = credentials.password

    correct_password = USERS.get(username)
    if not correct_password or not secrets.compare_digest(password, correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Basic"},
        )
    return username


# --- Routes ---
@app.post("/applications/", response_model=JobApplication)
def add_application(
    application: JobApplication, user: str = Depends(get_current_user)
):
    data = load_data()
    if user not in data:
        data[user] = []

    data[user].append(application.dict())
    save_data(data)

    return application


@app.get("/applications/", response_model=List[JobApplication])
def get_applications(user: str = Depends(get_current_user)):
    data = load_data()
    return data.get(user, [])
