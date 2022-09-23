"""
  Faca um programa que receba do usuário um arquivo e um caractere que e mostre quantas vezes
aquele caractere ocorre dentro do arquivo

"""

# Realizando import

from MyFolder.MySources.myFunctions import strFunction as stFun

n = f"{input('Digite caminho/nome do arquivo : ')}"

if n == 'arq.txt':
    with open("arq.txt", "r+") as arq:
        arqLen = arq.read()
        print(stFun.put_case(f"{arqLen}"), f"ocorrencias encontras ")
