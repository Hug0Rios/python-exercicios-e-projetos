#14. Desenvolva um algoritmo que leia o nome de um aluno, suas notas em 2 provas e em um trabalho
# (todas com valores entre 0 e 10) e sua frequência, definindo e imprimindo se ele foi aprovado,
# reprovado ou se fará prova final. O aluno será reprovado se faltou mais de 15 aulas.
# Será aprovado se não for reprovado por falta e sua média for maior ou igual a 6,0.
# Caso tenha média menor, deverá fazer prova final. O cálculo da média deve ser feito com peso 3 para a primeira prova,
# 5 para a segunda prova e 2 para o trabalho.

nome_do_aluno = input('Digite o nome do aluno: ')
faltas = int(input("Digite o numero de faltas: "))
if faltas > 15:
    print("Aluno reprovado!")
else:
    nota1 = float(input("Digite a nota 1: "))
    if nota1 < 0:
        print("Nota 1 invalida!")
    else:
        if nota1 > 10:
            print("Nota 1 invalida!")
        else:
            nota2 = float(input("Digite a nota 2: "))
            if nota2 < 0:
                print("Nota 2 invalida!")
            else:
                if nota2 > 10:
                    print("Nota 2 invalida!")
                else:
                    nota_trabalho = float(input("Digite a nota do trabalho: "))
                    if nota_trabalho < 0:
                        print("Nota trabalho invalida!")
                    else:
                        if nota_trabalho > 10:
                            print("Nota trabalho invalida!")
                        else:
                            media = ((nota1 * 3) + (nota2 * 5) + (nota_trabalho * 2)) / 10
                            if media >= 6:
                                print("Aluno aprovado!")
                            else:
                                print("O Aluno deverá fazer a prova final!")