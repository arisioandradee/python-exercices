#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

num = int(input('Digite o número que deseja descobrir o fatorial: '))

resultado = 1
fato = num

while fato > 1:
    resultado *= fato
    fato -= 1

print(f"O fatorial de {num} é: {resultado}")
