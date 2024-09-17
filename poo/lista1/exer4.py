#4. Desejando obter a média aritmética das idades dos alunos do curso de Odontologia, construa um programa que leia, 
#calcule e mostre a média aritmética das idades. 
#O programa deve ser encerrado quando for lida uma idade igual a zero e deve rejeitar idades negativas, pedindo que o usuário redigite.
def average_age():
    total_age = 0
    count = 0
    
    while True:
        age = int(input("Digite a idade do aluno (ou 0 para terminar): "))
        
        if age == 0:
            break
        elif age < 0:
            print("Idade inválida. Digite uma idade positiva.")
        else:
            total_age += age
            count += 1
    
    if count > 0:
        average = total_age / count
        print(f"Média de idade: {average:.2f}")
    else:
        print("Nenhuma idade válida foi inserida.")

average_age()  # Exemplo de uso
