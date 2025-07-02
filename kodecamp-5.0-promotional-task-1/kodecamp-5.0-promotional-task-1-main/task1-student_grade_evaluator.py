def student_grade_evaluator():
    # Ask how many students to process
    num_students = int(input("Enter the number of students to process: "))

    # Counters for summary

    passed = 0
    failed = 0
    excellent = 0

    for i in range(num_students):
        print(f"\nStudent {i+1}:")
        name = input("Enter student's name: ")
            
        # Get and convert scores
        scores = []
        for j in range(1, 4):
            score = float(input(f"Enter score {j} for {name}: "))
            scores.append(score)

        average = sum(scores) / 3

         # Display result
        if average < 50:
            print(f"{name}'s Average: {average:.2f} - Result: Fail")
            failed += 1
        elif 50 <= average < 80:
            print(f"{name}'s Average: {average:.2f} - Result: Pass")
            passed += 1
        else:
            print(f"{name}'s Average: {average:.2f} - Result: Excellent!")

    # Summary
    print("\nSummary:")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")
    print(f"Excellent: {excellent}")

# Run the function
student_grade_evaluator()