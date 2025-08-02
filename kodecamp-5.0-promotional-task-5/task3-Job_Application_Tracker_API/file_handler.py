import json
from typing import List

FILE_NAME = "applications.json"

def load_applications() -> List[dict]:
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
def save_applications(applications: List[dict]) -> None:
    with open(FILE_NAME, "w") as f:
        json.dump(applications, f, indent=4)
