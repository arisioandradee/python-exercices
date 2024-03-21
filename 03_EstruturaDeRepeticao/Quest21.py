#21. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. 
    #Um número primo é aquele que é divisível somente por ele mesmo e por 1.

num = int(input('Digite um número: '))

if num >= 1:
    for i in range(1, num):
        if num % i != 0:
            print(num, 'é primo')
        else:
            print(num, 'não é primo')
            break
elif num == 0:
    print(num, 'é zero')
else:
    print(num, 'é negativo')
