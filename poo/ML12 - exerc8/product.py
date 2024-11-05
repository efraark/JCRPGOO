class Product:
    def __init__(self, name, price, description="Produto de informática"):
        self._name = name
        self._price = price
        self._description = description

    # Métodos getters e setters para name e price
    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_price(self, price):
        self._price = price

    def get_price(self):
        return self._price

    # Método get para descrição
    def get_description(self):
        return self._description


class Mouse(Product):
    def __init__(self, name, price, description, mouse_type):
        super().__init__(name, price, description)
        self._type = mouse_type

    # Método get para retornar a descrição do Mouse
    def get_description(self):
        return f"{self._description} - Tipo: {self._type}"


class Book(Product):
    def __init__(self, name, price, description, author):
        super().__init__(name, price, description)
        self._author = author

    # Método get para retornar a descrição do Book
    def get_description(self):
        return f"{self._description} - Autor: {self._author}"
