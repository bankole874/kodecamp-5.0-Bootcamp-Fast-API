# app/core/config.py
from typing import List

# Add more origins here if needed
ALLOW_ORIGINS: List[str] = [
    "http://localhost:3000",
    "http://127.0.0.1:5500",
]

# Optional: change database path or use env vars later
DATABASE_URL: str = "sqlite:///./notes.db"

# Where to write JSON backups
BACKUP_PATH: str = "notes.json"
