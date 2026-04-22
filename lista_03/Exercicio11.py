# 11.	Escrever um algoritmo que leia um
# número não determinado de valores e calcule
# a média aritmética dos valores lidos, a
# quantidade de valores positivos, a quantidade
# de valores negativos e o percentual de valores
# negativos e positivos. Mostre os resultados.

qtde_positivos = 0
qtde_negativos = 0
soma_positivos = 0
soma_negativos = 0
continuar = True
while continuar:
    valor = int(input("Digite um valor: "))
    if valor > 0:
        qtde_positivos += 1
        soma_positivos += valor
    else:
        if valor < 0:
            qtde_negativos += 1
            soma_negativos += valor
    resposta = input("Deseja continuar? [S/N] ")
    if resposta == "N":
        continuar = False
print(f"Quantidade de positivos: {qtde_positivos}")
print(f"Quantidade de negativos: {qtde_negativos}")
print(f"Soma de positivos: {soma_positivos}")
print(f"Soma de negativos: {soma_negativos}")
total = qtde_negativos + qtde_positivos
if total != 0:
    percentual_positivos = (qtde_positivos / total) * 100
    percentual_negativos = (qtde_negativos / total) * 100
    print(f"Percentual positivos: {percentual_positivos:.2f}%")
    print(f"Percentual negativos: {percentual_negativos:.2f}%")