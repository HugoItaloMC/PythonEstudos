"""
POO -
 - Propriedades
   : Ao Declararmos atributos privados em Nossas classes costumamos criar métodos publicos para
   manipular estes atributos. Esses métodos são conhecidos como getters e setters
   : O getter é para a recuperacão da informacão, já o setter devemos utilizar com cautela pois
   vai alterar o valor do atributo.

"""


class Conta:

    contador = 599

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador = self.__numero

    #  Getter`s and Setter`s:

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @property
    def limite(self, limite):
        self.__limite = limite

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

    def extrato(self):
        return f"{self.__saldo}"

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo - valor

    def transferir(self, valor, destino_conta):
        self.__saldo -= valor
        destino_conta.__saldo += valor
