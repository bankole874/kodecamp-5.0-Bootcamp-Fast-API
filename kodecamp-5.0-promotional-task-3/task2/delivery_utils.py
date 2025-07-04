import json

def load_packages(filename):
    """Load packages from a JSON file."""
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error decoding JSON. Starting with an empty package list.")
        return []

def save_packages(filename, packages):
    """Save packages to a JSON file."""
    with open(filename, 'w') as file:
        json.dump(packages, file) 