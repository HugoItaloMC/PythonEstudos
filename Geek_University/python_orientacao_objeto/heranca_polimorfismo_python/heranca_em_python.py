"""
 POO em Python
  - Heranca (Inheritance)
   : A ideia de heranca é de reaproveitar código
   : Extender nossas Classes
   : A partir de uma classe existente nós utilizamos essa classe, herdamos atributos
   e métodos em uma nova classe.
   :Quando uma classe herda de outra classe, ela herda TODOS os atributos e métodos
   da classe herdada.
   : Quando uma classe é herdada, essa classe é chamda de Super Classe
   : Quando uma classe herda de outra classe, essa classe é chamada de sub-classe
   : Fazemos acesso a o construtor da Super Classe utilizando o método super()
   : Podemos reescrever/refatorar métodos da Super Classe nas sub-classes (Overrading)
"""


class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f"{self.__nome} {self.__sobrenome}"


class Cliente(Pessoa):
    """Cliente Herda de Pessoa"""

    def __init__(self, nome, sobrenome, cpf, renda):
        Pessoa.__init__(self ,nome, sobrenome, cpf)  # Acessando Super classe [Pessoa] - forma incomum
        self.__renda = renda


class Funcionario(Pessoa):
    """Funcionario Herda de Pessoa"""

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)  # Acessando Super Classe [Pessoa] - Forma convencional
        self.__matricula = matricula

    def nome_completo(self):  # Overreding
        print(super().nome_completo())
        print(self._Pessoa__nome)
        return f"...Funcionario : {self.__matricula} \n\t...Nome : {self._Pessoa__nome}"


cliente1 = Cliente('Italo', 'Correia', '123.456.789-00', 50000)
funcionario1 = Funcionario('Hugo', 'Magalhaes', '987.654.321-11', 14443)


print(f"{cliente1.nome_completo()}")
print(f"{funcionario1.nome_completo()}")
