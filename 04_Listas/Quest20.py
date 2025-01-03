'''
As Organizações Tabajara resolveram dar um abono aos seus colaboradores em reconhecimento ao bom resultado alcançado durante o ano que passou. Para isto contratou você para desenvolver a aplicação que servirá como uma projeção de quanto será gasto com o pagamento deste abono.
Após reuniões envolvendo a diretoria executiva, a diretoria financeira e os representantes do sindicato laboral, chegou-se a seguinte forma de cálculo:
a.Cada funcionário receberá o equivalente a 20% do seu salário bruto de dezembro; a.O piso do abono será de 100 reais, isto é, aqueles funcionários cujo salário for muito baixo, recebem este valor mínimo; Neste momento, não se deve ter nenhuma preocupação com colaboradores com tempo menor de casa, descontos, impostos ou outras particularidades. Seu programa deverá permitir a digitação do salário de um número indefinido (desconhecido) de salários. Um valor de salário igual a 0 (zero) encerra a digitação. Após a entrada de todos os dados o programa deverá calcular o valor do abono concedido a cada colaborador, de acordo com a regra definida acima. Ao final, o programa deverá apresentar:
O salário de cada funcionário, juntamente com o valor do abono;
O número total de funcionário processados;
O valor total a ser gasto com o pagamento do abono;
O número de funcionário que receberá o valor mínimo de 100 reais;
O maior valor pago como abono; A tela abaixo é um exemplo de execução do programa, apenas para fins ilustrativos. Os valores podem mudar a cada execução do programa.
'''
salarios, abonos = [], []

while True:
    salario = float(input('Salário: '))

    if salario == 0:
        break

    abono = max(salario * 0.20, 100)
    salarios.append(salario)
    abonos.append(abono)

    abonos_minimos = sum(1 for abono in abonos if abono == 100)

print('Salário     -    Abono')
for salario, abono in zip(salarios, abonos):
        print(f"R$ {salario:7.2f} - R$ {abono:7.2f}")

print(f'Foram processados {len(salarios)} colaboradores')
print(f'Total gasto com abonos: R${sum(abonos)}')
print(f'Valor mínimo pago a {abonos_minimos} colaboradores')
print(f'Maior valor de abono pago: R${max(abonos)}')