from student import UndergraduateStudent, SpecializationStudent, MasterStudent, PhDStudent

# Função principal para gerenciar os estudantes
def main():
    students = []

    # Criando instâncias de diferentes tipos de estudantes
    students.append(UndergraduateStudent("Ana", 20, "Engenharia"))
    students.append(SpecializationStudent("Bruno", 30, "Gestão de Projetos"))
    students.append(MasterStudent("Carla", 27, "Inteligência Artificial"))
    students.append(PhDStudent("Daniel", 35, "Física Quântica"))

    # Exibindo informações de todos os estudantes
    for student in students:
        print(student.display_info())

if __name__ == "__main__":
    main()
