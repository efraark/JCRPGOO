#10. A convenção de graus Fahrenheit para Celsius é obtida pela fórmula:
#𝐶=5/9×(𝐹−32)
#Escreva um programa que calcule e imprima uma tabela de graus centígrados em função de graus Fahrenheit que variem de 50 a 150, de 5 em 5.
#Utilize constantes simbólicas para indicar o início (50), o fim (150) do intervalo, além do passo (5).
def fahrenheit_to_celsius():
    START = 50
    END = 150
    STEP = 5
    
    print("Tabela de conversão Fahrenheit para Celsius:")
    print("Fahrenheit\tCelsius")
    
    for fahrenheit in range(START, END + 1, STEP):
        celsius = (5/9) * (fahrenheit - 32)
        print(f"{fahrenheit}\t\t{celsius:.2f}")

fahrenheit_to_celsius()  # Exemplo de uso
