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
