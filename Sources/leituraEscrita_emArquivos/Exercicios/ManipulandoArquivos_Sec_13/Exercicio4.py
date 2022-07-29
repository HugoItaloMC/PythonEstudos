"""
Receba do usuário arquivo de texto, e verifique quantas letras são vogais e quantas consoantes

"""


# Realizando imports

from testesEstudos.myFunctions import strFunction as stFun

n = input('Digite path (caminho/nome) do arquivo: ')
if n == 'arq.txt':
    with open('arq.txt', 'r+') as arq:
        arqLen = arq.read()
        print(stFun.it_vogais(arqLen), f"Vogais")
        print(stFun.it_consoantes(arqLen), f"Consoantes")
