#30. Escreva uma função FparaC que receba uma temperatura em graus Fahrenheit e retorne a temperatura em graus Celsius, utilizando a fórmula 
#𝐶=5/9×(𝐹−32)
#Em seguida, faça um programa que, em loop, leia um valor para F da entrada padrão e o converta para C utilizando a função FparaC.
def FparaC(fahrenheit):
    celsius = (5/9) * (fahrenheit - 32)
    return celsius

def loop_conversao_temperatura():
    while True:
        fahrenheit = float(input("\nDigite a temperatura em Fahrenheit (ou digite '999' para sair): "))
        if fahrenheit == 999:
            break
        celsius = FparaC(fahrenheit)
        print(f"{fahrenheit}°F equivale a {celsius:.2f}°C")

loop_conversao_temperatura()
