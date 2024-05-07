#Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. 
    #Imprima a idade e a altura na ordem inversa a ordem lida.

idades = [0] * 5
alturas = [0] * 5

for i in range(5):
    idade = int(input('Digite a idade: '))
    idades[i] = idade

    altura = float(input('Digite a altura: '))
    alturas[i] = altura

print(idades[::-1])
print(alturas[::-1])