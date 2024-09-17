#3. Crie uma classe Account que representa uma conta bancária. A classe deve fornecer 
#débito não exceda o saldo de Account. Se exceder, o saldo deve ser deixado 
#inalterado e o método deve imprimir uma mensagem que indica “Quantia de débito 
#excedeu o saldo da conta”. Teste a classe implementada e seus métodos
class Account:
    def __init__(self, balance):
        self.balance = balance

    def debit(self, amount):
        if amount > self.balance:
            print("Quantia de débito excedeu o saldo da conta")
        else:
            self.balance -= amount

# Teste
acc = Account(500)
acc.debit(600)
acc.debit(300)
