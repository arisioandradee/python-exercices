#A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... 
    #Faça um programa que gere a série até que o valor seja maior que 500.

posicao = 1
numero_anterior = 0
num = 500

while numero_anterior <= num:
    print(posicao)
    aux = posicao
    posicao += numero_anterior
    numero_anterior = aux

