'''
8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas
no mês. Calcule e mostre o total do seu salário no referido mês.
'''

SalarioHora = float(input("Digite quanto você recebe por hora trabalhada: "))
HorasTrabalhadas = float(input("Digite quantas horas você trabalhou no mês: "))
Salario = SalarioHora * HorasTrabalhadas
print("Você ganha R$",SalarioHora, "por hora trabalhada. E você trabalhou", HorasTrabalhadas,"horas, você ira receber R$",Salario, "no final do mês")