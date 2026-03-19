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