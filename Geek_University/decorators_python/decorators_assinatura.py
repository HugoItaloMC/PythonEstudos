"""
 - Decorators com diferentes assinaturas
A assinatura de uma funcão são seus parametros, retorno e nome
"""

# Decorator Pattern:
#  Com Decorator pattern podemos decorar funcões com mais de um parametro ou nem um parametro


def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f"Olá eu sou {nome}"


@gritar
def pedido_cardapio(principal, acompanhamento):
    return f"Olá gostaria de {principal}, acompanhado por {acompanhamento}"


@gritar
def lol():
    return 'lol'


#  Testando:
print(saudacao('Italo'))
print(pedido_cardapio('Bife', "Batata-Frita"))
print(lol())

# Decorator com argumentos


def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def pattern(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor informado invalido, o primeiro valor deve ser {valor}'
            return funcao(*args, **kwargs)
        return pattern
    return interna


@verifica_primeiro_argumento('pizza')
def comida_favorita(*args):
    print(args)


@verifica_primeiro_argumento(10)
def soma_dez(n1, n2):
    return n1 + n2


# Testando
print(soma_dez(10, 22))
print(soma_dez(1, 22))
while True:
    n = input('Digite Pedido\n Q para sair : ')  # Entrada de dados
    if n != '0':  # Caso condicional
    else:  # Caso de condicão de parada do arquivo
        break

comida_favorita("pizza", "Batata-Frita")

print(f"Pedido informado {pedido}")
print(comida_favorita('salada', 'pizza'))
