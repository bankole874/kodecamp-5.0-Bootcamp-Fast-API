def number_analyzer():

    even_count = 0
    odd_count = 0
    negative_count = 0
    zero_count = 0
    
    for i in range(1, 6):
        num = int(input(f"\nEnter number {i}: "))
        
        # Even or Odd
        if num % 2 == 0:
            print(f"{num} is Even.")
            even_count += 1
        else:
            print(f"{num} is Odd.")
            odd_count += 1
            
        # Positive, Negative or Zero
        if num > 0:
            print(f"{num} is Positive.")
        elif num < 0:
            print(f"{num} is Negative.")
            negative_count += 1
        else:
            print("The number is Zero.")
            zero_count += 1
            
    # Summary
    print("\n--- Summary ---")
    print(f"Even numbers: {even_count}")
    print(f"Odd numbers: {odd_count}")
    print(f"Negative numbers: {negative_count}")
    print(f"Zeroes: {zero_count}")
    
# Run the function
number_analyzer()