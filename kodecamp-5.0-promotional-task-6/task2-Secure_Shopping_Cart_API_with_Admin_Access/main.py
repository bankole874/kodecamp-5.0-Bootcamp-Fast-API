# Task 2: Secure Shopping Cart API with Admin Access
# Goal: Create a FastAPI shopping API where only admins can add products, but all users can browse and shop.
# Features:
# User class with role (admin or customer)
# Module auth.py to handle authentication & role checking
# Endpoints:
# POST /admin/add_product/ — admin only
# GET /products/ — public
# POST /cart/add/ — authenticated users only
# Save data to products.json and cart.json
# Use dependency injection for role-based access

import json
from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from typing import List
from auth import get_current_user, admin_required, User

app = FastAPI(title="Secure Shopping Cart API")

PRODUCT_FILE = "products.json"
CART_FILE = "cart.json"

class Product(BaseModel):
    id: int
    name: str
    price: float
    
class CartItem(BaseModel):
    username: str
    product_id: int
    quantity: int

# Load products from JSON file
def load_products(filename: str):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
# Save products to JSON file
def save_products(filename: str, data):
    with open(filename, "w") as file:
        json.dump(data, file, indent=2)
        
@app.post("/admin/add_product/", dependencies=[Depends(admin_required)])
def add_product(product: Product):
    products = load_products(PRODUCT_FILE)

    if any(p['id'] == product.id for p in products):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Product with this ID already exists."
        )

    products.append(product.dict())
    save_products(PRODUCT_FILE, products)

    return {"message": "Product added successfully", "product": product}

@app.get("/products/", response_model=List[Product])
def get_products():
    products = load_products(PRODUCT_FILE)
    return products

@app.post("/cart/add/")
def add_to_cart(cart_item: CartItem, current_user: User = Depends(get_current_user)):
    cart = load_products(CART_FILE)
    
    # Check if the product exists
    products = load_products(PRODUCT_FILE)
    if not any(p['id'] == cart_item.product_id for p in products):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found.")
    
    # Add item to cart
    cart_item_dict = cart_item.dict()
    cart_item_dict['username'] = current_user.username
    
    cart.append(cart_item_dict)
    save_products(CART_FILE, cart)
    
    return {"message": "Item added to cart successfully", "cart_item": cart_item}
