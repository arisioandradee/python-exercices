#Faça um programa que leia 5 números e informe a soma e a média dos números.

cont = 0
soma = 0
media = 0

for cont in range(5):
    num = int(input('Digite um número: '))
    soma += num

media = soma / 5

print(f'A soma dos valores é: {soma}')
print(f'A média dos valores é: {media}')