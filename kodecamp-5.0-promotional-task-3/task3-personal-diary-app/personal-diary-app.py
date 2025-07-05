# Task 3: Personal Diary App
# Goal: Write and view personal diary entries.
# Features:
# - Create a DiaryEntry class with date, title, and content.
# - Use datetime.now() to timestamp each entry.
# - Use 'json' to store/load all diary entries.
# - Place helper functions in a module called diary_tools.py.
# - Validate input and handle file-related exceptions.
# Menu Options:
# - Add entry
# - View all entries
# - Search by date or title
# - Save & Exit

import diary_tools as diary
from diary_tools import load_entries, save_entries
from datetime import datetime

class DiaryEntry:
    def __init__(self, title, content):
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.title = title
        self.content = content

    def to_dict(self): # to_dict method to convert entry to dictionary
        return {
            "date": self.date,
            "title": self.title,
            "content": self.content
        }

    @staticmethod
    def from_dict(data): # from_dict method to create an entry from a dictionary
        entry = DiaryEntry(data['title'], data['content'])
        entry.date = data['date']
        return entry

class Diary_app():
    def __init__(self, filename='diary.json'):
        self.filename = filename
        self.entries = [DiaryEntry.from_dict(e) for e in diary.load_entries(self.filename)]

    def add_entry(self, title, content):
        entry = DiaryEntry(title, content)
        self.entries.append(entry)
        print("Entry added successfully.")

    def view_entries(self):
        if not self.entries:
            print("No entries found.")
            return
        for entry in self.entries:
            print(f"{entry.date} - {entry.title}\n{entry.content}\n")

    def search_entries(self, query):
        results = [entry for entry in self.entries if query.lower() in entry.title.lower() or query in entry.date]
        return results
    
    def save_and_exit(self):
        diary.save_entries([entry.to_dict() for entry in self.entries], self.filename)
        print("Entries saved successfully. Exiting the app.")

def main():
    app = Diary_app()

    while True:
        print("\nPersonal Diary App")
        print("1. Add Entry")
        print("2. View All Entries")
        print("3. Search Entries")
        print("4. Save & Exit")
        option = input("Choose an option: ")

        if option == '1':
            title = input("Enter title: ")
            content = input("Enter content: ")
            app.add_entry(title, content)
        elif option == '2':
            app.view_entries()
        elif option == '3':
            query = input("Enter date or title to search: ")
            results = app.search_entries(query)
            if results:
                for entry in results:
                    print(f"{entry.date} - {entry.title}\n{entry.content}\n")
            else:
                print("No entries found.")
        elif option == '4':
            app.save_and_exit()
            break
        else:
            print("Invalid option, please try again.")
            
if __name__ == "__main__":
    main()