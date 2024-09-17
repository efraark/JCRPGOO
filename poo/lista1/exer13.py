#13. A série de Fibonacci é gerada da seguinte forma: os dois primeiros termos são 1,
#e os demais são dados pela soma dos dois anteriores. 
#Faça um programa que imprima os "n" primeiros termos da série, sendo "n" dado pelo usuário.
def fibonacci(n):
    a, b = 1, 1
    print(a, b, end=" ")
    
    for _ in range(2, n):
        a, b = b, a + b
        print(b, end=" ")
    print()

n = int(input("Digite o número de termos da série de Fibonacci: "))
fibonacci(n)
