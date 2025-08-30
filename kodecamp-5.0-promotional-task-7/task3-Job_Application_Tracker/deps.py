from typing import Optional
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from sqlmodel import Session

from database import get_session

# --- Tiny demo auth layer ---
security = HTTPBearer(auto_error=True)

# Map bearer tokens -> user ids (replace with real auth/DB in production)
TOKENS = {
    "token-user-1": 1,
    "token-user-2": 2,
}

class CurrentUser:
    def __init__(self, user_id: int):
        self.id = user_id

def get_current_user(creds: HTTPAuthorizationCredentials = Depends(security)) -> CurrentUser:
    token = creds.credentials
    user_id: Optional[int] = TOKENS.get(token)
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing bearer token."
        )
    return CurrentUser(user_id=user_id)

# Re-export session dependency for routers
def session_dep():
    return Depends(get_session)
