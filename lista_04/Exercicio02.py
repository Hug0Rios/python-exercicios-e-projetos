# 2.	Faça uma função que recebe a média final de um aluno por parâmetro e retorna o seu conceito, conforme a tabela abaixo:  
# Nota 	Conceito
# De 0 a 49 = D
# De 50 a 69 = C
# De 70 a 89 = B
# De 90 a 100 = A

def checar_notas (media):
    if media >= 0 and media <= 49:
        conceito = "D"
    else:
        if media >= 50 and media <= 69:
            conceito = "C"
        else:
            if media >= 70 and media <= 89:
                conceito = "B"
            else:
                if media >= 90 and media <= 100:
                    conceito = "A"
    return conceito
media = int(input("Digite a sua media: "))

print(f"Seu conceito é: {checar_notas(media)}")