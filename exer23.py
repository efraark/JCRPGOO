#23. Em um cinema com capacidade de 50 lugares, foi distribuído um questionário aos espectadores,
#no qual constava a idade e a sua opinião em relação ao filme (ótimo, bom, regular, ruim ou péssimo). 
#Elabore um programa que leia estes dados de até 50 espectadores e calcule:
#A quantidade de respostas ótimo, bom, regular, ruim e péssimo.
#A porcentagem de respostas ótimo, bom, regular, ruim e péssimo.
#A idade do espectador mais velho e do mais novo.
def cinema_survey():
    max_capacity = 50
    opinions = {"ótimo": 0, "bom": 0, "regular": 0, "ruim": 0, "péssimo": 0}
    total_spectators = 0
    oldest = 0
    youngest = float('inf')
    
    while total_spectators < max_capacity:
        age = int(input(f"Espectador {total_spectators + 1} - Idade: "))
        opinion = input("Opinião (ótimo, bom, regular, ruim, péssimo): ").lower()

        if opinion in opinions:
            opinions[opinion] += 1
        else:
            print("Opinião inválida, tente novamente.")
            continue
        
        if age > oldest:
            oldest = age
        if age < youngest:
            youngest = age
        
        total_spectators += 1
        continue_survey = input("Continuar? (s/n): ").lower()
        if continue_survey != 's':
            break
    
    print("\nResultados da pesquisa:")
    for opinion, count in opinions.items():
        percentage = (count / total_spectators) * 100
        print(f"{opinion.capitalize()}: {count} resposta(s) ({percentage:.2f}%)")
    
    print(f"Idade do mais velho: {oldest}")
    print(f"Idade do mais novo: {youngest}")

cinema_survey()  # Exemplo de uso
