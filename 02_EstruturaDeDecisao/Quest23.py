#23.Faça um Programa que peça um número e informe se o número é inteiro ou decimal. 
#Dica: utilize uma função de arredondamento.

def verificar_numero(numero):
    numero_arredondado = round(numero)
    
    if numero == numero_arredondado:
        return "O número é inteiro."
    else:
        return "O número é decimal."

# Solicita o número ao usuário
numero = float(input("Digite um número: "))

resultado = verificar_numero(numero)
print(resultado)
