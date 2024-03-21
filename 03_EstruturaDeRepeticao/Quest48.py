# Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
# Exemplo:   12376489 => 98467321
  
while True:
    num = int(input('Digite um número para ser inverdito: '))

    if num < 0:
        print('Valor negativo, digite um número positivo: ')
        continue

    if num == 0:
        break

    num = str(num)
    print(f'{num[::-1]}')
    