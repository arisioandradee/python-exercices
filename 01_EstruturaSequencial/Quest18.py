#18.Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
#calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tam_arquivo = float(input('Digite o tamanho do arquivo em MB: '))
vel_link = float(input('Digite a velocidade do link em Mbps: '))

tam_arquivo = tam_arquivo * 8 * 1024 * 1024 #Convertendo pra bits
vel_link = vel_link * 1024 * 1024 #Convertendo pra bits

tempo = tam_arquivo / vel_link
tempo = tempo/60

print(f'O download irá demorar {tempo:2.f} minutos')