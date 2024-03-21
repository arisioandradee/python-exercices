'''
Faça um programa que leia e valide as seguintes informações:
    Nome: maior que 3 caracteres;
    Idade: entre 0 e 150;
    Salário: maior que zero;
    Sexo: 'f' ou 'm';
    Estado Civil: 's', 'c', 'v', 'd'; 
'''
#Validando nome
nome = input('Digite seu nome: ')

while len(nome) < 3:
    print('O nome deve possuir mais de 3 caracteres: ')
    nome = input('Digite seu nome: ')

#Validando idade
idade = int(input('Digite sua idade: '))

while idade <= 0 or idade >= 150:
    print('A idade deve estar no intervalo entre 0 e 150!')
    idade = input('Digite sua idade: ')

#Validando salário
salario = float(input("Digite seu salário: "))

while salario < 0:
    print('Valor negado, deve ser maior que zero!')
    salario = float(input("Digite seu salário: "))

#Validando genero
genero = input("Digite seu genero (F)eminino ou (M)asculino: ").lower()

while genero not in ['f', 'm']:
    print("Genero não permitido! ")
    genero = input("Digite seu genero (F)eminino ou (M)asculino: ").lower()

#Validando estado civil
estado_civil = input("Estado Civil: 's', 'c', 'v', 'd': ").lower()

while estado_civil not in['s', 'c', 'v', 'd']:
    print("Estado civil não permitido! ")
    estado_civil = input("Estado Civil: 's', 'c', 'v', 'd': ").lower()