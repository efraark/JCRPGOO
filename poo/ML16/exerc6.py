from abc import ABC, abstractmethod

# Interface para cálculo de taxas
class FeeCalculator(ABC):
    @abstractmethod
    def calculate_fee(self):
        pass


# Interface para obter o nível do estudante
class LevelProvider(ABC):
    @abstractmethod
    def get_level(self):
        pass


# Classe abstrata Student com dependências injetadas
class Student:
    def __init__(self, name, age, course, fee_calculator: FeeCalculator, level_provider: LevelProvider):
        self.name = name
        self.age = age
        self.course = course
        self.fee_calculator = fee_calculator
        self.level_provider = level_provider

    def calculate_fee(self):
        return self.fee_calculator.calculate_fee()

    def get_level(self):
        return self.level_provider.get_level()

    def display_info(self):
        return (
            f"Nome: {self.name}, Idade: {self.age}, Curso: {self.course}, "
            f"Nível: {self.get_level()}, Mensalidade: R${self.calculate_fee():.2f}"
        )


# Implementações de FeeCalculator e LevelProvider para diferentes níveis
class UndergraduateFeeCalculator(FeeCalculator):
    def calculate_fee(self):
        return 800.00


class UndergraduateLevelProvider(LevelProvider):
    def get_level(self):
        return "Graduação"


class SpecializationFeeCalculator(FeeCalculator):
    def calculate_fee(self):
        return 1200.00


class SpecializationLevelProvider(LevelProvider):
    def get_level(self):
        return "Especialização"


class MasterFeeCalculator(FeeCalculator):
    def calculate_fee(self):
        return 1500.00


class MasterLevelProvider(LevelProvider):
    def get_level(self):
        return "Mestrado"


class PhDFeeCalculator(FeeCalculator):
    def calculate_fee(self):
        return 2000.00


class PhDLevelProvider(LevelProvider):
    def get_level(self):
        return "Doutorado"


# Exemplo de uso
if __name__ == "__main__":
    # Estudantes criados com dependências injetadas
    student1 = Student(
        name="Alice",
        age=20,
        course="Engenharia",
        fee_calculator=UndergraduateFeeCalculator(),
        level_provider=UndergraduateLevelProvider(),
    )

    student2 = Student(
        name="Bruno",
        age=28,
        course="Administração",
        fee_calculator=SpecializationFeeCalculator(),
        level_provider=SpecializationLevelProvider(),
    )

    student3 = Student(
        name="Clara",
        age=35,
        course="Ciência de Dados",
        fee_calculator=MasterFeeCalculator(),
        level_provider=MasterLevelProvider(),
    )

    student4 = Student(
        name="Daniel",
        age=40,
        course="Física",
        fee_calculator=PhDFeeCalculator(),
        level_provider=PhDLevelProvider(),
    )

    # Exibição das informações dos estudantes
    print(student1.display_info())
    print(student2.display_info())
    print(student3.display_info())
    print(student4.display_info())
