'''
Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                          Até 5 Kg           Acima de 5 Kg
    Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
    Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
    Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá 
    ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morango
    s e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente. 
'''

qtd_morango = float(input('Digite a quantidade de quilos de morango: '))
qtd_maca = float(input('Digite a quantidade de quilos de maçã: '))

preco_morango = 0
preco_maca = 0

if qtd_morango <= 5:
    preco_morango = qtd_morango * 2.50
else:
    preco_morango = qtd_morango * 2.20

if qtd_maca <= 5:
    preco_maca = qtd_maca * 1.80
else:
    preco_maca = qtd_maca * 1.50

valor_total = preco_morango + preco_maca

if qtd_morango + qtd_maca > 8 or valor_total > 25:
    desconto = valor_total * 0.10
    valor_total -= desconto
    print(f'Você ganhou um desconto de R${desconto:.2f} reais')

print(f'O valor total a ser pago é R${valor_total:.2f} reais')
