# Task 2: Mini Shopping API with Cart
# Goal: Create a product API that lets users browse, add to cart, and checkout.
# Features:
# - Product class: id, name, price
# - cart.py module to handle logic
# - Endpoints:
#  * GET /products/
#  * POST /cart/add?product_id=1&qty=2
#  * GET /cart/checkout
# - Use math module for rounding
# - Save cart to JSON file
# - Use Git and GitHub for version tracking

from fastapi import FastAPI, HTTPException
import math
import cart
from products import product_list, Product

app = FastAPI(title="Mini Shopping API with Cart")

@app.get("/products/")
def get_products():
    return product_list

@app.post("/cart/add")
def add_to_cart(product_id: int, qty: int):
    if qty <= 0:
        raise HTTPException(status_code=400, detail="Quantity must be greater than zero.")
    
    product = next((p for p in product_list if p.id == product_id), None)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found.")
    
    cart_data = cart.load_cart()
    cart_data.append({"product": product.dict(), "quantity": qty})
    cart.save_cart(cart_data)
    
    return {"message": "Product added to cart successfully."}

@app.get("/cart/checkout")
def checkout():
    cart_data = cart.load_cart()
    if not cart_data:
        raise HTTPException(status_code=404, detail="Cart is empty.")
    
    total = sum(item["product"]["price"] * item["quantity"] for item in cart_data)
    total = math.ceil(total * 100) / 100  # Round to two decimal places
    
    cart.save_cart([])  # Clear the cart after checkout
    return {"message": "Checkout successful.", "total": total}
