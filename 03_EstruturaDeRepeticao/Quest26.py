'''
Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. 
Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
'''

candidato_1 = 0
candidato_2 = 0
candidato_3 = 0

numero_eleitores = int(input('Digite o número de eleitores: '))

for n in range(numero_eleitores):
    voto = int(input('Em qual candidato você deseja votar? '))
    if voto == 1:
        candidato_1 += 1
    elif voto == 2:
        candidato_2 += 1
    elif voto == 3:
        candidato_3 += 1
    else:
        print('Voto inválido!')

print(f"Candidato 1: {candidato_1} votos")
print(f"Candidato 2: {candidato_2} votos")
print(f"Candidato 3: {candidato_3} votos")