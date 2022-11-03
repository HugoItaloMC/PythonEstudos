"""
  - Assertions (afirmacão)
   : Pensamos afirmacões em testes como checagem/questionamentos
   : Em Python utilizamos assertions para questionamentos
   : Utilizamos a palavra 'assert' para realizar simples afirmacões
utilizadas nos testes
   : O 'assert' em uma expressão que queremos checar se é válido ou não,
se a expressão for verdadeira retorna None se caso seja falsa levanta um Erro
AssertionError
   : Podemos especificar, opicionalmente, um segundo argumento ou mesmo mensagem
personalizada para determinado erro
  : assert pode ser utilizada em qualquer funcão ou código nosso...não precisa exclusivamente
ser nos testes

  ATENCÃO : deve-se ter cuidado ao utilizar 'assert' pois a passarmos a flag -O na execucão do módulo
que se encontra o bloco os tratanentos serão ignorados e o código é executado normalmente sem as regras
estabelecidas
"""

# assert 4 == 2, 'Numerics not equals'

# Utilizando funcões com assrert
def positive_number(a, b):
    assert a> 0 and b > 0, 'Don`t write number negative'
    return a + b


ret = positive_number(1, 2)
print(ret)

ret_foo = positive_number(1, -1)
print(ret_foo)


def fast_food(food):
    assert food in [
        'pizza',
        'sorvete',
        'lanche',
        'batata-frita',
        'doce'
    ], 'Request food in Menu'
    return f'Eating food {food}'

pedido = fast_food('arroz')
print(pedido)

pedido_foo = fast_food('pizza')
print()