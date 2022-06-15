"""
Levantando os próprios erros com raise

 OBS: O raise ñ é uma funcão. É uma palavra reservada, assim como def ou qualquer outra em Python

 raise -> Lanca excecões e finaliza a funcão

 Para simplificar, pense no raise como sendo útil para que possamos criar nossas próprias excecões e
mensagens de erro

 # Exemplos de como ultilizar o raise:

raise TypeError('Mensagem de Erro')
"""


# Exemplos :

def colore(texto, cor):
    cores = ('vermelho', 'rosa', 'azul', 'amarelo', 'verde')
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('Texto precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'As cores tem que ser {cores}')
    print(f'{texto}, {cor}')


colore('ana', 'lilas')
