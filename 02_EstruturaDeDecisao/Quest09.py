#9. Faça um Programa que leia três números e mostre-os em ordem decrescente.

print('Digite três valores:')
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

# Ordena os valores em ordem decrescente usando uma lista e a função sort()
valores = [n1, n2, n3]
valores.sort(reverse=True)

print(f'Ordem decrescente: {valores[0]}, {valores[1]}, {valores[2]}')
