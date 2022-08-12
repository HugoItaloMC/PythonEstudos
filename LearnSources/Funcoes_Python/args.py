"""
*args
 Poderíamos chamar este parametro de (*x, *n, *par) mas por convencão da comunidade chamamos de *args
    - O paramëtro *args ultilizado em uma funcão, coloca valores extras informados como
entrada em uma tuple. Então desde já lembre-se que tuplas são imutáveis.
"""


def teste(nome='', email='', *args):
    return nome, email, sum(args)


print(teste(2, 3, 4, 5, 7, 200))
print(teste(2, 3, 4, 5, 7, 200))
print(teste('joao', 'joao@email.com', 11, 22, 33, 55, 77, 1011))
print(teste())


# Outros exemplos com *args:


def ver_info(*args):
    if 'Hugo' in args and 'Italo' in args: return 'Bem Vindo Hugo !'
    return 'Não tenho ctz que é o Hugo !'


print(ver_info(input(": "), input(": ")))


def soma_total(*args):
    return sum(args)


# Desempacotamento

lista = [11, 22, 33, 44, 55, 66, 77, 10001]


print(soma_total(*lista))

# OBS :  o '*' serve para informar ao Python que estamos passando como argumento uma colecão de dados.
# Desta forma saberá que precisará antes desempacotar esses dados.