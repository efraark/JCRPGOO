#33. O valor aproximado de π pode ser calculado a partir da série:
#𝜋=4(1−1/3+1/5−1/7+… )

#Escreva uma função que calcule o valor de π, com precisão dada como parâmetro.
def calcular_pi(precisao):
    pi_aprox = 0
    sinal = 1
    denominador = 1
    termo = 4 / denominador
    
    while abs(termo) > precisao:
        pi_aprox += termo
        denominador += 2
        sinal *= -1
        termo = sinal * (4 / denominador)
    
    return pi_aprox

precisao = float(input("Digite a precisão desejada para o cálculo de pi: "))
pi_calculado = calcular_pi(precisao)
print(f"Valor aproximado de pi com precisão {precisao}: {pi_calculado:.6f}")
