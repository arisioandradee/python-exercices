'''
Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos
existentes entre 1 e um número inteiro informado pelo usuário.
'''
try:
    limit = int(input("Digite um número inteiro para encontrar os números primos até esse limite: "))
    if limit < 2:
        print("Por favor, insira um número inteiro maior ou igual a 2.")
    else:
        prime_numbers = []

        for num in range(2, limit + 1):
            is_prime = True
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                prime_numbers.append(num)

        print(f"Números primos até {limit}:")
        print(prime_numbers)

except ValueError:
    print("Por favor, insira um número inteiro válido.")
