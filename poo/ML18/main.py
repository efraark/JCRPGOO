from university import University

# Função principal para gerenciar os estudantes
def main():
    # Criando uma universidade e adicionando estudantes diretamente
    university = University("IFSP")

    # Adicionando estudantes à universidade
    university.add_undergraduate_student("Ana", 20, "Engenharia")
    university.add_specialization_student("Bruno", 30, "Gestão de Projetos")
    university.add_master_student("Carla", 27, "Inteligência Artificial")
    university.add_phd_student("Daniel", 35, "Física Quântica")

    # Exibindo informações de todos os estudantes
    university.display_all_students()

if __name__ == "__main__":
    main()
