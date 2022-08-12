"""
Módulo Collections: Default Dict

# Recapitulando dict
dicionario = {'curso': 'Programacão em Python: Essensial'}

print(dicionario)
#{'curso': 'Programacão em Python: Essensial'}

print(dicionario['curso'])
# Programacão em Python: Essensial

print(dicionario['outro'])
# KeyError
Default Dict: Ao criar um um dict ultilizando-o nós informamos um valor default,
podendo ultilizar um lambda. Este valor será ultilizado sempre que não houver um valor definido.
 Caso tentamos acessar uma chave que não existe , esta chave criada e o valor default será atribuído.

OBS: lambdas são funcões sem nome que podem ou não receber parametros e retornar valores
"""

# fazendo import
from collections import defaultdict

# Exemplo 1:
dicionario= defaultdict(lambda: 0)

dicionario['curso'] = 'Programacão em Python: Essensial'
print(dicionario)
# defaultdict(<function <lambda> at 0x7f94fc04ac10>, {'curso': 'Programacão em Python: Essensial'})

print(dicionario['outro']) # KeyError no dicionário comum, aqui não existe valor em default.

print(dicionario)
#defaultdict(<function <lambda> at 0x7fd9c572ac10>, {'curso': 'Programacão em Python: Essensial', 'outro': 0})