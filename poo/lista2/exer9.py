#9. Crie uma classe chamada Date que inclui três variáveis de instância: dia (int), mês 
#(int) e ano (int). Sua classe deve ter um construtor que inicializa as três variáveis de 
#instância e assume que os valores fornecidos são corretos. Forneça um método get e 
#um set para cada variável. Forneça um método que exibe o dia, o mês e o ano 
#separados por barras “/”. Teste a classe implementada e seus métodos
class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def display_date(self):
        print(f"{self.day}/{self.month}/{self.year}")

# Teste
date = Date(15, 9, 2024)
date.display_date()
