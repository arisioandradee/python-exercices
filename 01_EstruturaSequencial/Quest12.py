#12. Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula:
# (72.7*altura) - 58

altura = input('Digite sua altura em metros: ')
altura = float(altura)

peso_ideal = (72.7*altura) - 58

print(f'Com uma altura de {altura}m o peso ideal é de: {peso_ideal:.2f}kg')