#18. O número 3025 possui a interessante característica:
#30+25=55 e 552=3025
#Faça um programa que procure todos os números de 4 algarismos que possuem essa característica.
def find_special_numbers():
    for num in range(1000, 10000):
        left = num // 100
        right = num % 100
        if (left + right) ** 2 == num:
            print(num)

find_special_numbers()  # Exemplo de uso
