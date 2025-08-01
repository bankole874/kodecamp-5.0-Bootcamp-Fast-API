import json
from typing import List
from products import Product

CART_FILE = "carts.json"

def load_cart() -> List[dict]:
    try:
        with open(CART_FILE, "r") as f:
            data = json.load(f)
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_cart(cart: List[dict]):
    with open(CART_FILE, "w") as f:
        json.dump(cart, f, indent=4)
