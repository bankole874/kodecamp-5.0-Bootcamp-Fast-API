# Task 4: Shopping Cart System
# Scenario: Simulate a mini-store system.
# Instructions:
# - Show a list of available items with prices (use a dictionary)
# - Let the user "add to cart" by entering item name and quantity
# - Store cart in a list of dictionaries:
#  {"item": "Rice", "quantity": 2, "price": 400}
# - Calculate total bill
# - Option to remove an item or clear cart
# - Loop until user exits
# - Handle invalid inputs and missing items

store = {
    "Rice": 1000,
    "Garri": 800,
    "Boku Bread": 1600,
    "Eggs": 300
}

cart = []

def show_items():
    print("Available items:")
    for item, price in store.items():
        print(f"{item} - {price} Naira")
    print()

def add_to_cart():
    item = input("Enter item name: ")
    if item in store:
        try:
            quantity = int(input("Enter quantity: "))
            cart.append({"item": item, "quantity": quantity, "price": store[item]})
            print("Added to cart.\n")
        except ValueError:
            print("Quantity must be a number.\n")
    else:
        print("Item not found.\n")

def view_cart():
    if not cart:
        print("Cart is empty.\n")
        return
    total = 0
    for c in cart:
        subtotal = c["quantity"] * c["price"]
        total += subtotal
        print(f"{c['item']} x {c['quantity']} = {subtotal} Naira")
    print(f"Total: {total} Naira\n")

def remove_item():
    name = input("Enter item to remove: ")
    for c in cart:
        if c["item"].lower() == name.lower():
            cart.remove(c)
            print("Item removed.\n")
            return
    print("Item not in cart.\n")

def clear_cart():
    cart.clear()
    print("Cart cleared.\n")

def shopping_menu():
    while True:
        print("1. Show Items\n2. Add to Cart\n3. View Cart\n4. Remove Item\n5. Clear Cart\n6. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            show_items()
        elif choice == "2":
            add_to_cart()
        elif choice == "3":
            view_cart()
        elif choice == "4":
            remove_item()
        elif choice == "5":
            clear_cart()
        elif choice == "6":
            break
        else:
            print("Invalid option.\n")

shopping_menu()