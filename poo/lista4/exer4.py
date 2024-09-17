#4. Implemente uma classe chamada CardsGame que represente um jogo de cartas 
#simples, como o Uno. Essa classe deve ter métodos para embaralhar as cartas, 
#distribuir as cartas aos jogadores e permitir jogadas
import random

class CardsGame:
    deck = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

    @staticmethod
    def shuffle_deck():
        random.shuffle(CardsGame.deck)

    @staticmethod
    def deal_cards(num_players):
        hand_size = len(CardsGame.deck) // num_players
        return [CardsGame.deck[i * hand_size:(i + 1) * hand_size] for i in range(num_players)]

# Teste
CardsGame.shuffle_deck()
players_hands = CardsGame.deal_cards(2)
print(players_hands)
