horas_trabalhadas= float(input("Digite a Quantidade de horas trabalhadas essa semana: "))
if horas_trabalhadas <= 0:
  print("Horas inválidas!")
else:
  if horas_trabalhadas <= 40:
    print  ('O salário será de R$:',(horas_trabalhadas * 15))
  else:
    print ('O salário será de R$:', (600+(horas_trabalhadas*21)))
