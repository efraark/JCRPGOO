#19. Faça um programa didático para estudo de tabuadas de 1 até 10, onde:
#A criança escolhe a tabuada a ser estudada.
#O programa gera um número aleatório e pergunta à criança qual o valor dele multiplicado pela tabuada escolhida. 
#Se a criança errar, o programa pergunta novamente, se acertar o programa pergunta à criança se ela deseja continuar respondendo.
#Ao final, o programa deve imprimir o número de perguntas respondidas, o número de acertos e o número de erros cometidos pela criança.
import random

def tabuada_treino():
    tabuada = int(input("Escolha a tabuada (1 a 10): "))
    acertos = 0
    erros = 0
    total_perguntas = 0

    while True:
        numero = random.randint(1, 10)
        resposta_correta = tabuada * numero
        resposta = int(input(f"Quanto é {tabuada} x {numero}? "))

        if resposta == resposta_correta:
            print("Correto!")
            acertos += 1
        else:
            print(f"Errado! A resposta correta é {resposta_correta}.")
            erros += 1

        total_perguntas += 1
        continuar = input("Deseja continuar? (s/n): ").lower()
        if continuar != 's':
            break

    print(f"Número de perguntas respondidas: {total_perguntas}")
    print(f"Número de acertos: {acertos}")
    print(f"Número de erros: {erros}")

tabuada_treino()  # Exemplo de uso
