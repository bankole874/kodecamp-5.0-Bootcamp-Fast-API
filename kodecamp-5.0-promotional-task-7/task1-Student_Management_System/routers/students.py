# routers/students.py
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select, delete
from core.database import get_session
from core.security import get_current_user
from models.student import Student, Grade
from models.schemas import StudentCreate, StudentRead, GradeRead

router = APIRouter(prefix="/students", tags=["students"])

@router.post("/", response_model=StudentRead, status_code=status.HTTP_201_CREATED)
def create_student(student_in: StudentCreate, session: Session = Depends(get_session), current_user: dict = Depends(get_current_user)):
    student = Student(name=student_in.name, age=student_in.age, email=student_in.email)
    session.add(student)
    session.commit()
    session.refresh(student)

    for g in student_in.grades or []:
        session.add(Grade(subject=g.subject, score=g.score, student_id=student.id))
    session.commit()

    grades = session.exec(select(Grade).where(Grade.student_id == student.id)).all()
    return StudentRead(
        id=student.id, name=student.name, age=student.age, email=student.email,
        grades=[GradeRead(id=g.id, subject=g.subject, score=g.score) for g in grades]
    )

@router.get("/", response_model=List[StudentRead])
def list_students(session: Session = Depends(get_session)):
    students = session.exec(select(Student)).all()
    out = []
    for s in students:
        grades = session.exec(select(Grade).where(Grade.student_id == s.id)).all()
        out.append(StudentRead(
            id=s.id, name=s.name, age=s.age, email=s.email,
            grades=[GradeRead(id=g.id, subject=g.subject, score=g.score) for g in grades]
        ))
    return out

@router.get("/{student_id}", response_model=StudentRead)
def get_student(student_id: int, session: Session = Depends(get_session)):
    student = session.get(Student, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    grades = session.exec(select(Grade).where(Grade.student_id == student.id)).all()
    return StudentRead(
        id=student.id, name=student.name, age=student.age, email=student.email,
        grades=[GradeRead(id=g.id, subject=g.subject, score=g.score) for g in grades]
    )

@router.put("/{student_id}", response_model=StudentRead)
def update_student(student_id: int, student_in: StudentCreate, session: Session = Depends(get_session), current_user: dict = Depends(get_current_user)):
    student = session.get(Student, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    student.name, student.age, student.email = student_in.name, student_in.age, student_in.email
    session.add(student)
    session.commit()

    session.exec(delete(Grade).where(Grade.student_id == student.id))
    session.commit()
    for g in student_in.grades or []:
        session.add(Grade(subject=g.subject, score=g.score, student_id=student.id))
    session.commit()

    grades = session.exec(select(Grade).where(Grade.student_id == student.id)).all()
    return StudentRead(
        id=student.id, name=student.name, age=student.age, email=student.email,
        grades=[GradeRead(id=g.id, subject=g.subject, score=g.score) for g in grades]
    )

@router.delete("/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_student(student_id: int, session: Session = Depends(get_session), current_user: dict = Depends(get_current_user)):
    student = session.get(Student, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    session.exec(delete(Grade).where(Grade.student_id == student.id))
    session.delete(student)
    session.commit()
    return None

