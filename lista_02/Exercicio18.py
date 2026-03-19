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