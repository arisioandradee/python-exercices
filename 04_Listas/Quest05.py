'''
Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no 
vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
'''

numeros = []
pares = []
impares = []

for i in range(20):
    num = int(input('Digite um número: '))
    numeros.append(num)

    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print(f'Os números digitados foram: {numeros}')
print(f'Os números pares são: {pares}')
print(f'Os números impares são: {impares}')