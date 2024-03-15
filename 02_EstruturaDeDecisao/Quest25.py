'''
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
    "Telefonou para a vítima?"
    "Esteve no local do crime?"
    "Mora perto da vítima?"
    "Devia para a vítima?"
    "Já trabalhou com a vítima?" 
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente". 
'''

print('Você está sendo interrogado, responda "s" ou "n"! ')
p1 = input('Telefonou para a vítima? ').lower()
p2 = input('Esteve no local do crime? ').lower()
p3 = input('Mora perto da vítima? ').lower()
p4 = input('Devia para a vítima? ').lower()
p5 = input('Já trabalhou com a vítima? ').lower()

respostas_positivas = 0

if p1 == 's':
    respostas_positivas += 1
if p2 == 's':
    respostas_positivas += 1
if p3 == 's':
    respostas_positivas += 1
if p4 == 's':
    respostas_positivas += 1
if p5 == 's':
    respostas_positivas += 1

if respostas_positivas == 2:
    print("Classificação: Suspeita")
elif 3 <= respostas_positivas <= 4:
    print("Classificação: Cúmplice")
elif respostas_positivas == 5:
    print("Classificação: Assassino")
else:
    print("Classificação: Inocente")


