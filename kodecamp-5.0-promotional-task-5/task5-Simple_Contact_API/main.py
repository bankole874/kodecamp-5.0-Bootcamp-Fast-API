# Task 5: Simple Contact API (Using Path & Query Parameters)
# Goal: Create a FastAPI contact management system.
# Features:
# - Contact model: name, phone, email
# - Endpoints:
#  * POST /contacts/
#  * GET /contacts/?name=John
#  * POST /contacts/{name}
#  * POST /contacts/{name}
# - Use path and query parameters
# - Store data in a dictionary
# - Handle invalid input gracefully

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr

app = FastAPI()

contacts: Dict[str, Dict[str, str]] = {}

class Contact(BaseModel):
    name: str
    phone: str
    email: EmailStr

@app.post("/contacts/")
def create_contact(contact: Contact):
    if contact.name in contacts:
        raise HTTPException(status_code=400, detail="Contact already exists")
    contacts[contact.name] = {
        "phone": contact.phone,
        "email": contact.email
    }
    return {"message": "Contact created successfully", "contact": contacts[contact.name]}
