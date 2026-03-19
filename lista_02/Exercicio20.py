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
