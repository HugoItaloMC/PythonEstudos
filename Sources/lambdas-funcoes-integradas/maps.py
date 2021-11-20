"""



Repositório Remoto : github.com/HugoItaloMC/PythonEstudos/Comprehensions


Python, versão :  3.10

 Base :
    Curso : Programacão Python Essensial. Didática : Geek University. Plataforma :  udemy.com


Secão 10 : Expressões lambdas e funcões integradas.

    Map :
       Mapeamento de valores para funcão.



.==============================================.
|     " " " " " " " " " " " " " " " " " "      |
|     "  Ordem alfabetica nas variáveis "      |
|     "      globais e locais :         "      |
|     "                                 "      |
|     "       Examples Global :         "      |
|     "                                 "      |
|     "            a = ''               "      |
|     "             b = 0               "      |
|     "             c = True            "      |
|     "                                 "      |
|     "                                 "      |
|     "       Examples Local :          "      |
|     "                                 "      |
|     "        a = range(0, 10)         "      |
|     "                                 "      |
|     "        for b, c in a:           "      |
|     "            for d, in b:         "      |
|     "                print(d)         "      |
|     "            for e in c:          "      |
|     "                print(e)         "      |
|     "                                 "      |
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


# Iterando com listas ultilizando Map
# exemplos:


import math


def area(r):
    " Calcula a area de um circulo com raio ' r ' "
    return math.pi * (r ** 2)


raios = [1, 3, 5.1, 66.6, 10]
areas = []


# Forma Comum

raios = [1, 3, 5.1, 66.6, 10]

areas = []
for r in raios:
    areas.append((area(r)))

print(areas)


# Map é uma funcão que recebe dois parametros: O primeiro a funcão, o segundo um iterável

areas = map(area, raios)

print(areas)  # Retorna um map object
print(list(areas))


# Refatorando

print(f"{list(map(area, raios))}")

print(list(map(lambda r: math.pi * (r ** 2), raios)))

# OBS :  Após ultilizar a funcão map, depois do primeiro retorno do resultado ele zera.
"""
