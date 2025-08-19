# Task 1: Secure Student Portal API
# Goal: Build a FastAPI API where students can log in to view their grades.
# Features:
# Student class with username, password (hashed), grades list
# POST /register/ to register students (store in students.json)
# POST /login/ to authenticate
# GET /grades/ — requires authentication via HTTP Basic or OAuth2 dependency
# Use try-except to handle file errors
# Commit changes to GitHub with descriptive messages

from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel
from typing import List, Dict
import json
import hashlib
import secrets
import os

app = FastAPI(title="Secure Student Portal API")

STUDENTS_FILE = "students.json"
class Student(BaseModel):
    username: str
    password: str
    grades: List[int] = []

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def load_students() -> List[Student]:
    try:
        if not os.path.exists(STUDENTS_FILE):
            return []
        with open(STUDENTS_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_students(students: Dict[str, dict]) -> None:
    try:
        with open(STUDENTS_FILE, "w") as f:
            json.dump(students, f, indent=4)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error saving students: {str(e)}")
    
def authenticate(credentials: HTTPBasicCredentials) -> dict:
    students = load_students()
    student = students.get(credentials.username)
    
    if not student:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    
    hashed_password = hash_password(credentials.password)
    if not secrets.compare_digest(student["password"], hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    
    return student

@app.post("/register/", status_code=status.HTTP_201_CREATED)
def register_student(student: Student):
    students = load_students()
    if student.username in students:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already registered")
    
    students[student.username] = {
        "username": student.username,
        "password": hash_password(student.password),
        "grades": student.grades
    }
    save_students(students)
    return {"message": "Student registered successfully"}

@app.post("/login/")
def login_student(credentials: HTTPBasicCredentials):
    student = authenticate(credentials)
    return {"message": f"Welcome {student['username']}!"}

@app.get("/grades/")
def get_grades(credentials: HTTPBasicCredentials):
    student = authenticate(credentials)
    return {"username": student["username"], "grades": student["grades"]}