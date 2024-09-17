#10. Escreva um programa completo para jogar o jogo da velha. Para tanto crie uma 
#classe NoughtsAndCrosses (jogo da velha):
#• a classe deve conter como dados privados um array bidimensional 3x3 para 
#casa na grade (vazia, jogador 1 ou jogador 2)
#• o construtor deve inicializar a grade como vazia
#• forneça um método para exibir a grade
#• permita dois jogadores humanos
#• forneça um método para jogar o jogo; todo movimento deve ocorrer em uma 
#casa vazia; depois de cada movimento, determine se houve uma derrota ou um 
#empate
from enum import Enum

class Player(Enum):
    EMPTY = 0
    PLAYER_1 = 1
    PLAYER_2 = 2

class NoughtsAndCrosses:
    def __init__(self):
        self.board = [[Player.EMPTY for _ in range(3)] for _ in range(3)]
    
    def display_board(self):
        for row in self.board:
            print([cell.name for cell in row])
    
    def make_move(self, row, col, player):
        if self.board[row][col] == Player.EMPTY:
            self.board[row][col] = player
            return True
        return False

# Teste
game = NoughtsAndCrosses()
game.display_board()
game.make_move(0, 0, Player.PLAYER_1)
game.display_board()
