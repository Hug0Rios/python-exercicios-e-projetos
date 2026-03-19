Nota= float(input("Digite a sua nota: "))
if Nota >= 60 and Nota < 100:
    print("Aprovado!")
else:
    if Nota < 60 and Nota > 0:
        print("Reprovado!")
    else:
        if Nota > 100 or Nota < 0:
            print("Nota Invalida!")