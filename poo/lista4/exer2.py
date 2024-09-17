#2. Implemente uma classe chamada Schedule que represente uma agenda telefônica. 
#Essa classe deve permitir adicionar, editar e remover contatos, além de buscar por 
#contatos a partir de um nome ou número de telefone
class Schedule:
    contacts = {}

    @classmethod
    def add_contact(cls, name, phone):
        cls.contacts[name] = phone

    @classmethod
    def edit_contact(cls, name, new_phone):
        if name in cls.contacts:
            cls.contacts[name] = new_phone

    @classmethod
    def remove_contact(cls, name):
        if name in cls.contacts:
            del cls.contacts[name]

    @classmethod
    def search_contact(cls, search_term):
        for name, phone in cls.contacts.items():
            if search_term in name or search_term in phone:
                print(f"{name}: {phone}")

# Teste
Schedule.add_contact('Rafael', '123456789')
Schedule.add_contact('Carlos', '987654321')
Schedule.search_contact('Rafael')
