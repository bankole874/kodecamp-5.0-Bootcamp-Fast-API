# Task 4: Notes App API (With File System Support)
# Goal: Create a FastAPI app to add, update, and delete notes saved as files.
# Features:
# - Endpoints:
#  * POST /notes/
#  * GET /notes/{title}
#  * POST /notes/{title}
#  * DELETE /notes/{title}
# - Save each note as a .txt file
# - Use os module and error handling
# - Use Git branches for feature development

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os

app = FastAPI()
NOTES_DIR = "notes"

class Note(BaseModel):
    title: str
    content: str

def get_note_path(title: str) -> str:
    main_title = title.replace("/", "_")
    return os.path.join(NOTES_DIR, f"{main_title}.txt")

@app.post("/notes/")
def create_note(note: Note):
    file_path = get_note_path(note.title)
    if os.path.exists(file_path):
        raise HTTPException(status_code=400, detail="Note already exists.")
    with open(file_path, "w") as f:
        f.write(note.content)
    return {"message": f"Note '{note.title}' created successfully."}

@app.get("/notes/{title}")
def read_notes(title: str):
    file_path = get_note_path(title)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Note not found.")
    with open(file_path, "r") as f:
        content = f.read()
    return {"title": title, "content": content}

@app.post("/notes/{title}")
def update_note(title: str, note: Note):
    file_path = get_note_path(title)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Note not found.")
    with open(file_path, "w") as f:
        f.write(note.content)
    return {"message": f"Note '{title}' updated successfully."}

@app.delete("/notes/{title}")
def delete_note(title: str):
    file_path = get_note_path(title)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Note not found.")
    os.remove(file_path)
    return {"message": f"Note '{title}' deleted successfully."}
