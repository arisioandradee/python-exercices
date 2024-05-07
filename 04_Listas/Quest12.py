#Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com 
 #mais de 13 anos possuem altura inferior à média de altura desses alunos

alunos = [[0,0]] * 30
total_altura = 0
count = 0

for i in range(30):
    idade = int(input('Digite uma idade: '))
    altura = float(input('Digite uma altura: '))
    alunos.append((idade, altura))

    total_altura += altura
    media = total_altura / 30

    if idade > 13:
        if altura > media:
            count += 1
        else:
            count += 0
    else:
        count += 0

print(f'A quantidade de alunos com mais de 13 anos e altura superior a média é: {count}')