'''
Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber qual
o melhor jogador após cada jogo. Para isto, faz-se necessário o desenvolvimento de um programa, que 
será utilizado pelas telefonistas, para a computação dos votos. Sua equipe foi contratada para 
desenvolver este programa, utilizando a linguagem de programação C++. Para computar cada voto, 
a telefonista digitará um número, entre 1 e 23, correspondente ao número da camisa do jogador. 
Um número de jogador igual zero, indica que a votação foi encerrada. Se um número inválido for digitado,
o programa deve ignorá-lo, mostrando uma breve mensagem de aviso, e voltando a pedir outro número. 
Após o final da votação, o programa deverá exibir:
O total de votos computados;
Os númeos e respectivos votos de todos os jogadores que receberam votos;
O percentual de votos de cada um destes jogadores;
O número do jogador escolhido como o melhor jogador da partida, juntamente com o número de votos e o percentual de votos dados a ele.
'''
qtd_votos = 0
votos_por_jogador = [0] * 24  # Índice 0 não será usado, então reservamos espaço para 23 jogadores

print('Enquete: Quem foi o melhor jogador?')

while True:
    voto = int(input('Número do jogador (0 = fim): '))
    
    if voto == 0:
        break

    if voto < 1 or voto > 23:
        print('Informe um valor entre 1 e 23 ou 0 para sair.')
        continue

    qtd_votos += 1
    votos_por_jogador[voto] += 1

print(f'Foram computados {qtd_votos} votos.')

print('Resultado da votação:')
for jogador in range(1, 24):
    votos = votos_por_jogador[jogador]
    if votos > 0:
        percentual = (votos / qtd_votos) * 100
        print(f'Jogador número {jogador}: {votos} voto(s) ({percentual:.2f}%)')

melhor_jogador = votos_por_jogador.index(max(votos_por_jogador))
votos_melhor_jogador = votos_por_jogador[melhor_jogador]
percentual_melhor_jogador = (votos_melhor_jogador / qtd_votos) * 100

print(f'O melhor jogador foi o número {melhor_jogador} com {votos_melhor_jogador} voto(s) '
      f'({percentual_melhor_jogador:.2f}% dos votos).')
