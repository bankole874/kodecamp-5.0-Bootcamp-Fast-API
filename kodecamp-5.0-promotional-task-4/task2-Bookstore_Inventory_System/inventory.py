import json
import os

def load_inventory(file_path):
    """Load inventory from a JSON file."""
    if not os.path.exists(file_path):
        return []
    with open(file_path, 'r') as file:
        return json.load(file)
    
def save_inventory(file_path, inventory):
    """Save inventory to a JSON file."""
    with open(file_path, 'w') as file:
        json.dump(inventory, file, indent=4)
