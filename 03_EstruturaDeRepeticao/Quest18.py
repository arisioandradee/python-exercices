#Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

soma = 0

qtd_num = int(input('Digite quantos números deseja digitar: '))

numeros = []

for a in range(qtd_num):
    num = int(input('Digite os números: '))
    numeros.append(num)
    menor_valor = min(numeros)
    maior_valor = max(numeros)
    soma = sum(numeros)

print(f'MENOR VALOR: {menor_valor} | MAIOR VALOR:{maior_valor} | SOMA DOS VALORES:{soma}')