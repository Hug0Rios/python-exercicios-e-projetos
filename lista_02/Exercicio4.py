#4.	Ler um número inteiro e informar se o número lido é par ou impar.
Numero= int (input("Digite um Número: "))
Divisao= Numero//2
resto = Numero%2
resultado=resto
if (resto == 0):
    print("Numero Par")
else :
    print("Numero Impar")