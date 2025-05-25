# 🎓 Student Record Manager (Python + PostgreSQL)

A command-line app to manage student records using PostgreSQL and Python. Ideal for learning SQL integration, CRUD operations, and clean Python structuring.

## 🧰 Tech Stack

- Python 3
- PostgreSQL
- `psycopg2` (PostgreSQL client)
- `tabulate` (pretty CLI tables)

## 🔧 Features

- Add student with name, email, course, and grade
- View all students
- Update individual fields
- Delete by ID
- Search by name or course
- Timestamp for record creation

## 🛠️ Setup Instructions

1. Create PostgreSQL database:
    ```sql
    CREATE DATABASE student_db;
    ```

2. Use the schema:
    ```bash
    psql -U postgres -d student_db -f schema.sql
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the app:
    ```bash
    python student_manager.py
    ```

## 📂 Folder Structure

```
student-record-manager/
├── student_manager.py
├── schema.sql
├── requirements.txt
└── README.md
```

## 📘 License

MIT License
