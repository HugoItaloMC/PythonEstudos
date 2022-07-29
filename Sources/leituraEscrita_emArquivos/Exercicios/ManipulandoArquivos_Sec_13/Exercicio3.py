"""
  Faca um programa que receba do usuário um arquivo de texto e retorne quantas letras são vogais e
quantas letras são consoantes.

"""

# Realizando imports

from testesEstudos.myFunctions import strFunction as stFun

n = input('Digite path (caminho/nome) do arquivo: ')
if n == 'arq.txt':
    with open('arq.txt', 'r+') as arq:
        arqLen = arq.read()
        print(stFun.it_vogais(arqLen), f"Vogais")
