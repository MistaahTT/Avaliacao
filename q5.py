carro_nome= input("escreva o nome do carro que deseja comprar: ")

carro_valor= float(input("escreva o valor do carro que deseja conhecer: "))

print("voce deseja saber o valor do carro: ", carro_valor)

if carro_valor < 10000:
    print("Para o carro", carro_nome + ", o estado é: malestado")
elif carro_valor < 30000:
    print("Para o carro", carro_nome + ", o estado é: conservado")
elif carro_valor < 60000:
    print("Para o carro", carro_nome + ", o estado é: seminovo")
else:
    print("Para o carro", carro_nome + ", o estado é: novo")