"""
Repositório Remote : github.com/HugoItaloMC/PythonEstudos/09-Comprehensions


Python, versão :  3.10

 Base :
    Curso : Programacão Python Essensial. Didática : Geek University. Plataforma :  udemy.com


Secão 9 ; 09-Comprehensions em Python :

    List 09-Comprehensions pt1
       - Ultilizando list comprehension podemos gerar novas listas com dados processados a partir de outro
iterável

    # Sintax da list comprehension :

        [dado for dado in iterável]


.==============================================.
|     " " " " " " " " " " " " " " " " " "      |
|     "       Ordem alfabetica na       "      |
|     "    declarassão de variáveis :   "      |
|     "                                 "      |
|     "            Examples :           "      |
|     "                                 "      |
|     "            a = ''               "      |
|     "             b = 0               "      |
|     "             c = True            "      |
|     "                                 "      |
|     "    Ordem válida para funcões    "      |
|     "      e seus parametros :        "      |
|     "                                 "      |
|     "          Examples:              "      |
|     "                                 "      |
|     "       def d(da, db):            "      |
|     "       return (da + db) * da     "      |
|     " " " " " " " " " " " " " " " " " "      |
.==============================================.


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

# Comparando solucões, ultilizando loops e depois list comprehensions.

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