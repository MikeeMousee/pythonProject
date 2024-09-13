import tkinter as tk
import main as sqlcode

class HomeworkTrackerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Secure Homework Tracker")
        self.geometry("400x300")
        sqlcode.connect_db()  # Ensure the database is set up
        self.show_login_page()

    # Clear screen and show login page
    def show_login_page(self):
        self.clear_window()
        tk.Label(self, text="Welcome to Homework Tracker").pack(pady=10)
        tk.Label(self, text="Username").pack()
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        tk.Label(self, text="Password").pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        tk.Label(self, text="Login as").pack(pady=10)
        tk.Button(self, text="Teacher", command=self.teacher_login).pack(side=tk.LEFT, padx=20)
        tk.Button(self, text="Student", command=self.student_login).pack(side=tk.RIGHT, padx=20)
    # Clear the current window's widgets
    def clear_window(self):
        for widget in self.winfo_children():
            widget.destroy()

    # Teacher login verification
    def teacher_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        self.login(username, password, 'teacher')

    # Student login verification
    def student_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        self.login(username, password, 'student')

    # Login handler (common for teacher and student)
    def login(self, username, password, role):
        conn = sqlcode.connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=? AND role=?", (username, role))
        result = cursor.fetchone()
        conn.close()

        if result and sqlcode.verify_password(result[2], password):
            if role == 'teacher':
                self.show_teacher_dashboard()
            elif role == 'student':
                self.student_id = result[0]
                self.show_student_dashboard()
        else:
            tk.messagebox.showerror("Error", f"Invalid {role} credentials")

    # Show teacher dashboard
    def show_teacher_dashboard(self):
        self.clear_window()
        tk.Label(self, text="Teacher Dashboard").pack(pady=10)

        tk.Button(self, text="Assign Homework", command=self.assign_homework).pack(pady=5)
        tk.Button(self, text="View Assignments", command=self.view_assignments).pack(pady=5)
        tk.Button(self, text="Create Student Account", command=self.create_student_account).pack(pady=5)
        tk.Button(self, text="Logout", command=self.show_login_page).pack(pady=5)

    # Show student dashboard
    def show_student_dashboard(self):
        self.clear_window()
        tk.Label(self, text="Student Dashboard").pack(pady=10)
        tk.Button(self, text="View My Homework", command=self.view_assignments_student).pack(pady=5)
        tk.Button(self, text="Logout", command=self.show_login_page).pack(pady=5)

    # Assign homework (Teacher functionality)
    def assign_homework(self):
        self.clear_window()
        tk.Label(self, text="Assign Homework").pack(pady=10)

        tk.Label(self, text="Assignment Title").pack()
        self.assignment_title_entry = tk.Entry(self)
        self.assignment_title_entry.pack()

        tk.Label(self, text="Due Date (YYYY-MM-DD)").pack()
        self.due_date_entry = tk.Entry(self)
        self.due_date_entry.pack()

        tk.Label(self, text="Max Score").pack()
        self.max_score_entry = tk.Entry(self)
        self.max_score_entry.pack()

        tk.Button(self, text="Submit", command=self.submit_assignment).pack(pady=5)
        tk.Button(self, text="Back", command=self.show_teacher_dashboard).pack(pady=5)

    def create_student_account(self):
        self.clear_window()
        tk.Label(self, text="Create New Student Account").pack(pady=10)

        tk.Label(self, text="New Student Username").pack()
        self.new_student_username_entry = tk.Entry(self)
        self.new_student_username_entry.pack()

        tk.Label(self, text="New Student Password").pack()
        self.new_student_password_entry = tk.Entry(self, show="*")
        self.new_student_password_entry.pack()

        tk.Button(self, text="Create Account", command=self.add_student_account).pack(pady=5)
        tk.Button(self, text="Back", command=self.show_teacher_dashboard).pack(pady=5)

if __name__ == "__main__":
    app = HomeworkTrackerApp()
    app.mainloop()