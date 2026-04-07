# 2.	Escreva um algoritmo que leia 20
# valores e encontre o maior e o menor deles.
# Mostre o resultado.
maior = int(input("Digite um numero: "))
menor = maior
for i in range(4):
    valor = int(input("Digite um numero: "))
    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor
print("O maior Numero digitado foi:",maior)
print("O menor Numero digitado foi:",menor)