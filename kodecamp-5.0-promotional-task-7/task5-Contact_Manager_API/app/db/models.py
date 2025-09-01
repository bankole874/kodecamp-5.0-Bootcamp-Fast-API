from typing import List, Optional

from pydantic import EmailStr
from sqlmodel import Field, Relationship, SQLModel

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: EmailStr = Field(index=True, nullable=False, unique=True)
    hashed_password: str
    full_name: Optional[str] = None

    contacts: List["Contact"] = Relationship(back_populates="owner")

class Contact(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    user_id: int = Field(foreign_key="user.id")

    owner: Optional[User] = Relationship(back_populates="contacts")
