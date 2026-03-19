#8.	Faça a leitura do ano atual e do ano de nascimento de uma pessoa e exibir sua idade. A seguir,
# informe se a pessoa é bebê (0 a 3 anos), criança (4 a 11 anos), adolescente (12 a 17 anos),
# adulta (18 a 64 anos) ou idosa (65 anos em diante).
ano_atual= int(input("Digite o ano atual: "))
ano_de_nascimento = int(input("Digite o ano de nascimento: "))
idade =(ano_atual - ano_de_nascimento)
if idade <0:
    print ('Idade invalida!')
else:
    if  idade <=3:
        print('A idade é', idade,"e a pessoa é um Bebê!")
    else :
        if idade <=11:
            print('A idade é', idade,"e a pessoa é uma Criança!")
        else :
            if idade <=17:
                print('A idade é', idade,"e apessoa é um Adolescente!")
            else :
                if idade <=64:
                    print('A idade é', idade,"e a pessoa é um Adulto!")
                else :
                        print('A idade é', idade,"e a pessoa é idosa!")