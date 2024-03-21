#Altere o programa anterior para mostrar no final a soma dos números.

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

soma = 0

if n1 > n2:
    for i in range(n2, n1):
        print(i)
        soma += i
elif n2 > n1:
    for i in range(n1, n2):
        print(i)
        soma += i
else: 
    print('Os valores são iguais!')

print(f'A soma dos números é: {soma}')