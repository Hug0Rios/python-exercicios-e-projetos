#15.	Faça um algoritmo para verificar e imprimir entre 4 números lidos qual é o menor.
primeiro_numero= float(input('Digite o primeiro numero: '))
segundo_numero= float(input('Digite o segundo numero: '))
terceiro_numero= float(input('Digite o terceiro numero: '))
quarto_numero= float(input('Digite o quarto numero: '))
menor= primeiro_numero
if segundo_numero < menor:
    menor = segundo_numero
else:
    if terceiro_numero < menor:
        menor = terceiro_numero
    else:
        if quarto_numero < menor:
         menor = quarto_numero

print('O Menor número é: {menor}')