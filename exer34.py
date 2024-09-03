#34. Uma equação do segundo grau é escrita 
#𝑎𝑥2+𝑏𝑥+𝑐=0 e sua solução depende dos valores de a, b, e 𝑐. A equação pode ter duas raízes, uma ou nenhuma. 
#Escreva uma função que resolva a equação do segundo grau, retornando o número de raízes encontradas. 
#Os valores dessas raízes devem ser retornados em parâmetros.
import math

def resolver_equacao_segundo_grau(a, b, c):
    discriminante = b**2 - 4*a*c
    if discriminante < 0:
        return 0, None, None
    elif discriminante == 0:
        raiz = -b / (2*a)
        return 1, raiz, None
    else:
        raiz1 = (-b + math.sqrt(discriminante)) / (2*a)
        raiz2 = (-b - math.sqrt(discriminante)) / (2*a)
        return 2, raiz1, raiz2

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

numero_raizes, raiz1, raiz2 = resolver_equacao_segundo_grau(a, b, c)

if numero_raizes == 0:
    print("A equação não possui raízes reais.")
elif numero_raizes == 1:
    print(f"A equação possui uma única raiz: {raiz1:.2f}")
else:
    print(f"A equação possui duas raízes: {raiz1:.2f} e {raiz2:.2f}")
