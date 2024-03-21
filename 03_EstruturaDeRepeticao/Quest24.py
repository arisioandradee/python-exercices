# Faça um programa que calcule o mostre a média aritmética de N notas.

soma = 0
media = 0
cont_nota = 0

qtd_nota = int(input('Quantas notas deseja calcular: '))

for i in range(qtd_nota):
    nota = float(input('Digite uma nota: '))
    cont_nota += 1
    soma += nota


media = soma / cont_nota
print(f'A média das notas é:{media}')