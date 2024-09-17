#1. Crie uma classe chamada VirtualStore que represente uma plataforma de vendas 
#online. Essa classe deve ter funcionalidades para cadastrar produtos, gerar carrinho 
#de compras, aplicar descontos e calcular o valor total da compra
class VirtualStore:
    products = {}

    @classmethod
    def add_product(cls, name, price):
        cls.products[name] = price

    @staticmethod
    def calculate_discount(total, discount_percent):
        return total - (total * discount_percent / 100)

    def __init__(self):
        self.cart = []

    def add_to_cart(self, product_name):
        if product_name in self.products:
            self.cart.append(self.products[product_name])

    def calculate_total(self):
        return sum(self.cart)

# Teste
VirtualStore.add_product('Laptop', 2000)
VirtualStore.add_product('Mouse', 50)

store = VirtualStore()
store.add_to_cart('Laptop')
store.add_to_cart('Mouse')

total = store.calculate_total()
discounted_total = VirtualStore.calculate_discount(total, 10)
print(f"Total com desconto: {discounted_total}")
