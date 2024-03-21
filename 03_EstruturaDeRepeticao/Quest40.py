'''
Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. 
Foram obtidos os seguintes dados:
Código da cidade;
Número de veículos de passeio (em 1999);
Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
Qual a média de veículos nas cinco cidades juntas;
Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.
'''
codigos = []
veiculos = []
acidentes = []
acidentes_2000 = []

maior_indice = 0
menor_indice = float('inf')

while len(acidentes) < 5:
    cod_cidade = int(input('Digite o código da cidade: '))
    codigos.append(cod_cidade)
    num_veiculos = int(input('Digite o número de veiculos: '))
    veiculos.append(num_veiculos)
    num_acidentes = int(input('Digite o número de acidentes: '))
    acidentes.append(num_acidentes)

    if num_acidentes > maior_indice:
        maior_cod = cod_cidade
        maior_indice = num_acidentes

    if num_acidentes < menor_indice:
        menor_cod = cod_cidade
        menor_indice = num_acidentes

    if num_veiculos < 2000:
        acidentes_2000.append(num_acidentes)

# Qual o maior e menor índice de acidentes de trânsito e a que cidade pertence;
print(f'O maior índice de acidentes é {maior_indice} e pertence à cidade de código {maior_cod}')
print(f'O menor índice de acidentes é {menor_indice} e pertence à cidade de código {menor_cod}')

# Qual a média de veículos nas cinco cidades juntas;
media_veiculos = sum(veiculos) / len(veiculos)
print(f'A média de veículos nas cinco cidades é {media_veiculos}')

# Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.
if acidentes_2000:
    media_acidentes_2000 = sum(acidentes_2000) / len(acidentes_2000)
    print(f'A média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio é {media_acidentes_2000}')
else:
    print('Não há cidades com menos de 2.000 veículos de passeio.')
