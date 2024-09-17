#7. Crie uma classe Invoice para que uma loja de suprimentos de informática possa 
#utilizá-la para representar a fatura de um item vendido na loja. Uma Invoice deve 
#a quantidade comprada de um item (int) e o preço por item (float). Sua classe deve ter 
#um construtor que inicializa as quatro variáveis de instância. Forneça um método set 
#e um get para cada variável de instância. Forneça também um método chamado que 
#calcula o valor da fatura (multiplica preço por quantidade do item) e retorna o 
#resultado. Se a quantidade de itens passada pelo usuário não for positiva, deve ser 
#configurada como 0. Se o preço do item não for positivo, deve ser configurado como 
#0.0. Teste a classe implementada e seus métodos
class Invoice:
    def __init__(self, invoice_number, description, quantity, price_per_item):
        self.invoice_number = invoice_number
        self.description = description
        self.quantity = max(0, quantity)
        self.price_per_item = max(0.0, price_per_item)

    def calculate_invoice(self):
        return self.quantity * self.price_per_item

# Teste
inv = Invoice("1234", "Teclado", 10, 50.0)
print("Valor da fatura:", inv.calculate_invoice())
