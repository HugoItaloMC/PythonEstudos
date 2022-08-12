"""
  Faca um programa que receba do usuário um arquivo, e mostre na tela quantas vezes cada caractere
é ocorrido dentro do arquivo.

"""

from collections import Counter

way = f"{input('Digite caminho/nome do arquivo : ')}"

if way == 'arq.txt':
    with open('arq.txt', 'r+') as arq:
        arqLen = arq.read()
        res = Counter(arqLen)
        print(res)
