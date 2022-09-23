"""
  Faca um programa que que abra um arquivo, calcule e escreva  o número de linhas,  caracteres, palavras,
neste arquivo. Escreva também quantas vezes cada letra ocorre no arquivo (ignorando letras com acento). OBS:
palavras são separadas por um espaco ou mais, tabulacão '\t' nova linha '\n'

"""

import re
from collections import Counter
from MyFolder.MySources.myFunctions import regexFunction as rgFunc
arq = open("dataCitys.txt", "r+")
arq = arq.read()
a = ''
print(len(re.sub(r"[^\n]", '', arq)), f'linhas, \n{len(rgFunc.rgx_put_char(arq))} caracteres\n',
      f"{len(rgFunc.rgx_put_word(arq))} palavras\n",
      f"""{Counter([line for line in arq.split()], ).get(f"{input('Digite busca: ')}")} Ocorrências da busca """)