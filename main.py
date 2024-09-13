import tkinter as tk
from tkinter import messagebox
import sqlite3

from datetime import datetime




# Database connection
def connect_db():
    conn = sqlite3.connect('homework_tracker_secure.db')
    cursor = conn.cursor()

    # Create users table with hashed passwords
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT UNIQUE NOT NULL,
                        password TEXT NOT NULL,
                        role TEXT NOT NULL CHECK (role IN ('teacher', 'student'))
                    )''')

    # Create assignments table
    cursor.execute('''CREATE TABLE IF NOT EXISTS assignments (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL,
                        due_date TEXT NOT NULL,
                        max_score INTEGER NOT NULL,
                        student_id INTEGER,
                        FOREIGN KEY (student_id) REFERENCES users(id)
                    )''')

    conn.commit()
    conn.close()


# Main Application Class



    # Submit the new assignment to the database
def submit_assignment(self):
    title = self.assignment_title_entry.get()
    due_date = self.due_date_entry.get()
    max_score = self.max_score_entry.get()

    try:
        due_date = datetime.strptime(due_date, "%d/%m/%y")
        max_score = int(max_score)

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO assignments (title, due_date, max_score) VALUES (?, ?, ?)",
                        (title, due_date.strftime('%d/%m/%y'), max_score))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Assignment added successfully!")
        self.show_teacher_dashboard()

    except ValueError:
        messagebox.showerror("Error", "Invalid data entered")

# View assignments for teachers
def view_assignments(self):
    self.clear_window()
    tk.Label(self, text="All Assignments").pack(pady=10)

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM assignments")
    assignments = cursor.fetchall()
    conn.close()

    if not assignments:
        tk.Label(self, text="No assignments available").pack()
    else:
        for assignment in assignments:
            text = f"{assignment[1]} | Due: {assignment[2]} | Max Score: {assignment[3]}"
            tk.Label(self, text=text).pack()

    tk.Button(self, text="Back", command=self.show_teacher_dashboard).pack(pady=5)

# Create new student account (Teacher functionality)


# Add a new student to the database
def add_student_account(): #
    new_username = new_student_username_entry.get()
     new_password = new_student_password_entry.get()

    hashed_password = hash_password(new_password)

    conn = connect_db()
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, 'student')",
                        (new_username, hashed_password))
        conn.commit()
        messagebox.showinfo("Success", "Student account created successfully!")
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Username already exists")
    conn.close()

    self.show_teacher_dashboard()

# View assignments for students
def view_assignments_student():
    self.clear_window()
    tk.Label(self, text="My Homework").pack(pady=10)

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM assignments WHERE student_id IS NULL OR student_id=?", (self.student_id,))
    assignments = cursor.fetchall()
    conn.close()

    if not assignments:
        tk.Label(self, text="No assignments assigned yet").pack()
    else:
        for assignment in assignments:
            text = f"{assignment[1]} | Due: {assignment[2]}"
            tk.Label(self, text=text).pack()

    tk.Button(self, text="Back", command=self.show_student_dashboard).pack(pady=5)


# Run the application
if __name__ == "__main__":
    Username = "abc"
    Password = "abc"
    role = 'teacher'
    import HashingFile

