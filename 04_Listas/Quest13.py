#Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após 
#isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, 
#e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 
         'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

temperaturas = [0] * 12
total_temp = 0

for i in range(12):
    temp = float(input(f'Digite a temperatura de {meses[i]}: '))
    temperaturas[i] = temp
    total_temp += temp

media = total_temp / 12
print(f'A média anual de temperatura é: {media:.2f}°C.')

print("Temperaturas acima da média anual:")
for i in range(12):
    if temperaturas[i] > media:
        print(f'{meses[i]}: {temperaturas[i]}°C')
