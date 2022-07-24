"""
Seek e Cursor

seek() -> É ultilizado para movimentar o cursor pelo arquivo
readline() -> Funcão que lê o arquivo linha-a-linha, retorna um tipo de classe Str()
readlines() -> Funcão que lê arquivo linha-a-linha, retorna um tipo de Classe list()
"""

# Ultilizando seek() :

arquivo = open('texto.txt')

print(arquivo.read())  # A funcão read() retorna um objeto ' str '
arquivo.seek(0)  # voltando o cursos para a posicão 0 da string

"""
Lembrando que podemos fazer o acesso de uma string pela posicão da ocorrencia

letras = 'abcdef'
print(letras[0])
"""

# Ultilizando readline()

print(f'{arquivo.readline()}')

arquivo.seek(0)

# Lendo linhas e quantidade de letras do arquivo

print(len(arquivo.read()))  # Quantidade de letras/ocorrenciasString

arquivo.seek(0)  # Voltando o cursor para a o inicio do arquivo

print(len(arquivo.readlines())) # Quantidade de linhas do arquivo ultilizando readlines()
