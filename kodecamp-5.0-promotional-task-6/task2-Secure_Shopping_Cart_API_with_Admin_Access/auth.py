from fastapi import FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from typing import Optional

dummy_users_db  = {
    "admin-token": {"username": "admin", "role": "admin"},
    "customer-token": {"username": "customer", "role": "customer"},
}

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token") # Dependency for token authentication

class User:
    def __init__(self, username: str, role: str):
        self.username = username
        self.role = role

# Function to get the current user based on the token
def get_current_user(token: str = oauth2_scheme) -> User:
    user_data = dummy_users_db.get(token)
    if not user_data:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
        )
    return User(username=user_data["username"], role=user_data["role"])

# Function to check if the current user is an admin
def admin_required(current_user: User = get_current_user) -> User:
    if current_user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required",
        )
    return current_user
