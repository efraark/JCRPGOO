#11. O volume de uma esfera pode ser calculado pela fórmula:
#𝑉(𝑟)=4/3×𝜋×𝑟3
#onde r é o raio da esfera. 
#Faça um programa que imprima uma tabela de volumes para esferas que tenham raios entre 0 e 15 cm, de 0.5 em 0.5 cm.
import math

def sphere_volume_table():
    print("Raio (cm)\tVolume (cm³)")
    
    raio = 0
    while raio <= 15:
        volume = (4/3) * math.pi * raio**3
        print(f"{raio:.1f}\t\t{volume:.2f}")
        raio += 0.5

sphere_volume_table()  # Exemplo de uso
