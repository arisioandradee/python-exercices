#Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

notas = [0] * 10
aprovados = 0

for n in notas:
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunda nota: '))
    n3 = float(input('Digite a terceira nota: '))
    n4 = float(input('Digite a quarta nota: '))

    media = (n1 + n2 + n3 + n4) / 4

    if media >= 7.0:
        aprovados += 1

print(f'O número de aprovados é: {aprovados}')