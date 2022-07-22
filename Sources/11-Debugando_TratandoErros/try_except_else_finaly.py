"""
Official Documentation :
https://docs.python.org/pt-br/3/library/exceptions.html

Try Except Else Finally


Dicas de quando e onde tratar seu código:

TODA ENTRADA DEVE SER TRATADA !!


# Else -> O bloco else é executado se nem um erro for encontrado
# Finally -> O bloco finally é executado mesmo se ñ houver excecão no programa
try:
    num = int(input("INforme Número: "))
except ValueError as VErr:
    print(f'''Encontrado ValueError : {VErr}''')
else:
    print(f'''Número Informado {num}''')
finally:
    print(f"End Program")

# OBS !  O bloco finally é ultilzado  para fechar ou desalocar recursos.


# Exemplos mais complexos ERRADO:

def operacao(n1, n2):
    return n1 / n2

num1 = int(input("Informe Numero : "))
try:
    num2 = int(input("Informe Numero: "))
except ValueError:
    print(f'''Valor não númerico informado''')

try:
    print(operacao(num1, num2))
except NameError:
    print(f'''Valor errado informado''')
"""


# Exemplo mais complexo CORRETO:
# OBS ! VC é responsável por seus códigos, trate-os


def operacao(n1, n2):  # funcão para dividir dois inteiros
    try:
        return int(n1) / int(n2)  # Convertendo valor de input em inteiros e retornando-os
    except (ValueError, NameError, ZeroDivisionError, TypeError) as err:  # Tratando erros Built-in's do Python
        return f"ERRO : {err}"  # Saída de Erro

# Entrada :
print("Resultado: ", operacao(input(f"operacão (divisão)\nDigite Valor: "), input("Digite Valor: ")))


# DICA :

def operacao(n1, n2):
    try:
        int(n1) / int(n2)
    except ArithmeticError:
        return "Operacao Inválida"

print("Resultado: ", operacao(input("Digite Numero : "), input("Digite Numero")))
'''
ArithmeticError: A classe base para as exceções embutidas levantadas para vários erros aritméticos: 
OverflowError, ZeroDivisionError, FloatingPointError.
'''

