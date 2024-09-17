#28. Em uma loja de eletrodomésticos, os funcionários da seção de TVs recebem, mensalmente, um salário fixo mais comissão.
#A comissão é calculada em relação ao tipo e ao número de televisores vendidos, de acordo com a tabela:
#8K: 10 ou mais TVs vendidas - R$ 550 por TV vendida, menos de 10 TVs - R$ 350 por TV vendida.
#4K: 10 ou mais TVs vendidas - R$ 420 por TV vendida, menos de 10 TVs - R$ 250 por TV vendida.
#Sabendo que o funcionário tem um desconto de 8% para o INSS e, se o salário total for superior a R$ 950,00, um desconto de 5% para imposto de renda,
#faça um programa que:

#Calcule o salário líquido de vários funcionários.
#Ao final, imprima o número total de funcionários, o total de salários pagos, a média das comissões, 
# e o valor da maior e da menor comissão paga pelo departamento.
def calculate_salaries():
    INSS_DISCOUNT = 0.08
    INCOME_TAX_DISCOUNT = 0.05
    salary_fixed = 1000.00
    
    total_employees = 0
    total_salaries = 0
    total_commissions = 0
    min_commission = float('inf')
    max_commission = 0

    while True:
        employee_name = input("Digite o nome do funcionário (ou 'fim' para encerrar): ")
        if employee_name.lower() == 'fim':
            break

        tv_type = input("Digite o tipo de TV vendida (8K/4K): ").lower()
        num_tvs = int(input("Digite o número de TVs vendidas: "))

        if tv_type == '8k':
            if num_tvs >= 10:
                commission = num_tvs * 550
            else:
                commission = num_tvs * 350
        elif tv_type == '4k':
            if num_tvs >= 10:
                commission = num_tvs * 420
            else:
                commission = num_tvs * 250
        else:
            print("Tipo de TV inválido.")
            continue

        total_salary = salary_fixed + commission
        total_salaries += total_salary
        total_commissions += commission
        total_employees += 1

        if commission > max_commission:
            max_commission = commission
        if commission < min_commission:
            min_commission = commission

        # Descontos
        salary_after_inss = total_salary * (1 - INSS_DISCOUNT)
        if salary_after_inss > 950:
            salary_final = salary_after_inss * (1 - INCOME_TAX_DISCOUNT)
        else:
            salary_final = salary_after_inss

        print(f"Salário líquido de {employee_name}: R$ {salary_final:.2f}\n")

    if total_employees > 0:
        avg_commission = total_commissions / total_employees
        print(f"Total de funcionários: {total_employees}")
        print(f"Total de salários pagos: R$ {total_salaries:.2f}")
        print(f"Média das comissões: R$ {avg_commission:.2f}")
        print(f"Maior comissão: R$ {max_commission:.2f}")
        print(f"Menor comissão: R$ {min_commission:.2f}")
    else:
        print("Nenhum funcionário foi registrado.")

calculate_salaries()  # Exemplo de uso
