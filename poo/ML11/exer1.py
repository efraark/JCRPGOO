class Person:
    def __init__(self, nome, endereco, cpf, rg, telefone):
        self.__nome = nome
        self.__endereco = endereco
        self.__cpf = cpf
        self.__rg = rg
        self.__telefone = telefone

    # Getters e Setters
    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome
    # Outros getters e setters para os atributos encapsulados...
