from fastapi import FastAPI, HTTPException
from models import Student
from utils import load_students, save_students, calculate_average_and_grade

app = FastAPI(title="Student Result Management API")

@app.post("/students/")
def add_student(student: Student):
    try:
        students = load_students()
        if any(s.name == student.name for s in students):
            raise HTTPException(status_code=400, detail="Student already exists.")

        student.average, student.grade = calculate_average_and_grade(student.subject_scores)
        students.append(student)
        save_students(students)
        return {"message": "Student added successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/students/{name}")
def get_student(name: str):
    try:
        students = load_students()
        for student in students:
            if student.name.lower() == name.lower():
                return student
        raise HTTPException(status_code=404, detail="Student not found.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/students/")
def get_all_students():
    try:
        return load_students()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
