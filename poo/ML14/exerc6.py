from abc import ABC, abstractmethod

# Classe abstrata Student
class Student(ABC):
    def __init__(self, name: str, age: int, student_id: int):
        self.name = name
        self.age = age
        self.student_id = student_id

    @abstractmethod
    def get_student_type(self) -> str:
        pass

    def __str__(self):
        return f"{self.get_student_type()} - Nome: {self.name}, Idade: {self.age}, ID: {self.student_id}"

# Mix-In para adicionar funcionalidade de pesquisador
class ResearcherMixin:
    def conduct_research(self):
        return f"{self.name} está conduzindo uma pesquisa."

# Mix-In para adicionar funcionalidade de monitor
class TeachingAssistantMixin:
    def assist_teaching(self):
        return f"{self.name} está auxiliando nas aulas."

# Classe UndergraduateStudent (Graduação) que pode ser pesquisador e/ou monitor
class UndergraduateStudent(Student, ResearcherMixin, TeachingAssistantMixin):
    def get_student_type(self) -> str:
        return "Graduação"

# Classe MasterStudent (Mestrado) que pode ser apenas pesquisador
class MasterStudent(Student, ResearcherMixin):
    def get_student_type(self) -> str:
        return "Mestrado"

# Exemplo de uso do sistema de Gestão Acadêmica com Mix-Ins
if __name__ == "__main__":
    student1 = UndergraduateStudent(name="Alice", age=20, student_id=1)
    student2 = MasterStudent(name="Bruno", age=28, student_id=2)

    print(student1)
    print(student1.conduct_research())
    print(student1.assist_teaching())

    print(student2)
    print(student2.conduct_research())
