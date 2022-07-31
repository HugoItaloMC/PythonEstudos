"""
Funcões com retorno
 - Funcões Python que retornam valores, devem retornar estes valores com a palavra
reservada 'return'
<<<<<<< HEAD
=======
 - OBS sobre a palavra reservada return:
    - Ela finaliza a funcão, ou seja, ela sai da execucão da funcão;
    - Podemos ter, em uma funcão, diferentes return's;
    - Podemos, em uma funcão, retornar qualquer tipo de dado e até mesmo multiplos valores;
 - Erros comuns na ultilizacão do retorno, que na verdade nem é erro mas sim condificacão desnecessáriia
"""


# - OBS :  Em python, quando uma funcão não retorna nem um valor, ela retorna None
# Exemplos :

def quadrada_7():
    print(7*7)

quadrada_7()
ret = quadrada_7()
print(f"Retorno : {ret}")


# Refatorando a funcão
def raiz_7():
    return 7 * 7


# Criamos uma variável para receber o retorno da funcão:
# Exemplo :
ret1 = raiz_7()
print(f"Retorno : {ret1}")
"""
 - OBS : Não precisamos necessáriamente criarmos uma variável para o retorno de uma funcão,
podemos passar a execucão da funcão para outras funcões.
"""

# Podemos declarar a funcão direto no print :
# Exemplo :

print(f"Rertorno : {raiz_7() + 1}")  # -- Podemos fazer operacões junto com as funcões

print(f"Retorno : {raiz_7() + 1}\n")  # -- Podemos fazer operacões junto com as funcões


# Exemplos práticos com a palavra reservada return:
# Finalizando a funcão, saindo da execucão da funcão:
# Exemplo :
def diz_oi():
    print("Estou sendo executado antes do retorno...")
    return 'Oi !\n'
# print("Estou sendo executado depois do retorno...")  # -- Essa linha não será executada, fim da execucão no return


print(diz_oi())


# Diferentes returns em uma funcão:
def nova_funcao():
    variavel = True
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'


print(nova_funcao())


# Retornando multiplos valores:
# Exemplo1:
def nova_funcao1():
    return 2, 4, 5, 19


num1, num2, num3, num4 = nova_funcao1()

print('\n', num1, num2, num3, num4)

# Exemplo2 :
print(f"{nova_funcao1()} \t{type(nova_funcao1())}")

# Gerando uma funcão bom a biblioteca random

from random import random


def joga_moeda():
    # Gera um número pseudo-randomico entre 0 e 1.
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'


print('\n', joga_moeda())
