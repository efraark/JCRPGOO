#3. Crie uma classe chamada VendingMachine que simule uma máquina de venda de 
#produtos. Essa classe deve permitir cadastrar produtos, selecionar um produto para 
#compra, inserir dinheiro, retornar o troco e exibir o estoque disponível
class VendingMachine:
    stock = {}

    @classmethod
    def add_product(cls, name, price, quantity):
        cls.stock[name] = {'price': price, 'quantity': quantity}

    @staticmethod
    def calculate_change(money_inserted, price):
        return money_inserted - price

    def select_product(self, product_name):
        if product_name in self.stock and self.stock[product_name]['quantity'] > 0:
            return self.stock[product_name]['price']
        return None

    def update_stock(self, product_name):
        if product_name in self.stock:
            self.stock[product_name]['quantity'] -= 1

# Teste
VendingMachine.add_product('Coca-Cola', 2.5, 10)
machine = VendingMachine()
price = machine.select_product('Coca-Cola')
if price:
    change = VendingMachine.calculate_change(5, price)
    machine.update_stock('Coca-Cola')
    print(f"Troco: {change}")
