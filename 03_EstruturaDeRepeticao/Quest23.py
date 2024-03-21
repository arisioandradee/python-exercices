'''
Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo 
usuário. O programa deverá mostrar também o número de divisões que ele executou para encontrar os 
números primos. Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.
'''
N = int(input("Digite um número inteiro para encontrar todos os primos até ele: "))

primos = []
divisoes = 0

for i in range(2, N + 1):
    eh_primo = True
    for j in range(2, int(i ** 0.5) + 1):
        divisoes += 1
        if i % j == 0:
            eh_primo = False
            break
    if eh_primo:
        primos.append(i)

print("Números primos até", N, ": ", primos)
print("Número de divisões executadas: ", divisoes)

