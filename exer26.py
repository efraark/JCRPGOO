#26. Uma empresa está fazendo um estudo de possibilidades de aumento para seus funcionários 
#e deseja saber se é mais vantajoso dar um aumento uniforme de 10% para todos os funcionários ou seguir uma tabela progressiva:
#Até R$ 1000,00: 15%
#Até R$ 2000,00: 10%
#Acima de R$ 2000,00: 5%
#Faça um programa que leia o salário de um número qualquer de funcionários,
#imprima para cada um o novo salário nos dois casos (aumento uniforme ou progressivo). Ao final, o programa deve fornecer:

#O total de funcionários.
#O salário médio dos funcionários.
#O total da folha de pagamentos atual.
#O total da folha de pagamentos futura nos dois casos, indicando qual é o caminho mais econômico para a empresa.
def salary_increase_study():
    total_employees = 0
    total_salary = 0
    total_new_salary_uniform = 0
    total_new_salary_progressive = 0

    while True:
        salary = float(input("Digite o salário do funcionário (ou 0 para sair): "))
        if salary == 0:
            break

        total_employees += 1
        total_salary += salary

        # Aumento uniforme
        new_salary_uniform = salary * 1.10
        total_new_salary_uniform += new_salary_uniform

        # Aumento progressivo
        if salary <= 1000:
            new_salary_progressive = salary * 1.15
        elif salary <= 2000:
            new_salary_progressive = salary * 1.10
        else:
            new_salary_progressive = salary * 1.05
        total_new_salary_progressive += new_salary_progressive

        print(f"Salário original: R$ {salary:.2f}")
        print(f"Novo salário com aumento uniforme: R$ {new_salary_uniform:.2f}")
        print(f"Novo salário com aumento progressivo: R$ {new_salary_progressive:.2f}\n")

    if total_employees > 0:
        average_salary = total_salary / total_employees
        print(f"Total de funcionários: {total_employees}")
        print(f"Salário médio dos funcionários: R$ {average_salary:.2f}")
        print(f"Total da folha de pagamento atual: R$ {total_salary:.2f}")
        print(f"Total da folha de pagamento com aumento uniforme: R$ {total_new_salary_uniform:.2f}")
        print(f"Total da folha de pagamento com aumento progressivo: R$ {total_new_salary_progressive:.2f}")

        if total_new_salary_uniform < total_new_salary_progressive:
            print("O aumento uniforme é mais econômico.")
        else:
            print("O aumento progressivo é mais econômico.")
    else:
        print("Nenhum funcionário foi registrado.")

salary_increase_study()  # Exemplo de uso
