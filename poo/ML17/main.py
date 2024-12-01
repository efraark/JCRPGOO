from student import UndergraduateStudent, SpecializationStudent, MasterStudent, PhDStudent
from university import University

# Função principal para gerenciar os estudantes
def main():
    # Instanciando a universidade
    university = University("IFSP")

    # Adicionando estudantes à universidade
    university.add_student(UndergraduateStudent("Ana", 20, "Engenharia"))
    university.add_student(SpecializationStudent("Bruno", 30, "Gestão de Projetos"))
    university.add_student(MasterStudent("Carla", 27, "Inteligência Artificial"))
    university.add_student(PhDStudent("Daniel", 35, "Física Quântica"))

    # Exibindo informações de todos os estudantes
    university.display_all_students()

if __name__ == "__main__":
    main()
