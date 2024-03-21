'''
Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs 
    e o valor médio gasto em cada um deles. 
O usuário deverá informar a quantidade de CDs e o valor para em cada um.
'''
total = 0
contador = 0

quantidade = int(input("Digite a quantidade de CD's da sua coleção: "))

for n in range(quantidade):
    contador += 1

    valor = float(input('Digite o valor do CD: '))
    total += valor

media = total / quantidade

print(f"Quantidade de CD's: {contador}")
print(f'Valor médio gasto em cada CD: {media}')