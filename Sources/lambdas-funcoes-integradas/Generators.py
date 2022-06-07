"""
Generators

ex simples :
(n for n in ['abcd'] if n in 'abcd')

 Não Vimos tuple comprehensions, o mesmo é chamado de Generatores,
Generators é um objeto do tipo Generator, seu uso em memória é menor
em relacão e os Comprehensions de Python.
"""
# Iterando sobre Generators

nomes = ['Camila', 'Karlos', 'Carol', 'Cairen']

res = (n[0] == 'C' for n in nomes)
print(res)  # Retorna um objeto Generators vazio

# Verificando diferenca de espaco em memória dos iteráveis com Python ultilizando a biblioteca sys
#  https://docs.python.org/3.10/library/sys.html

from sys import getsizeof

# List comprehensions
list_comp = getsizeof([x * 10 for x in range(1000)])

# Set comprehensions
set_comp = getsizeof({x * 10 for x in range(1000)})

# Dict comprehensions
dict_comp = getsizeof({x: x * 10 for x in range(1000)})

# Generator
gen = getsizeof(x * 10 for x in range(1000))


print(
 f"\tEspaco de list comprehensions em memória {list_comp} mb \n",
f"\tEspaco de set comprehensions em memoria {set_comp} mb \n",
f"\tEspaco de dict comprehensions em memoria {dict_comp} mb \n",
f"\tEspaco de Generators em memoria {gen} mb \n")

# podemos iterar sobre Generatores

iterable = (x * 10 for x in range(1000) )
for event in iterable:
    print(event)