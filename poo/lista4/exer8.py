#8. Implemente uma classe chamada GuessingGame que represente um jogo de 
#adivinhação. Essa classe deve gerar um número aleatório, permitir que o jogador faça 
#palpites e informar se o palpite está correto, informando se é maior ou menor que o 
#número gerado.
import random

class GuessingGame:
    @staticmethod
    def generate_number():
        return random.randint(1, 100)

    @staticmethod
    def check_guess(number, guess):
        if guess < number:
            return "Menor"
        elif guess > number:
            return "Maior"
        return "Correto"

# Teste
number = GuessingGame.generate_number()
guess = 50  # Exemplo de palpite
result = GuessingGame.check_guess(number, guess)
print(result)
