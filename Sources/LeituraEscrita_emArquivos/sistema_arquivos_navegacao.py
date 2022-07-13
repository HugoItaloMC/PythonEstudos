"""
Sistema de arquivos e Nevegacão

 Para fazer o uso e manipulacão de arquivos do sistema operacional, precisamos importar
o módulo ' os '.

os -> Operating System - Sistema Operacional

"""

# Fazendo o import

import os

# retornando o caminho corrente :

print(os.getcwd())  # /home/correia/PycharmProjects/PythonEstudos/Sources/LeituraEscrita_emArquivos

# Mudando de diretório

os.chdir('/etc/')
print(os.getcwd())  # /etc

# Retornando sistema operacional

print(os.name)  # posix (Mac, Linux), nt (windows)

#  Ultilizando o módulo sys
#  Fazendo import

import sys
print(sys.platform)

# Retornando mais detalhes do Sistema Operacional

print(os.uname())
"""
posix.uname_result(sysname='Linux', nodename='bulleyese', release='5.10.0-16-amd64', 
version='#1  SMP  Debian  5.10.127-1  (2022-06-30)',  machine='x86_64')

"""

# Podemos Chegar se um diretório é absoluto ou relativo

print(os.path.isabs('/home/correia'))  # True


# Exemplos mais complexos

print(os.getcwd())  # /etc/

res = os.path.join(os.getcwd(), 'network')
"""
 Perceba que os.path.join() recebe dois parametros, sendo o primeiro o diretório atual, e os seguintes os diretórios
vão se integrar ao diretório atual.
"""
os.chdir(res)

print(os.getcwd())  # /etc/network

# Listando os diretórios

print(os.listdir())
# /etc/network -> ['if-post-down.d', 'if-down.d', 'interfaces.d', 'if-pre-up.d', 'interfaces', 'if-up.d']

# Podemos passar um path (caminho) para ser listado no siste

print(os.listdir('/home/correia/Downloads'))

# Podemos listar arquivos e diretórios com mais detalhes

scan = os.scandir()

arq = list(scan)

print(arq[0])

print(dir(arq[0]))  # Métodos que podemos ultilizar com a variável

print(arq[0].name)  # Retorna o nome do arquivo na posicão 0
print(arq[0].inode())  # Retorna o valor node da árvore de diretórios
print(arq[0].is_dir())  # É um diretório? False
print(arq[0].is_file())  # É um arquivo (file) ? True
print(arq[0].is_symlink())  # É um link simbólico? False
print(arq[0].path)  # Retorna o caminho que o arquivo se encontra
print(arq[0].stat())  # Estatísticas sobre o arquivo

# OBS !  Quando ultilizamos a funcão scandir() criamos uma conexão, temos que fecha-lá

scan.close()