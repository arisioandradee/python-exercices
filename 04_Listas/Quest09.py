#Faça um Programa que leia um vetor A com 10 números inteiros, 
    #calcule e mostre a soma dos quadrados dos elementos do vetor.

numeros = [0] * 10
soma_quadrados = 0

for i in range(10):
    num = int(input('Digite um número: '))
    numeros[i] = num

    quadrado = numeros[i] ** 2
    print(quadrado)

    soma_quadrados += quadrado

print(f'O valor da soma dos quadrados é: {soma_quadrados}')