#1. Faça um Programa que peça dois números e imprima o maior deles.

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))

if n1 > n2:
    print(f'O maior numero é o {n1}')
elif n2 > n1:
    print(f'O maior numero é o {n2}')   
else:
    print(f'Os números {n1} e {n2} são iguais!')