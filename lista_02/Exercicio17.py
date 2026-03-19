#17. Uma encomenda de unidades de disco contém unidades marcadas com um código de 1 a 4, que indica o tipo seguinte:
#Código 	Tipo da unidade
#1   	CD-ROM (700MB)
#2   	DVD-ROM (4.7GB)
#3   	DVD-9 (8.54 GB)
#4   	Blu-Ray (25 GB)
#Escreva um programa que receba o número de um código como entrada e, baseado no valor digitado,
# informe o tipo correto de unidade de disco.
codigo= int(input('Digite um Código: '))
if codigo <1:
    print('Código Invalido!')
else:
    if codigo >4:
        print('Código Invalido!')
    else:
        if codigo ==1:
            print('O Tipo de Unidade de disco é: CD-ROM (700MB)')
        else:
            if codigo ==2:
                print('O Tipo de Unidade de disco é: DVD-ROM (4.7GB)')
            else:
                if codigo ==3:
                    print('DVD-9 (8.54 GB)')
                else:
                    if codigo ==4:
                        print('Blu-Ray (25 GB)')