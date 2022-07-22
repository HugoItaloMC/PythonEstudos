"""
Repositório Remoto : github.com/HugoItaloMC/PythonEstudos/09-Comprehensions


Python, versão :  3.10

 Base :
    Curso : Programacão Python Essensial. Didática : Geek University. Plataforma :  udemy.com


Secão 10 : Expressões lambdas e funcões integradas.

    lambdas :
        Conhecidas por ' Expressões lambdas ' são funcões sem nome, ou seja
funcões anonimas.

    # exemplos

     : # - Recapitulando Funcões em python:
       def soma(a):
         return 3 * a + 1;

      # Ultilizando lambda :

    lambda x: 3 * x + 1




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

# Como ultilizar a expressão lambda :


a = lambda x: 3 * x + 1


print(calc(4))
print(calc(7))


# Podemos ter expressões lambdas com múltiplas entradas :


nome_comp = lambda nome, snome: nome.strip().title() + ' ' + snome.strip().title()


# Módulo .strip() remove espaco no comeco e no fim de uma string, o title capitaliza a inicial de uma string


print(nome_comp(' Hugo ', 'ITALO'))  #  Hugo Italo

# Em funcões Python nem uma ou várias entradas, em lambdas também :


a = lambda :  'Retorno de teste, sem entrada'

b = lambda x: 3 * x + 1

c = lambda x, y: (x * y) ** 0.5

d = lambda n, x, y: 3 /(1 / n +1 / x + 1 / y)

# n = lambda a, b, c, ..., z1001: <expressão>


print(a())

print(b(4))

print(c(4, 6))

print(d(2, 3, 100))


# OBS : Se passarmos mais parametros que argumentos teremos TypeError


# Iterando em listas ultilizando expressões lambdas :

#      Ordenando uma lista pelo ordem alfabetica pelo sobrenome  :
#           Exemplos :


autores = [
     'Hugo Italo',
     'Italo C. Magalhaes',
    'H. I. Magalhaes Correia',
     'Hugo I. M. Correia',
     'Hugo I. Magalhaes C.',
     'Italo Hugo C. Magalhaes',
     'Correia Italo',
]

print(autores)

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())

print(autores)

# Funcões 'def' com return uma 'expressão lambda'  :

# Exemplos :


def gerador_funcao_quadratica(a, b, c):
    "retorna a funcão f(x) = a * x ** 2 + b * x + c"
    return lambda x: a * x ** 2 + b * x + c


retorno = gerador_funcao_quadratic(2, 3, -5)

print(retorno(0))
print(retorno(1))
print(retorno(2))

# Refatorando

print(gerador_funcao_quadratica(3, 5, 10)(2))
print(gerador_funcao_quadratica(33, 17, 13)(5))
"  Podemos na mesma linha declarar os argumentos da funcão 'def' e
logo após declarar o argumenta da 'expressão lambda' "

"""


