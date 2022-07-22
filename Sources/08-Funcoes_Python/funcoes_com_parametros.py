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


def canta_parabens(aniversariante):
    print(f"Parabéns pra voce\nnesta data querida\nmuitas felicidades",
          f"\nmuitos anos de vida.\n Felicidades {aniversariante} !!!\n")


canta_parabens('Ana')


def soma(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def multi(a, b, msg):
    return (a + b) * msg


print(soma(2, 15))


print(subtracao(10, 8))


print(multi(10, 20, 'Teste'))


# Nomeando funcões


def nome_nompleto(nome, sobrenome):
    return f"Nome Completo : {nome} {sobrenome}"


print(nome_nompleto('Angeline', 'Jolie'))


# OBS : se informarmos um número errado de parametros, sera gerado TypeError

# Parametros são variáveis declaradas na definicão de uma funcão;
# Argumentos são dados passados durante a execucão da funcão;

# A Ordem dos argumentos importam
# Nomear a funcão com o sentido que ela tem

# Exemplo:


nome = 'Sofia'
sobrenome = 'Souza'


print(nome_nompleto(nome, sobrenome))


# Arhumentos nomeados (Keyword Arguments)

# Caso ultilizemos o nome dos parametros nos argumentos podemos, para informa-los, podemos
# ultilizar qualquer ordem

print(nome_nompleto(nome='Clara ', sobrenome=' Silva'))
print(nome_nompleto(nome='Ingrid ', sobrenome=' Souza'))
print(nome_nompleto(sobrenome=' Silva', nome='Clara '))


def soma_impares(numero):
    total = 0
    for num in numero:
        if num % 2 != 0:    # -- return dentro do deste bloco if causaria a interrupcão da funcão
            total += num
    return total


list1 = [1, 2, 3, 4, 5, 6, 7]
print(soma_impares(list1))
