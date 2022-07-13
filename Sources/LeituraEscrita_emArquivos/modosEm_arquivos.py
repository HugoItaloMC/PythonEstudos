"""
Modos em arquivos com Python.

 'r' -> Modo de leitura (default)
 'w' -> Modo de escrita, sobreescreve caso o arquivo já exista
 'a' -> Modo escrita, SEMPRE escreve na última linha caso o arquivo já exista. Não controlamos o cursor
 'x' -> Modo escrita, cria um arquivo, caso já exista será gerado  ' FileExistsError '
 '+' -> Modo de atualizacão, deve-se ser atribuido com outro modo: " Ex open('texto.txt', 'r+') "
com esse modo podemos controlar o cursor
"""
