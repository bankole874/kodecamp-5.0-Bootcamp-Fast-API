# app/routers/notes.py
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.db import get_session
from app.models import Note, NoteCreate, NoteRead
from app.utils.backup import backup_notes

router = APIRouter(prefix="/notes", tags=["notes"])

@router.post("/", response_model=NoteRead, status_code=201)
def create_note(payload: NoteCreate, session: Session = Depends(get_session)):
    note = Note(**payload.dict())
    session.add(note)
    session.commit()
    session.refresh(note)
    backup_notes(session)
    return note

@router.get("/", response_model=List[NoteRead])
def list_notes(session: Session = Depends(get_session)):
    notes = session.exec(select(Note)).all()
    return notes

@router.get("/{note_id}", response_model=NoteRead)
def get_note(note_id: int, session: Session = Depends(get_session)):
    note = session.get(Note, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

@router.delete("/{note_id}")
def delete_note(note_id: int, session: Session = Depends(get_session)):
    note = session.get(Note, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    session.delete(note)
    session.commit()
    backup_notes(session)
    return {"message": f"Note {note_id} deleted successfully."}
