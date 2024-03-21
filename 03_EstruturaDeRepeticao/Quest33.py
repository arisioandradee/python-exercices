'''
O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um 
conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas,
bem como a média das temperaturas.
'''
menor_temp = float('inf') 
maior_temp = float('-inf') 

temperatura = []

print("Digite as temperaturas (digite '0' para sair):")

while True:
    temp = float(input("Digite a temperatura: "))
    if temp == 0:
        break
    temperatura.append(temp)

    if temp < menor_temp:
        menor_temp = temp

    if temp > maior_temp:
        maior_temp = temp

if not temperatura:
    print("Nenhuma temperatura foi inserida.")
else:
    print(f"A menor temperatura é: {menor_temp}")
    print(f"A maior temperatura é: {maior_temp}")
