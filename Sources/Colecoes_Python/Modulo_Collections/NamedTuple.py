"""
Módulo Collections: Named Tuple

# Recapitulando tuple:
tupla = (1, 2, 3)

print(tuple[1])

Named Tuple: São tuplas diferenciada onde especificamos um nome para a mesma e parametros
"""

# Importando
from collections import namedtuple

# Precisamos definir nome e parametros

# Forma 1, declaracão namedtuple
cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2, declaracão da namedtuple
cachorro2 = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3, declaracão namedtuple
cachorro3 = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Ultilizando
dog = cachorro(idade=2, raca='chow-chow', nome='dog')
print(dog)

# Acessando os dados
# Forma 1:
print(dog[0]) # idade
print(dog[1]) # raca
print(dog[2]) # nome

# Forma 2 :
print('\n',dog.idade)
print(dog.raca)
print(dog.nome, '\n')

# Posicão de indice
print(dog.index('chow-chow'))

# Número de ocorrencias do valor declarado
print( dog.count('chow-chow'))