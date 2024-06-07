def avaliacao_carro(preco):
    if preco < 10000:
        return "Malestado"
    elif preco < 30000:
        return "Conservado"
    elif preco < 60000:
        return "Seminovo"
    else:
        return "Novo"

carro_nome = input("Escreva o nome do carro que deseja comprar: ")

carro_valor = float(input("Escreva o valor do carro que deseja conhecer: "))

avaliacao = avaliacao_carro(carro_valor)

print("Para o carro", carro_nome + ", o estado é:", avaliacao)