#21. Faça um programa didático para estudo das raízes quadradas dos números, da seguinte forma: o programa gera um número aleatório, 
#eleva ao quadrado e pergunta qual a raiz quadrada desse valor para o estudante.
#O programa deve apresentar as mensagens de erro e incentivo e os números de perguntas, acertos e erros de forma semelhante aos anteriores.
def raiz_quadrada_treino():
    acertos = 0
    erros = 0
    total_perguntas = 0

    while True:
        numero = random.randint(1, 20)
        quadrado = numero ** 2

        resposta = int(input(f"Qual é a raiz quadrada de {quadrado}? "))

        if resposta == numero:
            print("Correto!")
            acertos += 1
        else:
            print(f"Errado! A raiz quadrada correta é {numero}.")
            erros += 1

        total_perguntas += 1
        continuar = input("Deseja continuar? (s/n): ").lower()
        if continuar != 's':
            break

    print(f"Número de perguntas respondidas: {total_perguntas}")
    print(f"Número de acertos: {acertos}")
    print(f"Número de erros: {erros}")

raiz_quadrada_treino()  # Exemplo de uso
