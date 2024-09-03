#25. Foi realizada uma pesquisa de algumas características físicas da população de uma certa região. 
#Foram coletados os seguintes dados de cada habitante:
#Sexo.
#Cor dos olhos (azuis, verdes, castanhos).
#Cor dos cabelos (louros, castanhos, pretos).
#Idade.
#O programa deve determinar e escrever:

#O total de entrevistados.
#O total de homens e o total de mulheres entrevistados.
#A maior e a menor idade.
#A média de idade do conjunto de habitantes.
#A porcentagem de mulheres entre 18 e 35 anos, inclusive, com olhos verdes e cabelos louros.
def population_survey():
    total_people = 0
    total_men = 0
    total_women = 0
    total_age = 0
    women_criteria_count = 0
    max_age = 0
    min_age = float('inf')

    while True:
        sex = input("Sexo (M/F): ").upper()
        eyes = input("Cor dos olhos (azuis, verdes, castanhos): ").lower()
        hair = input("Cor dos cabelos (louros, castanhos, pretos): ").lower()
        age = int(input("Idade: "))

        total_people += 1
        total_age += age

        if sex == 'M':
            total_men += 1
        elif sex == 'F':
            total_women += 1
            if 18 <= age <= 35 and eyes == 'verdes' and hair == 'louros':
                women_criteria_count += 1

        if age > max_age:
            max_age = age
        if age < min_age:
            min_age = age

        continue_survey = input("Deseja continuar? (s/n): ").lower()
        if continue_survey != 's':
            break

    if total_people > 0:
        average_age = total_age / total_people
        women_criteria_percentage = (women_criteria_count / total_people) * 100
    else:
        average_age = 0
        women_criteria_percentage = 0

    print(f"\nTotal de entrevistados: {total_people}")
    print(f"Total de homens: {total_men}")
    print(f"Total de mulheres: {total_women}")
    print(f"Maior idade: {max_age}")
    print(f"Menor idade: {min_age}")
    print(f"Média de idade: {average_age:.2f}")
    print(f"Porcentagem de mulheres com 18 a 35 anos, olhos verdes e cabelos louros: {women_criteria_percentage:.2f}%")

population_survey()  # Exemplo de uso
