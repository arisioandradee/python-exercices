'''
Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
    par ou ímpar;
    positivo ou negativo;
    inteiro ou decimal. 
'''

def verificar_par_ou_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"

def verificar_positivo_ou_negativo(numero):
    if numero > 0:
        return "positivo"
    elif numero < 0:
        return "negativo"
    else:
        return "neutro"

def verificar_inteiro_ou_decimal(numero):
    if numero.is_integer():
        return "inteiro"
    else:
        return "decimal"

# Solicita os dois números ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Solicita a operação desejada
operacao = input("Digite a operação desejada (+, -, *, /): ")

# Realiza a operação escolhida
if operacao == '+':
    resultado = num1 + num2
elif operacao == '-':
    resultado = num1 - num2
elif operacao == '*':
    resultado = num1 * num2
elif operacao == '/':
    resultado = num1 / num2
else:
    print("Operação inválida!")
    exit()

print(f"O resultado da operação é: {resultado}")
print(f"O resultado é {verificar_par_ou_impar(resultado)}, {verificar_positivo_ou_negativo(resultado)} e {verificar_inteiro_ou_decimal(resultado)}.")
