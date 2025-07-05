
# Employee Record Manager

A simple Python application to manage employee records with file storage. This command-line tool allows users to add, view, search, save, and load employee data using JSON files.

## 🔧 Features

* ✅ Add employee records with name, ID, department, and salary
* ✅ View all employee records
* ✅ Search for an employee by ID
* ✅ Save employee records to a file (JSON format)
* ✅ Load employee records from a file
* ✅ Error handling for invalid salary input
* ✅ Modular design with separate utility file (`employee_utils.py`)
* ✅ File existence check using the `os` module

---

## 🚀 Getting Started

### Prerequisites

* Python 3.x installed

### How to Run

1. **Clone the repository** or download the source files.

2. **Navigate to the project directory**:

   ```bash
   cd task5-employee-record-manager
   ```

3. **Run the application**:

   ```bash
   python employee-record-manager.py
   ```

---

## 📌 Usage

### Menu Options

* **Add employee**
  Prompts the user to enter employee details and adds them to the record.

* **View all employees**
  Displays all employee records currently stored in memory.

* **Search by ID**
  Search for an employee using their ID.

* **Save to file**
  Saves the current employee records to a JSON file.

* **Load from file**
  Loads employee records from the JSON file into memory.

---

## ⚠️ Error Handling

* The program uses `try-except` to catch and handle invalid inputs, particularly for salary (non-numeric values).
* Checks if the file exists using the `os` module before loading.

---

## 🧩 Modules Used

* `json` – For saving and loading employee data
* `os` – For checking file existence
* Custom module: `employee_utils.py`
