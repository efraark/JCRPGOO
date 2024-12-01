from student import UndergraduateStudent, SpecializationStudent, MasterStudent, PhDStudent

class University:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_undergraduate_student(self, name, age, course):
        self.students.append(UndergraduateStudent(name, age, course))

    def add_specialization_student(self, name, age, course):
        self.students.append(SpecializationStudent(name, age, course))

    def add_master_student(self, name, age, course):
        self.students.append(MasterStudent(name, age, course))

    def add_phd_student(self, name, age, course):
        self.students.append(PhDStudent(name, age, course))

    def display_all_students(self):
        print(f"Universidade: {self.name}")
        for student in self.students:
            print(student.display_info())
