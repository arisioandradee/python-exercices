'''15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
    quanto pagou ao INSS.
    quanto pagou ao sindicato.
    o salário líquido.
    calcule os descontos e o salário líquido, conforme a tabela abaixo:
    + Salário Bruto : R$
    - IR (11%) : R$
    - INSS (8%) : R$
    - Sindicato ( 5%) : R$
    = Salário Liquido : R$
    Obs.: Salário Bruto - Descontos = Salário Líquido.'''

valor_hora = float(input('Digite o valor ganho por hora trabalhada: '))
num_horas = float(input('Digite o valor de horas trabalhadas: '))
qtd_dias = float(input('Digite a quantidade de dias de trabalho: '))

salario = (valor_hora * num_horas) * qtd_dias

imposto = (salario * 0.11)
inss = (salario * 0.08)
sindicato = (salario * 0.05)
salario_liquido = salario - (imposto + inss + sindicato)

print(f'+ Salário Bruto : R${salario:.2f}')
print(f'- IR (11%) : R${imposto}')
print(f'- INSS (8%) : R${inss}')
print(f'- Sindicato ( 5%) : R${sindicato}')
print(f'= Salário Liquido : R${salario_liquido}')