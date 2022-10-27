"""
 POO -
  - Polimorfismo em Python

  : Poli -> Muitas
  : Morfis -> Formas
  : Quando reimplimentamos um método presente na Classe Pai em classes filhas
  realizando  uma  sobreescrita de  método  (Overriding)  que é  a  forma  de
  representacão do Polimorfismo

"""

class Animal(object):
    """ Classe Genérica """

    def __init__(self, nome):
        self.__nome = nome

    def comprimentar(self):
        raise NotImplementedError("Método comprimentar() deve ser implentado na Heranca")

    def comer(self):
        print(f"{self.__nome} está comendo")

class Cachorro(Animal):
    """ Herda de Animal """

    def __init__(self, nome):
        super().__init__(nome)

    def comprimentar(self):
        print(f"{self._Animal__nome} woof !")


class Gato(Animal):
    """ Herda de Animal """

    def __init__(self, nome):
        super().__init__(nome)

    def comprimentar(self):
        print(f"{self._Animal__nome} faz miau ! ")


class Rato(Animal):
    """ Herda de Animal """

    def __init__(self, nome):
        super().__init__(nome)


pluto = Cachorro('pluto')
tom = Gato('Tom')
mikey = Rato('Rato')

# Testando Métodos

pluto.comprimentar()
tom.comprimentar()
mikey.comprimentar()