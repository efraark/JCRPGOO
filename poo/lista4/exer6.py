#6. Implemente uma classe chamada Library que represente uma biblioteca virtual. Essa 
#classe deve permitir cadastrar livros, fazer empréstimos, devolver livros e verificar a 
#disponibilidade de um livro
class Library:
    books = {}

    @classmethod
    def add_book(cls, title):
        cls.books[title] = {'available': True}

    def borrow_book(self, title):
        if title in Library.books and Library.books[title]['available']:
            Library.books[title]['available'] = False
            return True
        return False

    def return_book(self, title):
        if title in Library.books:
            Library.books[title]['available'] = True

# Teste
Library.add_book('Python 101')
library = Library()
if library.borrow_book('Python 101'):
    print('Livro emprestado.')
library.return_book('Python 101')
