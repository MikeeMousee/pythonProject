class Homework:
    def __init__(self, subject, due_date, description):
        self.subject = subject
        self.due_date = due_date
        self.description = description
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
        return f"{self.subject}: {self.description} due on {self.due_date} {'(Completed)' if self.completed else ''}"


class Tracker:
    def __init__(self):
        self.homework_list = []

    def add_homework(self, homework):
        self.homework_list.append(homework)

    def display_homework(self):
        for homework in self.homework_list:
            print(homework)


if __name__ == "__main__":
    tracker = Tracker()
    tracker.add_homework(Homework('Math', '2024-06-30', 'Algebra worksheet'))
    tracker.add_homework(Homework('Science', '2024-07-05', 'Chemistry lab report'))
    tracker.display_homework()
