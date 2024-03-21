'''
Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, 
a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes 
da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o 
usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informados os códigos
e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas
e dos pesos dos clientes
'''
codigos = []
alturas = []
pesos = []

menor_altura = float('inf')
maior_altura = float('-inf')

menor_peso = float('inf')
maior_peso = float('-inf')

print('Bem-vindo ao sistema! Digite 0 no campo código para cancelar.')

while True:
    codigo = int(input('Digite seu código: '))
    if codigo == 0:
        break
    
    alt = float(input('Digite sua altura em metros: '))
    alturas.append(alt)

    if alt < menor_altura:
        menor_altura = alt
        codigo_menor_altura = codigo
    if alt > maior_altura:
        maior_altura = alt
        codigo_maior_altura = codigo

    peso = float(input('Digite seu peso em quilogramas: '))
    pesos.append(peso)

    if peso < menor_peso:
        menor_peso = peso
        codigo_menor_peso = codigo
    if peso > maior_peso:
        maior_peso = peso
        codigo_maior_peso = codigo

media_altura = sum(alturas) / len(alturas)
media_peso = sum(pesos) / len(pesos)

print("\nCliente mais alto:")
print("Código:", codigo_maior_altura)
print("Altura:", maior_altura, "m")
print("\nCliente mais baixo:")
print("Código:", codigo_menor_altura)
print("Altura:", menor_altura, "m")
print("\nCliente mais gordo:")
print("Código:", codigo_maior_peso)
print("Peso:", maior_peso, "kg")
print("\nCliente mais magro:")
print("Código:", codigo_menor_peso)
print("Peso:", menor_peso, "kg")
print("\nMédia das alturas:", media_altura, "m")
print("Média dos pesos:", media_peso, "kg")


