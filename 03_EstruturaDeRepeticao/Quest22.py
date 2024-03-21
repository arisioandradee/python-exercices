#Altere o programa de cálculo dos números primos, informando, caso o número não seja primo,
    #por quais número ele é divisível.

num = int(input('Digite um número: '))

if num > 1:
    divisores = []
    for i in range(2, num):
        if num % i == 0:
            divisores.append(i)
    if divisores:
        print(num, 'não é primo')
        print(num, 'é divisível por:', divisores)
    else:
        print(num, 'é primo')
elif num == 1:
    print(num, 'não é primo')
    print('1 não é um número primo')
else:
    print(num, 'não é um número válido para verificar se é primo')
