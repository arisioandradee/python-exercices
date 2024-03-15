#8. Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
#sabendo que a decisão é sempre pelo mais barato.

print('Digite três valores:')
n1 = float(input())
n2 = float(input())
n3 = float(input())

if n1 < n2 and n1 < n3:
    print(f'O produto mais bararo é {n1}')
elif n2 < n1 and n2 < n3:
    print(f'O produto mais bararo é {n2}')
elif n3 < n1 and n3 < n2:
    print(f'O produto mais bararo é {n3}')
else:
    print('Os produtos possuem o mesmo valor')