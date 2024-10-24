class Supplier(Person):
    def __init__(self, nome, endereco, cpf, rg, telefone, valueCredit, valueDebt):
        super().__init__(nome, endereco, cpf, rg, telefone)
        self.__valueCredit = valueCredit
        self.__valueDebt = valueDebt

    def get_balance(self):
        return self.__valueCredit - self.__valueDebt
