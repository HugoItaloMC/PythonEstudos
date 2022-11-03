import unittest
from atividades import dormir, comer

#


class AtividadesTestes(unittest.TestCase):
    """
      Por padrão declaramos o nome da clas
    se com o mesmo nome do módulo que esta-
    mos testando.
    """
    def test_comer_saudavel(self):
        self.assertEqual(
            comer('quiabo', True),
            'Estou comendo quiabo quero manter a forma'
        )

    def test_comer_nao_saudavel(self):
        self.assertEqual(
            comer(food='pizza', qualidade=False),
            'Estou comendo pizza Só se vive uma vez'
        )

    def test_dormir_pouco(self):
        self.assertEqual(
            dormir(4),
            'Estou cansado dormi pouco'
                         )

    def test_dormir_muito(self):
        self.assertEqual(
            dormir(10),
            'Dormi demais, estou atrasado'
        )

if __name__ == '__main__':
    unittest.main()