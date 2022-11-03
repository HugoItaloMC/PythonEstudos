"""
 - Por que testar nosso código
   : Reduzir bugs (problemas)
   : Testes garantem que novos recursos da sua aplicacão não quebrem (alterem) recursos antigos
   : Testes garantem que bugs (problemas) que foram corrigidos anteriormente continuem corrigidos
   : Testes garantem que a refatoracão (refinamento) não tragam novos bugs (problemas)
 - Testes Automátizados é mais uma camada de código da aplicacão, sempre que desenvolvemos uma solucão desenvolvemos
a camda backend frontend e a camda de testes de ambas as partes, testes backend e testes frontend. Temos que pensar no
algoritmo pra desenvolver o sistema e na forma de programar os testes.
 - Hoje uma vertente mais utilizada conhecida como TDD (Test Driven Development) Desenvolvimento Guiado por Teste
  : No TDD primeiro criamos nosso teste (instância) depois escrevemos o código (Classes, Atributos e Métodos)
  : Estágios TDD ->
    - Escreve o teste Primeiro
    - Então vc escreve o código no minímo suficiente para fazer o teste passar( ou seja, executado com sucesso)
    - Então refatora o código pra realizar a funcionalidade e testa novamente
    - Uma vez que o teste passe, o recurso e considerado completo

 - Estes estágios de desenvolvimento do TDD são quase como um mantra que os desenvolvedores seguem, conhecidos como:
   : RED
   : GREEN
   : REFACTOR
"""

class Gato:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def comprimenta(self):
        print(f"{self.__nome} faz miau !!")


# Instânciamento (TDD)

felix = Gato('felix')

felix.comprimenta()

print(felix.nome)