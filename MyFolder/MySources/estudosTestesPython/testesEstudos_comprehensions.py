"""
  Testes com comprehensions de Python,
  Ultilizando a versão do Python 3.10

"""

iteravel = [[1, 2, 3, 4], [6, 5, 4, 3, 2, 1], [0, 2, 4, 6]]

put = [[print(it2, end=f', ') for it2 in it1] for it1 in iteravel[::1]]
