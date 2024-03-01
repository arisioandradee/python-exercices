# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

lado = input('Digite o tamanho do lado do quadrado: ')
lado = float(lado)

area = lado ** 2

print(f'A área do quadrado é: {area}')
print(f'O dobro desta área é: {area * 2}')
