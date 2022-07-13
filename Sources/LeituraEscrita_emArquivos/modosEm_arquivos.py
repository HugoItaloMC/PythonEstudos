"""
Modos em arquivos com Python.

 'r' -> Modo de leitura (default)
 'w' -> Modo de escrita, sobreescreve caso o arquivo já exista
 'a' -> Modo escrita, SEMPRE escreve na última linha caso o arquivo já exista. Não controlamos o cursor
 'x' -> Modo escrita, cria um arquivo, caso já exista será gerado  ' FileExistsError '
 '+' -> Modo de atualizacão, deve-se ser atribuido com outro modo: " Ex open('texto.txt', 'r+') "
com esse modo podemos controlar o cursor
"""
# Exemplos :

with open('teste.txt', 'w') as arq:  # Modo de reescrita
    arq.write('Teste')

# with open('teste1.txt', 'x') as arq:  # Modo de criacão e escrita, FileExistsError se o arquivo já existir
#    arq.write('Teste')

with open('teste1.txt', 'a') as arq:  # Modo de escrita, insere conteúdo SEMPRE ao final do arquivo
    arq.write('teste222')

with open('teste1.txt', 'r+') as arq: # Modo de atualizacão, leitura e escrita, controlamos o cursor.
    arq.seek(0)
    arq.write('\nTeste')
    arq.seek(7)
    arq.write('\nTEste222')