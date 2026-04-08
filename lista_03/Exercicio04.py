#4. A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados
#sobre o salário e número de filhos. A prefeitura deseja saber:
#a) média do salário da população;
#b) média do número de filhos;
#c) maior salário;
#d) percentual de pessoas com salário até R$1000,00.
#O final da leitura de dados se dará com a entrada de um salário negativo.
habitantes = int(input("Digite o numero de habitantes: "))
filhos = 0
salario = 0
percentual = 0
salario = float(input("Digite o valor do salario: "))
numero_filhos = int(input("Digite o numero de filhos: "))
if habitantes and salario <=0:
    print("Dados digitados inválidos!")
else:
    if numero_filhos < 0:
        print("Dados Invalidos!")
    else:
        for i in range(habitantes):
            media_salarial = salario / habitantes
        print("Salario medio dos  habitantes: ", media_salarial)
        media_filhos = numero_filhos / habitantes
        print("Media de: ", media_filhos, "filhos")
    if salario <=1000:
        percentual += 1
        print("Salario percentual até R$1000: ", percentual/100)
