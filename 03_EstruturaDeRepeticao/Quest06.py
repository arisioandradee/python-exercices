#Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele mostre os números um ao lado do outro.


#Um abaixo do outro:
num = 0
while num < 20:
    num += 1
    print(num)

# Imprimindo os números de 1 a 20 ao lado do outro
for numero in range(1, 21):
    print(numero, end=' ')

    