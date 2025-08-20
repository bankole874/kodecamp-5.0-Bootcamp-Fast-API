# Task 4: Notes API with Token Authentication
# Goal: Build a notes management API with JWT token authentication.
# Features:
# Note class: title, content, date
# Endpoints:
# POST /login/ — returns a token
# POST /notes/ — add a note (requires token)
# GET /notes/ — view own notes
# Notes stored in a notes.json file per user
# Secure routes using JWT Bearer token dependency

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from datetime import datetime, timedelta
from typing import List
import jwt, json, os

# ========================
# CONFIG
# ========================
SECRET_KEY = "supersecretkey"   # change in production
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# Dummy user database
fake_users_db = {
    "alice": {"username": "alice", "password": "password123"},
    "bob": {"username": "bob", "password": "secret456"}
}

# ========================
# MODELS
# ========================
class Token(BaseModel):
    access_token: str
    token_type: str

class Note(BaseModel):
    title: str
    content: str
    date: str = datetime.now().isoformat()

# ========================
# AUTH HELPERS
# ========================
def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None or username not in fake_users_db:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
        return username
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expired")
    except jwt.PyJWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    return verify_token(token)

# ========================
# STORAGE HELPERS
# ========================
def get_user_notes(username: str):
    file_path = f"{username}_notes.json"
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            return json.load(f)
    return []

def save_user_notes(username: str, notes: List[dict]):
    file_path = f"{username}_notes.json"
    with open(file_path, "w") as f:
        json.dump(notes, f, indent=4)

# ========================
# ROUTES
# ========================
@app.post("/login/", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = fake_users_db.get(form_data.username)
    if not user or user["password"] != form_data.password:
        raise HTTPException(status_code=400, detail="Invalid username or password")

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user["username"]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.post("/notes/")
async def add_note(note: Note, username: str = Depends(get_current_user)):
    notes = get_user_notes(username)
    notes.append(note.dict())
    save_user_notes(username, notes)
    return {"msg": "Note added", "note": note}


@app.get("/notes/", response_model=List[Note])
async def get_notes(username: str = Depends(get_current_user)):
    return get_user_notes(username)
