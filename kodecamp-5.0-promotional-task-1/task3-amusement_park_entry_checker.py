def amusement_park_entry_checker():

    while True:
        # Ask for visitor's name
        name = input("\nEnter your name: (or type 'exit' to quit) ").strip()
        if name.lower() == "exit":
            print("Exiting the amusement park entry checker. Goodbye!")
            break
        
        age =int(input(f'Hello {name}, please enter your age: '))
        
        # Determine base price according to ages
        if age < 5:
            price = 0
        elif 5 <= age <= 17:
            price = 5
        elif 18 <= age <= 59:
            price = 10
        else:  # age >= 60
            price = 7
            
        # Ask about coupon code
        coupon_code = input("Do you have a coupon code? (yes/no): ").strip().lower()
        if coupon_code == "yes" and price > 0:
            price *= 0.8  # Apply 20% discount
            
        print(f"{name}, your entry fee is: ${price:.2f}")
    
# Run the amusement park entry checker
amusement_park_entry_checker()
