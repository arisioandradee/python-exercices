'''
Faça um programa que calcule o número médio de alunos por turma. 
Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. 
As turmas não podem ter mais de 40 alunos.
'''
total_alunos = 0
quantidade_turma = int(input('Digite a quantidade de turmas: '))

for n in range(quantidade_turma):
    quantidade_aluno = int(input('Digite a quantidade de alunos em cada turma :'))

    if quantidade_aluno > 40:
        print('Erro!')
    else:
        total_alunos += quantidade_aluno

#print(total_alunos)
media = total_alunos / quantidade_turma
print(f'A média de alunos por turma é: {media:.2f}')


