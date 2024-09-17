#9. Crie uma classe chamada Invoice que possa ser utilizado por uma loja de 
#suprimentos de informática para representar uma fatura de um item vendido na loja. 
#Uma fatura deve incluir as seguintes informações como atributos:
#• o número do item faturado,
#• a quantidade comprada do item e
#• o preço unitário do item.
#Sua classe deve ter um construtor que inicialize os quatro atributos. Se a quantidade 
#não for positiva, ela deve ser configurada como 0. Se o preço por item não for 
#positivo ele deve ser configurado como 0.0. Forneça um método set e um método get 
#para cada variável de instância. Além disso, forneça um método chamado que calcula 
#o valor da fatura (isso é, multiplica a quantidade pelo preço por item) e depois retorna 
#o valor real. Escreva um aplicativo de teste que demonstra as capacidades da classe 
#Invoice.
class Invoice:
    def __init__(self, item_number, description, quantity, price_per_item):
        self.item_number = item_number
        self.description = description
        self.quantity = max(0, quantity)
        self.price_per_item = max(0.0, price_per_item)

    def calculate_total(self):
        return self.quantity * self.price_per_item

# Teste
invoice = Invoice('123', 'Teclado', 3, 50)
print(f"Total da fatura: {invoice.calculate_total()}")
