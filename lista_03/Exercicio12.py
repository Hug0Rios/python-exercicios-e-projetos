#  Escrever um algoritmo que leia uma quantidade desconhecida de números e conte
# quantos deles estão nos seguintes intervalos: [0,25], [26,50], [51,75] e [76,100]. A
# entrada de dados deve terminar quando for lido um número negativo.
numeros = int(input("Digite o numero: "))
qnt_1 = 0
qnt_2 = 0
qnt_3 = 0
qnt_4 = 0
while numeros >= 0:
    if numeros >= 0 and numeros <= 25:
        qnt_1 += 1
    else:
        if numeros >= 26 and numeros <= 50:
            qnt_2 += 1
        else:
            if numeros >= 51 and numeros <= 75:
                qnt_3 += 1
            else:
                if numeros >= 76 and numeros <= 100:
                    qnt_4 += 1
    numeros = int(input("Digite o numero: " ))

print(qnt_1)
print(qnt_2)
print(qnt_3)
print(qnt_4)

        