from product import Mouse, Book

# Simulação de carrinho de compras com diferentes produtos
def main():
    cart = []

    # Adicionando alguns mouses e livros ao carrinho
    cart.append(Mouse("Mouse Gamer", 99.99, "Mouse ótico, Saída USB. 1.600 dpi", "Óptico"))
    cart.append(Mouse("Mouse Wireless", 149.99, "Mouse sem fio, Saída USB", "Sem fio"))
    cart.append(Book("Python para Iniciantes", 59.90, "Livro sobre programação Python", "João Silva"))
    cart.append(Book("Estruturas de Dados Avançadas", 89.90, "Livro sobre Estruturas de Dados", "Ana Souza"))

    # Exibindo informações de todos os produtos no carrinho
    for product in cart:
        print(f"Produto: {product.get_name()}")
        print(f"Descrição: {product.get_description()}")
        print(f"Preço: R${product.get_price()}\n")

if __name__ == "__main__":
    main()
