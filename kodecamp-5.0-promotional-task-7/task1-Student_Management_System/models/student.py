# models/student.py
from typing import Optional
from sqlmodel import SQLModel, Field

class Student(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    age: int
    email: str  # EmailStr enforced in schemas

class Grade(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    subject: str
    score: float
    student_id: Optional[int] = Field(default=None, foreign_key="student.id")

