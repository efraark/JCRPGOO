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
class NoughtsAndCrosses:
    def __init__(self):
        # Inicializa o tabuleiro 3x3 vazio (' ' representa uma casa vazia)
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'  # Jogador 1 será 'X', Jogador 2 será 'O'
    
    def display_board(self):
        """Exibe o tabuleiro atual."""
        for row in self.board:
            print("|".join(row))
            print("-" * 5)

    def make_move(self, row, col):
        """Realiza o movimento em uma casa vazia."""
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            return True
        else:
            print("Essa casa já está ocupada!")
            return False

    def switch_player(self):
        """Alterna entre os jogadores 'X' e 'O'."""
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        """Verifica se há um vencedor ou se houve um empate."""
        # Verifica linhas, colunas e diagonais
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return self.board[0][i]

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]
        
        # Verifica se há casas vazias
        for row in self.board:
            if ' ' in row:
                return None  # Jogo ainda não terminou

        return "Empate"

    def play_game(self):
        """Executa o loop principal do jogo."""
        while True:
            # Exibe o tabuleiro e solicita a jogada
            self.display_board()
            print(f"Jogador {self.current_player}, é a sua vez.")
            
            # Solicita a jogada
            try:
                row = int(input("Escolha a linha (0, 1 ou 2): "))
                col = int(input("Escolha a coluna (0, 1 ou 2): "))
                if row not in range(3) or col not in range(3):
                    print("Entrada inválida! Tente novamente.")
                    continue
            except ValueError:
                print("Por favor, insira números válidos!")
                continue

            # Tenta realizar o movimento
            if self.make_move(row, col):
                # Verifica se há um vencedor ou empate após o movimento
                winner = self.check_winner()
                if winner:
                    self.display_board()
                    if winner == "Empate":
                        print("O jogo terminou em empate!")
                    else:
                        print(f"Parabéns! Jogador {winner} venceu!")
                    break
                # Alterna entre os jogadores
                self.switch_player()

# Executa o jogo da velha
game = NoughtsAndCrosses()
game.play_game()
