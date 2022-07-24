"""
 O bloco with
 Forma geral de uso :
 with open('texto.txt') as arquivo:
     // Trabalhando o arquivo

 Há ultilizacão do bloco with para se manipular arquivos é a forma 'pythônica' de executar essa tarefa por
linhas de comando.
"""
with open('texto.txt') as arquivo:
    print(arquivo.read())