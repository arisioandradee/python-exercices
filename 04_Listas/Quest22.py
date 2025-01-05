'''
Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer um levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testar todos os cerca de 200 mouses que se encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles.
Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá receber um número indeterminado de entradas, cada uma contendo: um número de identificação do mouse o tipo de defeito:
necessita da esfera;
necessita de limpeza; a.necessita troca do cabo ou conector; a.quebrado ou inutilizado Uma identificação igual a zero encerra o programa. Ao final o programa deverá emitir o seguinte relatório:
'''

tipo1, tipo2, tipo3, tipo4 = [], [], [], []
qtdEntradas = int(input('Quantidade de mouses: '))

for i in range(qtdEntradas):
   print('1 - Necessita da esfera. ')
   print('2 - Necessita de limpeza. ')
   print('3 - Necessita troca de cabo/conetor. ')
   print('4 - Quebrado/Inutilizado. ')
   print('0 - Encerrar programa.')
   escolha = int(input())

   if escolha == 0:
    break
   if escolha == 1:
     tipo1.append(escolha)
   elif escolha == 2:
     tipo2.append(escolha)
   elif escolha == 3:
     tipo3.append(escolha)
   elif escolha == 4:
     tipo4.append(escolha)

total = len(tipo1) + len(tipo2) + len(tipo3) + len(tipo4) 

print("\nSituação do mouse           -  Quantidade  -  Percentual(%)")
print(f"1 - Necessita da esfera       -  {len(tipo1)}         -  {len(tipo1) / total * 100:.2f}%")
print(f"2 - Necessita de limpeza      -  {len(tipo2)}         -  {len(tipo2) / total * 100:.2f}%")
print(f"3 - Necessita troca de cabo   -  {len(tipo3)}         -  {len(tipo3) / total * 100:.2f}%")
print(f"4 - Quebrado/Inutilizado      -  {len(tipo4)}         -  {len(tipo4) / total * 100:.2f}%")
    