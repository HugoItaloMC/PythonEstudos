"""

Repositorio remoto : https://github.com/HugoItaloMC/PythonEstudos/tree/main/Sources/lambdas-funcoes-integradas/filter.py


Python, versão :  3.10

Base :
Curso : Programacão Python Essensial. Didática : Geek University. Plataforma :  udemy.com


Secão 10 : Expressões lambdas e funcões integradas.

Filter :
Filtra dados de uma colecão.



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


# Biblioteca para se trabalhar com dados estatisticos

import statistics

dados = [1.5, 2.4, 3.3, 4.2, 5.1]

# Calculando a media dos dados ultilizando o metodo mean() da lib statistics
media = statistics.mean(dados)

print(f"Media: {media}")

# O filter() tambem possui dois parametros de entrada sendo o primeiro uma funcao e o segundo um iteravel :

print(list(filter(lambda x: x > media, dados)))


paises = ['', '', 'Brasil', '', 'Argentina', '', 'Equador', '', '', 'Venezuela', '', 'Chile', 'Mexico', '', 'Paraguai',
          '', 'Colombia', '', '']

# print(list(filter(lambda pais: len(pais) > 0, paises)))

# print(list(filter(lambda pais: pais != '', paises)))


print(list(filter(None, paises)))

# ['Brasil', 'Argentina', 'Equador', 'Venezuela', 'Chile', 'Mexico', 'Paraguai', 'Colombia']


# Iterando sobre list e dict :


usuarios = [
    {'username': 'Carol', 'tweets': ['Gosto de carros', 'Fui viajar']},
    {'username': 'Daiane', 'tweets': ['Ola mundo', 'Gato e bonito']},
    {'username': 'Renan', 'tweets': []},
    {'username': 'Carlos', 'tweets': []},
    {'username': 'dog1233', 'tweets': ['Show maneiro', '100 crise']},
    {'username': 'sod', 'tweets': []},
]

# Filtrar usuários que não estão ativos :

# forma 1 :

print(list(filter(lambda u: len(u['tweets']) == 0, usuarios)))

# Refatorando:

print(list(filter(lambda u: not u['tweets'], usuarios)))
"""


# Combinando filter com map :

# Crie uma lista contento uma msg 'Seu instrutor (a) é : ' + nome, desde que cada nome tenha menos de 5 carcteres

nomes = ['ana', 'Carol', 'Luiz', 'Val', 'Will']

print(list(map(lambda nome: f"Seu instrutor (a) é :  {nome} ", filter(lambda nome: len(nome) < 5, nomes))))
