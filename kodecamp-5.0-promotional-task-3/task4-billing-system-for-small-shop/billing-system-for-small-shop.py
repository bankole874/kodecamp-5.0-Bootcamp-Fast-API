# Task 4: Billing System for Small Shop
# Goal: Create a system to manage bills and apply discounts.
# Features:
# - Create a Product class with name, price, and quantity.
# - Create a Cart class to handle billing logic.
# - Use math.ceil() to round up totals.
# - Use datetime for timestamps and json for bill history.
# - All billing logic should be in a separate module billing.py.
# Menu Options:
# - Add product to cart
# - View cart and total
# - Apply discount if total > N10,000
# - Save bill to file
# - View previous transactions

import math
from billing import load_entries, save_entries
from datetime import datetime

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.total = math.ceil(self.price * self.quantity)
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            'name': self.name,
            'price': self.price,
            'quantity': self.quantity,
            'total': self.total
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data['name'],
            price=data['price'],
            quantity=data['quantity']
        ) 

class Cart:
    def __init__(self):
        self.products = []
        self.total = 0
        self.discount_applied = False
        self.bill_history = []

    def add_to_cart(self, product):
        self.products.append(product)
        self.total += product.total
        print(f"Added {product.name} to cart. Current total: N{self.total}")
        
    def view_cart(self):
        if not self.products:
            print("Cart is empty.")
            return
        print("Current Cart:")
        for product in self.products:
            print(f"{product.name} - N{product.price} x {product.quantity} = N{product.total}")
        print(f"Total: N{self.total}")

    def apply_discount(self):
        if self.total > 10000 and not self.discount_applied:
            discount = self.total * 0.1
            self.total -= discount
            self.discount_applied = True
            print(f"Discount applied! New total: N{self.total}")
        else:
            print("No discount applied. Total is less than N10,000 or discount already applied.")

    def save_and_exit(self):
        if not self.products:
            print("No products in cart to save.")
            return
        
        entry = {
            'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'products': [product.to_dict() for product in self.products],
            'total': self.total,
            'discount_applied': self.discount_applied
        }
        
        self.bill_history.append(entry)
        save_entries(self.bill_history)
        print("Bill saved successfully. Exiting the app.")
    
    def view_previous_transactions(self):
        entries = load_entries()
        if not entries:
            print("No previous transactions found.")
            return
        print("Previous Transactions:")
        for entry in entries:
            print(f"Total: N{entry['total']}, Discount Applied: {entry['discount_applied']}")
            for product in entry['products']:
                print(f"{product['name']} - N{product['price']} x {product['quantity']} = N{product['total']}")
            print("-" * 20)

def main():
    cart = Cart()
    while True:
        print("\nMenu:")
        print("1. Add product to cart")
        print("2. View cart and total")
        print("3. Apply discount if total > N10,000")
        print("4. Save bill to file")
        print("5. View previous transactions")
        print("6. Exit")

        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            product = Product(name, price, quantity)
            cart.add_to_cart(product)
        
        elif choice == '2':
            cart.view_cart()
        
        elif choice == '3':
            cart.apply_discount()
        
        elif choice == '4':
            cart.save_and_exit()
        
        elif choice == '5':
            cart.view_previous_transactions()
        
        elif choice == '6':
            break
        
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()