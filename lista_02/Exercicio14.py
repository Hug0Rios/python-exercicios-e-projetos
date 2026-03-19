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