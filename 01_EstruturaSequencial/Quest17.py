'''17. Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 
ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
1. comprar apenas latas de 18 litros; 2. comprar apenas galões de 3,6 litros;
3. misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
'''
import math

area = input('Digite o tamanho da área a ser pintada: ')
area = float(area)

litro = area / 6
quantidade_lata = math.ceil(litro / 18)
quantidade_galao = math.ceil(litro / 3.6)

valor_lata = quantidade_lata * 80
valor_galao = quantidade_galao * 25

folga = litro * 0.1  # 10% de folga
mistura_lata = math.floor((litro + folga) / 18)
mistura_galao = math.ceil(((litro + folga) - (mistura_lata * 18)) / 3.6)
preco_c = (mistura_lata * 80.00) + (mistura_galao * 25.00)

print(f'Latas de 18L - Quantidade:{quantidade_lata}, Valor:R${valor_lata}')
print(f'Galões de 3,6L - Quantidade:{quantidade_galao}, Valor:R${valor_galao}')
print(f'Misturando latas e galões - Quantidade:{mistura_galao}, Valor:R${preco_c}')


