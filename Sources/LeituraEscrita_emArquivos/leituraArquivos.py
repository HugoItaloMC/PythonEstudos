"""
Leitura de arquivos

  Para lermos um arquivo ultilizamos a funcão integrada open()
  open() -> Na sua forma mais simples de ultilizacão, passamos como parametro apenas o caminho do arquivo a ser
lido. Essa funcão retorna um _io.TextIOWrapper e é com ele que trabalhamos.

# OBS !  Por padrão a funcão open() abre o arquivo para leitura, o arquivo deve existir, senão teremos
FileNotFoundError

  Para visualizarmos um conteúdo do arquivo ultilizamos a funcão read()
  read() -> Visualiza o arquivo especificado ultilizando o cursor, após a visualizacão o cursor
se encontra-rá no final do arquivo impossibilitando a leitura do conteúdo no caso de ultilizar
o read() em outra parte do código novamente.
"""

arquivo = open('texto.txt')

print(arquivo)  # Retorna Parametros e atributos do arquivo

print(type(arquivo))  # Retorna o tipo do arquivo ' _io.TextIOWrapper '

print(arquivo.read())  # Retorna conteúto do arquivo
