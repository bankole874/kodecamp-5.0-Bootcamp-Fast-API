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
from typing import Dict

app = FastAPI()

contacts: Dict[str, Dict[str, str]] = {
    "Hammed Bankole":{
        "phone":"08012345678",
        "email":"damilarehammed.hd@gmail.com"
    },
    "John Doe":{
        "phone":"1234567890",
        "email":"gbemilekeransom@gmail.com"
    }
}

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

@app.get("/contacts/")
def get_contact(name: str = None):
    if name:
        if name not in contacts:
            raise HTTPException(status_code=404, detail="Contact not found")
        return {"contact": {name: contacts[name]}}
    return {"contacts": contacts}

@app.post("/contacts/{name}")
def update_contact(name: str, contact: Contact):
    if name not in contacts:
        raise HTTPException(status_code=404, detail="Contact not found")
    contacts[name] = {
        "phone": contact.phone,
        "email": contact.email
    }
    return {"message": "Contact updated successfully", "contact": contacts[name]}

@app.delete("/contacts/{name}")
def delete_contact(name: str):
    if name not in contacts:
        raise HTTPException(status_code=404, detail="Contact not found")
    del contacts[name]
    return {"message": "Contact deleted successfully"}

@app.get("/contacts/{name}")
def get_contact_by_name(name: str):
    if name not in contacts:
        raise HTTPException(status_code=404, detail="Contact not found")
    return {"contact": {name: contacts[name]}}

