import json
from datetime import datetime

def load_entries(filename='bills.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_entries(entries, filename='bills.json'):
    with open(filename, 'w') as file:
        json.dump(entries, file, indent=4)
