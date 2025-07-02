# Task 5: Movie Ticket Booking System
# Scenario: Manage ticket booking for a cinema.
# Instructions:
# - Show movie options with available seats and ticket price (dictionary)
# - Allow users to:
#  - Book a ticket (reduce seat count)
#  - View movies and seats
#  - Exit
# - Validate:
#  - That the movie exists
#  - That enough seats are available
# - Use functions, loops, error handling, and data structures
movies = {
    "Iyalode": {"seats": 100, "price": 3500},
    "Straw": {"seats": 50, "price": 5000},
    "Owambe": {"seats": 75, "price": 1800}
}

def show_movies():
    print("Available Movies:")
    for movie, details in movies.items():
        print(f"{movie} - Seats: {details['seats']}, Price: {details['price']} Naira")
    print()
    
def book_ticket():
    movie = input("Enter movie name to book a ticket: ")
    if movie in movies:
        if movies[movie]["seats"] > 0:
            movies[movie]["seats"] -= 1
            print(f"Ticket booked for {movie}. Remaining seats: {movies[movie]['seats']}\n")
        else:
            print("Sorry, no seats available for this movie.\n")
    else:
        print("Movie not found.\n")

def movie_booking_menu():
    while True:
        print("1. Show Movies\n2. Book Ticket\n3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            show_movies()
        elif choice == "2":
            book_ticket()
        elif choice == "3":
            print("Exiting the booking system. Thank you!")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Start the movie booking system function
movie_booking_menu()
