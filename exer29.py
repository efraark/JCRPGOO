#29. Escreva uma função que imprima seus dados pessoais: nome completo, endereço, telefone e e-mail.
#E escreva uma função que imprima seus dados profissionais: nome, endereço e telefone da empresa, função, salário e data de admissão.
#Em seguida, faça um programa que apresente continuamente (em loop) um menu com as seguintes opções:
#Imprimir dados pessoais.
#Imprimir dados profissionais.
#Sair.
def dados_pessoais():
    print("\nDados Pessoais:")
    print("Nome: Rafael Rodrigues dos Santos")
    print("Endereço: Jacareí, SP, Brasil")
    print("Telefone: +55 12 98853-4870")
    print("E-mail: rafa.275rrs@gmail.com")

def dados_profissionais():
    print("\nDados Profissionais:")
    print("Empresa: IFSP")
    print("Endereço da empresa: Jacareí, SP, Brasil")
    print("Telefone da empresa: +55 12 3456-7890")
    print("Função: Analista de Sistemas")
    print("Salário: R$ 4000,00")
    print("Data de admissão: 01/08/2020")

def menu():
    while True:
        print("\nMenu:")
        print("1. Imprimir dados pessoais")
        print("2. Imprimir dados profissionais")
        print("3. Sair")
        escolha = int(input("Escolha uma opção: "))
        
        if escolha == 1:
            dados_pessoais()
        elif escolha == 2:
            dados_profissionais()
        elif escolha == 3:
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()
