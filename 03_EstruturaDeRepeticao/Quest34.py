#Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. 
#Um número primo é aquele que é divisível apenas por um e por ele mesmo. 
#Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.

num = int(input('Digite um número (0 para cancelar): '))

while num != 0:
    if num <= 1:
        print('Não é primo!')
    else:
        primo = True
        for i in range(2, num):
            if num % i == 0:
                primo = False
                break
        if primo:
            print('Primo!')
        else:
            print('Não é primo!')
    
    num = int(input('Digite um número (0 para cancelar): '))

