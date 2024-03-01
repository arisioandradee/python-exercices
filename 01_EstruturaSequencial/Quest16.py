#16. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
#Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
#Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

import math

area = input('Digite o tamanho da área a ser pintada(em metros quadrados): ')
area = float(area)

tinta = area / 3 #Quantidade em litros
quantidade_latas = math.ceil(tinta / 18)
valor = quantidade_latas * 80 #Calcular o valor

print(tinta)
print(f'A quantidade de latas de tinta a serem comradas é: {quantidade_latas} e o valor é: R${valor:.2f}')
