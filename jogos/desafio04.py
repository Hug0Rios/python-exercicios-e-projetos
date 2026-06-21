#Jogo da Velha
print("Bem-Vindo ao jogo da velha")
print("O tabuleiro será dividido em uma matriz 3x3")
vencedor =  0
tabuleiro =[
    [0,0,0],
    [0,0,0],
    [0,0,0]
    ]
while vencedor == 0:
    simbolos= {0: "-",1:"X",2:"0"}
for i in range (3):
    for j in range (3):
        print(simbolos[tabuleiro[i],[j]],end=" ")
        print()
    