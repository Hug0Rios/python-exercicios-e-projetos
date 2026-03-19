#3.	Efetuar a leitura de uma nota e, se o valor for maior ou igual a 60, imprimir na tela "APROVADO", se for menor,
# imprimir reprovado. Testar ainda se o valor lido foi maior do que 100 ou menor do que zero. Neste caso,
# imprimir "NOTA INVÁLIDA".
Nota= float(input("Digite a sua nota: "))
if Nota >= 60 and Nota < 100:
    print("Aprovado!")
else:
    if Nota < 60 and Nota > 0:
        print("Reprovado!")
    else:
        if Nota > 100 or Nota < 0:
            print("Nota Invalida!")