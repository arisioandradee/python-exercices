#Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

consoantes = []
vogais = ['a', 'e', 'i', 'o', 'u']

count_consoantes = 0

for i in range(10):
    letra = input('Digite uma letra: ')

    if letra not in vogais:
        consoantes.append(letra)
        count_consoantes += 1
        
print(f'A quantidade de consoantes foi {count_consoantes} e as letras são {consoantes}')

