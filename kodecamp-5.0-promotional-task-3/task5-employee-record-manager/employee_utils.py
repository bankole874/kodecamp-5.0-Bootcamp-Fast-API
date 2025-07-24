import json
import os

def load_employees(filename='employees.json'):
    if not os.path.exists(filename):
        return []
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError) as e:
        print(f"Error loading employees: {e}")
        return []

def save_employees(employees, filename='employees.json'):
    try:
        with open(filename, 'w') as file:
            json.dump(employees, file, indent=4)
    except IOError as e:
        print(f"Error saving employees: {e}")
