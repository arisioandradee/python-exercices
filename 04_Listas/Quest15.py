'''
Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada 
de dados quando for informado um valor igual a -1 (que não deve ser armazenado). 
Após esta entrada de dados, faça:
Mostre a quantidade de valores que foram lidos;
Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
Calcule e mostre a soma dos valores;
Calcule e mostre a média dos valores;
Calcule e mostre a quantidade de valores acima da média calculada;
Calcule e mostre a quantidade de valores abaixo de sete;
Encerre o programa com uma mensagem;
'''

valores = []
soma = 0

while True:
    valor = int(input('Digite um valor: '))

    if valor == -1:
        break

    valores.append(valor)
    soma += valor

media = soma / len(valores)
acima_media = sum(1 for v in valores if v > media)
abaixo_sete = sum(1 for v in valores if v < 7)

print(f'Quantidade de valores lidos: {len(valores)}')
print('Valores na ordem em que foram informados:', *valores)
print('Valores na ordem inversa:', *reversed(valores), sep='\n')
print(f'Soma dos valores: {soma}')
print(f'Média dos valores: {media}')
print(f'Quantidade de valores acima da média: {acima_media}')
print(f'Quantidade de valores abaixo de sete: {abaixo_sete}')
print('Programa encerrado.')

