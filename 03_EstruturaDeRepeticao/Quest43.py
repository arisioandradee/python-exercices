'''
O cardápio de uma lanchonete é o seguinte:
Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00
Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. 
Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. 
Considere que o cliente deve informar quando o pedido deve ser encerrado.
'''

# Dicionário com os códigos e preços dos produtos
cardapio = {
    100: 1.20,
    101: 1.30,
    102: 1.50,
    103: 1.20,
    104: 1.30,
    105: 1.00
}

total_pedido = 0

print('Seja bem-vindo! (Digite 0 para encerrar)')

while True:
    cod = int(input('Digite o código do produto: '))
    
    if cod == 0:
        break
    
    if cod not in cardapio:
        print('Código inválido. Tente novamente.')
        continue
    
    qtd = int(input('Digite a quantidade do produto: '))
    
    pagar = cardapio[cod] * qtd
    print(f'O valor a pagar por esse produto é: R$ {pagar:.2f}')
    total_pedido += pagar

# Imprime o total do pedido
print(f'O valor total a pagar é R$ {total_pedido:.2f}')
