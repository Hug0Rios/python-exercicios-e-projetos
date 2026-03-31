#Jogo-do-Pedra-Papel-Tesoura
jogada = int(input("Digite Sua Jogada, 0 é pedra, 1 é papel, 2 é tesoura: "))
from random import *
pedra = 0
papel = 1
tesoura = 2
computador = randint(0,2)
if jogada !=0 and jogada != 1 and jogada != 2:
    print("jogada invalida")
else:
    print(f"Voce jogou {jogada} e o computador jogou {computador}")
    if jogada == computador:
        print("Empate")
    else:
        if jogada == 0 and computador == 2:
            print("Voce ganhou")
        else:
            if jogada == 0 and computador == 1:
                print("Computador ganhou")
            else:
                if jogada == 1 and computador == 0:
                    print("Voce ganhou")
                else:
                    if jogada == 1 and computador == 2:
                        print("Computador ganhou")
                    else:
                        if jogada == 2 and computador == 1:
                            print("Voce ganhou")
                        else:
                            if jogada == 2 and computador == 0:
                                print("Computador ganhou")