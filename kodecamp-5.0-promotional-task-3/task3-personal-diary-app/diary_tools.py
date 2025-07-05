import json
import os
from datetime import datetime

def load_entries(filename='diary.json'):
    """Load diary entries from a JSON file."""
    if not os.path.exists(filename):
        return []
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError) as e:
        print(f"Error loading entries: {e}")
        return []

def save_entries(entries, filename='diary.json'):
    """Save diary entries to a JSON file."""
    try:
        with open(filename, 'w') as file:
            json.dump(entries, file, indent=4)
    except IOError as e:
        print(f"Error saving entries: {e}")