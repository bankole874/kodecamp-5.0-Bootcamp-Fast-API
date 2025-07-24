import json
import os

def save_student_data(students, filename='students.json'):
    with open(filename, 'w') as file:
        json.dump([student.__dict__ for student in students], file, indent=4)
        
def load_student_data(Student, filename='students.json'):
    if not os.path.exists(filename):
        return []
    with open(filename, 'r') as file:
        student_data = json.load(file)
        students = []
        for data in student_data:
            student = Student(data['name'])
            student.subjects = data['subjects']
            students.append(student)
        return students
    