"""
Link com built-in do tratamento de excessoes
https://docs.python.org/pt-br/3/library/exceptions.html

Erros mais comuns em Python

ATENCAO! E importante prestar atencao a ler as saidas de erros geradas pela execucao
do nosso codigo

Os Erros mais comuns:

SyntaxError -> Ocorre quando o Python encontra um erro de sintaxe. Ou seja, vc escreveu algo que
o Python nao reconhece como parte da linguagem.

# Exemplos SyntaxError:

a)
def funcao:
    print("Ola")

b)
def = 1

c)
return

2 - NameError -> Ocorre quando uma variavel nao foi definida.

# Exemplo NameError:

a)
print(geek)

b)
geek()

3 - TypeError -> Ocorre quando uma funcao/operacao/acao e aplicada a um tipo errado.

# Exemplos TypeError:

a)
print(lent(5))

b)
print('geek' + [])

4 - IndexError -> Ocorre quando tentamos acessar um elemento em um iteravel ou outro tipo de dado indexado
ultilizando um indice invalido

# Exemplos IndexError

a)
lista = ['geek']
print(lista[2])

b)
lista = ['geek']
print(lista[0][10])

c)
tupla = ('geek')
print(tupla[0][10])

5 - ValueError -> Ocorre quando uma funcao integrada (built-in) recebe um argumento com tipo correto
mas com valor inapropriado

# Exemplos ValueError:

a)
print(int('geek'))

6 - KeyError -> Ocorre quando tentamos acessar um dicionario com uma chave inexistente

# Exemplos KeyError:

a)
dic = {'python': 'university'}
print(dic['geek'])

7 - AtributeError -> Ocorre quando uma variavel nao tem um atributo/funcao

# Exemplos AtributeError:

a)
tupla = 11, 22, 37, 488
print(tupla.sort())

8 - IndentationError -> Ocorre quando nao respeitamos a indentacao do Python (4 espacos)

# Exemplos IndentationError:

a)
def funcao():
print('ola')

b)
for n in range(1000):
print(n)
"""

