'''
Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles 
estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. 
A entrada de dados deverá terminar quando for lido um número negativo.
'''
counts = [0, 0, 0, 0]

while True:
    num = int(input('Digite um número: '))

    if num < 0:
        break

    if num >= 0 and num <= 25:
        counts[0] += 1
    elif num >= 26 and num <= 50:
        counts[1] += 1
    elif num >= 51 and num <= 75:
        counts[2] += 1
    else:
        counts[3] += 1

print(f'Números no intervalo [0-25]: {counts[0]}')
print(f'Números no intervalo [26-50]: {counts[1]}')
print(f'Números no intervalo [51-75]: {counts[2]}')
print(f'Números no intervalo [76-100]: {counts[3]}')