#24. Para fazer uma pesquisa sobre o consumo de energia elétrica de uma cidade, são fornecidos os seguintes dados:
#Preço do kWh.
#Número de identificação de cada consumidor.
#Quantidade de kWh consumido no mês por cada um.
#Código do tipo de consumidor (residencial, comercial ou industrial).
#A partir desses dados, calcule:

#O total a pagar para cada consumidor.
#O maior e o menor consumo verificado.
#O total de consumo para cada tipo de consumidor (residencial, comercial, industrial).
#A média de consumo para cada tipo de consumidor.
#O total arrecadado pela companhia elétrica.
def electricity_survey():
    consumers = []
    total_consumption = {"residencial": 0, "comercial": 0, "industrial": 0}
    count_consumers = {"residencial": 0, "comercial": 0, "industrial": 0}
    total_revenue = 0
    max_consumption = 0
    min_consumption = float('inf')

    kwh_price = float(input("Digite o preço do kWh: "))

    while True:
        id_consumer = input("Digite o número de identificação do consumidor: ")
        consumption = float(input(f"Digite a quantidade de kWh consumido pelo consumidor {id_consumer}: "))
        consumer_type = input("Digite o tipo de consumidor (residencial, comercial, industrial): ").lower()

        if consumer_type in total_consumption:
            total_consumption[consumer_type] += consumption
            count_consumers[consumer_type] += 1
        else:
            print("Tipo de consumidor inválido.")
            continue

        total_payment = consumption * kwh_price
        total_revenue += total_payment
        consumers.append({"id": id_consumer, "consumption": consumption, "total_payment": total_payment})

        if consumption > max_consumption:
            max_consumption = consumption
        if consumption < min_consumption:
            min_consumption = consumption

        continue_survey = input("Deseja inserir mais um consumidor? (s/n): ").lower()
        if continue_survey != 's':
            break

    print("\nResumo da Pesquisa:")
    for consumer in consumers:
        print(f"Consumidor {consumer['id']}: Consumo: {consumer['consumption']} kWh, Total a pagar: R$ {consumer['total_payment']:.2f}")
    
    print(f"Maior consumo verificado: {max_consumption} kWh")
    print(f"Menor consumo verificado: {min_consumption} kWh")

    for consumer_type, total in total_consumption.items():
        if count_consumers[consumer_type] > 0:
            average_consumption = total / count_consumers[consumer_type]
        else:
            average_consumption = 0
        print(f"Total de consumo {consumer_type}: {total} kWh, Média de consumo: {average_consumption:.2f} kWh")

    print(f"Total arrecadado pela companhia elétrica: R$ {total_revenue:.2f}")

electricity_survey()  # Exemplo de uso
