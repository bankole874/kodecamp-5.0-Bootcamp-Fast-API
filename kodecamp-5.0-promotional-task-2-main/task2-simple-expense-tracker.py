# Task 2: Simple Expense Tracker
# Scenario: Help users track their daily expenses.
# Instructions:
# - Let user enter multiple expenses: description + amount
# - Store as a list of dictionaries e.g., {"item": "Transport", "amount": 150.0}
# - Allow menu options:
#  - Add expense
#  - View all expenses
#  - Total and average
#  - Exit
# - Use try-except for amount input
# - Use loops and functions

expenses = []

def add_expense():
    item = input("Type in expense description (e.g. A Cup of Rice): ")
    try:
        amount = float(input("Enter amount: "))
        expenses.append({"item": item, "amount": amount})
        print("Expense added.\n")
    except ValueError:
        print("Invalid amount. Must be a number.\n")

def view_expenses():
    for expense in expenses:
        print(f"{expense['item']} - ${expense['amount']:.2f}")
    print()

def total_and_average():
    if expenses:
        total = sum(e["amount"] for e in expenses)
        avg = total / len(expenses)
        print(f"Total: ${total:.2f}, Average: ${avg:.2f}\n")
    else:
        print("No expenses recorded.\n")

def expense_menu():
    while True:
        print("1. Add Expense\n2. View All\n3. Total and Average\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_and_average()
        elif choice == "4":
            break
        else:
            print("Invalid choice.\n")

expense_menu()