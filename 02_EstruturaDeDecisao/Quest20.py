''' 
20.Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
    A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
    A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
    A mensagem "Aprovado com Distinção", se a média for igual a 10. 
'''

print('Digite as notas: ')
n1 = float(input())
n2 = float(input())
n3 = float(input())

media = (n1 + n2 +n3)/3

if media >= 7 and media < 10:
    print(f'Aluno aprovado! Média:{media}')
elif media >= 10:
    print(f'Aluno aprovado com Distinção! Média:{media}')
else:
    print(f'Aluno reprovado! Média:{media}')