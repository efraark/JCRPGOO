#31. Escreva funções para conversões de temperatura:
#CparaF: Faz a conversão de graus Celsius para Fahrenheit.
#CparaK: Faz a conversão de Celsius para Kelvin.
#KparaC: Faz a conversão de Kelvin para Celsius.
#KparaF: Faz a conversão de Kelvin para Fahrenheit (utilize as funções anteriores).
#FparaK: Faz a conversão de Fahrenheit para Kelvin.
#Em seguida, faça um programa que apresente continuamente um menu na tela com todas as opções de conversão que você implementou.
#Uma vez feita a opção, o programa lê do teclado o valor a ser convertido e imprime o resultado.
def CparaF(celsius):
    return (celsius * 9/5) + 32

def CparaK(celsius):
    return celsius + 273.15

def KparaC(kelvin):
    return kelvin - 273.15

def KparaF(kelvin):
    celsius = KparaC(kelvin)
    return CparaF(celsius)

def FparaK(fahrenheit):
    celsius = FparaC(fahrenheit)
    return CparaK(celsius)

def menu_conversoes_temperatura():
    while True:
        print("\nMenu de Conversões de Temperatura:")
        print("1. Celsius para Fahrenheit")
        print("2. Celsius para Kelvin")
        print("3. Kelvin para Celsius")
        print("4. Kelvin para Fahrenheit")
        print("5. Fahrenheit para Kelvin")
        print("6. Sair")
        
        opcao = int(input("Escolha uma opção: "))
        
        if opcao == 1:
            celsius = float(input("Digite a temperatura em Celsius: "))
            print(f"{celsius}°C equivale a {CparaF(celsius):.2f}°F")
        elif opcao == 2:
            celsius = float(input("Digite a temperatura em Celsius: "))
            print(f"{celsius}°C equivale a {CparaK(celsius):.2f}K")
        elif opcao == 3:
            kelvin = float(input("Digite a temperatura em Kelvin: "))
            print(f"{kelvin}K equivale a {KparaC(kelvin):.2f}°C")
        elif opcao == 4:
            kelvin = float(input("Digite a temperatura em Kelvin: "))
            print(f"{kelvin}K equivale a {KparaF(kelvin):.2f}°F")
        elif opcao == 5:
            fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
            print(f"{fahrenheit}°F equivale a {FparaK(fahrenheit):.2f}K")
        elif opcao == 6:
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu_conversoes_temperatura()
