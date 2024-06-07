carros_nomes= ["FIAT UNO", "FERRARI SF90", "MACLAREN P1", "RANGE OVER", "FUSCAO PRETO", "GOL BOLINHA", "GOL QUADRADO", "LAMBORGHINI", "KWID", "HONDA CIVIC", "CELTA", "ASTON MARTIN", "FIAT MOBI", "NISSAN GT-R", "MERCEDES-BENZ AMG-GT", "AUDI R8", "CITROEN C3", "MITSUBISHI ASX", "FIAT SUV", "TESLA MODEL S"]
print (carros_nomes)

carro_nome_desejado= "FIAT UNO"

for carro in carros_nomes:
    if carro == carro_nome_desejado:
        print("carro encontrado!")
        break
    else:
        print("carro nao encontrado!")
        break