#Faça um programa que mostre os n termos da Série a seguir:
  #S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 

n = int(input('Digite a quantidade de termos da série: '))

soma = 0
numerador = 1
denominador = 1

for i in range(n):
    soma += numerador / denominador
    print(f'S = {numerador}/{denominador}')
    numerador += 1
    denominador += 2

print(f'A soma dos {n} termos da série é: {soma}')
