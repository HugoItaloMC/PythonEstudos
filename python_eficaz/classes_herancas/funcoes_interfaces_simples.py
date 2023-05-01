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

# As funcoes acima sao stateless por nao conter um a variavel de estado
# O codigo a seguir implementa um funcao para determinar um estados que define quantas novas chaves foram acrescentadas


def set_default(ocorre, increment):
    # Hook statefull to defaultdict when key not in dict
    added = 0
    def missing():
        nonlocal added
        added += 1
        print("Key added")
        return 0

    result = defaultdict(missing, ocorre)
    for key, valur in increment:
        result[key] += valur
    return result, added


print("Before : ", dict(ocorre))
print('After : ', dict(set_default(ocorre, increment)[0]))


# Podemos implementar um pequena classe para ter o mesmo comportamento

class KeyMissing:

    def __init__(self):
        self.added = 0

    def missing(self):
        # statefull

        self.added += 1
        return 0


statefull = KeyMissing()


result = defaultdict(statefull.missing, ocorre)
print('Before :', dict(result))

for key, valur in increment:
    result[key] += valur

print("After : ", dict(result))

# Para que nosso objeto seja chamado como funcao, vamos atribuir uma configuracao ao metodo __call__

class WhenMissing:
    # Hook statefull to defaultdict when key not content
    def __init__(self):
        self.added = 0

    def __call__(self):
        self.added += 1
        return 0


# Agora toda vez que nossa classe for chamada como funcao, ela vai ter esse comportamento
count = WhenMissing()

result = defaultdict(count, ocorre)
print('Before :', dict(result))

for key, valur in increment:
    result[key] += valur

print("After : ", dict(result))

