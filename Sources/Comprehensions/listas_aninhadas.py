"""
Repositório Remote : github.com/HugoItaloMC/PythonEstudos/Comprehensions


Python, versão :  3.10

 Base :
    Curso : Programacão Python Essensial. Didática : Geek University. Plataforma :  udemy.com


Secão 9 ; Comprehensions em Python :

    Listas aninhadas (Nested lists)
       Em python temos como iterar em listas dentro de uma lista, formando colunas e linhas
linhas, formando uma matriz

    # exemplo :

    lista = [[1, 2, 3], [2, 3, 4, 5], [6, 5, 4, 3, 2], [1, 2, 3, 4]]
    print(lista[0][2])

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

# Exemplos :

a = [[1, 2, 3], [2, 3, 4, 5], [6, 5, 4, 3, 2], [1, 2, 3, 4]]

print(a[3][2])

for b in a:
    for c in b:
        print(c)

"""

# Praticando com lists comprehensions
# Exemplos


a = [[1, 2, 3], [2, 3, 4, 5], [6, 5, 4, 3, 2], [1, 2, 3, 4]]

[[print(b) for b in c] for c in a]