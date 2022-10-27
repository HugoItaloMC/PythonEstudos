"""
  POO - 
   - Metodo super()
    : Método super() se refere á super classe
"""


class Animal:
    """Classe Genérica"""

    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especie = especie

    def faz_som(self, som):
        print(f"{self.__nome} faz o som : {som}")


class Gato(Animal):
    """Herda de Animal"""

    def __init__(self, nome, especie, raca):
        Animal.__init__(self, nome, especie)
        # super().__init__(nome, especie)
        super().faz_som('miaumiau')
        self.__raca = raca


felix = Gato('Felix', 'felino', 'angorá')

felix.faz_som('miau')
