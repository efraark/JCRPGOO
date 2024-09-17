#Escreva uma classe chamada Vehicle que possua campos para a velocidade atual em 
#km/h, a direção em graus dos pneus e o nome do proprietário. Crie métodos de 
#acesso e impressão para esta classe e faça um programa de teste
class Vehicle:
    def __init__(self, speed, tire_direction, owner):
        self.speed = speed
        self.tire_direction = tire_direction
        self.owner = owner
    
    def print_info(self):
        print(f"Proprietário: {self.owner}, Velocidade: {self.speed} km/h, Direção dos pneus: {self.tire_direction} graus")
    
    def get_speed(self):
        return self.speed
    
    def get_tire_direction(self):
        return self.tire_direction
    
    def get_owner(self):
        return self.owner

# Teste
v = Vehicle(100, 45, "João")
v.print_info()
