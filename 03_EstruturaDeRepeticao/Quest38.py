'''
Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano
 anterior. Faça um programa que determine o salário atual desse funcionário. Após concluir isto, 
 altere o programa permitindo que o usuário digite o salário inicial do funcionário.
'''

'''
from decimal import Decimal

percentual = Decimal('0.15')
salario = Decimal('1000.00')
ano_inicial = 1996
ano_atual = 2024

while ano_inicial <= ano_atual:
    aumento = salario * percentual
    salario += aumento
    ano_inicial += 1
    print(f"Ano: {ano_inicial}, Salário: {salario:.2f}, Aumento: {aumento:.2f}")
'''
from decimal import Decimal

ano = 1995
ano_atual = 2024
aumento_porcentagem = Decimal('1.5') / 100

salario = Decimal(input("Digite o salário inicial do funcionário: "))

while ano < ano_atual:
    ano += 1
    salario += salario * aumento_porcentagem
    aumento_porcentagem *= 2

print(f"O salário em {ano} é de R$ {salario:.2f}")