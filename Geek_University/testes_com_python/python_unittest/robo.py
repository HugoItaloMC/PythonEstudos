class Robo:

    def __init__(self, nome, bateria=100, habilidades=[]):
        self.__nome = nome
        self.__bateria = bateria
        self.__habilidades = habilidades

    @property
    def nome(self):
        return self.__nome

    @property
    def bateria(self):
        return self.__bateria

    @property
    def habilidades(self):
        return self.__habilidades

    def carregar(self):
        self.__bateria = 100

    def comprimentar(self):
        if self.__bateria > 0:
            self.__bateria -= 1
            return f"Eu sou {self.__nome.upper()}"
        return 'Bateria Fraca por favor recarregue'

    def nova_habilidade(self, habilidade, custo):
        if self.__bateria >= custo:
            self.__bateria -= custo
            self.__habilidades.append(habilidade)
            return f"APRENDI {habilidade.upper()} UM NOVA HABILIDADE"
        return 'Bateria insuficiente pf recarregar !'