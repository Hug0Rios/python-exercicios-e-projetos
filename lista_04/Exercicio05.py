# 5.	Escrever uma função verificarEstacao(dia, mes), que retorna qual a estação do ano da data
# passada por parâmetro. Lembrando que a primavera começa no dia 23 de setembro, o verão em 21 de dezembro,
# o outono em 21 de março e o inverno em 21 de junho.
def verificar_estacao (dia,mes):
    if dia == 23 and mes == 9:
        return (" A estação do ano é Primavera")
    else:
        if dia == 21 and mes == 12:
            return ("A estação do ano é Verão")
        else:
            if dia == 21 and mes == 3:
                return ("A estaçao do ano é Outono")
            else:
                if dia == 21 and mes == 6:
                    return ("A estação do ano é inverno")
dia = int(input("Digite o dia : "))
mes = int(input("Digite o mes : "))
print(verificar_estacao(dia,mes))