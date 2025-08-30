# Task 3: Job Application Tracker (Relational DB + Search)
# Goal: Build a Job Application Tracker with SQLModel.
# Features:
# JobApplication model: company, position, status, date_applied.
# Each user can only access their own applications (auth required).
# Endpoints:
# POST /applications/ — add new job application.
# GET /applications/ — list all.
# GET /applications/search?status=pending.
# Use error handling for invalid queries.
# Use middleware to reject requests if User-Agent header is missing.

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

from database import create_db_and_tables
from routers import applications

app = FastAPI(title="Job Application Tracker", version="1.0.0")

# --- Middleware: block requests missing User-Agent ---
@app.middleware("http")
async def require_user_agent(request: Request, call_next):
    if not request.headers.get("user-agent"):
        return JSONResponse(
            status_code=400,
            content={"detail": "User-Agent header is required."},
        )
    return await call_next(request)

# --- Error handling for invalid queries / payloads ---
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    # You still get full details, but with a simpler message + 400 status
    return JSONResponse(
        status_code=400,
        content={
            "detail": "Invalid request parameters or body.",
            "errors": exc.errors(),
        },
    )

# --- Routers ---
app.include_router(applications.router)

# --- Startup: create tables ---
@app.on_event("startup")
def on_startup():
    create_db_and_tables()
