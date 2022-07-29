"""
  Faca um programa que recebe udo usuario um arquivo, crie outro arquivo contendo as informacões do primeiro arquivo,
só que o usuário deve escolher qual caractere vai alterar e por qual caractere vai ser substituido:

"""
from testesEstudos.myFunctions import changeFunction as chFun
arq = open('arq.txt', 'r+')

chFun.change_string(arq)