# 3. Faça um algoritmo que lê um valor N inteiro e positivo e que calcula e escreve o
#fatorial de N (N!).
valor = int(input("Digite um numero: "))
resultado = 1
if valor <0:
    print ("O valor deve ser positivo")
else:
    for i in range(1, valor + 1):
        resultado *= i
    print ( "O fatorial do número é: " , resultado)
