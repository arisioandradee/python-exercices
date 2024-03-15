'''
Um posto está vendendo combustíveis com a seguinte tabela de descontos:
    Álcool:
    até 20 litros, desconto de 3% por litro
    acima de 20 litros, desconto de 5% por litro
    Gasolina:
    até 20 litros, desconto de 4% por litro
    acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos,
    o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor 
    a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool
    é R$ 1,90. 
'''

escolha = int(input('Digite: [1]Álcool [2]Gasolina: '))
qntd = float(input('Digite a quantidade em litros: '))

litro_gaso = 2.50
litro_alcool = 1.90

if escolha == 1:
    if qntd <= 20:
        desconto = (litro_alcool * 0.03) * qntd
        print(f'Seu desconto é: R${desconto} reais')
    else:
        desconto = (litro_alcool * 0.05) * qntd
        print(f'Seu desconto é: R${desconto} reais')     
elif escolha ==2:
    if qntd <= 20:
        desconto = (litro_gaso * 0.04) * qntd
        print(f'Seu desconto é: R${desconto} reais')
    else:
        desconto = (litro_gaso * 0.06) * qntd
        print(f'Seu desconto é: R${desconto} reais')   
else:
    print('Opção inválida!')