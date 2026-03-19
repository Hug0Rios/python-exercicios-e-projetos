#5.	Ler um número inteiro e testar se o valor lido termina com 0 (divisível por 10).
# Em caso positivo, exiba a metade deste número. Caso contrário, exibir a mensagem
# "O número digitado não termina com 0".
Numero=int(input("Digite um numero inteiro: "))
Divisao=Numero//10
resto=Numero%10
resultado=resto
if (resultado==0):
    print('A metade do numero é:',Numero/2)
else:print('O Número digitado nâo termina com 0')