# Task 3: Calculator with History
# Scenario: A basic calculator that remembers past results.
# Instructions:
# - Show options: Add, Subtract, Multiply, Divide, View History, Exit
# - Use input to take two numbers and perform operation
# - Store each operation and result in a list
# - Show history with index numbers
# - Use functions for operations and error handling for divide-by-zero

history = []

def calculate(op):
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        if op == "1":
            result = a + b
            operation = f"{a} + {b} = {result}"
        elif op == "2":
            result = a - b
            operation = f"{a} - {b} = {result}"
        elif op == "3":
            result = a * b
            operation = f"{a} * {b} = {result}"
        elif op == "4":
            if b == 0:
                print("Cannot divide by zero.\n")
                return
            result = a / b
            operation = f"{a} / {b} = {result}"
        else:
            print("Invalid operation.\n")
            return
        history.append(operation)
        print(f"Result: {result}\n")
    except ValueError:
        print("Invalid input. input the numbers given.\n")

def show_history():
    if not history:
        print("No history yet.\n")
    else:
        for i, entry in enumerate(history):
            print(f"{i+1}. {entry}")
        print()

def calculator_menu():
    while True:
        print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. View History\n6. Exit")
        op = input("Choose an operation: ")
        if op in ["1", "2", "3", "4"]:
            calculate(op)
        elif op == "5":
            show_history()
        elif op == "6":
            break
        else:
            print("Invalid choice.\n")

calculator_menu()