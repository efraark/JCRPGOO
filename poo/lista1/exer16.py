#16 - sendo Sn = 1-1/2+1/3-1/4+...,construa um programa que leia N calcule e mostre o valor da serie Sn.
def alternating_series(n):
    total_sum = 0
    
    for i in range(1, n + 1):
        if i % 2 == 0:
            total_sum -= 1 / i
        else:
            total_sum += 1 / i
    
    print(f"Valor da série S({n}) = {total_sum:.4f}")

n = int(input("Digite o valor de N: "))
alternating_series(n)
