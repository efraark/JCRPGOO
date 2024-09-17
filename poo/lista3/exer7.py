class Employee:
    def __init__(self, first_name, last_name, monthly_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.monthly_salary = max(0.0, monthly_salary)

class SalaryCalculator:
    @staticmethod
    def annual_salary(employee):
        return employee.monthly_salary * 12

    @staticmethod
    def give_raise(employee, percentage):
        employee.monthly_salary += employee.monthly_salary * percentage / 100
