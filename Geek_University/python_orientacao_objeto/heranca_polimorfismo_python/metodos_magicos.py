"""
  POO -
   - Métodos Mégicos com POO em Python
    : Métodos Mágicos são todos os métodos que utilizam __NomeDoMétodo__ 'dunder'
    Duble Underscore
    : Conhecendo alguns métodos mágicos
      ->  __repr__
           - Por padrão o Python Representa o objeto mostrando o seu tipo e o endereco de memório
           utilizando o método magico __repr__ podemos reescrever a representacão do objeto. Esse
           método é utilizado para o programador saber a representacão do objeto ñ é utilizado
           para representar para o usuário final


      -> __str__
          - Tem prioridade em representar o objeto ao usuário final utilizando a funcão
          print()

      -> __len__
          - Retorna o tamanho dos atributos do objeto

      -> __del__
          -  Controla Remocões do Objeto

      -> __add__
          - Quando executamos operador matemático + internamente estamos utilizando este método
          mágico da linguagem Python
"""


class Livro(object):
    """ Objeto Para instanciar livros"""

    def __init__(self, nome, autor, paginas):
        self.nome = nome
        self.autor = autor
        self.paginas = paginas

    # Aplicando Método __repr__
    def __repr__(self):
        return f"\n...livro : {self.nome} \n...Autoria : {self.autor}"

    # Aplicando __str__
    def __str__(self):
        return self.nome

    # Aplicando __len__
    def __len__(self):
        return self.paginas

    # Aplicando Método __del__
    def __del__(self):
        print("Um objeto do tipo Livro foi Excluido")

    # Aplicando __add__
    def __add__(self, other):
        return f"{self} - {other}"

    def __mul__(self, other):
        if isinstance(other, int):
            msg = ''
            for n in range(other):
                msg += ' ' + str(self)
            return msg
        return 'Object Not Implemented Operation *'



livro1 = Livro("Python Rocks ! ", "Geek", 400)
livro2 = Livro("Machine Learning with Python ", "geek", 480)

# Acessando __str__
print(livro1)
print(livro2)
foolivro = livro1
barlivro = livro2
print(foolivro)
print(barlivro)

#  Acessando __repr__
print(repr(livro1))
print(repr(livro2))

# Utilizando len()
print(f"\n...{len(livro1)} Páginas \n...Livro : {livro1}")
print(f"\n...{len(livro2)} Páginas \n...Livro: {livro2}")


# Concatenando
print(livro1 + livro2)
print(livro1 * 2)
print(livro2 * 3)

"""
 - Lembrando que retornamos a saída do Objeto no método mágico __str__, no exemplo Livro1 Retorna : Python Rocks ! 
 e livro2 retorna : Machine Learning Pythn
"""