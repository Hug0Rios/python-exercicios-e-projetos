#16.	Desenvolva um algoritmo que pergunte um código e de acordo com o valor digitado seja apresentado o cargo
# correspondente. Caso o usuário digite um código que não esteja na tabela, mostrar uma mensagem de código inválido.
# Utilize a tabela abaixo:
#Código Cargo
#101   	Vendedor
#103   	Auxiliar Técnico
#104   	Assistente
#105   	Coordenador de Grupo
#106   	Gerente

codigo= int(input('Digite um Código: '))
if codigo <101:
    print('Código Invalido!')
else:
    if codigo >106:
        print('Código Invalido!')

    else:
        if codigo ==101:
         print('Cargo de Vendedor!')
        else:
            if codigo ==102:
                print('Cargo de Atendente!')
            else:
                if codigo ==103:
                    print('Cargo de Auxiliar Técnico!')
                else:
                    if codigo ==104:
                        print('Cargo de Assistente!')
                    else:
                        if codigo ==105:
                            print('Cargo de Coordenador de Grupo!')
                        else:
                            if codigo ==106:
                                print('Cargo de Gerente!')