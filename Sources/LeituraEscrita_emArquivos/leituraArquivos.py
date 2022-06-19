"""
Leitura de arquivos

  Para lermos um arquivo ultilizamos a funcão integrada open()
  Para visualizarmos um conteúdo do arquivo 
  open() -> Na sua forma mais simples de ultilizacão, passamos como parametro apenas o caminho do arquivo a ser
lido. Essa funcão retorna um _io.TextIOWrapper e é com ele que trabalhamos.

# OBS !  Por padrão a funcão open() abre o arquivo para leitura, o arquivo deve existir, senão teremos
FileNotFoundError


"""

arquivo = open('texto.txt')

print(arquivo)  # Retorna Parametros e atributos do arquivo

print(type(arquivo))  # Retorna o tipo do arquivo ' _io.TextIOWrapper '

print(arquivo.read())  # Retorna conteúto do arquivo