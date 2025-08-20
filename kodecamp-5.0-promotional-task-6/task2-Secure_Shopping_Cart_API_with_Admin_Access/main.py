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
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List
from auth import get_current_user, admin_required, User

app = FastAPItitle="Secure Shopping Cart API"

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
def sace_products(filename: str, data):
    with open(filename, "w") as file:
        json.dump(data, file, indent=2)
        

@app.post("/admin/add_product/", response_model=Product, dependencies=[Depends(admin_required)])
def add