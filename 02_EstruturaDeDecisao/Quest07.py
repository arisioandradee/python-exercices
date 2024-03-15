#7. Faça um Programa que leia três números e mostre o maior e o menor deles.


print('Digite três valores:')
n1 = input()
n2 = input()
n3 = input()

#Checando maior número!
if n1 > n2 and n1 > n3:
    print(f'O maior número é {n1}')
elif n2 > n1 and n2 > n3:
    print(f'O maior número é {n2}')
elif n3 > n1 and n3 > n2:
    print(f'O maior número é {n3}')
else:
    print('Os números são iguais!')

#Checando menor número!
if n1 < n2 and n1 < n3:
    print(f'O menor número é {n1}')
elif n2 < n1 and n2 < n3:
    print(f'O menor número é {n2}')
elif n3 < n1 and n3 < n2:
    print(f'O menor número é {n3}')
else:
    print('Os números são iguais!')