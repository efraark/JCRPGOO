#17. O número 𝜋 pode ser calculado através da série:
#𝜋=4(1-1/3+1/5-1/7+...)
#Faça um programa para calcular o valor de 𝜋 com precisão de 0,00001 (o programa encerra quando a parcela da série for menor que a precisão).
def calculate_pi(precision=0.00001):
    pi_approx = 0
    denominator = 1
    sign = 1
    term = 1
    i = 0
    
    while abs(term) >= precision:
        term = sign * 4 / denominator
        pi_approx += term
        denominator += 2
        sign *= -1
        i += 1
    
    print(f"Valor aproximado de pi: {pi_approx:.5f}")
    print(f"Número de iterações: {i}")

calculate_pi()  # Exemplo de uso
