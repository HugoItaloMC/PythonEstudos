"""
 POO -
  - Herancas Múltiplas em Python

  : Em Python da suporte a herancas múltiplas, ou seja uma classe pode herdar de mais de uma classe
  : Uma Classe filha que herda de múltiplas classes vai também herdar todos seus atributos e métodos
  : A Heranca múltipla pode ser feita de duas maneiras
    - Por multiderivacão direta ;
    - Multiderivacão indireta ;


#  Multiderivacão direta :


class Base1:
    ...

class Base2:
    ...

class Multiderivada(Base1, Base2):
    ...

#  Multiderivacão Indireta ;

class FooBase1:
    ...

class FooBase2(FooBase1):
    ...

class FooBase3(FooBase2):
    ...

class FooMultiDerivacao(FooBase3):
    ...

    ##

    : Não Importa se a Multiderivacao é indireta ou direta, a classe que herdar outras classes herdara todos os
    atributos e métodos das super classes.

    : A ordem de heranca altera como sera o comportamento do objeto. (MRO)
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


aquatico = Aquatico('Golfinho')
terrestre = Terrestre('Lobo')

print(aquatico.nadar())
print(terrestre.andando())

# Testando Heranca multipla

tux = Pinguim('Tux')
print(tux.andando())
print(tux.nadar())
print(tux.comprimentar())  # Method Resolution Order - MRO

# Verificando se Objeto é instância de outro Objeto:

print(f"\n...Tux é objeto de Pinguim : {isinstance(tux, Pinguim)}")
print(f"\n...Tux é objeto de Aquatico : {isinstance(tux, Aquatico)}")
print(f"\n...Tux é objeto de Terrestre : {isinstance(tux, Terrestre)}")