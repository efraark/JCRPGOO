class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.name] = account

class BankTransaction:
    @staticmethod
    def debit(bank, name, amount):
        if name in bank.accounts:
            bank.accounts[name].debit(amount)
        else:
            print(f"Conta {name} não encontrada")
