from abc import ABC, abstractmethod

# Classe abstrata Student
class Student(ABC):
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    # Método abstrato para calcular o valor da mensalidade
    @abstractmethod
    def calculate_fee(self):
        pass

    # Método abstrato para retornar o nível do estudante
    @abstractmethod
    def get_level(self):
        pass

    # Método para exibir informações gerais do estudante
    def display_info(self):
        return f"Nome: {self.name}, Idade: {self.age}, Curso: {self.course}, Nível: {self.get_level()}, Mensalidade: R${self.calculate_fee():.2f}"


# Classe para estudantes de Graduação
class UndergraduateStudent(Student):
    def get_level(self):
        return "Graduação"

    def calculate_fee(self):
        return 800.00  # Exemplo de taxa fixa para graduação


# Classe para estudantes de Especialização
class SpecializationStudent(Student):
    def get_level(self):
        return "Especialização"

    def calculate_fee(self):
        return 1200.00  # Exemplo de taxa fixa para especialização


# Classe para estudantes de Mestrado
class MasterStudent(Student):
    def get_level(self):
        return "Mestrado"

    def calculate_fee(self):
        return 1500.00  # Exemplo de taxa fixa para mestrado


# Classe para estudantes de Doutorado
class PhDStudent(Student):
    def get_level(self):
        return "Doutorado"

    def calculate_fee(self):
        return 2000.00  # Exemplo de taxa fixa para doutorado
