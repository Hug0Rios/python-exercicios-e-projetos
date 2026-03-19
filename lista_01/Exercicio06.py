#6.	Calcular o salário líquido do funcionário sabendo que este é constituído pelo salário bruto mais o valor das horas
# extras subtraindo 8% de INSS do total. Serão lidos nesse problema o salário bruto, o valor das horas extras e o número
# de horas extras. Apresentar ao final o salário líquido.
Salario_Bruto=(float(input("Digite o seu salário bruto: ")))
Horas_Extras=(float(input("Digite a quantidade de horas extras: ")))
Valor_Horas_Extras=(float(input("Digite o valor da hora extra hora: ")))
resultado = (Salario_Bruto + (Valor_Horas_Extras * Horas_Extras - 8/100))
print(resultado)