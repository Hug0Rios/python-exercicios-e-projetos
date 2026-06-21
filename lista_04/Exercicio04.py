# 4. Escrever uma função contarImpar(n1, n2) que retorna o número de inteiros ímpares que existem entre n1 e n2
# (inclusive ambos, se for o caso). A função deve funcionar inclusive se o valor de n2 for menor que n1.
def contarimpar(n1,n2):
    contador = 0
    if n1 > n2:
        variavel = n1
        n1 = n2
        n2 = variavel

    for numero in range(n1,n2+1):
        if n1 and n2 % 2 != 0:
            contador + 1
        return contador
numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))
print("A quantidade de numeros impares é:" ,
      contarimpar(numero1,numero2))