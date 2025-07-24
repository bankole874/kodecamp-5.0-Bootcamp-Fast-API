
# **Student Report Card App**

A simple terminal-based Python application to manage students, their subjects, scores, average marks, and grades.  
The application stores student data in a JSON file for persistence.

---

## **Features**
- **Add Students:** Create a new student with subjects and scores.
- **View Students:** Display all students, their subjects, scores, average, and grade.
- **Update Student Data:** Update scores for an existing student's subjects.
- **Save & Load:** Automatically saves data to `students.json` and loads it on startup.
- **Grades:** Automatically assigns grades based on average scores:
  - **A:** 90–100
  - **B:** 80–89
  - **C:** 70–79
  - **D:** 60–69
  - **F:** below 60

---

## **Installation and Setup**

### **1. Clone the Repository**
```bash
git clone https://github.com/bankole874/kodecamp-5.0-Bootcamp-Fast-API.git
cd /kodecamp-5.0-promotional-task-4/task1-Student_Report_Card_App/
````

### **2. Create a Virtual Environment (Optional but Recommended)**

```bash
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### **3. Run the Application**

```bash
python Student_report_card_app.py
```

---

## **Usage**

When you start the app, you'll see a menu:

```
Student Report Card App
1. Add Student
2. View Students
3. Update Student Data
4. Exit
```

**Example Workflow:**

1. Choose `1` to add a student.
2. Enter subjects and scores.
3. Choose `2` to view all students with their average and grade.
4. Choose `3` to update an existing student’s subject scores.

---

## **Data Storage**

* All student data is stored in `students.json` (auto-created in the project directory).
* You can delete `students.json` to reset all data.

---

## **Version Control with Git**

When making changes, follow commit message guidelines:

```
* Add Student class and JSON save feature
* Fix average score calculation
```

---

## **Future Improvements**

* Add support for deleting students.
* Add GPA calculation.
* Improve user interface with color formatting.
* Add unit tests for core functions.

```

---

Would you like me to **generate this `README.md` file in your current directory** and give you the content as a downloadable file?
```
