tempo_de_investmento = float(input("Digite quantos anos o dinheiro está investido no fundo: "))
if tempo_de_investmento <0:
    print('tempo inválido!')
else:
    if tempo_de_investmento <1:
        print('Sua taxa de juros é de 0,55%')
    else:
        if tempo_de_investmento <2:
            print('Sua taxa de juros é de 0,65%')
        else:
            if tempo_de_investmento <3:
                print('Sua taxa de juros é de 0,75%')
            else:
                if tempo_de_investmento <4:
                    print('Sua taxa de juros é de 0,85%')
                else:
                    if tempo_de_investmento <5:
                        print('Sua taxa de Juros é de 0,90%')
                    else:
                        if tempo_de_investmento <=5:
                            print('Sua taxa de juros é de 0,95%')

