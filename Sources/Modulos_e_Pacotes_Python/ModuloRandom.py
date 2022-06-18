'''
  O que são módulos, em Python ?
  Módulos nada mais são do que outros arquivos Python.

  Módulo Random -> Possui várias funcões para geracão de números pseudo-aleatório



# OBS !  Exite dois métodos de se importar um módulo

# Forma 1 - Import todos_o_módulo

# import random

   OBS ! Ao realizar o import de todo o módulo, todas as funcões, atributos, classes e propriedades que estiverem
dentro do módulo ficarão disponíveis (Ficarão em memória). Caso vc saiba quais funcões vc precisa ultilizar deste
módulo, enão está não seria a forma ideal para a ultilizacão.

print(random.random())
'''




# Método 2 de importacão do módulo
# Especificando uma funcão do módulo

from random import random

for n in range(10): print(random())

# uniform() -> Gerar um número real pseudo-aleatório entre valores estabelecidos

from random import uniform

for n in range(10): print(f'\n{uniform(1, 100)}')


# randint() -> Gera um número inteiro pseudo-aleatório entre valores estabelecidos

from random import randint

for n in range(6): print(randint(1, 60), end=', ')

# choice() -> Mostra um valor aleatório entre um iterável

from random import choice; print('\n',choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

# shuffle() -> Bagunca ocorrencias de iteráveis

from random import shuffle

cartas = ['K', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10']

print(cartas)

shuffle(cartas)
print(cartas)

print(cartas[0]) # Devolve valor na posicão [0] do iterável
