"""
Tendo como dado de entrada a altura (h) de uma pessoa,
construa um algoritmo que calcule seu peso ideal,
utilizando as seguintes fórmulas:
    Para homens: (72.7*h) - 58
    Para mulheres: (62.1*h) - 44.7
"""
alt = float(input("Digite sua altura em metros: "))
sexo = input("informe <F>eminino ou <M>asculino: ")
if sexo == 'F':
    pesoIdeal = 62.1 * alt - 44.7
else:
    pesoIdeal = 72.7 * alt - 58
print("Seu peso ideal é", pesoIdeal)