import json
from typing import List
from models import Student

FILE = "students.json"

def load_students() -> List[Student]:
    try:
        with open(FILE, "r") as f:
            data = json.load(f)
            return [Student(**item) for item in data]
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_students(students: List[Student]):
    with open(FILE, "w") as f:
        json.dump([student.dict() for student in students], f, indent=4)

def calculate_average_and_grade(scores: dict) -> tuple:
    if not scores:
        return 0.0, "F"
    avg = sum(scores.values()) / len(scores)
    if avg >= 90:
        grade = "A"
    elif avg >= 80:
        grade = "B"
    elif avg >= 70:
        grade = "C"
    elif avg >= 60:
        grade = "D"
    else:
        grade = "F"
    return avg, grade
