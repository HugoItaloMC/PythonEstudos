"""
 POO -
  - Method Resoluction Order (MRO) `Resolucão de Ordem de Métodos`
   : Ordem de Execucão dos Métodos, quem vai ser executado primeiro
   : Quando temos mais de uma heranca executando o mesmo método, isso vai impactar no resultado da classe conforme
   a ordem da declaracão dos objetos herdados no cabecalho da classe
   : Em python temos 3 maneiras de Verificar a Ordem dos Métodos (MRO), sendo elas :
    - via propriedade ce classe __mro__
    - via método mro()
    - via help()
"""
class Animal:
    """Classe Super"""

    def __init__(self, nome):
        self.__nome = nome

    def comprimentar(self):
        return f"O animal {self.__nome} diz oi !"

class Aquatico(Animal):
    """Herda de Animal"""

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f"{self._Animal__nome} está nadando"

    def comprimentar(self):
        return f"Olá {self._Animal__nome} eu sou do mar !"


class Terrestre(Animal):
    """ Herda de Animal"""

    def __init__(self, nome):
        super().__init__(nome)

    def andando(self):
        return f"Eu {self._Animal__nome} estou andando"

    def comprimentar(self):
        return f"Olá {self._Animal__nome} eu sou terrestre !"


class Pinguim(Aquatico, Terrestre):
    """ Classe Com Múltiplas Herancas"""

    def __init__(self, nome):
        super().__init__(nome)
"""
  - Repare que Pinguim está declarando primeiro nas suas herancas como atributo o Objeto Aquatico()
  ou seja, a execucão do método comprimentar na classe Pinguim vai retornar o método na ordem da 
  classe Aquatico() pois, no cabecalho da classe Pinguim(), Aquatico() está declarado na primeira
  posicão.
"""


print(Pinguim.__mro__)  # Verificando ordem de Métodos do Objeto via propriedade de Classe
print(Pinguim.mro())  # Verificando orden de Métodos de Objeto via método mro()
print(help(Pinguim))  # Verificando Ordem de Métodos de Objeto via help()