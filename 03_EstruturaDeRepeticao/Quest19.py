#Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

soma = 0

qtd_num = int(input('Digite quantos números deseja digitar: '))

numeros = []

for a in range(qtd_num):
    num = int(input('Digite os números: '))
    if num >= 0 and num <= 1000:
        numeros.append(num)
        menor_valor = min(numeros)
        maior_valor = max(numeros)
        soma = sum(numeros)
    else:
        print('Números fora do intervalo!')

print(f'MENOR VALOR: {menor_valor} | MAIOR VALOR:{maior_valor} | SOMA DOS VALORES:{soma}')