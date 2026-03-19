#20.Desenvolva um algoritmo para que, dados dois valores inteiros entre 1 e 10 lidos,
# calcule e imprima: a média dos números caso a soma deles for menor que 8, seu produto caso a soma seja igual a 8
# ou a divisão do maior pelo menor caso a soma dos valores for maior que 8.
numero_1= int(input('Digite um primeiro valor inteiro: '))
numero_2= int(input('Digite um segundo valor inteiro: '))
maior = numero_1
if numero_1 <0 and numero_1 >10:
    print('Valor invalido!')
else:
    if numero_2 <0 and numero_2 >10:
        print('Valor invalido!')
if (numero_1+numero_2)<8:
    resultado = (numero_1+numero_2)/2
    print('Média igual a:',resultado)
else:
    if (numero_1+numero_2)==8:
        resultado = (numero_1*numero_2)
        print('O produto é igual a:',resultado)
if ((numero_1+numero_2)>8):
    if numero_2<numero_1:
        print('A divisão é igual a',numero_1/numero_2)
    else:
        print('A divisão é igual a',numero_2/numero_1)
