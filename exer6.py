#6. Um dado material radioativo perde metade de sua massa a cada 50 segundos. 
#Dada a massa inicial em gramas, faça um algoritmo que determine o tempo necessário para que essa massa seja menor que 0,5g.
def radioactive_decay(massa_inicial):
    tempo = 0
    
    while massa_inicial >= 0.5:
        massa_inicial /= 2
        tempo += 50
    
    print(f"Tempo necessário: {tempo} segundos")

radioactive_decay(100)  # Exemplo de uso
