#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. 
    #A saída deve ser conforme o exemplo abaixo:
    #Fatorial de: 5 / #5! =  5 . 4 . 3 . 2 . 1 = 120
resultado = 1
count = 1

numero = int(input('Digite um número: '))

while count <= numero:
    resultado *= count
    count += 1

print(f'Fatorial de {numero}: {resultado}') 