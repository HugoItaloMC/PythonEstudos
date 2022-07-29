"""
 Sistema de Arquivos - Manipulacão

"""

import os

# Descobrindo se um arquivo ou diretório existe

print(os.path.exists('teste.txt'))  # True
print(os.path.exists('arquivo.txt'))  # False

print(os.path.exists('/home/correia/PycharmProjects/PythonEstudos/Sources')) # True

# Criando arquivos

# os.mknod('testeN1.txt')  # path relativo

# Se o arquivo já existir FileExistsError será gerado

# os.mknod('/home/correia/PycharmProjects/PythonEstudos/Sources/testesEstudos/testeString.txt')  # Path absoluto

# Criando diretórios

# os.mkdir('testePython')  # Path relativo

# os.mkdir('/home/correia/PycharmProjects/PythonEstudos/Sources/testePython')  # Path absoluto

# FileExistsError será gerado se o diretório já existir

# os.mkdir('/etc/testePython')  # PermissionError é gerado por falta de permissão no sistema operacional

# Criando multiplos diretórios (árvore-de-diretórios)

# os.makedirs('/home/correia/PycharmProjects/PythonEstudos/Sources/templates/core/app/style/script/', exist_ok=True)

# Renomeando arquivos ou diretórios

# Diretórios

# os.rename('/home/correia/PycharmProjects/PythonEstudos/Sources/templates', 'pattern')

# Alterou o nome e moveu o diretório para onde se encontra o '__main__'

# os.rename('pattern', 'templatePattern')

# Arquivos

os.rename('teste.txt', 'arquivoTeste.txt')