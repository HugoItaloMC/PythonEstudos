"""
POO - Métodos
- Métodos (POO) -> Representam os comportamentos dos objetos, acões que o objeto tem em seu sistema.
- Em Python, dividimos os métodos em 2 grupos: Métodos de Instância e Métodos de Classes.
# Método de instância
  - O método dunder init __init__ é um método especial chamado de construtor e sua funcão
 é criar o objeto a partir da classe.
  - Os métodos/funcões dunder do Python são chamados de métodos mágicos
"""
from passlib.hash import pbkdf2_sha256 as cryp


class Lampada:

    def __init__(self, voltagem, cor):
        self.__voltagem = voltagem
        self.__cor = cor
        self.__ligado = False


class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:

    # Atribuindo Atributo de classe
    imposto = 1.05  # 0.05% de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = (valor * Produto.imposto)
        Produto.contador = self.__id


class Usuario:

    # MÉTODOS DE CLASSES
    contador = 0

    @classmethod
    def conta_usuario(cls):
        print(f"Total usuarios {cls.contador}")

    # MÉTODO ESTÁTICO
    @staticmethod
    def definicao():
        return 'UXR34466'

    def __init__(self, nome, sobre_nome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobre_nome = sobre_nome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.__id
        print(f"Usuario criado {self.__gera_usuario()}")

    # MÉTODOS DE INSTÂNCIA
    def nome_completo(self):
        return f"{self.__nome} {self.__sobre_nome}"

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

    # MÉTODOS privados
    def __gera_usuario(self):
        return self.__email.split('@')[0]


nome = input("Informe Nome: ")
sobrenome = input("Informe sobre nome : ")
email = input("Informe Email : ")
senha = input("Informe Senha : ")
confirma_senha = input("Confirme Senha : ")

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)
else:
    print("Senha ñ confere")
    exit(1)

print("Usuário criado com sucesso !!!")

senha = input("Digite senha para acesso : ")

if user.checa_senha(senha):
    print("Login Sucefull ")
else:
    print("Acesso Negado")

print(f"Senha criptografada {user._Usuario__senha}")  # Acesso Errado a senha para verificar o hash da senha

Usuario.conta_usuario()
