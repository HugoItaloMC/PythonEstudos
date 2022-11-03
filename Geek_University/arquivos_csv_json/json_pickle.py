"""
 JSON and PICKLE

  - JSON -> JavaScript Object Notation
  : Este tipo de arquivo é super comum em API`s de grandes empresas
  : API são meios de comunicacão entre os servicos oferecidos por
  empresas (Twitter, Facebook, Youtube...) e terceiros (mós desenvolvedores)

"""

import json

arq = json.dumps(['produto', {'Playstation 4': ('2TB', 'NOVO', '220V', 2345)}])

print(type(arq))
print(arq)

# Exemplos mais complexos

class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca

felix = Gato('Felix', 'Malte')
print(felix.__dict__)
foo = json.dumps(felix.__dict__)
print(foo)

# Integrando JSON com Pickle
# Escrevendo arquivo JSON/Pickle

import jsonpickle

foobar = jsonpickle.encode(felix)
print(foobar)

# Serializando arquivos JSON com pickle
with open('material_apoio/felix.json', "w") as arq:
    conteudo = jsonpickle.encode(felix)
    arq.write(conteudo)

# Deserializando arquivos JSON
with open('material_apoio/felix.json', "r") as arq:
    arquivo = arq.read()
    foo = jsonpickle.decode(arquivo)
    print(foo)
    print(type(foo))
    print(foo.nome)
    print(foo.raca)

