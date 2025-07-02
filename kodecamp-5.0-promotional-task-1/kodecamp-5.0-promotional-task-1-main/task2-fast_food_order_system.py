def fast_food_order_system():

    customer_count = 0
    
    while True:
        name = input("\nEnter customer's name (or type 'exit' to finish): ")
        if name.lower() == 'exit':
            break
        
        # Ask for quantities of food items
        burgers = int(input(f"Enter quantity of Burgers ($5 each): "))
        fries = int(input(f"Enter quantity of Fries ($2 each): "))
        drinks = int(input(f"Enter quantity of Drinks ($1.5 each): "))
        
        # Calculate total cost
        total = (burgers * 5) + (fries * 2) + (drinks * 1.5)
        
        # Apply discount if price exceeds $20
        if total > 20:
            discount = total * 0.1
            total -= discount
            print(f"\n{name}'s Bill (10% discount applied): ${total:.2f}")
        else:
            print(f"\n{name}'s Bill: ${total:.2f}")
            
        customer_count += 1
        
    print(f"\nTotal number of customers served: {customer_count}")
    
# Run the fast food order system's function
fast_food_order_system()
