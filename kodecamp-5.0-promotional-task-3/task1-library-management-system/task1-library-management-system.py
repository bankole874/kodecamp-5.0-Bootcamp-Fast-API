# Task 1: Library Management System
# Goal: Manage a collection of books that users can borrow and return.
# Features:
# - Create a Book class with title, author, and available status.
# - Create a Library class that holds a list of Book objects.
# - Use the 'json' module to save/load book records to/from file.
# - Use the 'os' module to check if the data file exists before loading.
# - Create a separate module (library_utils.py) to handle file saving/loading.
# Menu Options:
# - Add a new book
# - Borrow a book
# - Return a book
# - View all books
# - Save & Exit

from library_utils import load_books, save_books

class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available

    def to_dict(self):
        return {
            'title': self.title,
            'author': self.author,
            'available': self.available
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(data['title'], data['author'], data['available'])

class Library:
    def __init__(self, filename='books.json'):
        self.filename = filename
        self.books = [Book.from_dict(b) for b in load_books(self.filename)]
    def add_book(self, title, author):
        self.books.append(Book(title, author))
        print(f"A new book titled \"{title}\", by \"{author}\" has been added.")
    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.available:
                book.available = False
                print(f"you borrowed '{book.title}'.")
                return
        print("Book not available.")
    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.available == False:
                book.available = True
                print(f"you returned '{title}'.")
                return
        print("Book not found or not borrowed.")
    def view_books(self):
        count = 0
        if not self.books:
            print("books not available.")
        for book in self.books:
            count += 1
            status = "Available" if book.available else "Borrowed"
            print(f"{count}. {book.title} by {book.author} - {status}")
    def save_and_exit(self):
        save_books(self.filename, [book.to_dict() for book in self.books])
        print("Saved and Exited Successfully")

def main():
    lib = Library()

    while True:
        print()
        print("Welcome to the Library Management System!")
        print("1. add a new book")
        print("2. borrow a book")
        print("3. return a book")
        print("4. view all books")
        print("5. save and exit")
        option = int(input("Please select your option: "))

        if (option == 1):
            title = input("enter book title: ")
            author = input("enter author's name: ")
            lib.add_book(title,author)
        elif (option == 2):
            title = input("enter book title: ")
            lib.borrow_book(title)
        elif (option == 3):
            title = input("enter book title: ")
            lib.return_book(title)
        elif (option == 4):
            lib.view_books()
        elif (option == 5):
            lib.save_and_exit()
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
