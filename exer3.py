#3. Em um frigorífico, cada boi é identificado por um cartão que contém seu número e seu peso. 
#Faça um programa que leia os números de identificação e o peso de cada boi e ao final imprima o número de identificação e o peso do boi mais gordo,
#do boi mais magro e o total de peso dos bois do frigorífico.
def cattle_info():
    boi_gordo = {'id': None, 'peso': 0}
    boi_magro = {'id': None, 'peso': float('inf')}
    total_peso = 0
    
    while True:
        id_boi = int(input("Digite o número de identificação do boi (ou 0 para terminar): "))
        if id_boi == 0:
            break
        
        peso_boi = float(input(f"Digite o peso do boi {id_boi}: "))
        total_peso += peso_boi
        
        if peso_boi > boi_gordo['peso']:
            boi_gordo = {'id': id_boi, 'peso': peso_boi}
        
        if peso_boi < boi_magro['peso']:
            boi_magro = {'id': id_boi, 'peso': peso_boi}
    
    if boi_gordo['id'] is not None and boi_magro['id'] is not None:
        print(f"Boi mais gordo: ID {boi_gordo['id']}, Peso {boi_gordo['peso']} kg")
        print(f"Boi mais magro: ID {boi_magro['id']}, Peso {boi_magro['peso']} kg")
        print(f"Peso total dos bois: {total_peso:.2f} kg")
    else:
        print("Nenhum boi foi inserido.")

cattle_info()  # Exemplo de uso
