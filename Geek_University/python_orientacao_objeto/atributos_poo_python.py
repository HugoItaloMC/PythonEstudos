"""
POO - Atributos:
  - Atributos: Representam características do objeto. Pelos atributos
  nós conseguimos representar computacionalmente os estados do objeto.

# Em Python , dividimos os atributos em 3 grupos
    - Atributos de Instância
    - Atributos de classe
    - Atributo dinâmico

    :Atributos de Instâncias -> São atributos declarados dentro do método construtos '__init__'
    :OBS -> Método construtor é um método especial utilizado para a construcão do objeto.

"""

# ATRIBUTOS DE INSTÂNCIAS

# Atributos Públicos


class Lampada:

    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligado = False


class ContaCorrente:

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


""" 
  Em python por convencão todos os atributos são públicos, podem ser acessados em todo o projeto.
Caso queiramos demonstrar que determinado atributo deve ser tratado como privado, ou seja, que deve
ser acessado /utilizado somente dentro da própria classe onde está declarado, utiliza-se __ duplo
underscore no inicio do seu nome.
 Lembre-se que isso é apenas uma convencão, ou seja, a linguagem Python não vai impedir que facamos
acesso aos atributos sinalizados como privados fora da classe

Isso é conhecido também como Name Mangling
"""

# Atributos Privados


class Acesso:

    def __init__(self, email, senha):
        # Declarando atributo privado com duplo underscore __
        self.email = email
        self.__senha = senha

    def mostra_email(self):
        print(self.email)

    def mostra_senha(self):
        print(self.__senha)


user = Acesso('email@meuemail.com', '1020304050')

print(user.email)

# print(user.__senha)  # AttributeError:

print(dir(user))  # Verificando métodos com a classe

# OBS: Ao criarmos atributos privados o Python utiliza Name Mangling e cria um método iniciando com underscore
# o nome da classe duplo underscore o nome do atributo privado

print(user._Acesso__senha)  # Temos acesso. MAs não deveriamos fazer esse acesso Name Mangling.

user.mostra_email()
user.mostra_senha()

"""
 # O que significa atributos de instância?
 
     - Significa que ao criarmos instâncias/objetos de uma classe, todas as instâncias
terão esse atributo.
"""

user1 = Acesso('userfoo@fooemail.com', '1251414')
user2 = Acesso('userline@lineemail.com', '1222323990')

user1.mostra_email()
user2.mostra_email()

user1.mostra_senha()
user2.mostra_senha()


""" 
# ATRIBUTOS DE CLASSES
  - Atributos de classes são atributos declarados diretamente na classe, fora do método construtor.
Geralmente já inicializamos um valor, e este valor é compartilhado entre todas as instâncias da classe.
Ao invés de cada instância da classe ter seus próprios valores como é o caso dos atributos de instâncias,
com os atributos de classe todas as instâncis terão o mesmo valor para este atributo.
"""

class Produto:

    # Atribuindo Atributo de classe
    imposto = 1.05  # 0.05% de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id

produto1 = Produto('Playstation 5', 'video-game', 2500)
produto2 = Produto('Xbox S', 'video-game', 4500)

print(produto1.valor)
print(produto2.valor)

print(produto1.id)
print(produto2.id)

# OBS :  Não precisamos criar uma instância de uma classe para fazermos acesso ao um Atributo de Classe
print(Produto.imposto)

# ATRIBUTOS DINÂMICOSi -> Atributos de instâncias que pode ser criado em tempo de execucão
# OBS :  O Atributo Dinâmico será exclusivo da instância que o criou

# Criando um atributo dinâmico em tempo de execucão

produto2.peso = '5kg'  # Note que na classe Produto mão existe o atributo Peso

print(f"\n\t...Produto : {produto2.nome} \n\t...Descricao : {produto2.descricao} \n\t...Valor : {produto2.valor} \n\t...Peso : {produto2.peso}")
#  print(f"Produto : {produto1.nome} Descricao : {produto1.descricao} Valor : {produto1.valor} Peso : {produto1.peso}")  # AttributeError:



# Verificando estrutura da classe
print(produto1.__dict__)
print(produto2.__dict__)

# Deletando Atributos Dinâmicos
del produto2.peso
print(produto2.__dict__)

