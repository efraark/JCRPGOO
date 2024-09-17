#27. O custo de produção de um livro é constituído dos custos por página, mais o custo de encadernação,
#além do custo fixo. O custo por página impressa é de R$ 0,03, o custo fixo é de R$ 4397,00 e o custo de encadernação depende de cada livro,
#conforme a tabela:
#Encadernação simples: R$ 4,30
#Encadernação especial: R$ 7,80
#Encadernação luxo: R$ 10,50
#Faça um programa que leia o número de páginas, o tipo de encadernação e o número de vendas previstas (número de cópias) e:

#Calcule o preço mínimo de cada livro para cobrir os custos de produção.
#Calcule o preço de venda para que a editora tenha um lucro de 20%.
#Imprima o total de livros analisados, o preço médio de venda, o preço de venda do livro mais barato e o mais caro.
def book_cost():
    COST_PER_PAGE = 0.03
    FIXED_COST = 4397.00
    encadernacao_types = {"simples": 4.30, "especial": 7.80, "luxo": 10.50}
    
    total_books = 0
    total_sale_price = 0
    min_sale_price = float('inf')
    max_sale_price = 0

    while True:
        num_pages = int(input("Digite o número de páginas do livro (ou 0 para sair): "))
        if num_pages == 0:
            break

        encadernacao = input("Digite o tipo de encadernação (simples, especial, luxo): ").lower()
        if encadernacao not in encadernacao_types:
            print("Tipo de encadernação inválido.")
            continue

        num_copies = int(input("Digite o número de vendas previstas (cópias): "))

        # Cálculo do custo de produção
        production_cost = (num_pages * COST_PER_PAGE + encadernacao_types[encadernacao]) * num_copies + FIXED_COST
        sale_price_min = production_cost / num_copies
        sale_price_with_profit = sale_price_min * 1.20

        print(f"Preço mínimo do livro para cobrir os custos: R$ {sale_price_min:.2f}")
        print(f"Preço de venda para 20% de lucro: R$ {sale_price_with_profit:.2f}\n")

        total_books += 1
        total_sale_price += sale_price_with_profit
        if sale_price_with_profit < min_sale_price:
            min_sale_price = sale_price_with_profit
        if sale_price_with_profit > max_sale_price:
            max_sale_price = sale_price_with_profit

    if total_books > 0:
        avg_sale_price = total_sale_price / total_books
        print(f"Total de livros analisados: {total_books}")
        print(f"Preço médio de venda: R$ {avg_sale_price:.2f}")
        print(f"Preço de venda do livro mais barato: R$ {min_sale_price:.2f}")
        print(f"Preço de venda do livro mais caro: R$ {max_sale_price:.2f}")
    else:
        print("Nenhum livro foi analisado.")

book_cost()  # Exemplo de uso
