from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlmodel import Session, select

from models import JobApplication, JobApplicationCreate, JobApplicationRead, JobStatus
from deps import get_current_user, CurrentUser, session_dep

router = APIRouter(prefix="/applications", tags=["applications"])

@router.post("/", response_model=JobApplicationRead, status_code=status.HTTP_201_CREATED)
def create_application(
    payload: JobApplicationCreate,
    session: Session = session_dep(),
    user: CurrentUser = Depends(get_current_user),
):
    # Create owned record
    app = JobApplication(**payload.model_dump(), user_id=user.id)
    session.add(app)
    session.commit()
    session.refresh(app)
    return app


@router.get("/", response_model=List[JobApplicationRead])
def list_applications(
    session: Session = session_dep(),
    user: CurrentUser = Depends(get_current_user),
):
    stmt = select(JobApplication).where(JobApplication.user_id == user.id)
    apps = session.exec(stmt).all()
    return apps


@router.get("/search", response_model=List[JobApplicationRead])
def search_applications(
    status: JobStatus = Query(..., description="Filter by status, e.g. pending"),
    session: Session = session_dep(),
    user: CurrentUser = Depends(get_current_user),
):
    stmt = (
        select(JobApplication)
        .where(JobApplication.user_id == user.id)
        .where(JobApplication.status == status)
    )
    results = session.exec(stmt).all()
    return results
