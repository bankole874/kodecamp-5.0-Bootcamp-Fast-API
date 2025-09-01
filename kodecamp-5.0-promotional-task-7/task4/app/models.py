# app/models.py
from datetime import datetime
from typing import Optional, List
from sqlmodel import SQLModel, Field

# Shared fields
class NoteBase(SQLModel):
    title: str
    content: str

# Table model
class Note(NoteBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)

# Request/response models
class NoteCreate(NoteBase):
    pass

class NoteRead(NoteBase):
    id: int
    created_at: datetime
