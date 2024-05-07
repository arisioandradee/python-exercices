'''
Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente".
'''

resultado = ['Inocente', 'Suspeita', 'Cúmplice', 'Assassino']

count = 0

p1 = input('Telefonou para a vítima? ').lower()
if p1 == 'y':
    count += 1 

p2 = input('Esteve no local do crime? ').lower()
if p2 == 'y':
    count += 1 

p3 = input('Mora perto da vítima? ').lower()
if p3 == 'y':
    count += 1 

p4 = input('Devia para a vítima? ').lower()
if p4 == 'y':
    count += 1 

p5 = input('Já trabalhou com a vítima? ').lower()
if p5 == 'y':
    count += 1 

if count == 2:
    print(resultado[1])
elif 3 <= count <= 4:
    print(resultado[2])
elif count == 5:
    print(resultado[3])
else:
    print(resultado[0])

