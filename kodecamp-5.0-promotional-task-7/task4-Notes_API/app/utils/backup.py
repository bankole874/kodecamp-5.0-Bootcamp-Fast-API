# app/utils/backup.py
import json
from typing import List
from sqlmodel import Session, select
from app.models import Note
from app.core.config import BACKUP_PATH

def backup_notes(session: Session, path: str = BACKUP_PATH) -> None:
    notes: List[Note] = session.exec(select(Note)).all()
    notes_data = [
        {
            "id": n.id,
            "title": n.title,
            "content": n.content,
            "created_at": n.created_at.isoformat(),
        }
        for n in notes
    ]
    with open(path, "w", encoding="utf-8") as f:
        json.dump(notes_data, f, indent=2, ensure_ascii=False)
