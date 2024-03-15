'''
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                          Até 5 Kg           Acima de 5 Kg
    File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
    Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
    Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

    Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, 
    porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o 
    cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo 
    e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra
    : tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar. 
'''

print('Bem-vindo ao Tabajara! Escolha um tipo de carne para comprar: ')
print('[1] Filé Duplo | [2] Alcatra | [3] Picanha')
escolha = int(input('Escolha o tipo de carne: '))
quantidade = float(input('Digite a quantidade em quilos: '))

# Definição dos preços por tipo e quantidade de carne
if escolha == 1:
    preco = 4.90 if quantidade <= 5 else 5.80
    tipo_carne = 'Filé Duplo'
elif escolha == 2:
    preco = 5.90 if quantidade <= 5 else 6.80
    tipo_carne = 'Alcatra'
elif escolha == 3:
    preco = 6.90 if quantidade <= 5 else 7.80
    tipo_carne = 'Picanha'
else:
    print('Escolha inválida!')
    exit()

# Cálculo do valor total
valor_total = preco * quantidade

# Verificação de desconto com o cartão Tabajara
cartao_tabajara = input('Você possui nosso cartão? [S] Sim | [N] Não: ')
desconto = 0
if cartao_tabajara.upper() == 'S':
    desconto = valor_total * 0.05
    valor_total -= desconto

# Impressão do cupom fiscal
print("\nCUPOM FISCAL")
print(f"Tipo de Carne: {tipo_carne}")
print(f"Quantidade: {quantidade} Kg")
print(f"Preço total: R${valor_total:.2f}")
print(f"Tipo de pagamento: {'Cartão Tabajara' if cartao_tabajara.upper() == 'S' else 'Dinheiro'}")
print(f"Desconto: R${desconto:.2f}")
print(f"Valor a pagar: R${valor_total:.2f}")
