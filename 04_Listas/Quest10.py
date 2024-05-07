#Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos,
    #cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

vetor1 = [0] * 10
vetor2 = [0] * 10
vetor3 = [0] * 20

for i in range(10):
    num_v1 = int(input('Digite um valor para o vetor [1]: '))
    vetor1[i] = num_v1

for i in range(10):
    num_v2 = int(input('Digite um valor para o vetor [2]: '))
    vetor2[i] = num_v2

for i in range(10):
    vetor3[2*i] = vetor1[i]  # Preenche nos índices pares
    vetor3[2*i + 1] = vetor2[i]  # Preenche nos índices ímpares

print(f'O vetor três ficou: {vetor3}')