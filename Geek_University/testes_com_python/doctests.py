"""
  - Doctests
    : O próprio teste é uma documentacão, com o seus testes outros desenvolvedores podem enteder
melhor do funcionamento do seu sistema
    : É a mesta idéia de docstrings em nossas funcões, ou seja doctests serve para documentar
nossos testes.

"""
def soma(a, b):
    """
    Soma os valores de a e b

    >>> soma(1, 2)
    3
    """
    return a + b
"""
 python -m doctest -v nome_do_modulo.py 
Trying:
    soma(1, 2)
Expecting:
    3
ok
1 items had no tests:
    doctests
1 items passed all tests:
   1 tests in doctests.soma
1 tests in 2 items.
1 passed and 0 failed.
Test passed.

"""

# Outro Exemplo Aplicando o TDD

def duplicar_valores(valor):
    """
    Duplica valores em uma lista

    >>> duplicar_valores([1, 2, 3, 4])
    [2, 4, 6, 8]

    >>> duplicar_valores([])
    []

    >>> duplicar_valores(['a', 'b', 'c'])
    ['aa', 'bb', 'cc']

    # OBS :  Ao testarmos erros devemos saber qual sua mensagem no console Python
    >>> duplicar_valores([True, None])
    Traceback (most recent call last):
      ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    """
    return [] # - Com TDD vamos testando cada teste por vez
    #return [2 * line for line in valor]