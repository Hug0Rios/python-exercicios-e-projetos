#11. Escreva um programa para calcular e mostrar o salário semanal de uma pessoa,determinado pelas condições que seguem.
# Se o número de horas trabalhadas for inferior ou igual a 40, a pessoa recebe R$15,00 por hora,
# senão a pessoa recebe R$600,00 mais R$21,00 para cada hora trabalhada acima de 40 horas.
# O programa deve pedir o número de horas trabalhadas como entrada e deve dar o salário como saída.
horas_trabalhadas= float(input("Digite a Quantidade de horas trabalhadas essa semana: "))
if horas_trabalhadas <= 0:
  print("Horas inválidas!")
else:
  if horas_trabalhadas <= 40:
    print  ('O salário será de R$:',(horas_trabalhadas * 15))
  else:
    print ('O salário será de R$:', (600+(horas_trabalhadas*21)))
