# 3.	Faça uma função que recebe por parâmetro o raio de uma esfera e calcule o seu volume (v = (4 x pi x R3)/3).
def calcular_volume(volume):
    return ( 4 * 3.14 * raio**3 ) /3
raio = float(input("Digite o raio: "))
print(f"O volume da esfera é: " ,calcular_volume(raio),"m³")