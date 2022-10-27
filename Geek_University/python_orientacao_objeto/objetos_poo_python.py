"""
POO: OBJETOS -> São instâncias da classe, após o mapeamento do objeto do mundo real para a sua repre-
sentacão computacional, devemos poder criar quantos objetos forem necessários. Podemos pensar nos ob-
jetos/instâncias de uma classe como variáveis do tipo definido na classe.
"""


class Lampada:

    def __init__(self, voltagem, cor, luminosidade):
        self.__luminosidade = luminosidade
        self.__voltagem = voltagem
        self.__cor = cor
        self.__ligado = False

    def checa_lampada(self):
        return self.__ligado

    def ligar_desligar_lampada(self):
        if self.__ligado:
            self.__ligado = False
        else:
            self.__ligado = True


class Cliente:

    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    def diz_oi(self):
        print(f"O cliente {self.__nome} diz oi !!")


class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo, cliente):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        self.__cliente = cliente
        ContaCorrente.contador = self.__numero

    # Acessando atributos de outras Classes via método de instância utilizando 'Name Mangling'

    def mostra_cliente(self):
        print(f"O clinte é {self.__cliente._Cliente__nome}")


class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__sobrenome = sobrenome
        self.nome = nome
        self.email = email
        self.senha = senha


# INSTÂNCIA(s)/OBJETO(s):

lamp1 = Lampada(110, 'azul', 60)
# Por Default definimos a lampada desligada 'False'
lamp1.ligar_desligar_lampada()  # Ligando lampada
print(f'A lampada está ligada? \n\t...{lamp1.checa_lampada()}')
lamp1.ligar_desligar_lampada()  # Desligando Lampada

# conta_corrente = ContaCorrente(5000, 20000)

usuario_sys = Usuario('Italo', 'Correia', 'italo@gmail.com', '1020304050')

# Instânciando Classes com outras classes

cliente_conta_corrente = Cliente('Italo Correia', '787.334.981-22')
conta_cliente = ContaCorrente(5000, 20000, cliente_conta_corrente)

conta_cliente.mostra_cliente()

"""
  Ao passarmos como argumento de uma Classe outro objeto de classe, da classe herdada temos acesso a todos os 
atributos, métodos de instâncias. No nosso exemplo conta_cliente que é do tipo ContaCorrente() recebe no seu
atributo cliente como valor clinete_conta_corrente que é do tipo Cliente(), fazendo isso conta_cliente tem 
acesso total a atributos e métodos de instâncias de cliente_conte_corrente.
"""
conta_cliente._ContaCorrente__cliente.diz_oi()  # Acessando utilizando 'Name Mangling'. Lembrando que é uma má prática.
