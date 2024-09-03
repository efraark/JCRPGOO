#12. Elabore um programa que calcule e mostre o fatorial de um número 𝑁!, sendo que 𝑁 é fornecido pelo usuário.
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

n = int(input("Digite um número para calcular o fatorial: "))
print(f"{n}! = {factorial(n)}")
