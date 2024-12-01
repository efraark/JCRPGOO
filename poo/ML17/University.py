class university:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_all_students(self):
        print(f"Universidade: {self.name}")
        for student in self.students:
            print(student.display_info())
