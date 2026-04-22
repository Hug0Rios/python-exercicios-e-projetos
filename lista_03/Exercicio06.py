#6 Construir um algoritmo que calcule a média aritmética de vários valores inteiros
#positivos, digitados pelo usuário. O final da leitura acontecerá quando for lido um
#valor negativo
soma = 0
quantidade = 0
valores = int(input("Digite um valor inteiro positivo: "))
while valores >= 0:
    soma = soma + valores
    quantidade = quantidade + 1
    valores = int(input("Digite um valor inteiro positivo: "))
if quantidade > 0:
    media = soma / quantidade
    print(f"Media = {media:.2f}")