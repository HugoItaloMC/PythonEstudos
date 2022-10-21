"""
Funcões de Maior Grande (High Order Functions) - HOF

 - Quando uma linguagem da suporte a HOF, indica que podemos ter funcões
 que retornam outras funcões como resultado ou mesmo podemos passar funcões
 como argumentos para outras funcões, e até mesmo criar variáveis do tipo
 funcões nos nossos programas.
Em Python funcões são Cidadões de Maior Classe, Firts Class Citizen
"""
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def dividir(a, b):
    return a / b

def multiplicar(a, b):
    return a * b

def calculo(a, b, func):
    return func(a, b)

print(calculo(10, 20, somar))
print(calculo(10, 20, subtrair))
print(calculo(10, 20, dividir))
print(calculo(10, 20, multiplicar))

"""
# Nested Functions - Funcões aninhadas;

- Em Python podemos também ter funcões dentro de funcões, que são conhecidas como Nested Functions ou também 
Inner Functions (Funcões internas)

# Exemplo abaixo ->
"""

from random import choice

def cumprimento(pessoa):
    def humor():
        return choice(("E ai ", "Suma daqui ", "I love you "))
    return humor() + pessoa


print(cumprimento("Hugo"))
print(cumprimento("Italo"))

# Retornando Funcões de outras funcões:

def faz_rir():
    def rir():
        return choice(("kkkkkkkkkkkk", "hahahhaahahahahaha", "uahuahsaushausha"))
    return rir

risada = faz_rir()
print(risada())

#  Funcões aninhadas podem acessar o escopo de sua funcão mais externa

def faz_me_rir(pessoa):
    def dando_risada():
        risada = choice(("haahaaahah", "hohohohohohoh", "kkkkkkkkk"))
        return f"{risada} {pessoa}"
    return dando_risada

rindo = faz_me_rir("Italo")

print(rindo())
print(rindo())
print(rindo())
print(rindo())