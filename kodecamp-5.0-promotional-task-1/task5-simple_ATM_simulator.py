def simple_atm_simulator():
    print("Welcome to the Simple ATM Simulator!")
    
    balance = 1000  # Starting balance

    while True:
        # Display menu
        print("\n--- ATM Menu ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            print(f"Your current balance is: ${balance:.2f}")

        elif choice == '2':
            try:
                amount = float(input("Enter amount to deposit: $"))
                if amount <= 0:
                    print("Amount must be positive.")
                else:
                    balance += amount
                    print(f"${amount:.2f} deposited successfully.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        elif choice == '3':
            try:
                amount = float(input("Enter amount to withdraw: $"))
                if amount <= 0:
                    print("Amount must be positive.")
                elif amount > balance:
                    print("Insufficient funds.")
                else:
                    balance -= amount
                    print(f"${amount:.2f} withdrawn successfully.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        elif choice == '4':
            print(f"\nThank you for using the ATM. Final balance: ${balance:.2f}")
            break

        else:
            print("Invalid choice. Please select from 1 to 4.")

# Run the function
simple_atm_simulator()
