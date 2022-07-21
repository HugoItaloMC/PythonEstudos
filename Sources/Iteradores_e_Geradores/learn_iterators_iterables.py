"""
Entendendo Iterators (iteradores) e Iterables (iteráveis)

Iterator ->
     - Um objeto que pode ser iterado
     - Um objeto que retorna um dado, sendo um elemtn o por vez quando uma funcão next() é chamada;

Iterable ->
    - É um objeto que irá retornar um iterator quando a funcão iter() for chamada.
"""

nome = 'Geek'  # É um iterable mas não é um iterator
numeros = [1, 2, 3, 4, 5]  # É um iterable mas não é um iterator

# Refatorando
# Chamando a funcão iter() tornando o iterável em um iterador
iter1 = iter(nome)
iter2 = iter(numeros)

# Entendendo a funcão next()
# A funcão next() retorna um elemtento por ocorrência
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))

# Acima ocorre inplicitamente dentro de um loop for em Python
# Ao chamarmos a funcão next() em um iterador sem ocorrência teremos StopIteration
# Exemplo ultilizando for:

for n in nome:
    print(n)

# Outro exemplo do next()

print(next(iter2))
print(next(iter2))
print(next(iter2))
print(next(iter2))
print(next(iter2))
# print(next(iter2))  # StopIteration
# Exemplo com o for:

for n in numeros:
    print(n)

# OBS !  O loop for trata StopIteration parando o loop antes de ñ haver ocorrência dentro do iterador