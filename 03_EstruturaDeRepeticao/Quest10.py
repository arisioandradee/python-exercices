#Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

soma = 0

if n1 > n2:
    for a in range(n2+1, n1):
        print(a)
        soma = soma + a
elif n2 > n1:
    for a in range(n1+1, n2):
        print(a)
        soma = soma + a
else:
    print('Os valores são iguais!')