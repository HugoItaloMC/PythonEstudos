"""
Reduce :
 Para ultilizar o reduce nós precisamos de uma funcão que receba dois parametros
 A funcão reduce() tem dois parametros como entrada, 1 uma funcão e 2 um iteravel
 A partir do python 3+  a funcão reduce() não é mais uma funcão integrada (built-in). Agora temos
importar e ultilizar esta funcão a partir do módulo 'functools'

Guido Van Rossum :  " Ultiliza a funcão reduce() se vc realmente precisa dela. Em todo caso,
99% das vezes um loop for é mais legível "

 A funcão reduce() funciona da seguinte forma :
   Passo 1 : Aplica a funcão nos dois primeiro elementos da lista e guarda o resultado
   Passo 2 : Aplica a funcão passando o resultado do Passo1 mais o elemento seguinte assim até o fim da lista
"""

# Exemplos práticos :

from functools import reduce

dados = list(range(1, 10))

print(reduce(lambda x, y: x * y, dados))

# Ultilizando o for :

o = 1

for n in dados:
    o *= n

print(o)
