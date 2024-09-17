#8. Numa universidade, o sistema de avaliação é o seguinte: para passar direto, o aluno precisa ter média do período (mp) igual ou superior a 7 pontos.
#Caso contrário, o aluno será submetido a exame final, sendo a sua média final (mf) calculada pela seguinte fórmula:
#mf=0.6×mp+0.4×ne
#onde ne é a nota do exame. Essa média final deverá ser igual ou superior a 5 pontos para que o aluno seja aprovado.
#Faça um programa que leia do usuário o número de créditos da disciplina, as notas dos créditos, 
#e se necessário calcule a nota que o aluno precisa tirar no exame final para ser aprovado. 
#Se antes de terminar todos os créditos o aluno já estiver aprovado, avise isso a ele e encerre a leitura de notas (utilize aqui um comando break).
def calculate_final_grade():
    num_credits = int(input("Digite o número de créditos da disciplina: "))
    total_grades = 0
    
    for i in range(num_credits):
        grade = float(input(f"Digite a nota do crédito {i+1}: "))
        total_grades += grade
        mp = total_grades / (i + 1)
        
        if mp >= 7:
            print("Aluno aprovado diretamente!")
            return
    
    print(f"Média do período: {mp:.2f}")
    
    if mp < 7:
        ne = float(input("Digite a nota do exame final: "))
        mf = 0.6 * mp + 0.4 * ne
        if mf >= 5:
            print(f"Aprovado com média final: {mf:.2f}")
        else:
            print(f"Reprovado com média final: {mf:.2f}")

calculate_final_grade()  # Exemplo de uso
