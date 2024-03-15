'''
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
    Desconto do IR:
    Salário Bruto até 900 (inclusive) - isento
    Salário Bruto até 1500 (inclusive) - desconto de 5%
    Salário Bruto até 2500 (inclusive) - desconto de 10%
    Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.

            Salário Bruto: (5 * 220)        : R$ 1100,00
            (-) IR (5%)                     : R$   55,00  
            (-) INSS ( 10%)                 : R$  110,00
            FGTS (11%)                      : R$  121,00
            Total de descontos              : R$  165,00
            Salário Liquido                 : R$  935,00

'''

valor_hora = float(input('Digite o valor da hora: '))
qtd_hora = float(input('Digite o valor da hora trabalhada: '))

salario = valor_hora * qtd_hora
salario = float(salario)

if salario <= 900:
    ir = 0
    inss = salario * 0.10
    fgts = salario * 0.11
elif salario > 900 and salario <= 1500:
    ir = salario * 0.05
    inss = salario * 0.10
    fgts = salario * 0.11
elif salario > 1500 and salario <= 2500:
    ir = salario * 0.10
    inss = salario * 0.10
    fgts = salario * 0.11
elif salario > 2500:
    ir = salario * 0.20
    inss = salario * 0.10
    fgts = salario * 0.11

total_desc = (ir + inss)
salario_lqd = salario - total_desc

#Tela de resposta!
print(f'Salário Bruto: R${salario:.2f}')
print(f'(-) IR: ({ir:.2f})')
print(f'(-) INSS: ({inss:.2f})')
print(f'(-) FGTS: ({fgts:.2f})')
print(f'Total de descontos: R${total_desc:.2f}')
print(f'Salário liquido: R${salario_lqd:.2f}')