#Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

numeros = [0] * 5
soma = 0
multi = 1

for i in range(5):
    num = int(input('Digite um número: '))
    numeros[i] = num

    soma += num
    multi *= num

print(f'Os números são: {numeros}, a soma deles é {soma} e a multiplicação é {multi}')