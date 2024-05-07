#Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

vetor1 = [0] * 10
vetor2 = [0] * 10
vetor3 = [0] * 10
vetor4 = [0] * 30

for i in range(10):
    num_v1 = int(input('Digite um valor para o vetor [1]: '))
    vetor1[i] = num_v1

for i in range(10):
    num_v2 = int(input('Digite um valor para o vetor [2]: '))
    vetor2[i] = num_v2

for i in range(10):
    num_v3 = int(input('Digite um valor para o vetor [2]: '))
    vetor3[i] = num_v3

for i in range(10):
    vetor4[3*i] = vetor1[i]   # Preenche nos índices múltiplos de 3
    vetor4[3*i + 1] = vetor2[i]  # Preenche nos índices que são um a mais que múltiplos de 3
    vetor4[3*i + 2] = vetor3[i]  # Preenche nos índices que são dois a mais que múltiplos de 3

print(f'O vetor resultante ficou: {vetor4}')