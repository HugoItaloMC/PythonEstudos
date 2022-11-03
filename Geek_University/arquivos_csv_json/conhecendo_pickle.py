"""
  - Conhecendo Pickle

   No processo de desenvolvimento haverá momentos que iremos armazenar dados sensíveis
 e esses dados ñ podem esta armazenados em testo puro, devem passar por uma serializa-
 cão para seu armazenamento
 : O Módulo pickle ñ é seguro contra script`s maliciosos, ñ é recomendado utilizar
arquivos pickle de fontes ñ confiáveis.

"""

import pickle


class Animal:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def comer(self):
        print(f"O {self.__nome} está comendo")


class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def comprimenta(self):
        print(f'{self.nome} faz miau !')


class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def comprimenta(self):
        print(f"{self.nome} está latindo...woof!")


felix = Gato('Felix')
pluto = Cachorro('Pluto')

# Fazendo a escrita em arquivos pickle
with open('material_apoio/teste_pickle.pickle', 'wb') as arq:
    pickle.dump((felix, pluto), arq)


# Fazendo leitura em arquivos pickle

with open('material_apoio/teste_pickle.pickle', 'rb') as arq:
    gato, cachorro = pickle.load(arq)
    print(f"O gato chama-se {gato.nome}")
    gato.comprimenta()

    print(f"O cachorro chama-se {cachorro.nome}")
    cachorro.comprimenta()
