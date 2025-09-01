# app/db.py
from sqlmodel import SQLModel, create_engine, Session
from typing import Generator
from app.core.config import DATABASE_URL

# SQLite requires this for multithreading with Uvicorn (single process)
connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}

engine = create_engine(DATABASE_URL, echo=False, connect_args=connect_args)

def init_db() -> None:
    SQLModel.metadata.create_all(engine)

def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session
