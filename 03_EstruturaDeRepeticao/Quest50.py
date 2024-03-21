#Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.
soma = 0

termos = int(input('Digite a quantidade de termos: '))

for i in range(1, termos + 1):
    soma += 1 / i

print(f'O valor de H com {termos} termos é: {soma}')