# Task 1: Student Management System (with Database + Security)
# Goal: Build a FastAPI backend for managing students and their grades.
# Features:
# Student model: name, age, email, grades (store in relational DB using SQLModel).
# CRUD endpoints (/students/) to create, view, update, delete students.
# Dependency injection for DB session.
# Authentication & Authorization → only logged-in users can add/edit.
# Store login credentials in users.json
# Add middleware to log every request into a log file.
# Allow CORS for http://localhost:3000 (frontend).

# main.py
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.database import init_db
from core.middleware import log_requests
from core import auth
from routers import students

logging.basicConfig(filename="app.log", level=logging.INFO, format="%(asctime)s - %(message)s")

app = FastAPI(title="Student Management API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.middleware("http")(log_requests)

app.include_router(auth.router)
app.include_router(students.router)

@app.on_event("startup")
def on_startup():
    init_db()

