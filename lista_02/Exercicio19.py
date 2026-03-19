nota_do_aluno= int(input('Digite a nota do aluno: '))
if nota_do_aluno >10:
    print('Nota Invalida!')
else:
    if nota_do_aluno <0:
        print('Nota Invalida!')
if nota_do_aluno ==10 or nota_do_aluno ==9:
    print('Nota Conceito A!')
else:
    if nota_do_aluno ==8 or nota_do_aluno ==7:
        print('Nota Conceito B!')
    else:
        if nota_do_aluno ==6 or nota_do_aluno ==5:
            print('Nota Conceito C!')
        else:
            if nota_do_aluno <5 and nota_do_aluno ==0:
                print('Nota Conceito D')

