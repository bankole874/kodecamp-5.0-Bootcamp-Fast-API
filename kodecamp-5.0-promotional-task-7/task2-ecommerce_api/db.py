from sqlmodel import create_engine, Session

# SQLite file; check_same_thread False for multi-thread usage with FastAPI dev server
DATABASE_URL = "sqlite:///./database.db"
engine = create_engine(DATABASE_URL, echo=False, connect_args={"check_same_thread": False})

def get_session():
    with Session(engine) as session:
        yield session
