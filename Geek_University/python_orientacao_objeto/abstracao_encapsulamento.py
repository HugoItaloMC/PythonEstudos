"""
POO : Abstracao e Encapsulamento -> O grande objetivo da POO é encapsular nosso código detro de um grupo
lógico e hierarquico utilizando classes.

    CLASSE
 _______________
|   ATRIBUTOS   |
|   MÉTODOS     |
----------------
# Relambrando Atributos/Métodos privados em PYthon

  Imagine que temos uma classe chamada Pessoa, contendo
um atributo privado chamado __nome e um método privado
chamado __falar().
  Esses elementos privados só devem/deveriam ser aces-
sados dentro da classe. Mas o PYthon não bloqueia este
acesso fora da classe. Com Python acontece o fenômeno
chamado 'Name Mangling', que faz uma alteracão na for-
ma de se acesar os elementos privados, conforme:

_Classe__elemento

Exemplo -> Acessando elementos privados fora da classe:

instancia._Pessoa__nome
instancia._Pessoa__falar()

  Abstracao em POO é o ato de expor apenas dados relevantes
de uma classe, escondendo  atributos e  métodos privados de
usuários.
"""

class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titulas = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador = self.__numero + 1

    def extrato(self):
        print(f"Saldo de \n\t...{self.__saldo}\n Titulas\n\t...{self.__titulas}\n Limite\n\t...{self.__limite}\n")

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("Error # Values Not 0 (zero)")

    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
            else:
                print("Not Found Value")
        else:
            print("Error # Values Not 0 (zero)")
    def transferir(self, valor, conta_destino):
        # 1 : Remover valalor da conta origem
        self.__saldo -= valor
        self.__saldo -= 10  # Taxa transferência para quem realizou a transferência
        # 2 : Adicionando o valor na conta destino
        conta_destino._Conta__saldo += valor



conta1 = Conta('Italo Correia', 200, 1500)

conta2 = Conta('Hugo Magalhaes', 150, 2000)

conta1.depositar(100)
conta2.depositar(120)

print(f"{conta1.__dict__}\n{conta2.__dict__}")

conta1.sacar(120)
conta2.sacar(20)

print(f"{conta1.__dict__}\n{conta2.__dict__}")

conta1.transferir(100, conta2)

print(f"{conta1.__dict__}\n{conta2.__dict__}")
