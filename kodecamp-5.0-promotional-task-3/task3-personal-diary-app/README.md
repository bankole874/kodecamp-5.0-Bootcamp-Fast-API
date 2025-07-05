
# 📝 Personal Diary App

A simple command-line diary application that allows you to write, view, search, and save personal diary entries.

---

## 📌 Features

- Create diary entries with automatic date stamping.
- View all saved entries.
- Search entries by date or title.
- Automatically saves all entries to a JSON file (`diary.json`).
- Handles file errors and input validation.
- Keeps logic modular using a helper module `diary_tools.py`.

---

## 🧑🏽‍💻 User Context

This project reflects the life of a **Muslim technical support engineer based in Lagos, Nigeria** working **9–5 (Mon–Fri)** and attending **madrasah on weekends**. Diary entries reflect a balance of work, spirituality, and daily life.

---

## 🚀 How to Run

1. Clone or download this repository.
2. Make sure you have Python 3 installed.
3. In your terminal, navigate to the project directory.
4. Run the app:

```bash
python3 personal-diary-app.py
````

---

## 📂 Data Format (`diary.json`)

Each entry in the JSON file includes:

```json
{
  "date": "2025-07-05",
  "title": "Sample Title",
  "content": "This is the diary content."
}
```

---

## ✅ Example Menu

```
Personal Diary App
1. Add Entry
2. View All Entries
3. Search Entries
4. Save & Exit
```

---

## 🛠 Requirements

* Python 3.x
* No external libraries needed (only `json`, `datetime`, `os`)