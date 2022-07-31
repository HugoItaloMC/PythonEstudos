"""



Repositório Remoto : github.com/HugoItaloMC/PythonEstudos/Sources/


Python, versão :  3.10

 Base :
    Curso : Programacão Python Essensial. Didática : Geek University. Plataforma :  udemy.com


Secão 10 : Expressões lambdas e funcões integradas.

    Map :
       Mapeamento de valores para funcão.

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


# Fixando o map() :

# Exemplos

# Convertendo dados ' graus ceucius ' para ' firenight  ' :

# expressão da formula : (9 / 5 ) * c + 32

f = lambda x: (x[0], (9 / 5) * x[1] + 32)


# Entrada de dados,  -- neste exemplo uma list com tuple como ocorrencias :

cidades = [('Sao Paulo', 29), ('Campinas', 26), ('Ribeirao Preto', 33), ('Sao Caetano', 31), ('Pilar do Sul', 23),
           ('Sao Caetano', 25), ('Santo andre', 31), ('Santos', 28)]

# Processamento : ultilizando map(), lembrando que o map tem 2 ocorrencias como parametros, 1 uma funcao, 2 um iteravel

print(list(map(f, cidades)))
"""
 - Passamos a funcão na primeira ocorrencia como parametro no map() e logo após os dados 
"""