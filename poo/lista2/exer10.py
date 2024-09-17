#10. Adicione três métodos à classe Student estudada em sala que compara dois objetos 
#método retorna o resultado da comparação dos nomes dos dois alunos. Inclua uma 
#função main que testa todos os operadores de comparação. Em seguida, coloque 
#vários objetos Student em uma lista e embaralhe. Em seguida, execute o método sort 
#com esta lista e exiba todas as informações dos alunos
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):
        return self.name < other.name

    def __ge__(self, other):
        return self.name >= other.name

# Teste
students = [Student("Ana", 9), Student("Carlos", 8), Student("Bruno", 10)]
students.sort()
for student in students:
    print(student.name, student.grade)
