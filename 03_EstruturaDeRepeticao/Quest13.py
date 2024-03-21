#Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. 
#Não utilize a função de potência da linguagem.

base = int(input('Digite a (BASE): '))
expoente = int(input('Digite o (EXPOENTE): '))

resultado = 0

for a in range(expoente):
    resultado = base * expoente

print(resultado)