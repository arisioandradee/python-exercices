#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

nome = input('Digite seu nome de usuário: ')
senha = input('Digite sua senha: ')

while nome == senha:
    print('Não é permitido o nome de usuário ser igual a senha!')
    nome = input('Digite seu nome de usuário: ')
    senha = input('Digite sua senha: ')

print('Nome de usuário e senha válidos!')