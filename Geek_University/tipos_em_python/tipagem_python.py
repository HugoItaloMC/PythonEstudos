"""
 - Python é uma linguagem de Tipagem Dinâmica, ou seja, diferente do Java/C
o tipo de dado é atribuido no valor declarado, em Java/C temos que informar
o tipo de dado na sua declaracão
"""

# Tipagem Dinâmica

numero = 1

nome = 'Geek'
"""
  A partir do python 3.5 podemos atribuir um tipo em uma variável, chamado de Type Hinting,
que trabalha em conjunto com outra ferramenta chamda mypy, que verifica se as variáveis es-
tão sendo intânciadas da forma correta respeitando o Type Hinting. 
  O mypy é executado diretamente no terminal após suas instalacão utilizando PIP, exemplo :
    mypy nome_do_modulo.py
"""
# Utilizando Type Hinting em nossas funcões

class People:

    def __init__(self,nome: str, idade: int, peso: float ) -> None:
        self.__nome: str = nome
        self.__idade: int = idade
        self.__peso: float = peso

    def __len__(self):
        return 42

    def nome(self) -> str:
        return f"Olá eu sou, {self.__nome}\nMuito Prazer"


"""
 Duck Typing
   - do Provérbio : "Se anda como pato, nada como pato, corre como pato, é um pato"
   Objetos que se assemelham não por seu tipo, mas sim por seu valor contido e métodos
   utilizados
 Veja que na classe People declaramos um método mágico __len__ para assim podermos utilizar
este método no objeto do tipo People
"""

"""
 Annotations:
  - __annotations__ : Método Mágico para se verificar a estrutura Typing Hinying declarada
no objeto
"""

if __name__ == '__main__':
    # Entendendo Typing Hinting
    pessoa = People('Italo', 'ola', 68.5)
    print(pessoa.nome())

    # Entendendo Duck Type
    print(len(pessoa))
    print(len([12, 22, 33]))
    print(len('Geek'))

    # Lembra de Duck Typing, que Objetos se assemelham ñ por seu tipo mas por seu valor e métodos atribuidos
    # print(len(44))  # Error 'int' não se atribui o método len():

    # Entendendo Annotations

    print(pessoa.nome.__annotations__)  # Verificando Annotations do método de classe
    print(pessoa.__init__.__annotations__)  # Verificando Annotations do construtor dos parametros de entrada do objeto