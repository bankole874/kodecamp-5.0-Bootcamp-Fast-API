# Goal: Build a terminal-based app to manage student scores and grades.
# Features:
# - Student class: name, subjects, scores, average, grade
# - Save/load data using JSON
# - Use functions for operations (add, view, update)
# - Use modules: os, json
# - Use Git to track versions with commit messages like:
#  * Add Student class and JSON save feature
#  * Fix average score calculation

from report_util import save_student_data, load_student_data

class Student:
    def __init__(self, name):
        self.name = name
        self.subjects = {}
    
    def add_subject(self, subject, score):
        self.subjects[subject] = score
    
    def calculate_average(self):
        if not self.subjects:
            return 0
        return sum(self.subjects.values()) / len(self.subjects)
    
    def get_grade(self):
        average = self.calculate_average()
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'

def main():
    students = load_student_data(Student)
    
    while True:
        print("\nStudent Report Card App")
        print("1. Add Student")
        print("2. View Students")
        print("3. update Student Data")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            name = input("Enter student name: ")
            student = Student(name)
            while True:
                subject = input("Enter subject (or 'done' to finish): ")
                if subject.lower() == 'done':
                    break
                score = float(input(f"Enter score for {subject}: "))
                student.add_subject(subject, score)
            students.append(student)
            save_student_data(students)
        
        elif choice == '2':
            for student in students:
                print(f"\nName: {student.name}")
                for subject, score in student.subjects.items():
                    print(f"{subject}: {score}")
                print(f"Average: {student.calculate_average()}")
                print(f"Grade: {student.get_grade()}")
        
        elif choice == '3':
            name = input("Enter student name to update: ")
            for student in students:
                if student.name == name:
                    while True:
                        subject = input("Enter subject to update (or 'done' to finish): ")
                        if subject.lower() == 'done':
                            break
                        if subject in student.subjects:
                            score = float(input(f"Enter new score for {subject}: "))
                            student.add_subject(subject, score)
                        else:
                            print(f"{subject} not found for {name}.")
                    save_student_data(students)
                    break
            else:
                print(f"No student found with name {name}.")
                
        elif choice == '4':
            print("Exiting the app.")
            break
        else:
            print("Invalid choice, please try again.")
            
if __name__ == "__main__":
    main()
