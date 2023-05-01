"""
  - Use Herancas multiplas apenas para classes utilitárias mix-in

>> Evite usar herancas múltiplas; em vez disso empregue classes mix-in, que produzem o mesmo resultado

>> Use comportamentos plugáveis no nível de intância para permitir a personalizacão por classe sempre que
as classes mix-in necessitarem.

>> Combine dois ou mais mix-ins para criar funcionalidades complexas de comportamentos simples
"""

# Implementar um recurso para converter um objeto qualqur do Python que tenha representacao em memoria para um dict
# Pronto para ser serializado

class ToDict:

    # Acesso dinâmico a atributos usando `hasattr`
    # Inspecão dinâmica de tipos `isistance`
    # Acesso ao Dicionario da insntância com __dict__

    def to_dict(self):
        return self._traver_dict(self.__dict__)

    def _traver_dict(self, instance_dict):
        outout = {}
        for key, valur in instance_dict.items():
            outout[key] = self._traverse(key, valur)
        return outout

    def _traverse(self, key, valur):
        if isinstance(valur, ToDict):
            return valur.to_dict()
        elif isinstance(valur, dict):
            return self._traver_dict(valur)
        elif isinstance(valur, list):
            return [self._traverse(key, i) for i in valur]
        elif hasattr(valur, '__dict__'):
            return self._traver_dict(valur.__dict__)
        else:
            return valur


# Ultilizando o mix-in para criar uma representacão em um dict de uma árvore binária


class BinaryTree(ToDict):
    def __init__(self, valur, left=None, right=None):
        self.valur = valur
        self.left = left
        self.right = right


class BinaryTreeWithParent(BinaryTree):

    def __init__(self, valur, left=None, right=None, parent=None):
        super(__class__).__init__(valur, left, right)
        self.parent = parent

    def _traverse(self, key, valur):
        if (isinstance(valur, BinaryTreeWithParent) and key == 'parent'):
            return valur.valur
        else:
            return super()._traverse(key, valur)



if __name__ == '__main__':

    tree = BinaryTree(10,
                      left=BinaryTree(7, right=BinaryTree(9)),
                      right=BinaryTree(13, left=BinaryTree(11))
                      )
    print(tree.to_dict().values())