#22. Calcule e mostre o imposto de renda de um grupo de contribuintes considerando que os dados de cada contribuinte 
#(número do CPF, número de dependentes e renda mensal) são valores fornecidos pelo usuário. Para cada contribuinte,
#será feito um desconto no imposto de 5% do salário mínimo (R$ 136,00) para cada dependente. Os valores da alíquota para cálculo do imposto são:
#Até R$ 900,00: isento
#De R$ 900,01 até R$ 1500,00: 5%
#De R$ 1500,01 até R$ 1900,00: 10%
#De R$ 1900,01 até R$ 2200,00: 15%
#Acima de R$ 2200,01: 20%
#O programa deve imprimir para cada contribuinte:

#O total a pagar.
#O número de contribuintes.
#O total de contribuintes isentos e não isentos.
#O total de impostos arrecadados.
#O número do CPF e o valor da contribuição daquele contribuinte que for pagar o maior imposto.
def calcular_imposto_de_renda():
    SALARIO_MINIMO = 136.00
    contribuintes = []
    total_contribuintes = 0
    total_isentos = 0
    total_nao_isentos = 0
    total_impostos = 0
    maior_imposto = 0
    cpf_maior_imposto = None

    while True:
        cpf = input("Digite o CPF (ou '0' para encerrar): ")
        if cpf == '0':
            break
        
        renda_mensal = float(input("Digite a renda mensal: "))
        dependentes = int(input("Digite o número de dependentes: "))
        
        desconto_dependentes = dependentes * (SALARIO_MINIMO * 0.05)
        renda_liquida = renda_mensal - desconto_dependentes
        
        if renda_liquida <= 900:
            imposto = 0
            total_isentos += 1
        elif renda_liquida <= 1500:
            imposto = renda_liquida * 0.05
            total_nao_isentos += 1
        elif renda_liquida <= 1900:
            imposto = renda_liquida * 0.10
            total_nao_isentos += 1
        elif renda_liquida <= 2200:
            imposto = renda_liquida * 0.15
            total_nao_isentos += 1
        else:
            imposto = renda_liquida * 0.20
            total_nao_isentos += 1

        total_contribuintes += 1
        total_impostos += imposto

        if imposto > maior_imposto:
            maior_imposto = imposto
            cpf_maior_imposto = cpf
        
        contribuintes.append({
            "cpf": cpf,
            "imposto": imposto
        })

    print(f"Total de contribuintes: {total_contribuintes}")
    print(f"Total de contribuintes isentos: {total_isentos}")
    print(f"Total de contribuintes não isentos: {total_nao_isentos}")
    print(f"Total de impostos arrecadados: R$ {total_impostos:.2f}")
    
    if cpf_maior_imposto:
        print(f"Contribuinte com maior imposto: CPF {cpf_maior_imposto}, Imposto: R$ {maior_imposto:.2f}")

calcular_imposto_de_renda()  # Exemplo de uso
