'''
Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve 
perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim 
calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar 
o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos 
terem respondido informar:
Maior e Menor Acerto;
Total de Alunos que utilizaram o sistema;
A Média das Notas da Turma.
Gabarito da Prova:

01 - A
02 - B
03 - C
04 - D
05 - E
06 - E
07 - D
08 - C
09 - B
10 - A
'''

gabarito = {
    1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E',
    6: 'E', 7: 'D', 8: 'C', 9: 'B', 10: 'A'
}

maior_acerto = 0
menor_acerto = 10
total_alunos = 0
soma_notas = 0

while True:
    respostas_aluno = {}
    acertos = 0

    for num_questao in range(1, 11):
        resposta = input(f'Digite a resposta da questão {num_questao}: ')
        respostas_aluno[num_questao] = resposta.upper()

    for num_questao, resposta_aluno in respostas_aluno.items():
        if resposta_aluno == gabarito[num_questao]:
            acertos += 1

    total_alunos += 1
    soma_notas += acertos

    if acertos > maior_acerto:
        maior_acerto = acertos

    if acertos < menor_acerto:
        menor_acerto = acertos

    continuar = input('Outro aluno vai utilizar o sistema? (S/N): ').upper()
    if continuar != 'S':
        break

media_notas = soma_notas / total_alunos

print(f'Maior acerto: {maior_acerto}')
print(f'Menor acerto: {menor_acerto}')
print(f'Total de alunos: {total_alunos}')
print(f'Média das notas da turma: {media_notas:.2f}')