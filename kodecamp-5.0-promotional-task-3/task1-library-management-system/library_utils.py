
import json
import os

def load_books(filename):
    if not os.path.exists(filename):
        return[]
    with open(filename, 'r') as file:
        data = json.load(file)
        return data
    
def save_books(filename, books):
    with open(filename, 'w') as file:
        json.dump(books, file, indent=4)
