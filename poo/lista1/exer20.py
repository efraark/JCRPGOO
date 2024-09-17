#20. Elabore um programa didático nos mesmos moldes do anterior para treino da divisão. 
#Neste programa deve ser perguntado à criança o resultado da divisão e o resto.
def divisao_treino():
    acertos = 0
    erros = 0
    total_perguntas = 0

    while True:
        dividendo = random.randint(1, 100)
        divisor = random.randint(1, 10)
        quociente_correto = dividendo // divisor
        resto_correto = dividendo % divisor

        quociente = int(input(f"Qual é o quociente de {dividendo} ÷ {divisor}? "))
        resto = int(input(f"Qual é o resto de {dividendo} ÷ {divisor}? "))

        if quociente == quociente_correto and resto == resto_correto:
            print("Correto!")
            acertos += 1
        else:
            print(f"Errado! O quociente correto é {quociente_correto} e o resto é {resto_correto}.")
            erros += 1

        total_perguntas += 1
        continuar = input("Deseja continuar? (s/n): ").lower()
        if continuar != 's':
            break

    print(f"Número de perguntas respondidas: {total_perguntas}")
    print(f"Número de acertos: {acertos}")
    print(f"Número de erros: {erros}")

divisao_treino()  # Exemplo de uso
