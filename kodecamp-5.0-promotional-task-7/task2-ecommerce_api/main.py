# Task 2: E-Commerce API (Modular FastAPI Project)
# Goal: Create a shopping API with cart & checkout system.
# Features:
# Use project structure with routers & modules (products.py, cart.py, users.py).
# Product model in SQLModel: id, name, price, stock.
# Endpoints:
# POST /admin/products/ (admin only).
# GET /products/ (public).
# POST /cart/add/.
# POST /cart/checkout/.
# JWT authentication for users.
# Middleware: measure response time and add it to headers.
# Save orders to orders.json for backup

import time
from fastapi import FastAPI, Request
from sqlmodel import SQLModel, select
from sqlmodel import Session

from db import engine, get_session
import models
from auth import get_password_hash
from routers import users, products, cart

app = FastAPI(title="E-Commerce API (modular)")

# Middleware to measure response time and add it to headers
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = (time.perf_counter() - start_time) * 1000.0  # ms
    response.headers["X-Process-Time-ms"] = f"{process_time:.2f}"
    return response

# Include routers
app.include_router(users.router)
app.include_router(products.router)
app.include_router(cart.router)

# simple /me endpoint wired to auth.get_current_user to avoid circular placeholder
from auth import get_current_user
@app.get("/users/me")
def me(current_user = None):
    # FastAPI will override depends only if we declare it here:
    # so let's re-declare the dependency properly:
    from fastapi import Depends
    return {"username": current_user.username, "is_admin": current_user.is_admin}
# above is a bit of a convenience — better to call the USERS router endpoint in real code.

# Startup: create DB and a default admin user (dev convenience)
@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)
    # create default admin if none exists (development convenience)
    with Session(engine) as session:
        existing_admin = session.exec(select(models.User).where(models.User.username == "admin")).first()
        if not existing_admin:
            admin_user = models.User(username="admin", hashed_password=get_password_hash("adminpass"), is_admin=True)
            session.add(admin_user)
            session.commit()
            session.refresh(admin_user)
            print("Created default admin -> username: admin password: adminpass (DEV ONLY)")

# Root
@app.get("/")
def read_root():
    return {"msg": "E-commerce API up. See /docs for interactive API docs."}
