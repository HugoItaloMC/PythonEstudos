"""
 Unittest - Antes e Depois dos Hooks
   - Hooks são os testes em sí, execucão dos testes

setup() -> É executado antes de cada método de teste.
É útil para criarmos isntâncias de objetos e outros
dados.

tearDown() -> É executado ao final de cada método de teste
É útil para excluir dados e fechar coneXões com banco de
dados.
"""

import unittest

class ModuloTest(unittest.TestCase):

    def setUp(self):
        # Configuracao setuo()
        pass
    