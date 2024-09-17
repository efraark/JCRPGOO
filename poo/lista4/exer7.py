#7. Crie uma classe chamada Calendar que represente um calendário anual. Essa classe 
#deve ter métodos para exibir o calendário de um determinado mês, verificar se uma 
#data é feriado e calcular a diferença de dias entre duas datas.
from datetime import date, timedelta

class Calendar:
    holidays = [date(2024, 1, 1), date(2024, 12, 25)]
    
    @staticmethod
    def is_holiday(check_date):
        return check_date in Calendar.holidays
    
    @staticmethod
    def days_between(date1, date2):
        return abs((date2 - date1).days)

# Teste
today = date.today()
new_year = date(2024, 1, 1)
print(Calendar.is_holiday(new_year))
print(Calendar.days_between(today, new_year))

