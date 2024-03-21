#Faça um programa que leia 5 números e informe o maior número.

maior_numero = None

for _ in range(5):
    numero = float(input("Digite um número: "))

    if maior_numero is None or numero > maior_numero:
        maior_numero = numero

print(f"O maior número digitado é: {maior_numero}")

