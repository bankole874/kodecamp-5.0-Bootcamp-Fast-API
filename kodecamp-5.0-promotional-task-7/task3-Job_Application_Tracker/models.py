from __future__ import annotations
from datetime import date
from enum import Enum
from typing import Optional

from sqlmodel import SQLModel, Field


class JobStatus(str, Enum):
    pending = "pending"
    interviewing = "interviewing"
    offer = "offer"
    rejected = "rejected"


class JobApplicationBase(SQLModel):
    company: str = Field(index=True, min_length=1, description="Company name")
    position: str = Field(min_length=1, description="Position title")
    status: JobStatus = Field(default=JobStatus.pending, description="Application status")
    date_applied: date = Field(description="Date applied (YYYY-MM-DD)")


class JobApplication(JobApplicationBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(index=True, description="Owner user id")


# Request/Response schemas
class JobApplicationCreate(JobApplicationBase):
    pass


class JobApplicationRead(JobApplicationBase):
    id: int
