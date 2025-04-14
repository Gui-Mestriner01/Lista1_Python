"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas
no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados
11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos
dê:
o salário bruto.
o quanto pagou ao INSS.
o quanto pagou ao sindicato.
o o salário líquido.
o calcule os descontos e o salário líquido, conforme a tabela abaixo:
o + Salário Bruto : R$
o - IR (11%) : R$
o - INSS (8%) : R$
o - Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
"""
salario_hora = float(input("Digite quanto você recebe por hora trabalhada: "))
hora_mes = float(input("Quantas horas você trabalha por mês: "))
bruto = salario_hora * hora_mes
IR = bruto * 0.11
INSS = bruto * 0.08
sindicato = bruto * 0.05

print("Seu salário bruto é de R$",bruto)
print("O valor do imposto de renda é R$",IR)
print("O valor do INSS é R$",INSS)
print("Você tem que pagar R$",sindicato,"para o sindicato")
print("O valor liquido do seu salário ficara em R$",(bruto - IR - INSS - sindicato))