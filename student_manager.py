# student_manager.py

import psycopg2
from tabulate import tabulate

DB_PARAMS = {
    'dbname': 'student_db',
    'user': 'postgres',
    'password': 'your_password',
    'host': 'localhost',
    'port': '5432'
}

def connect():
    return psycopg2.connect(**DB_PARAMS)

def create_table():
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS students (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    email VARCHAR(100) UNIQUE NOT NULL,
                    course VARCHAR(100),
                    grade VARCHAR(2),
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)
        conn.commit()

def add_student(name, email, course, grade):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO students (name, email, course, grade)
                VALUES (%s, %s, %s, %s)
            """, (name, email, course, grade))
        conn.commit()

def view_students():
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id, name, email, course, grade, created_at FROM students ORDER BY id;")
            rows = cur.fetchall()
            print(tabulate(rows, headers=["ID", "Name", "Email", "Course", "Grade", "Created At"], tablefmt="psql"))

def update_student(student_id, name=None, email=None, course=None, grade=None):
    fields = []
    values = []
    if name:
        fields.append("name = %s")
        values.append(name)
    if email:
        fields.append("email = %s")
        values.append(email)
    if course:
        fields.append("course = %s")
        values.append(course)
    if grade:
        fields.append("grade = %s")
        values.append(grade)

    if not fields:
        print("No updates provided.")
        return

    values.append(student_id)
    query = f"UPDATE students SET {', '.join(fields)} WHERE id = %s"

    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute(query, tuple(values))
        conn.commit()

def delete_student(student_id):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM students WHERE id = %s", (student_id,))
        conn.commit()

def search_students(keyword):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT id, name, email, course, grade, created_at
                FROM students
                WHERE name ILIKE %s OR course ILIKE %s
                ORDER BY id
            """, (f"%{keyword}%", f"%{keyword}%"))
            rows = cur.fetchall()
            print(tabulate(rows, headers=["ID", "Name", "Email", "Course", "Grade", "Created At"], tablefmt="psql"))

def menu():
    create_table()
    while True:
        print("""
\n📚 Student Record Manager
1. Add Student
2. View Students
3. Update Student
4. Delete Student
5. Search Students
6. Exit
""")
        choice = input("Select an option: ")
        if choice == '1':
            name = input("Name: ")
            email = input("Email: ")
            course = input("Course: ")
            grade = input("Grade: ")
            add_student(name, email, course, grade)
        elif choice == '2':
            view_students()
        elif choice == '3':
            student_id = int(input("Enter Student ID to update: "))
            name = input("New Name (leave blank to skip): ") or None
            email = input("New Email (leave blank to skip): ") or None
            course = input("New Course (leave blank to skip): ") or None
            grade = input("New Grade (leave blank to skip): ") or None
            update_student(student_id, name, email, course, grade)
        elif choice == '4':
            student_id = int(input("Enter Student ID to delete: "))
            delete_student(student_id)
        elif choice == '5':
            keyword = input("Enter name or course keyword to search: ")
            search_students(keyword)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == '__main__':
    menu()
