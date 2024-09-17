#32. A multiplicação entre dois números inteiros pode ser definida como uma repetição da adição de um deles. 
#Escreva uma função que multiplique dois números inteiros utilizando esse método. 
#A seguir, escreva um programa que peça ao usuário um número inteiro e imprima a tabuada para aquele número (de 1 a 10) utilizando a função construída.
def multiplicacao_por_soma(a, b):
    resultado = 0
    for _ in range(abs(b)):
        resultado += a
    return resultado if b >= 0 else -resultado

def tabuada_por_soma():
    numero = int(input("Digite um número inteiro para ver a tabuada: "))
    for i in range(1, 11):
        print(f"{numero} x {i} = {multiplicacao_por_soma(numero, i)}")

tabuada_por_soma()
