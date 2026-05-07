# 	Escrever um algoritmo que gere e escreva
# os 3 primeiros números perfeitos. Um número
# perfeito é aquele que é igual a soma dos seus
# divisores. (Ex.: 6 = 1+2+3; 28= 1+2+4+7+14, etc)
# .

numero = 2
qtde_numeros_perfeitos = 0
while qtde_numeros_perfeitos < 5:
    if numero % 10 == 6 or numero % 10 == 8:
        soma_divisores = 0
        for i in range(1, int(numero/2) + 1):
            if numero % i == 0:
                soma_divisores = soma_divisores + i
        if numero == soma_divisores:
            qtde_numeros_perfeitos += 1
            print(numero)
    numero += 1