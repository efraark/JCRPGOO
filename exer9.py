#9. Em um sistema de ensino experimental em 10 níveis, o aluno é submetido a exercícios até que ele alcance a nota máxima (100 pontos) em cada nível,
#para só então passar ao nível seguinte. Entretanto, se após 5 tentativas no mesmo nível o aluno obtiver menos de 300 pontos acumulados,
#ele retorna ao nível anterior. 
#Caso contrário, ele permanece no mesmo nível, zerando novamente os pontos acumulados. Faça um programa que compute o progresso do aluno.
def compute_student_progress():
    level = 1
    while level <= 10:
        points = 0
        attempts = 0
        
        while points < 100 and attempts < 5:
            score = int(input(f"Digite a pontuação da tentativa {attempts+1} no nível {level}: "))
            points += score
            attempts += 1
        
        if points >= 100:
            print(f"Parabéns! Você passou para o nível {level + 1}.")
            level += 1
        elif points < 300:
            print("Você acumulou menos de 300 pontos e voltará para o nível anterior.")
            level = max(1, level - 1)
        else:
            print("Você permanece no mesmo nível e suas pontuações foram zeradas.")
        
compute_student_progress()  # Exemplo de uso
