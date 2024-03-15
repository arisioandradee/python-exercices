#3. Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
#Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.


letra = input('Digite a letra que representa o genero: ')
letra = letra.lower()

if letra == 'f':
    print("A letra representa o genero feminino!")
elif letra == 'm':
    print("A letra representa o genero masculino!")
else:
    print("A letra não representa nenhum genero!")