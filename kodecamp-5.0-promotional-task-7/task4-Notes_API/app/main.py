# app/main.py
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import ALLOW_ORIGINS
from app.db import init_db
from app.middleware.request_counter import register_request_counter
from app.routers.notes import router as notes_router

# Configure logging (optional)
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def create_app() -> FastAPI:
    app = FastAPI(title="Notes API", version="1.0.0")

    # CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=ALLOW_ORIGINS,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Middleware
    register_request_counter(app)

    # Routers
    app.include_router(notes_router)

    # Startup
    @app.on_event("startup")
    def on_startup():
        init_db()
        logging.getLogger("uvicorn").info("Database ready.")

    return app

app = create_app()
