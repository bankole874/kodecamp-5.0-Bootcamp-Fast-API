# models/schemas.py
from typing import List, Optional
from pydantic import BaseModel, EmailStr

class GradeCreate(BaseModel):
    subject: str
    score: float

class StudentCreate(BaseModel):
    name: str
    age: int
    email: EmailStr
    grades: Optional[List[GradeCreate]] = []

class GradeRead(BaseModel):
    id: int
    subject: str
    score: float

class StudentRead(BaseModel):
    id: int
    name: str
    age: int
    email: EmailStr
    grades: List[GradeRead] = []

