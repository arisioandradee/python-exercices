'''
Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc). Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro de combustível. Calcule e mostre:
O modelo do carro mais econômico;
Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros e quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro. Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa
'''
carros = []
consumos = []
litros = []
valores = []

for i in range(5):
    print(f'Veículo {i+1}')
    carro = input('Nome: ')
    consumo = float(input('Km por litro: '))

    carros.append(carro)
    consumos.append(consumo)

    consumoReal = 1000 / consumo
    valor = consumoReal * 2.25

    litros.append(consumoReal)
    valores.append(valor)

print('RELATÓRIO FINAl:   ')
for carro, consumo, litro, valor in zip(carros,consumos,litros,valores):
    print(f'{i+1} - {carro}   -  {consumo}km/l  -  {litro:.2f} litros -  R${valor:.2f}')

menorValor = min(litros)
indice = litros.index(menorValor)
carroCorrespodente = carros[indice]

print(f'O menor consumo é do {carroCorrespodente}')