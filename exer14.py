#14. Construa um programa que calcule e mostre a soma dos 30 primeiros termos da série:
#450/10+445/11+440/12+…
def series_sum():
    numerator = 450
    denominator = 10
    total_sum = 0
    
    for _ in range(30):
        total_sum += numerator / denominator
        numerator -= 5
        denominator += 1
    
    print(f"Soma dos 30 primeiros termos da série: {total_sum:.2f}")

series_sum()  # Exemplo de uso
