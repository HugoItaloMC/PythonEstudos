"""
Ultilizando linguagem Python, versão 3.10
===========================================
    Ordem de declarassão de variáveis :
        .  .


List Comprehensions
    - Ultilizando list comprehension podemos gerar novas listas com dados processados a partir de outr
iterável
    # Sintax da list comprehension :

        [dado for dado in interável]

"""
a = [1, 2, 3, 4, 5, 6]

a0 = [n * 10 for n in a]
a01 = [n / 2 for n in a]
print(a)  # [10, 20, 30, 40, 50, 60]
print(a01)  # [0.5, 1.0, 1.5, 2.0, 2.5, 3.0]

"""
Para entender melhor o que está acontecendo devemos dividir a expressão em 2 partes:
    - 1) : for n in n
    - 2) : n * 10
"""


def b(c):
    return c * c


r1 = [b(n1) for n1 in a]

print(r1)  # [1, 4, 9, 16, 25, 36]

# Comparando solucões, ultilizando comprehensions e depois loops.

# Loop :

n1 = []

for n in range(1, 6):
    n1.append(n * 2)

print(n1)  # [2, 4, 6, 8, 10]

# list comprehension :

print([n * 2 for n in range(1, 6)])  # [2, 4, 6, 8, 10]

# list comprehensions com strings :

# 1

nome = 'Geek University'

print(f"{[letra.upper() for letra in nome]}")

# 2

def d(e):
    e = e.replace(e[0], e[0].upper())
    return e


amigos = ['beatriz', 'ana', 'joao', 'flavio', 'maria']

print([d(n) for n in amigos])

# 3 2000000066089154466

print([a * 3 for a in range(1, len(a)+1)])

print([bool(n) for n in [0,'', [], True, 1, 14, 15.444]])