# 13.	Baseado no ano e peso do modelo de um automóvel, o estado de Nova Jersey determina a sua classe de peso
# e taxa de registro usando a seguinte tabela:
# Ano do modelo_Peso_Classe_Taxa de registro
#,1970 ou antes, Menos de 1200 kg  1 16,50
#de 1200 a 1700 kg	2	25,50
#Mais de 1700 kg	3	46,50
#1971 a 1979	Menos de 1200 kg	4	27,00
#de 1200 a 1700 kg	5	30,50
#Mais de 1700 kg	6	52,50
#1980,ou depois 	Menos de 1600 kg	7	19,50,
#1600 kg ou mais	8	55,50
#Usando esta informação, escreva um programa que receba o ano e o peso do modelo de um automóvel e
# calcule e imprima a classe de peso e a taxa de registro para o carro.

ano_do_carro:int = int(input("Digite o ano do carro: "))
peso_do_carro:float = float(input("Digite o peso do carro em KG: "))
if ano_do_carro <=1970:
    if peso_do_carro <=1200 :
        print ('Classe 1 de Peso, Taxa de registro: 16,50')
    else:
        if peso_do_carro <=1700:
            print('Classe 2 de Peso,Taxa de registro: 25,50')
        else:
            if peso_do_carro >1700:
                print('Classe 3 de Peso,Taxa de registro: 46,50')

else:
    if ano_do_carro >=1972<=1979:
        if peso_do_carro <=1200:
            print('Classe 4 de Peso, Taxa de registro: 27,00')
        else:
            if peso_do_carro <=1700:
                print('Classe 5 de Peso, Taxa de registro: 30,50')
            else:
                if peso_do_carro >1700:
                    print('Classe 6 de Peso, Taxa de registro: 52,50')
if ano_do_carro >=1980:
    if peso_do_carro <1600:
        print('Classe 7 de Peso, Taxa de registro: 19,50')
    else:
        if peso_do_carro >=1600:
            print('Classe 8 de Peso, Taxa de registro: 55,50')
