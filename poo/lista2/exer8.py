#8. Crie uma classe chamada Employee que inclui três variáveis de instância: um nome 
#(string), um sobrenome (string) e um salário mensal (float). Sua classe deve ter um 
#construtor que inicializa as três variáveis. Forneça um método get e set para cada 
#variável. Se o salário mensal fornecido pelo usuário não for positivo, configure-o 
#como 0.0. Teste a classe implementada e seus métodos. Crie dois objetos Employee e 
#exiba o salário anual de cada objeto. Depois, dê 10% de aumento para cada 
#empregado e exiba novamente os salários
class Employee:
    def __init__(self, first_name, last_name, monthly_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.monthly_salary = max(0.0, monthly_salary)

    def annual_salary(self):
        return self.monthly_salary * 12

    def give_raise(self, percentage):
        self.monthly_salary += self.monthly_salary * percentage / 100

# Teste
emp = Employee("João", "Silva", 3000)
print("Salário anual:", emp.annual_salary())
emp.give_raise(10)
print("Salário anual após aumento:", emp.annual_salary())
