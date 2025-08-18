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
from typing import List

app = FastAPI()

class Student(BaseModel):
    username: str
    password: str
    grades: List[float] = []

students_db = []

