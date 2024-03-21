#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

valor = int(input("Digite um número entre 0 e 10: "))

while valor >= 0 and valor <= 10:
    valor = int(input("Digite um número entre 0 e 10: "))

print('O valor não está no intervalo entre 0 e 10!')