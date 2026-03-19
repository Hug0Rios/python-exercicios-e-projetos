#14. Desenvolva um algoritmo que leia o nome de um aluno, suas notas em 2 provas e em um trabalho
# (todas com valores entre 0 e 10) e sua frequência, definindo e imprimindo se ele foi aprovado,
# reprovado ou se fará prova final. O aluno será reprovado se faltou mais de 15 aulas.
# Será aprovado se não for reprovado por falta e sua média for maior ou igual a 6,0.
# Caso tenha média menor, deverá fazer prova final. O cálculo da média deve ser feito com peso 3 para a primeira prova,
# 5 para a segunda prova e 2 para o trabalho.

nome_do_aluno = input('Digite o nome do aluno: ')
frequencia= int(input('Digite o numero de faltas do aluno: '))
if frequencia>15:
    print('Aluno Reprovado!')
else:
    nota_primeira_prova= int(input('Digite a nota da primeira prova: '))
    nota_segunda_prova = int(input('Digite a nota da segunda prova: '))
    trabalho= int(input('Digite a nota do trabalho: '))
    if nota_primeira_prova <0>10:
        print('Nota inválida!')
    else:
        if nota_segunda_prova <0>10:
                print('Nota inválida!')
        else:
            if trabalho <0>10:
                    print('Nota inválida!')

    if ( ((nota_primeira_prova *3 ) + (nota_segunda_prova *5) + (trabalho *2))/10>6 ):
        print('Aluno Aprovado!')
    else:
        print('O Aluno deverá fazer prova final!')