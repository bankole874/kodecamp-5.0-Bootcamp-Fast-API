# Task 1: Student Management System
# Goal: Build a program to store student names and their scores using lists/dictionaries.
# Core Features:
# - Add new students (with 3 subject scores)
# - Show all students with average and performance status
# - Search for a student by name
# - Use functions for actions
# - Use error handling for invalid inputs

students = []

def add_student():
    name = input("Enter your name: ")
    try:
        score = [float(input(f"Enter score for subject {i+1}: ")) for i in range(3)]
        students.append({"name": name, "scores": score})
        print(f"{name} added successfully.\n")
    except ValueError:
        print("Invalid input. Please enter numeric scores.\n")

def show_students():
    for student in students:
        average_score = sum(student["scores"]) / 3
        performance_status = "Pass" if average_score >= 50 else "Fail"
        print(f"Name: {student['name']}, Scores: {student['scores']}, Average: {average_score:.2f}, Status: {performance_status}")

def search_student():
    name = input("Enter the name of the student to search: ")
    found_student = False
    for student in students:
        if student["name"].lower() == name.lower():
            average_score = sum(student["scores"]) / 3
            performance_status = "Pass" if average_score >= 50 else "Fail"
            print(f"Name: {student['name']}, Scores: {student['scores']}, Average: {average_score:.2f}, Status: {performance_status}\n")

def main():
    while True:
        print("Student Management System")
        print("1. Add Student")
        print("2. Show All Students")
        print("3. Search Student")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            show_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")
            
main()