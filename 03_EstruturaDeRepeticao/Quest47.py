'''
Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes. Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados alcançadas pelo atleta em sua apresentação e depois informe a sua média, conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média com as notas restantes). As notas não são informados ordenadas. Um exemplo de saída do programa deve ser conforme o exemplo abaixo:
Atleta: Aparecido Parente
Nota: 9.9
Nota: 7.5
Nota: 9.5
Nota: 8.5
Nota: 9.0
Nota: 8.5
Nota: 9.7

Resultado final:
Atleta: Aparecido Parente
Melhor nota: 9.9
Pior nota: 7.5
Média: 9,04
'''
while True:
    nome_ginasta = input("Digite o nome do ginasta (ou deixe em branco para sair): ")
    if not nome_ginasta:
        break

    notas = []
    for i in range(7):
        nota = float(input(f"Digite a nota do {i+1}º jurado: "))
        notas.append(nota)

    melhor_nota = max(notas)
    pior_nota = min(notas)
    notas.remove(melhor_nota)
    notas.remove(pior_nota)
    media_notas = sum(notas) / len(notas)

    print("\nResultado final:")
    print(f"Atleta: {nome_ginasta}")
    print(f"Melhor nota: {melhor_nota}")
    print(f"Pior nota: {pior_nota}")
    print(f"Média: {media_notas:.2f}\n")
