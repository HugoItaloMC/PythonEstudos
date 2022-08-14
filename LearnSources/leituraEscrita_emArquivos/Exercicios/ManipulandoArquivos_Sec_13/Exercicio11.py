"""
  Faca um programa em que o usuário informe o nome do arquivo e uma palavra, e retorne
o número de vezes que aquela palavra aparece no arquivo

"""

arq = open(
    '/home/correia/PycharmProjects/MyPythonSources/LearnSources/leituraEscrita_emArquivos'
    '/Exercicios/ManipulandoArquivos_Sec_13/Exercicio10/dataCitys.txt')

arq = arq.read().lower()
print(arq.count(f"{input('Digite o nome da cidade : ').lower()}"), 'Ocorrência(s) no arquivo')
