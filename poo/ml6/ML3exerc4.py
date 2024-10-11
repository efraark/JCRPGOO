class Account:
    def __init__(self, name, balance):
        self.name = name
        if balance >= 0:
            self.balance = balance
        else:
            raise ValueError("O saldo inicial não pode ser negativo.")
    
    def debit(self, amount):
        if amount > self.balance:
            print("Quantia de débito excedeu o saldo da conta.")
        else:
            self.balance -= amount
            print(f"R${amount} debitados com sucesso.")
    
    def get_balance(self):
        return self.balance
    
    def displayAccount(self):
        print(f"Nome: {self.name}, Saldo: R${self.balance}")


class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []
    
    def add_account(self, account):
        self.accounts.append(account)
        print(f"Conta de {account.name} adicionada ao banco {self.name}.")
    
    def display_all_accounts(self):
        print(f"Contas no banco {self.name}:")
        for account in self.accounts:
            account.displayAccount()

# Testando a Associação entre Bank e Account
if __name__ == "__main__":
    # Criando instâncias de Account
    account1 = Account("Rafael Rodrigues", 1000)
    account2 = Account("Maria Silva", 1500)

    # Criando uma instância de Bank
    bank = Bank("Banco Central")

    # Associando as contas ao banco
    bank.add_account(account1)
    bank.add_account(account2)

    # Exibindo todas as contas associadas ao banco
    bank.display_all_accounts()

    # Testando operações em uma conta
    account1.debit(200)
    account1.displayAccount()
