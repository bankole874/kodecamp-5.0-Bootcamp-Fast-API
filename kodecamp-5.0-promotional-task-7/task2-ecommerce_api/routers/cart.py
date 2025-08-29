from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import select
from sqlmodel import Session
from typing import List, Dict, Any
import json
from datetime import datetime

from db import get_session
from models import CartItem, Product, Order
from auth import get_current_user

router = APIRouter(prefix="/cart", tags=["cart"])

class AddCartItemSchema:
    def __init__(self, product_id: int, quantity: int):
        self.product_id = product_id
        self.quantity = quantity

@router.post("/add/")
def add_to_cart(product_id: int, quantity: int, session: Session = Depends(get_session), current_user = Depends(get_current_user)):
    if quantity <= 0:
        raise HTTPException(status_code=400, detail="Quantity must be positive")
    product = session.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    if product.stock < quantity:
        raise HTTPException(status_code=400, detail="Not enough stock available")

    existing = session.exec(select(CartItem).where(CartItem.user_id == current_user.id, CartItem.product_id == product_id)).first()
    if existing:
        existing.quantity += quantity
        session.add(existing)
    else:
        c = CartItem(user_id=current_user.id, product_id=product_id, quantity=quantity)
        session.add(c)
    session.commit()
    return {"message": "added_to_cart"}

@router.get("/")
def view_cart(session: Session = Depends(get_session), current_user = Depends(get_current_user)):
    items = session.exec(select(CartItem).where(CartItem.user_id == current_user.id)).all()
    result = []
    for it in items:
        product = session.get(Product, it.product_id)
        result.append({"product_id": product.id, "name": product.name, "price": product.price, "quantity": it.quantity})
    return result

@router.post("/checkout/")
def checkout(session: Session = Depends(get_session), current_user = Depends(get_current_user)):
    items = session.exec(select(CartItem).where(CartItem.user_id == current_user.id)).all()
    if not items:
        raise HTTPException(status_code=400, detail="Cart is empty")

    # verify stock and compute total
    total = 0.0
    order_items = []
    for it in items:
        product = session.get(Product, it.product_id)
        if product.stock < it.quantity:
            raise HTTPException(status_code=400, detail=f"Product {product.name} does not have enough stock")
        total += product.price * it.quantity
        order_items.append({"product_id": product.id, "name": product.name, "price": product.price, "quantity": it.quantity})

    # deduct stock and clear cart (keep all changes in a single DB session)
    for it in items:
        product = session.get(Product, it.product_id)
        product.stock -= it.quantity
        session.add(product)
        # remove cart item
        session.delete(it)

    # create order record
    o = Order(user_id=current_user.id, total=total, items=json.dumps(order_items), created_at=datetime.utcnow())
    session.add(o)
    session.commit()
    session.refresh(o)

    # append to backup orders.json
    order_record = {
        "id": o.id,
        "user_id": o.user_id,
        "total": o.total,
        "items": order_items,
        "created_at": o.created_at.isoformat()
    }
    try:
        # open or create file and append
        with open("orders.json", "r+", encoding="utf-8") as fh:
            try:
                data = json.load(fh)
            except Exception:
                data = []
            data.append(order_record)
            fh.seek(0)
            json.dump(data, fh, indent=2)
    except FileNotFoundError:
        with open("orders.json", "w", encoding="utf-8") as fh:
            json.dump([order_record], fh, indent=2)

    return {"message": "checkout_success", "order": order_record}
