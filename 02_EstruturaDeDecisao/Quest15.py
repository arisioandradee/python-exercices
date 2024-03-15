'''
Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. 
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
    Dicas:
    Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
    Triângulo Equilátero: três lados iguais;
    Triângulo Isósceles: quaisquer dois lados iguais;
    Triângulo Escaleno: três lados diferentes; 
'''

print('Digite os valores dos lados do triângulo: ')
v1 = float(input())
v2 = float(input())
v3 = float(input())

if v1 == v2 and v1 == v3:
    print('Triângulo Equilátero')
elif v1 == v2 or v1 == v2:
    print('Triângulo Isósceles')
else:
    print('Triângulo Escaleno')