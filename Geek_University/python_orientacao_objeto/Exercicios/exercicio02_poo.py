"""
  Crie uma classe Agenda que pode armazenar 10 pessoas e seja capaz de realizar
as seguintes operacões:
  - armazenar
  - remover
  - buscar
  - imprimir lista de agenda
  - imprimir dados de contato
"""

class Pessoa():

    def __init__(self, nome: str, phone: str, email: str) -> None:
        self.__nome: str = nome
        self.__phone: str = phone
        self.__email: str = email


    @property
    def nome(self):
        return self.__nome

    @property
    def phone(self):
        return self.__phone

    @property
    def email(self):
        return self.__email
