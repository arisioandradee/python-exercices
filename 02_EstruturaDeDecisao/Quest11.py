'''
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para calculará os reajustes.
    Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
    salários até R$ 280,00 (incluindo) : aumento de 20%
    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:

'''

salario = input('Digite seu salário: ')
salario = float(salario)

if salario <= 280:
    reajuste = 0.20
    aumento = salario * reajuste
    novo_salario = salario + aumento
elif salario > 280 and salario <= 700:
    reajuste = 0.15
    aumento = salario * reajuste
    novo_salario = salario + aumento
elif salario > 700 and salario <= 1500:
    reajuste = 0.10
    aumento = salario * reajuste
    novo_salario = salario + aumento
elif salario > 1500:
    reajuste = 0.05
    aumento = salario * reajuste
    novo_salario = salario + aumento

print(f'Seu salário antes do reajuste era: R${salario},00')
print(f'O percentual de aumento aplicado foi: {reajuste*100}%')
print(f'O aumento do seu salário foi de: R${aumento},00')
print(f'O valor do seu novo salário é: R${novo_salario},00')
