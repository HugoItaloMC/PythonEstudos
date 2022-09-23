"""
Pacotes

Módulos -> São arquivos Python contendo diversas funcões

Pacote -> É um direório contendo diversos módulos

  Em Python 2.x em um pacote deveria conter dentro dele um arquivo __init__.py,
nas versões 3.x este arquivo não é obrigaório, normalmene ainda é ultilizado para
manter a compatibilidade.

"""

#  Importando pacotes e sub-pacotes

from Sources.Funcoes_Python import funcoes_com_parametroPadrao as fcPp

try:
    quantidade_loop = int(input("Digite Quantidade de loops: "))
except (ValueError, NameError, ArithmeticError, TypeError) as err:  # Tratando erros Built-in's do Python
    print(f"ERRO : {err}")  # Saída de Erro
else:
    for _ in range(1, quantidade_loop):
        try:
            n = 0
            a = int(input('Digite Valor 1: '))
            b = int(input('Digite Valor 1: '))
            n += fcPp.soma(a, b)
        except (ValueError, NameError, ArithmeticError, TypeError) as err:  # Tratando erros Built-in's do Python
            print(f"ERRO : {err}")  # Saída de Erro
        print(f'''resulado {n}''') if n != 0 else None
