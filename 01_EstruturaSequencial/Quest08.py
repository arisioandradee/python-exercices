# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês.

valor_hora = input('Digite o valor ganho por hora trabalhada: ')
valor_hora = float(valor_hora)

numero_hora = input('Digite a quantidade de horas trabalhadas: ')
numero_hora = float(numero_hora)

quant_dias = input('Digite a quantidade de dias de trabalho: ')
quant_dias = float(quant_dias)


salario = (valor_hora * numero_hora) * quant_dias
print(f'Seu salário é de: R${salario:.0f}')