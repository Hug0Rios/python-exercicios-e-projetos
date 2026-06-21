# jogo da forca
letra_escolhida = ""
erro = 0
acerto = 0
import random

print("Voce tem 6 chances de jogadas antes de perder!")

palavras = ["Nebulosa","Engrenagem", "Horizonte", "Labirinto", "Faisca", "Eclipse","Ancora","Tempestade",
                       "Cristal",  "Miragem"]
palavra_sorteada = random.choice(palavras)
palavra_sorteada = palavra_sorteada.lower()
tamanho = len(palavra_sorteada)
print("A palavra possui" , tamanho, "letras")

while erro != 7 and acerto != tamanho :
    exibicao = ""
    for letras in palavra_sorteada:
        if letras in letra_escolhida:
            exibicao += letras
        else:
            exibicao += "_"
    print (exibicao)
    print(letra_escolhida)
    letra = input('Digite uma  letra: ').lower()
    if letra in letra_escolhida:
        print("Você já jogou essa letra!")
    else:
            if not letra in palavra_sorteada :
                erro += 1
                print("Voce perdeu uma vida!")
            else:
                print("Voce acertou uma letra!")
                acerto += palavra_sorteada.count(letra)
            letra_escolhida += letra  + "-"
    if erro == 7:
        print("Game Over!","A palavra era:",palavra_sorteada)
    else:
         print("Game Win!","A palavra é:",palavra_sorteada)