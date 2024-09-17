#Problemas de Avaliação
#1. Elabore um programa que:
#Mostre um menu de opções de conversão entre moedas (1 – dólar americano, 2 – euro, 3 – libra esterlina e 4 – yuan).
#Leia a escolha do usuário e o valor em reais.
#Imprima o valor correspondente na moeda escolhida de acordo com a tabela de conversão abaixo:
#Dólar americano: R$ 3,258
#Euro: R$ 4,095
#Libra esterlina: R$ 4,529
#Yuan: R$ 0,515
def currency_conversion():
    DOLAR = 3.258
    EURO = 4.095
    LIBRA = 4.529
    YUAN = 0.515
    
    print("Menu de conversão:")
    print("1 – Dólar americano")
    print("2 – Euro")
    print("3 – Libra esterlina")
    print("4 – Yuan")
    
    choice = int(input("Escolha uma opção de conversão: "))
    reais = float(input("Digite o valor em R$: "))
    
    if choice == 1:
        converted_value = reais / DOLAR
        print(f"Valor em Dólar americano: ${converted_value:.2f}")
    elif choice == 2:
        converted_value = reais / EURO
        print(f"Valor em Euro: €{converted_value:.2f}")
    elif choice == 3:
        converted_value = reais / LIBRA
        print(f"Valor em Libra esterlina: £{converted_value:.2f}")
    elif choice == 4:
        converted_value = reais / YUAN
        print(f"Valor em Yuan: ¥{converted_value:.2f}")
    else:
        print("Opção inválida.")

currency_conversion()  # Exemplo de uso
