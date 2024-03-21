'''
Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno 
e o segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. 
Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.
'''

codigo = []
altura = []

mais_baixo = float('inf')
mais_alto = float('-inf')

while len(codigo) < 10 and len(altura) < 10:
    cod = int(input('Digite o código do aluno: '))
    codigo.append(cod)
    alt = float(input('Digite a altura do aluno: '))
    altura.append(alt)

    if alt < mais_baixo:
        cod_mais_baixo = cod 
        mais_baixo = alt

    if alt > mais_alto:
        cod_mais_alto = cod 
        mais_alto = alt

print(f'Código do aluno mais alto: {cod_mais_alto} / altura: {mais_alto}')
print(f'Código do aluno mais baixo: {cod_mais_baixo} / altura: {mais_baixo}')
