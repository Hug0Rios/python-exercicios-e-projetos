#9.	Informar o número do mês do ano e mostrar o nome do mês por extenso.
# Caso o número do mês não exista, exibir a mensagem "Mês inválido".
numero_mes = int(input("Digite o némero do mês desejado: "))
if numero_mes == 1: print("O mês informado é Janeiro")
else :
        if numero_mes == 2:
            print("O mês informado é Fevereiro")
        else :
            if numero_mes == 3:
                print("O mês informado é Março")
            else :
                if numero_mes == 4:
                    print("O mês informado é Abril")
                else :
                    if numero_mes == 5:
                        print("O mês Informado é Maio")
                    else:
                        if numero_mes == 6:
                            print("O mês informado é Junho")
                        else :
                            if numero_mes == 7:
                                print("O mês informado é Julho")
                            else :
                                if numero_mes == 8:
                                    print("O mês informado é Agosto")
                                else:
                                    if numero_mes == 9:
                                        print("O mês informado é Setembro")
                                    else :
                                        if numero_mes == 10:
                                            print("O mês informado é Outubro")
                                        else :
                                            if numero_mes == 11:
                                                print("O mês informado é Novembro")
                                            else :
                                                if numero_mes == 12:
                                                    print("O mês informado é Dezembro")
                                                else :
                                                    if numero_mes < 0 or numero_mes > 12:
                                                        print("Mês Inválido")

