from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import select
from sqlmodel import Session

from db import get_session
from models import Product
from auth import get_current_admin_user

router = APIRouter(tags=["products"])

@router.post("/admin/products/", status_code=201)
def create_product(name: str, price: float, stock: int, session: Session = Depends(get_session),
                   _admin = Depends(get_current_admin_user)):
    product = Product(name=name, price=price, stock=stock)
    session.add(product)
    session.commit()
    session.refresh(product)
    return product

@router.get("/products/")
def list_products(session: Session = Depends(get_session)):
    products = session.exec(select(Product)).all()
    return products
