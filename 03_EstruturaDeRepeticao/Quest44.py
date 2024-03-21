'''
Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. 
Os códigos utilizados são:
1 , 2, 3, 4  - Votos para os respectivos candidatos 
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco
Faça um programa que calcule e mostre:
O total de votos para cada candidato;
O total de votos nulos;
O total de votos em branco;
A percentagem de votos nulos sobre o total de votos;
A percentagem de votos em branco sobre o total de votos. 
Para finalizar o conjunto de votos tem-se o valor zero.
'''

votos = {
    1: 'José',
    2: 'Ana',
    3: 'Francisco',
    4: 'Joana',
    5: 'Nulo',
    6: 'Branco'
}

counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
total_votos = 0
total_nulos = 0
total_brancos = 0

while True:
    voto = int(input('Digite o código do candidato (1 a 4), 5 (Voto nulo) ou 6 (Voto em branco): '))

    if voto == 0:
        break
    
    if voto not in votos:
        print('Código inválido, tente novamente.')
        continue
    
    total_votos += 1

    if voto == 5:
        total_nulos += 1
    elif voto == 6:
        total_brancos += 1
    else:
        counts[voto] += 1

# Calculando as percentagens
percentual_nulos = (total_nulos / total_votos) * 100 if total_votos > 0 else 0
percentual_brancos = (total_brancos / total_votos) * 100 if total_votos > 0 else 0

# Exibindo os resultados
print('Total de votos para cada candidato:')
for candidato, nome in votos.items():
    if candidato in counts:
        print(f'{nome}: {counts[candidato]} votos')

print(f'Total de votos nulos: {total_nulos}')
print(f'Total de votos em branco: {total_brancos}')
print(f'Percentual de votos nulos sobre o total de votos: {percentual_nulos:.2f}%')
print(f'Percentual de votos em branco sobre o total de votos: {percentual_brancos:.2f}%')


