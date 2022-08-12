"""
Módulo Collections: Ordered Dict

# Em um dicionário não é garantido a ordem de insercão dos elementos
dicionario = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
for chave, valor in dicionario.items():
    print(f"chave= {chave}: valor= {valor}")
# chave= a: valor= 1
  chave= b: valor= 2
  chave= c: valor= 3
  chave= d: valor= 4
  chave= e: valor= 5

Ordered Dict: É um dicionário que garante a insercão dos elementos.
"""

# Fazendo um import
from collections import OrderedDict

# Exemplo1:
dicionario = OrderedDict({'a':1, 'b':2, 'c':3, 'd':4, 'e':5})
for chave, valor in dicionario.items():
    print(f"chave= {chave}: valor= {valor}")

# Entendendo a diferenca entre os dicionarios

# Dicionario comum:
dict1 = {'a':1, 'b':2}
dict2 = {'b':2, 'a':1}
print( dict1 == dict2) # True: Já que a ordem dos elementos não importa

# Ordered Dict
odict1= {'a':1, 'b':2}
odict2= {'b':2, 'a':1}
print(odict1 == odict2) # False: Já que a ordem dos elementos importa para o Ordered Dict