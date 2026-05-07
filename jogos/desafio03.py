# jogo da forca

erro = 0
acerto = 0
import random

print("Voce tem 6 chances de jogadas antes de perder!")

palavras = ["Nebulosa","Engrenagem", "Horizonte", "Labirinto", "Faisca", "Eclipse","Ancora","Tempestade",
                       "Cristal",  "Miragem"]
palavra_sorteada = random.choice(palavras)
tamanho = len(palavra_sorteada)
print("A palavra possui" , tamanho, "letras")

while erro != 7 and acerto != tamanho :
    letra = input('Digite uma  letra: ')
    letra = letra.lower()
    if not letra in palavra_sorteada :
        erro += 1
        print("Voce perdeu uma vida!")

    else:
        print("Voce acertou uma letra!")
        acerto += 1
if erro == 7:
    print("Game Over!","A palavra era:",palavra_sorteada)
else:
    print("Game Win!","A palavra é:",palavra_sorteada)