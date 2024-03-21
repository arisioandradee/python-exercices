'''
Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média
 de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem
 , adulta ou idosa, conforme a média calculada.
'''

media = 0
cont = 0
soma = 0

qtd_turma = int(input('Quantos alunos tem na turma? '))

for i in range(qtd_turma):
    idade = float(input('Digite uma idade: '))
    cont += 1
    soma =+ idade

media = idade/cont

if media >= 0 and media <= 25:
    print('Turma jovem!')
elif media >= 26 and media <= 60:
    print('Turma adulta!')
else:
    print('Turma idosa!')
