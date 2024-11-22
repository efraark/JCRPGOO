from abc import ABC, abstractmethod

# Classe abstrata base Student
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


# Interface específica para Pesquisa
class Researcher(ABC):
    @abstractmethod
    def conduct_research(self):
        pass


# Interface específica para Assistência em Monitoria
class TeachingAssistant(ABC):
    @abstractmethod
    def assist_teaching(self):
        pass


# Classe UndergraduateStudent (Graduação) - Registrada como subclasse virtual das interfaces
class UndergraduateStudent(Student):
    def get_student_type(self) -> str:
        return "Graduação"


# Registrar UndergraduateStudent como subclasse virtual das interfaces
Researcher.register(UndergraduateStudent)
TeachingAssistant.register(UndergraduateStudent)


# Classe MasterStudent (Mestrado) - Registrada como subclasse virtual de Researcher
class MasterStudent(Student):
    def get_student_type(self) -> str:
        return "Mestrado"


# Registrar MasterStudent como subclasse virtual de Researcher
Researcher.register(MasterStudent)


# Implementação específica para GraduateStudent
class UndergraduateStudentImplementation(UndergraduateStudent):
    def conduct_research(self):
        return f"{self.name} está conduzindo uma pesquisa."

    def assist_teaching(self):
        return f"{self.name} está auxiliando nas aulas."


# Implementação específica para MasterStudent
class MasterStudentImplementation(MasterStudent):
    def conduct_research(self):
        return f"{self.name} está conduzindo uma pesquisa."


# Exemplo de uso
if __name__ == "__main__":
    student1 = UndergraduateStudentImplementation(name="Alice", age=20, student_id=1)
    student2 = MasterStudentImplementation(name="Bruno", age=28, student_id=2)

    print(student1)
    print(student1.conduct_research())
    print(student1.assist_teaching())

    print(student2)
    print(student2.conduct_research())

    # Verificar se as classes são subclasses virtuais
    print(isinstance(student1, Researcher))  # True
    print(isinstance(student1, TeachingAssistant))  # True
    print(isinstance(student2, Researcher))  # True
    print(isinstance(student2, TeachingAssistant))  # False
