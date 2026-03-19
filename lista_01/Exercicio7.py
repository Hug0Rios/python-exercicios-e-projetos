#7.	Efetuar a leitura do número de quilowatts consumidos e calcular o valor a ser pago de energia elétrica, sabendo-se
# que o valor a pagar por quilowatt é de 0,12. Apresentar o valor total a ser pago pelo usuário acrescido de 18% de
# ICMS.
Quilowatts = float(input( "Digite a Quantidade de Quilowatas: "))
Horas = float(input( "Digite a Quantidade de Horas: " ))
resultado = (Quilowatts * 12/100 * Horas - 18/100)
print("R$",resultado)