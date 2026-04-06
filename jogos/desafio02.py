#Jogo-do-Pedra-Papel-Tesoura com numero de jogadas e numero de vitorias de cada e numero de empates
jogadas= int(input("Digite quantas jogadas você vai jogar: "))
vitorias_humano = 0
vitorias_computador = 0
for i in range(jogadas):
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

vitorias_humano = vitorias_humano + 1
vitorias_computador = vitorias_computador + 1
print("Você ganhou:",vitorias_humano)
print("O computador ganhou:" ,vitorias_computador)
empate = (jogadas -(vitorias_humano + vitorias_computador))
print("Vocês empataram: ", empate)