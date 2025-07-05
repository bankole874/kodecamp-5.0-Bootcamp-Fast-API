### 📦 Package Delivery System

A simple Python-based console application to manage and track package deliveries.

---

### 🚀 Features

* Register a new package with sender and recipient
* View all registered packages
* Mark packages as delivered
* Save and load package data using JSON files
* Unique ID generation using `uuid`

---

### 🛠 Requirements

* Python 3.6 or higher

No external dependencies required.

---

### 📄 Usage

1. **Run the application:**

   ```bash
   python3 package-delivery-system.py
   ```

2. **Choose from the menu:**

   ```
   1. Register a package
   2. Mark package as delivered
   3. View all packages
   4. Save & Exit
   ```

3. **Data is saved to `packages.json` automatically on exit.**

---

### 📂 Sample JSON Format

```json
[
    [
        "uuid",
        "sender",
        "recipient",
        "status"]
]
```

Example:

```json
[
    [
        "7e59d95a-6e9f-4c12-8fa9-1b02f45d7a78",
        "Chinedu",
        "Amina",
        "Delivered"]
]
```