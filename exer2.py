#2. Faça um programa que leia um conjunto de números positivos, sendo o conjunto finalizado quando for digitado um número negativo.
#Ao final, imprima o maior e o menor número lido e a média deles.
def read_numbers():
    numbers = []
    while True:
        number = float(input("Digite um número positivo (ou negativo para parar): "))
        if number < 0:
            break
        numbers.append(number)
    
    if numbers:
        maior = max(numbers)
        menor = min(numbers)
        media = sum(numbers) / len(numbers)
        print(f"Maior número: {maior}")
        print(f"Menor número: {menor}")
        print(f"Média dos números: {media:.2f}")
    else:
        print("Nenhum número foi inserido.")

read_numbers()  # Exemplo de uso
