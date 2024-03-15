#18.Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
from datetime import datetime

ano = input('Digite um ano no formato dd/mm/aaaa: ')

try:
    data = datetime.strptime(ano, "%d/%m/%Y")
    print('Data válida!')
except ValueError:
    print('Data inválida!')
