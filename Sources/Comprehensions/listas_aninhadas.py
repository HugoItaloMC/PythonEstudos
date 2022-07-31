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

# Exemplos :

a = [[1, 2, 3], [2, 3, 4, 5], [6, 5, 4, 3, 2], [1, 2, 3, 4]]

# Acessando dados da matriz 'a'

print(a[3][2])
print(a[2][0]

# Iterando com loops em uma lista aninhada
for b in a:
    for c in b:
        print(c)


# Iterando com lists comprehensions
# Exemplos


a = [[1, 2, 3], [2, 3, 4, 5], [6, 5, 4, 3, 2], [1, 2, 3, 4]]

# 1

[[print(b) for b in c] for c in a]


# 2 - Gerando uma matriz

b = [[a for a in range(1, 4)] for b in range(1, 4)]

print(b)


# 3 - Gerando Matriz com estrutura condicional e strings

c = [['x' if a % 2 == 0 else 'o' for a in range(1, 101)] for b in range(1, 1001)]
print(c)
for a in c: print(a)

# 4 - Gerando matriz com strings

print([['*' for a in range(1, 5)] for b in range(1, 5)])
"""
