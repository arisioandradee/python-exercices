#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. 
#Valide a entrada e permita repetir a operação.
 
print('Digite a população e a taxa de crescimento da cidade A: ')
populacao_a = float(input(""))
taxa_a = float(input(""))

print('Digite a população e a taxa de crescimento da cidade B: ')
populacao_b = float(input(""))
taxa_b = float(input(""))

ano = 0 

if populacao_a >= populacao_b:
    print("A população da cidade A já é maior ou igual à população da cidade B.")
else:
    while populacao_a < populacao_b:
        populacao_a = populacao_a + populacao_a * taxa_a
        populacao_b = populacao_b + populacao_b * taxa_b
        ano += 1

print(f'A cidade A levará {ano} anos para ultrapassar a cidade B!')