# Task 5: Employee Record Manager
# Goal: Manage employee records with file storage.
# Features:
# - Create an Employee class with name, ID, department, and salary.
# - Save/load employees using 'json'.
# - Use the 'os' module to check file existence.
# - Handle invalid salary input with try-except.
# - Move data handling logic into employee_utils.py.
# Menu Options:
# - Add employee
# - View all employees
# - Search by ID
# - Save to file
# - Load from file

import employee_utils as utils

class Employee:
    def __init__(self, name, emp_id, department, salary):
        self.name = name
        self.emp_id = emp_id
        self.department = department
        self.salary = salary

    def __str__(self):
        return f"ID: {self.emp_id}, Name: {self.name}, Department: {self.department}, Salary: {self.salary}"   

class Employee_menu:
    def __init__(self):
        self.employees = utils.load_employees()

    def add_employee(self):
        name = input("Enter employee name: ")
        emp_id = input("Enter employee ID: ")
        department = input("Enter employee department: ")
        
        while True:
            try:
                salary = float(input("Enter employee salary: "))
                if salary < 0:
                    raise ValueError("Salary cannot be negative.")
                break
            except ValueError as e:
                print(f"Invalid input for salary: {e}. Please try again.")
        
        new_employee = Employee(name, emp_id, department, salary)
        self.employees.append(new_employee)
        print(f"Employee {name} added successfully.")

    def view_all_employees(self):
        if not self.employees:
            print("No employees found.")
            return
        for emp in self.employees:
            print(emp)

    def search_employee_by_id(self):
        emp_id = input("Enter employee ID to search: ")
        for emp in self.employees:
            if emp.emp_id == emp_id:
                print(emp)
                return
        print(f"No employee found with ID {emp_id}.")

    def save_employees_to_file(self):
        utils.save_employees([emp.__dict__ for emp in self.employees])
        print("Employees saved to file successfully.")

    def load_employees_from_file(self):
        self.employees = [Employee(**emp) for emp in utils.load_employees()]
        print("Employees loaded from file successfully.")

def main():
    menu = Employee_menu()
    while True:
        print("\nEmployee Record Manager")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search Employee by ID")
        print("4. Save Employees to File")
        print("5. Load Employees from File")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            menu.add_employee()
        elif choice == '2':
            menu.view_all_employees()
        elif choice == '3':
            menu.search_employee_by_id()
        elif choice == '4':
            menu.save_employees_to_file()
        elif choice == '5':
            menu.load_employees_from_file()
        elif choice == '6':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
    