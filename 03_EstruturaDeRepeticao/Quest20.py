#Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a 
    #números inteiros positivos e menores que 16.

qtd_vezes = int(input('Digite quantas vezes você deseja calcular o fatorial: '))

for i in range(qtd_vezes):
    num = int(input('Digite o número que deseja descobrir o fatorial: '))

    if num > 0 and num <=16:
        resultado = 1
        fato = num

        while fato > 1:
            resultado *= fato
            fato -= 1

        print(f"O fatorial de {num} é: {resultado}")
    else:
        print('Números fora do intervalo!')

