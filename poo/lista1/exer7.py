#7. Para fazer o balanço mensal de um armazém, faça um programa que leia para um número qualquer de mercadorias diferentes o preço de custo,
#o preço de venda e a quantidade vendida. A partir desses dados, imprima: o número total de mercadorias diferentes lidas,
#o faturamento total e o lucro total do armazém.
def warehouse_balance():
    total_mercadorias = 0
    faturamento_total = 0
    lucro_total = 0
    
    while True:
        preco_custo = float(input("Digite o preço de custo da mercadoria (ou 0 para sair): "))
        if preco_custo == 0:
            break
        
        preco_venda = float(input("Digite o preço de venda da mercadoria: "))
        quantidade_vendida = int(input("Digite a quantidade vendida: "))
        
        total_mercadorias += 1
        faturamento_total += preco_venda * quantidade_vendida
        lucro_total += (preco_venda - preco_custo) * quantidade_vendida
    
    print(f"Número total de mercadorias: {total_mercadorias}")
    print(f"Faturamento total: R$ {faturamento_total:.2f}")
    print(f"Lucro total: R$ {lucro_total:.2f}")

warehouse_balance()  # Exemplo de uso
