#Escrever um algoritmo que leia uma variável n e calcule a tabuada de 1 até n.
#Mostre a tabuada na forma:
#1 x n = n
#2 x n = 2n
#3 x n = 3n
#...............
#n x n = n2
z = 0
y = 0
numero = int(input("Você quer a tabuada de qual numero: "))
if numero <= 0:
    print("Valor invalido!")
else:
    for i in range(numero):
        z += 1
        resultado = numero * z
        print(numero, "x", z, "=", resultado)


