#Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

impar = 0
par = 0
soma = 0

for a in range(10):
    num = int(input('Digite um número: '))
    soma += num

    if a % 2 == 0:
        par += 1
    else:
        impar += 1

print(f'Soma: {soma} | Impar: {impar} | Par: {par}')