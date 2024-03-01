#11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#    a. o produto do dobro do primeiro com metade do segundo .
#    b. a soma do triplo do primeiro com o terceiro.
#    c. o terceiro elevado ao cubo.

print('Digite dois valores inteiros e um real: ')
n1 = int(input())
n2 = int(input())
n3 = float(input())

a = (n1*2) + (n2/2)
b = (n2*3) + n3
c = (n3**3)

print(f'O produto do dobro do primeiro com metade do segundo: {a}')
print(f'A soma do triplo do primeiro com o terceiro: {b}')
print(f'O terceiro elevado ao cubo: {c}')
