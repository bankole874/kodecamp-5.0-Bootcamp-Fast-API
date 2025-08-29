from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import select
from sqlmodel import Session

from db import get_session
from models import User
from auth import get_password_hash, verify_password, create_access_token

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/register", status_code=201)
def register(username: str, password: str, session: Session = Depends(get_session)):
    """Register a normal user (no admin flag from public endpoint)."""
    existing = session.exec(select(User).where(User.username == username)).first()
    if existing:
        raise HTTPException(status_code=400, detail="Username already exists")
    user = User(username=username, hashed_password=get_password_hash(password), is_admin=False)
    session.add(user)
    session.commit()
    session.refresh(user)
    return {"id": user.id, "username": user.username}

@router.post("/token")
def login_token(form_data: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_session)):
    user = session.exec(select(User).where(User.username == form_data.username)).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password",
                            headers={"WWW-Authenticate": "Bearer"})
    access_token = create_access_token({"sub": user.username, "is_admin": user.is_admin})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me")
def read_me(current_user: User = Depends(lambda: None)):  # will be replaced by main import of dependency
    # This endpoint will be "overridden" by the dependency in main include - see main.py where dependency imports happen.
    return {"msg": "This route will be wired in main via dependency injection."}
