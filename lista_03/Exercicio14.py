# 	Uma empresa deseja aumentar seus preços
# em 20%. Faça um algoritmo que leia o código e
# o preço de custo de cada produto e calcule o
# preço novo. Calcule também, a média dos preços
# com e sem aumento. Mostre o código e o preço
# novo de cada produto e, no final, as médias. A
# entrada de dados deve terminar quando for lido
# um código de produto negativo.

soma_precos = 0
qtde_produtos = 0
codigo = int(input("Digite o codigo do produto: "))
while codigo >= 0:
    preco = float(input("Digite o preco do produto: "))
    novo_preco = preco * 1.2
    print(f"Produto {codigo}: R${novo_preco:.2f}")
    soma_precos += preco
    qtde_produtos += 1
    codigo = int(input("Digite o codigo do produto: "))
if qtde_produtos > 0:
    media = soma_precos / qtde_produtos
    print(f"Media dos precos: {media:.2f}")
    print(f"Media dos precos com aumento: {media * 1.2:.2f}")