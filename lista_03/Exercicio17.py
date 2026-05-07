# 	Escrever um algoritmo que lê 10 valores,
# um de cada vez, e conte quantos deles estão no
# intervalo [10,20] e quantos deles estão fora
# do intervalo, escrevendo estas informações.

intervalo = 0
for i in range(10):
    numero = int(input('Digite um numero: '))
    if numero >= 10 and numero <= 20:
        intervalo += 1
print(f"Valores dentro do intervalo = {intervalo}")
print(f"Valores fora do intervalo = {10 - intervalo}")