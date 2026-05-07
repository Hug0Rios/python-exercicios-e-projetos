# 	Faça um algoritmo que leia uma quantidade
# não determinada de números positivos. Calcule a
# quantidade de números pares e ímpares, a média
# de valores pares e a média geral dos números
# lidos. O número que encerrará a leitura será
# zero.

qtde_pares = 0
qtde_impares = 0
soma_pares = 0
soma_impares = 0
numero = int(input("Digite um numero: "))
while numero != 0:
    if numero % 2 == 0:
        qtde_pares += 1
        soma_pares += numero
    else:
        qtde_impares += 1
        soma_impares += numero
    numero = int(input("Digite um numero: "))
print(f"Quantidade de pares = {qtde_pares}")
print(f"Quantidade de impares = {qtde_impares}")
print(f"Soma dos pares = {soma_pares}")
print(f"Soma dos impares = {soma_impares}")
if qtde_pares > 0:
    media_pares = soma_pares / qtde_pares
    print(f"Media pares = {media_pares:.2f}")
if qtde_impares > 0:
    media_impares = soma_impares / qtde_impares
    print(f"Media impares = {media_impares:.2f}")
if qtde_pares + qtde_impares > 0:
    media_geral = (soma_pares + soma_impares) / (qtde_pares + qtde_impares)
    print(f"Media geral = {media_geral:.2f}")