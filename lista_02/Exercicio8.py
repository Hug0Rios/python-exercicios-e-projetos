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