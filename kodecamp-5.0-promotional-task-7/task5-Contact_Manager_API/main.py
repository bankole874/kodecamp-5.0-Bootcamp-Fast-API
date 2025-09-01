import logging
from sqlmodel import Session, select

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.core.security import get_password_hash
from app.db.session import init_db, engine
from app.db.models import User
from app.routers import auth as auth_router, contacts as contacts_router
from app.middleware import ip_logger

# logging setup (simple)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("app")

app = FastAPI(title="Contact Manager (modular)")

# CORS - tighten in production
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost", "http://localhost:3000", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# register middleware function
app.middleware("http")(ip_logger)

# include routers
app.include_router(auth_router.router)
app.include_router(contacts_router.router)

@app.on_event("startup")
def on_startup():
    init_db()
    # create demo user for quick testing (development only)
    with Session(engine) as session:
        demo = session.exec(select(User).where(User.email == "demo@example.com")).first()
    if not demo:
        user = User(email="demo@example.com", hashed_password=get_password_hash("demopassword"), full_name="Demo User")
        session.add(user)
        session.commit()
        logger.info("Created demo user: demo@example.com (password: demopassword)")
