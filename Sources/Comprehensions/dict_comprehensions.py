"""
Repositório Remoto : github.com/HugoItaloMC/PythonEstudos/Comprehensions


Python, versão :  3.10

 Base :
    Curso : Programacão Python Essensial. Didática : Geek University. Plataforma :  udemy.com


Secão 9 ; Comprehensions em Python :

    Dict's Comprehensions :
        Podemos iterar com os valores dentro de um dict

    # exemplo :

     dicty = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
     output = {chave : valor ** 2 for chave, valor in dicty.items()}

     print(output)


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

```
 Colocando cada valor da list 'a' como chave no dict 'b' e elevando ao quadrado esse valor,
e inserindo como valor de chave
```
# Exemplos :


a = [1, 2, 3, 4, 5]

b = {c: c ** 2 for c in a}

print(b)


# Iterando em dict comprehensions ultilizando lists e strings

a = 'abcde'
b = [1, 2, 3, 4, 5]

c = {a[d] : b[d] for d in range(0, len(c))}

print(c)


# Iterando em dict comprehensions com estrutura condicional :

# Exemplos :

a = [1, 2, 3, 4, 5]

b = {c: ('par' if c % 2 == 0 else 'impar') for c in a}

print(b)
"""
