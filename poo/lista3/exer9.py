class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

class StudentComparator:
    @staticmethod
    def is_equal(student1, student2):
        return student1.name == student2.name

    @staticmethod
    def is_less_than(student1, student2):
        return student1.name < student2.name

    @staticmethod
    def is_greater_or_equal(student1, student2):
        return student1.name >= student2.name
