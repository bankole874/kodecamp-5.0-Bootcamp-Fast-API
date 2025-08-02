# Task 3: Job Application Tracker API
# Goal: Build an API to manage and search job applications
# Features:
# - JobApplication class: name, company, position, status
# - Endpoints:
#  * POST /applications/
#  * GET /applications/
#  * GET /applications/search?status=pending
# - Save/load from applications.json
# - Use file_handler.py module
# - Handle input errors using try-except

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional
import file_handler

app = FastAPI()

class JobApplication(BaseModel):
    name: str
    company: str
    position: str
    status: str

@app.post("/applications/")
def create_application(application: JobApplication):
    try:
        applications = file_handler.load_applications()
        applications.append(application.model_dump())
        file_handler.save_applications(applications)
        return {"message": "Application added successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/applications/", response_model=List[JobApplication])
def get_all_applications():
    try:
        return file_handler.load_applcations()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get ("/applications/search", response_model=List[JobApplication])
def search_applications(status: Optional[str] = Query(None)):
    try:
        applications = file_handler.load_applicationsg()
        if status:
            filtered = [app for app in applications if app["status"].lower() == status.lower()]
            return filtered
        return applications
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

