#5. Escreva uma classe Point descrito por coordenadas reais x, y. Crie métodos get e set
#e faça um programa de teste para a sua classe. A seguir, crie e teste os seguintes 
#métodos para a classe Ponto: 
#a. O método que recebe como parâmetros um deslocamento dx e outro dy para 
#movimentar o Ponto.
#b. O método que retorna a distância entre este ponto e outro dado como 
#parâmetro.
#Crie e teste um construtor para a classe Point, que inicialize x e y em 1, mas que 
#também possa receber valores dados
class Point:
    def __init__(self, x=1, y=1):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

# Teste
p1 = Point()
p2 = Point(3, 4)
print("Distância entre os pontos:", p1.distance(p2))
p1.move(2, 3)
print(f"Novo ponto: ({p1.get_x()}, {p1.get_y()})")
