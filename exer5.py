#5. Fazer um programa que calcule e escreva o número de grãos de milho que podem ser colocados em um tabuleiro de xadrez, 
#colocando 1 no primeiro quadro e nos quadros seguintes o dobro do quadro anterior.
def calculate_grains():
    grains = 1
    total_grains = 1
    
    for i in range(2, 65):
        grains *= 2
        total_grains += grains
    
    print(f"Total de grãos no tabuleiro: {total_grains}")

calculate_grains()  # Exemplo de uso
