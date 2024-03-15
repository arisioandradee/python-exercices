'''
Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois
 informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. 
 O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas 
 existentes na máquina.
    Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
    Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1. 
'''

saque = float(input('Digite o valor do saque (entre R$ 10 e R$ 600): '))

if saque < 10 or saque > 600:
    print('Valor mínimo de saque não atingido ou valor máximo excedido!')
else:
    notas_100 = saque // 100
    saque %= 100

    notas_50 = saque // 50
    saque %= 50

    notas_10 = saque // 10
    saque %= 10

    notas_5 = saque // 5
    saque %= 5

    notas_1 = saque

    print(f'Notas de R$ 100: {int(notas_100)}')
    print(f'Notas de R$ 50: {int(notas_50)}')
    print(f'Notas de R$ 10: {int(notas_10)}')
    print(f'Notas de R$ 5: {int(notas_5)}')
    print(f'Notas de R$ 1: {int(notas_1)}')
