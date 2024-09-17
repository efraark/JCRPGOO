#11. Implemente a classe Bank considerando os métodos listados abaixo e acrescentando 
#métodos que considerar conveniente
class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.name] = account

    def debit(self, name, amount):
        if name in self.accounts:
            self.accounts[name].debit(amount)
        else:
            print(f"Conta {name} não encontrada")

# Teste
bank = Bank()
acc1 = Account("Rafael", 1000)
bank.add_account(acc1)
bank.debit("Rafael", 500)
acc1.displayAccount()
