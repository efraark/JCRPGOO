class Invoice:
    def __init__(self, invoice_number, description, quantity, price_per_item):
        self.invoice_number = invoice_number
        self.description = description
        self.quantity = max(0, quantity)
        self.price_per_item = max(0.0, price_per_item)

class InvoiceCalculator:
    @staticmethod
    def calculate(invoice):
        return invoice.quantity * invoice.price_per_item
