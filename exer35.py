#35. Faça um programa que apresente na tela um menu com as seguintes opções:
#Converter um ângulo em graus para radiano.
#Calcular o seno de um ângulo.
#Calcular o valor de π.
#Resolver uma equação do segundo grau.
#Sair.
#Depois de feita a opção, o programa deve chamar uma função que leia do usuário os parâmetros necessários para o cálculo escolhido e,
#em seguida, usar uma das funções implementadas anteriormente.
import math

def graus_para_radianos(graus):
    return graus * math.pi / 180

def seno_angulo(graus):
    radianos = graus_para_radianos(graus)
    return math.sin(radianos)

def menu_principal():
    while True:
        print("\nMenu de Opcoes:")
        print("1. Converter um angulo em graus para radiano")
        print("2. Calcular o seno de um angulo")
        print("3. Calcular o valor de pi")
        print("4. Resolver uma equacao do segundo grau")
        print("5. Sair")
        
        opcao = int(input("Escolha uma opcao: "))
        
        if opcao == 1:
            graus = float(input("Digite o angulo em graus: "))
            radianos = graus_para_radianos(graus)
            print(f"{graus} graus equivalem a {radianos:.4f} radianos.")
        elif opcao == 2:
            graus = float(input("Digite o angulo em graus: "))
            seno = seno_angulo(graus)
            print(f"O seno de {graus} graus e {seno:.4f}")
        elif opcao == 3:
            precisao = float(input("Digite a precisão desejada para o calculo de pi: "))
            pi_calculado = calcular_pi(precisao)
            print(f"Valor aproximado de pi com precisão {precisao}: {pi_calculado:.6f}")
        elif opcao == 4:
            a = float(input("Digite o valor de a: "))
            b = float(input("Digite o valor de b: "))
            c = float(input("Digite o valor de c: "))
            numero_raizes, raiz1, raiz2 = resolver_equacao_segundo_grau(a, b, c)
            if numero_raizes == 0:
                print("A equação não possui raizes reais.")
            elif numero_raizes == 1:
                print(f"A equação possui uma unica raiz: {raiz1:.2f}")
            else:
                print(f"A equação possui duas raizes: {raiz1:.2f} e {raiz2:.2f}")
        elif opcao == 5:
            print("Saindo...")
            break
        else:
            print("Opção invalida. Tente novamente.")

menu_principal()
