
# 📚 Library Management System

A simple terminal-based Library Management System in Python that allows users to manage a collection of books — add, borrow, return, view, and save book records.

## 🚀 Features

- Add new books with title and author
- Borrow and return books
- View all available and borrowed books
- Save and load data using JSON files
- Persistent storage with `books.json`
- File operations separated into utility module

## 🧾 Structure

```plaintext
task1-library-management-system.py       # Main program
library_utils.py                         # Handles JSON file load/save
books.json                               # Stores book data (20 books preloaded)
README.md                                # This file
````

## 📦 Requirements

* Python 3.x
* No external libraries required (uses built-in `json` and `os`)

## 📂 Setup

1. Clone the repository or download the files.
2. Make sure `books.json` exists in the same directory with preloaded books (or run the program to create one).
3. Run the main script:

```bash
python library_system.py
```

## 📘 Example Menu

```
Welcome to the Library Management System!
1. add a new book
2. borrow a book
3. return a book
4. view all books
5. save and exit
```