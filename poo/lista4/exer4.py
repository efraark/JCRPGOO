#4. Implemente uma classe chamada CardsGame que represente um jogo de cartas 
#simples, como o Uno. Essa classe deve ter métodos para embaralhar as cartas, 
#distribuir as cartas aos jogadores e permitir jogadas
import random

class Card:
    def __init__(self, color, value):
        self.color = color
        self.value = value

    def __str__(self):
        return f"{self.color} {self.value}"

    def matches(self, other_card):
        """Verifica se a carta combina com a outra (mesma cor ou valor)"""
        return self.color == other_card.color or self.value == other_card.value


class CardsGame:
    colors = ['Red', 'Green', 'Blue', 'Yellow']
    values = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'Skip', 'Reverse', 'Draw Two']

    def __init__(self, num_players):
        self.deck = self.create_deck()
        self.players = [[] for _ in range(num_players)]  # Cada jogador tem uma lista de cartas
        self.discard_pile = []  # Pilha de descarte
        self.current_player = 0  # Jogador inicial
        self.num_players = num_players

    def create_deck(self):
        """Cria um baralho com 108 cartas (4 cores e valores de 0 a 9 + especiais)"""
        deck = [Card(color, value) for color in self.colors for value in self.values] * 2  # Duas cópias de cada carta
        random.shuffle(deck)
        return deck

    def shuffle_deck(self):
        """Embaralha o baralho"""
        random.shuffle(self.deck)

    def deal_cards(self):
        """Distribui 7 cartas para cada jogador"""
        for player_hand in self.players:
            for _ in range(7):
                player_hand.append(self.deck.pop())

    def play_turn(self, player_index, card_index):
        """Permite que o jogador jogue uma carta, se for válida"""
        if card_index < len(self.players[player_index]):
            selected_card = self.players[player_index][card_index]
            if selected_card.matches(self.discard_pile[-1]):
                self.players[player_index].pop(card_index)  # Remove a carta da mão
                self.discard_pile.append(selected_card)  # Coloca a carta na pilha de descarte
                print(f"Jogador {player_index + 1} jogou {selected_card}")
                self.next_player()
            else:
                print("Carta inválida! Deve ter a mesma cor ou valor da carta no topo.")
        else:
            print("Índice de carta inválido!")

    def next_player(self):
        """Passa a vez para o próximo jogador"""
        self.current_player = (self.current_player + 1) % self.num_players

    def draw_card(self, player_index):
        """Jogador compra uma carta"""
        if self.deck:
            self.players[player_index].append(self.deck.pop())

    def display_player_hand(self, player_index):
        """Exibe as cartas na mão do jogador"""
        print(f"Jogador {player_index + 1} - Cartas na mão:")
        for i, card in enumerate(self.players[player_index]):
            print(f"{i}: {card}")

    def display_top_card(self):
        """Exibe a carta no topo da pilha de descarte"""
        if self.discard_pile:
            print(f"Carta no topo: {self.discard_pile[-1]}")

    def start_game(self):
        """Inicia o jogo colocando a primeira carta na pilha de descarte"""
        self.discard_pile.append(self.deck.pop())
        print(f"Iniciando com a carta: {self.discard_pile[-1]}")

# Teste
num_players = 2
game = CardsGame(num_players)

# Embaralhar o baralho, distribuir cartas e iniciar o jogo
game.shuffle_deck()
game.deal_cards()
game.start_game()

# Loop para o jogador escolher cartas
for _ in range(5):  # Simula 5 jogadas para fins de teste
    current_player = game.current_player
    game.display_player_hand(current_player)
    game.display_top_card()

    # Jogador escolhe a carta ou compra uma carta
    try:
        card_index = int(input(f"Jogador {current_player + 1}, escolha o índice da carta a ser jogada (ou -1 para comprar uma carta): "))
        if card_index == -1:
            game.draw_card(current_player)
            print("Carta comprada.")
        else:
            game.play_turn(current_player, card_index)
    except ValueError:
        print("Entrada inválida! Por favor, insira um número.")
