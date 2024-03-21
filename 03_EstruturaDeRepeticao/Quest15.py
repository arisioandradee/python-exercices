#A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo. 

num = int(input('Digite até qual posição irá a série de Fibonacci: '))

posicao = 1
numero_anterior = 0

for _ in range(num):
    print(posicao)
    aux = posicao
    posicao += numero_anterior
    numero_anterior = aux
