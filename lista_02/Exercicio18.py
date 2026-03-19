#18.	Escreva um programa que receba dois números reais e um código de seleção do usuário.
# Se o código digitado for 1, faça o programa adicionar os dois números previamente digitados e mostrar o resultado;
# se o código de seleção for 2, os números devem ser multiplicados; se o código de seleção for 3, o
# primeiro número deve ser dividido pelo segundo. Se nenhuma das opções acima for escolhida, mostrar "Código inválido".
primeiro_numero = float(input('Digite o primeiro Número: '))
segundo_numero = float(input('Digite o segundo numero: '))
codigo = int(input('Digite o código: '))
if codigo <1:
    print('Código Inválido!')
else:
    if codigo >3:
        print('Código Inválido!')
if codigo == 1:
    resultado = (1+ primeiro_numero + segundo_numero)
    print('Resultado igual a:',resultado)
else:
    if codigo == 2:
        resultado = primeiro_numero * segundo_numero
        print('Resultado igual a:',resultado)
    else:
        if codigo == 3:
            resultado = primeiro_numero/segundo_numero
            print('Resultado igual a:',resultado)