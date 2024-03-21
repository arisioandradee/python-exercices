'''
Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
Os juros e a quantidade de parcelas seguem a tabela abaixo:
Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
1       0
3       10
6       15
9       20
12      25
Exemplo de saída do programa:
Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
R$ 1.000,00     0               1                       R$  1.000,00
R$ 1.100,00     100             3                       R$    366,00
R$ 1.150,00     150             6                       R$    191,67
'''
# Dados da tabela de juros
tabela_juros = {
    1: 0,
    3: 10,
    6: 15,
    9: 20,
    12: 25
}

valor_divida = float(input('Digite o valor da dívida: '))

print("Valor da Dívida   Valor dos Juros   Quantidade de Parcelas   Valor da Parcela")

for parcelas, juros in tabela_juros.items():
    valor_juros = (valor_divida * juros) / 100
    valor_total = valor_divida + valor_juros
    valor_parcela = valor_total / parcelas
    print(f"R$ {valor_total:.2f}          R$ {valor_juros:.2f}              {parcelas}                        R$ {valor_parcela:.2f}")
