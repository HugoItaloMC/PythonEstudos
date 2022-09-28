"""
 Faca um programa que leia um arquivo contendo as dimensões de uma matriz (linha, coluna). a quantidade de posicões
que serão anuladas (linhas, colunas). O programa lê esse arquivo e em seguida gera um arquivo de saída com a matriz
com as posicões anuladas e as demais recebendo o valor 1.

"""
import re
# 2 - Gerando uma matriz
matriz_: list[int]
matriz_ = [['*' for a in range(1, 5)] for b in range(1, 5)]
try:
    with open(f"{input('Digite Arquivo de armazenamento : ')}.txt" ,"w+") as arq:
        arq.write(re.sub(r'],', ']\n', str(matriz_)))
        with open(f"{input('Digite Arquivo de saída : ')}", "w+") as arq_after:
            colune_ = int(input('Digite Coluna: '))
            line_   = int(input('Digite Linha: '))
            matriz_[colune_][line_] = '0'
            arq_after.write(re.sub(r'],', ']\n', str(matriz_)))
except Exception as err:
    print(f"Error && {err}")