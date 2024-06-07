def procurar_carro(carro_nome):
    carros_nomes = ["FIAT UNO", "FERRARI SF90", "MACLAREN P1", "RANGE OVER", "FUSCAO PRETO", "GOL BOLINHA", "GOL QUADRADO", "LAMBORGHINI", "KWID", "HONDA CIVIC", "CELTA", "ASTON MARTIN", "FIAT MOBI", "NISSAN GT-R", "MERCEDES-BENZ AMG-GT", "AUDI R8", "CITROEN C3", "MITSUBISHI ASX", "FIAT SUV", "TESLA MODEL S"]
    
    for carro in carros_nomes:
        if carro == carro_nome:
            return "Carro encontrado"
    
    return "Carro não encontrado"

carro_nome_desejado = "FIAT UNO"
saida = procurar_carro(carro_nome_desejado)
print(saida)