import unittest
from robo import Robo

class RoboTests(unittest.TestCase):

    def setUp(self):
        self.megamen = Robo('Mega Man', bateria=50)
        print('setUp() sendo executado ...')

    def test_carregar(self):
        self.megamen.carregar()
        self.assertEqual(self.megamen.bateria, 100)

    def test_comprimentar(self):
        self.assertEqual(self.megamen.comprimentar(), 'Eu sou MEGA MAN')
        self.assertEqual(self.megamen.bateria, 49, 'A bateria deveria estar 49%')

    def tearDown(self):
        print('tearDown() sendo executado ...')

if __name__ == '__main__':
    unittest.main()
