#15. Elabore um programa que calcule e mostre a soma dos 10 primeiros termos da série:
#100/0!+99/1!+98/2!+⋯+91/9
import math

def series_factorial_sum():
    total_sum = 0
    numerator = 100
    
    for i in range(10):
        total_sum += numerator / math.factorial(i)
        numerator -= 1
    
    print(f"Soma dos 10 primeiros termos da série: {total_sum:.2f}")

series_factorial_sum()  # Exemplo de uso
