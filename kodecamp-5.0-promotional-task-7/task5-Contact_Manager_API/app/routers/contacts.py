from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select

from app.db.models import Contact, User
from app.db.session import get_session
from app.deps import get_current_user
from app.schemas import ContactCreate, ContactRead, ContactUpdate

router = APIRouter(prefix="/contacts", tags=["contacts"])

@router.post("/", response_model=ContactRead, status_code=status.HTTP_201_CREATED)
def create_contact(contact_in: ContactCreate, current_user: User = Depends(get_current_user), session: Session = Depends(get_session)):
    contact = Contact(name=contact_in.name, email=contact_in.email, phone=contact_in.phone, user_id=current_user.id)
    session.add(contact)
    session.commit()
    session.refresh(contact)
    return ContactRead(id=contact.id, name=contact.name, email=contact.email, phone=contact.phone, user_id=contact.user_id)

@router.get("/", response_model=List[ContactRead])
def list_contacts(current_user: User = Depends(get_current_user), session: Session = Depends(get_session)):
    contacts = session.exec(select(Contact).where(Contact.user_id == current_user.id)).all()
    return [ContactRead(id=c.id, name=c.name, email=c.email, phone=c.phone, user_id=c.user_id) for c in contacts]

@router.put("/{contact_id}", response_model=ContactRead)
def update_contact(contact_id: int, contact_in: ContactUpdate, current_user: User = Depends(get_current_user), session: Session = Depends(get_session)):
    contact = session.get(Contact, contact_id)
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    if contact.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to modify this contact")
    if contact_in.name is not None:
        contact.name = contact_in.name
    if contact_in.email is not None:
        contact.email = contact_in.email
    if contact_in.phone is not None:
        contact.phone = contact_in.phone
    session.add(contact)
    session.commit()
    session.refresh(contact)
    return ContactRead(id=contact.id, name=contact.name, email=contact.email, phone=contact.phone, user_id=contact.user_id)

@router.delete("/{contact_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_contact(contact_id: int, current_user: User = Depends(get_current_user), session: Session = Depends(get_session)):
    contact = session.get(Contact, contact_id)
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    if contact.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this contact")
    session.delete(contact)
    session.commit()
    return None
    