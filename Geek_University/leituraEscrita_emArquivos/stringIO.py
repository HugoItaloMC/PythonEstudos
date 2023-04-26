"""
StringIO

 Para leitura e escrita de arquivos no Sistema Operacional, devemos ter permissão para manipular o arquivo
permissão de administrador.

StringIO -> Escreve em arquivos em memória no sistema

"""

# Exemplos

# Fazendo o import:

from io import StringIO

msg = 'Msg alocada'

# Criando arquivo já com uma string

arq = StringIO(msg)
# arq = open('teste.txt', 'w')

# Podemos ultilzar todos os métodos já conhecidos
print(arq.read())

# Escrevendo no arquivo StringIO
arq.write('Outra msg')

arq.seek(0)
print(arq.read())
"""
 OBS !  Ultilizando o StringIO o arquivo fica alocada na memória, e ñ é criado o arquivo na pasta do projeto
o arquivo fica implicito na memória
"""