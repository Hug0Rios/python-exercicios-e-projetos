# 4. A prefeitura de uma cidade fez uma pesquisa
# entre seus habitantes, coletando dados sobre o
# salário e número de filhos. A prefeitura deseja
# saber:
# a) média do salário da população;
# b) média do número de filhos;
# c) maior salário;
# d) percentual de pessoas com salário até R$1000,00.
# O final da leitura de dados se dará com a entrada de
# um salário negativo.

soma_salarios = 0
soma_filhos = 0
qtde_pessoas_ate_mil = 0
populacao = 0
salario = float(input("Digite o salario da familia: "))
maior_salario = salario
while salario >= 0:
    num_filhos = int(input("Digite o número de filhos: "))
    populacao = populacao + 1
    soma_salarios = soma_salarios + salario
    soma_filhos = soma_filhos + num_filhos
    if salario > maior_salario:
        maior_salario = salario
    if salario <= 1000:
        qtde_pessoas_ate_mil = qtde_pessoas_ate_mil + 1
    salario = float(input("Digite o salario da familia: "))

if populacao > 0:
    salario_medio = soma_salarios / populacao
    media_filhos = soma_filhos / populacao
    percentual_ate_mil = (qtde_pessoas_ate_mil / populacao) * 100
    print(f"Salario medio = {salario_medio:.2f}")
    print(f"Media filhos = {media_filhos:.2f}")
    print(f"Maior salario = {maior_salario:.2f}")
    print(f"Percentual ate mil = {percentual_ate_mil:.2f}%")
