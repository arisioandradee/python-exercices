#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

notas = []

for i in range(5):
    nota = float(input('Digite uma nota: '))
    notas.append(nota)

media = sum(notas) / len(notas)
print(f'A médias das notas é: {media}')