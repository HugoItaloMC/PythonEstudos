"""
Funcões com parametros padrões ( Default Parameters )
    - funcões onde a passagem de parametro seja opicional
Por quë ultilizar valores default nos parametros?:
    - Nos permite ser mais flexíveis nas funcões;
    - Evita erros com parametros incorretos;
    - Nos permite trabalhar com exemplos mais legiveis nos códigos;
Podemos ultilizar qualquer tipo de dados nos parametros das funcões:
    - Strings, Bolleans, integer, floats, tuple, list, dict, set, etc;
"""


def exponencial(numero, potencia=2):    # Quando informamos o valor ao parametro ele se torna opicional no argumento
    return numero ** potencia


print(exponencial(2, 5))
print(exponencial(5, 2))
print(exponencial(2))


# Exemplos mais complexos:


def mostra_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Bem vindo instrutor Geek'
    elif nome == 'Geek':
        return 'Pensei que vc era o instrutor !'
    return f'Ola {nome}'


print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao(True))
print(mostra_informacao('João'))
print(mostra_informacao(nome='Maria'))


def soma(n1, n2):
    if n1 > 0 and n2: return n1 + n2


def subtr(n1, n2):
    if n1 > 0 and n2: return n1 - n2


def mat(n1, n2, fun=soma):
    if (n1 > 0 or fun != None) and n2: return fun(n1, n2)


print(mat(2, 3))
print(mat(11, 6, subtr))

# Para ultilizar variáveis globais dentro de uma funcão se ultiliza a palavra reservada Global:
#   Exemplo :


total = []


def extr(n):
    global total
    total += n
    return total


extr(input(": "))
print(f"{''.join(total)}")

# Podemos ter funcões dentro de funcões e ultilizar suas variáveis locais de uma forma 'global' :
#   exemplo :


def saida(n):
    cont = []

    def ensaida():
        nonlocal cont

        cont += n
        return ''.join(cont)
    return ensaida()


print(saida(input(" : ")))
