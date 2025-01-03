'''
Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:
"Qual o melhor Sistema Operacional para uso em servidores?"

As possíveis respostas são:

1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro
Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma.
 O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados num vetor. Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:
Sistema Operacional     Votos   %
-------------------     -----   ---
Windows Server           1500   17%
Unix                     3500   40%
Linux                    3000   34%
Netware                   500    5%
Mac OS                    150    2%
Outro                     150    2%
-------------------     -----
Total                    8800

O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.
'''

votos = {
    "Windows Server": 0,
    "Unix": 0,
    "Linux": 0,
    "Netware": 0,
    "Mac OS": 0,
    "Outros": 0,
    "Nulos": 0,
}

print('Qual o melhor Sistema Operacional para uso em servidores?')
print('1- Windows Server')
print('2- Unix')
print('3- Linux')
print('4- Netware')
print('5- Mac OS')
print('6- Outro')
print("0- Encerrar votação")

while True:
    escolha = int(input("Digite sua escolha (ou 0 para encerrar): "))

    if escolha == 0:
        break
    elif escolha == 1:
        votos["Windows Server"] += 1
    elif escolha == 2:
        votos["Unix"] += 1
    elif escolha == 3:
        votos["Linux"] += 1
    elif escolha == 4:
        votos["Netware"] += 1
    elif escolha == 5:
        votos["Mac OS"] += 1
    elif escolha == 6:
        votos["Outros"] += 1
    else:
        votos["Nulos"] += 1

# Cálculo do total de votos válidos
total_votos_validos = sum(votos.values()) - votos["Nulos"]

for sistema, qtd_votos in votos.items():
    if sistema == "Nulos":
        continue
    porcentagem = (qtd_votos / total_votos_validos * 100) if total_votos_validos > 0 else 0
    print(f"{sistema:<15} {qtd_votos:<6} {porcentagem:>6.2f}%")

print(f"\nTotal de votos nulos: {votos['Nulos']}")