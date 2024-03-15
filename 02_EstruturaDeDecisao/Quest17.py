#17.Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se 
#este ano é ou não bissexto.

ano = input('Digite um ano: ')
ano = int(ano)

if ano % 4 == 0:
    print('Ano bissexto!')
else:
    print('Ano não bissexto!')