# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#C = 5 * ((F-32) / 9).

fah = input('Digite o grau em Fahrenheit: ')
fah = float(fah)
cel = 5 * ((fah - 32) / 9)

print(f'A quantidade de graus após converter é: {cel:.2f}°C')