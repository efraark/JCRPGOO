class Account:
    def __init__(self, balance):
        self.balance = balance

    def debit(self, amount):
        if amount > self.balance:
            return False
        self.balance -= amount
        return True

class AccountErrorReporter:
    @staticmethod
    def report_debit_error():
        print("Quantia de débito excedeu o saldo da conta")
