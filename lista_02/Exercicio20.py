#20.Desenvolva um algoritmo para que, dados dois valores inteiros entre 1 e 10 lidos,
# calcule e imprima: a média dos números caso a soma deles for menor que 8, seu produto caso a soma seja igual a 8
# ou a divisão do maior pelo menor caso a soma dos valores for maior que 8.
numero1 = int(input("Digite um numero: "))
numero2 = int(input("Digite um numero: "))
if numero1 < 1 or numero1 > 10 or numero2 < 1 or numero2 > 10:
    print("Numeros invalidos")
else:
    soma = numero1 + numero2
    if soma < 8:
        resultado = soma / 2
    else:
        if soma == 8:
            resultado = numero1 * numero2
        else:
            if numero1 > numero2:
                resultado = numero1 / numero2
            else:
                resultado = numero2 / numero1
    print(resultado)