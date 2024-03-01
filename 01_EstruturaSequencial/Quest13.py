#13. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as fórmulas:
#    Para homens: (72.7*h) - 58
#   Para mulheres: (62.1*h) - 44.7

altura = input('Digite sua altura em metros: ')
altura = float(altura)

peso_ideal_h = (72.7*altura) - 58
peso_ideal_m = (62.1*altura) - 44.7

print(f'Para os homens, o peso ideal é: {peso_ideal_h:.2f}kg')
print(f'Para as mulheres, o peso ideal é: {peso_ideal_m:.2f}kg')