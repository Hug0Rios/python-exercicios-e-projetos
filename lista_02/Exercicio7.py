#7.	Faça a leitura do salário atual e do tempo de serviço de um funcionário. A seguir, calcule o seu salário reajustado.
# Funcionários com até 1 ano de empresa, receberão aumento de 10%.
# Funcionários com mais de um ano de tempo de serviço, receberão aumento de 20%.
Salario_Atual = float(input("Digite o Salario Atual: "))
Tempo_de_Serviço = float(input("Digite o Tempo de Serviço em Meses: "))
Aumento_Anual= Salario_Atual + (Salario_Atual * 10/100)
aumento_pós_Ano= Salario_Atual + (Salario_Atual * 20/100)
if Tempo_de_Serviço <= 12:
    print("R$" , Aumento_Anual)
else:
    if Tempo_de_Serviço > 12:
        print("R$" , aumento_pós_Ano)
