'''
Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em 
comissões. O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. 
Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento 
de $3000, ou seja, um total de $470. Escreva um programa (usando um array de contadores) que determine
quantos vendedores receberam salários nos seguintes intervalos de valores:
$200 - $299
$300 - $399
$400 - $499
$500 - $599
$600 - $699
$700 - $799
$800 - $899
$900 - $999
$1000 em diante
'''
salario_semanal = 200
porcent = 0.09
count = [0] * 10

while True:
    salario_bruto = float(input('Digite o valor de vendas bruto: '))

    if salario_bruto == 0:
        break

    liquido = porcent * salario_bruto
    total = liquido + salario_bruto + salario_semanal

    if total >= 200 and total <= 299:
        count[0] += 1
    elif total >= 300 and total <= 399:
        count[1] += 1
    elif total >= 400 and total <= 499:
        count[2] += 1
    elif total >= 500 and total <= 599:
        count[3] += 1
    elif total >= 600 and total <= 699:
        count[4] += 1
    elif total >= 700 and total <= 799:
        count[5] += 1
    elif total >= 800 and total <= 899:
        count[6] += 1
    elif total >= 900 and total <= 999:
        count[7] += 1
    elif total >= 1000:
        count[8] += 1
    else:
        print('erro!')

for i in range(10):
    if i == 8:
        print(f'Vendedores com salários de $1000 em diante: {count[i]}')
    else:
        print(f'Vendedores com salários entre ${200 + i * 100} - ${299 + i * 100}: {count[i]}')
