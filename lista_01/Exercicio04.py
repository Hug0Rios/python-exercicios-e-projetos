#4.	Calcular o aumento que será dado a um funcionário, obtendo do usuário as seguintes informações: salário atual e a
# porcentagem de aumento. Apresentar o novo valor do salário e o valor do aumento.
salario_atual = float(input("digite seu salario atual: "))
aumento  = float(input("Digite o percentual de aumento: "))
valor_aumento = salario_atual * (aumento/100)
resultado = salario_atual * (aumento/100+1)
print("R$",resultado)
print  ("R$",valor_aumento)
print (str(aumento) + "% de aumento")
