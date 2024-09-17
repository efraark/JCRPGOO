class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

class DateFormatter:
    @staticmethod
    def display_date(date):
        print(f"{date.day}/{date.month}/{date.year}")
