'''
Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor . Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados.
'''
import random

contagens = [0] * 6
numeros = [1, 2, 3, 4, 5, 6]

for _ in range(100):
    numero = random.choice(numeros)
    contagens[numero - 1] += 1  

print("- - - RESULTADOS - - -")
for i, contagem in enumerate(contagens, start=1):
    print(f"Quantidade de números {i}: {contagem}")