"""
Faca um programa que receba do usuário um arquivo de texto e mostre quantas linhas esse arquivo contém

"""

n = input('Digite path (caminho/nome) do arquivo: ')
if n == 'arq.txt':  # Verificando se arquivo existe
    with open('arq.txt', 'r+') as arq:  # Abrindo arquivo
        arq = len(arq.readlines())  # Processando quantidade de linhas do arquivo
        print(arq, f"Linha(s)")  # Retornando quantidade de linhas do arquivo.
