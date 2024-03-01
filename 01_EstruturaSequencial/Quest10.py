# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

cel = input('Digite o grau em Celcius: ')
cel = float(cel)
fah = (cel * (9/5)) + 32

print(f'A quantidade de graus após converter é: {fah:.2f}°F')
