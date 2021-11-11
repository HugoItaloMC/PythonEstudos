"""
Funcoes com Parametros (entrada)
 - Funcões que recebem dados para serem processados dentro da mesma.

Se pensarmos em um programa qualquer, geralmente temos :
 - entrada;
 - processamento;
 - saída;

Se pensarmos em uma funcão, já sabemos que temos funcões que:
 - Não possuem entrada;
 - Não possuem saída;
 - Possuem entrada mas não possuem saída;
 - Não possuem entrada mas possuem saída;
 - Possuem entrada e saída;
"""

# Exemplos de funcões com parametros

def quadrado(numero):
    return numero ** 2

print(quadrado(2))

# print(quadrado()) -- TypeError funcão nescessita de um parametro