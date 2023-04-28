# Prefira funcoes para interfaces simples ao classes auxiliares

#  Ao inves de definir e instanciar classes, as funcoes sao normalmente tudo o que precisamos para interfaces simples
# entre os componentes do Python

#  Referencias as funcoes e metodos em Python sao de primeira classe, o que significa poderem ser usados em expressoes
# como qualquer outro tipo de dado

#  Quando precisar de uma funcao para armazenar estados, considere definir uma classe que ofereca o metodo __call__
# em vez de definir um closure que guarde estado

# Hooks para callbacks: Ordenacao por compprimento
from collections import defaultdict

names = ['Maria', 'Eduarda', 'Luis']
names.sort(key=lambda x: len(x))
print(names)
# with hook ['Luis', 'Maria', 'Eduarda'] | don't hook ['Eduarda', 'Luis', 'Maria']

# Logging para atribuir default para chaves inexistentes em defaultdict

def missing_default():
    print('Add new key')
    return 0
#  Dado um dicionario inicial e um conjunto de incrementos podemos usar a funcao missing_default para rodar
# e imprimir
ocorre = {"orange": 10, "blue": 5}
increment = [
    ('red', 2),
    ('blue', 15),
    ('green', 4)
    ]
default = defaultdict(missing_default, ocorre)
print('Antes: ' , dict(default))

for chave, valor in increment:
    default[chave] += valor

print('Apos :', dict(default))