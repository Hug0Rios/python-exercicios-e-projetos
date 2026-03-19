Salario_Atual = float(input("Digite o Salario Atual: "))
Tempo_de_Serviço = float(input("Digite o Tempo de Serviço em Meses: "))
Aumento_Anual= Salario_Atual + (Salario_Atual * 10/100)
aumento_pós_Ano= Salario_Atual + (Salario_Atual * 20/100)
if Tempo_de_Serviço <= 12:
    print("R$" , Aumento_Anual)
else:
    if Tempo_de_Serviço > 12:
        print("R$" , aumento_pós_Ano)
