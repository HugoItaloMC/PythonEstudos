"""
zip

zip(): Cria um iteravel do tipo (Zip Object) que agrega de cada um dos iteraveis passados como entrada em pares.
"""

# exemplos zip()

lista1 = [2, 3, 4, 5, 5, 9]
lista2 = [3, 4, 5, 6, 1, 2]

zip1 = zip(lista1, lista2)
print(zip1)  # Retornando o tipo (Zip object)

#  Retornando a ocorrencia de como funciona o comando zip(), ocorrencia em pares
# [(Posicao1_lista1, posicao1_lista2), (posicao2_lista1, posicao2_lista2), (posicao3_lista1, posicao3_lista2)]
print(list(zip1))  # Retornando uma lista com tuplas como ocorrencias

# Podemos ultilizar sintetizar diferentes iteraveis com o comando zip()

lista = [1, 2, 3, 4]
tupla = 1, 2, 4, 5
dicionario = {'a': 1, 'b': 2, 'c': 6, 'd': 7}

print(list(zip(lista, tupla, dicionario.values())))

# Descompactando uma lista de tuplas com zip()

listaTupla = [(1, 2, 3), (3, 2, 1), (6, 5, 4), (4, 5, 6)]

print(list(zip(*listaTupla)))  # Lembrando que (*iteravel) descompacta ocorrencias no iteravel


# Exemplos mais complexos

valor1 = [88, 90, 102]
valor2 = [77, 344, 1]

pessoas = ['joao', 'maria', 'pedro']

#  Ultilizando dict comprehensions
verificacao = {dados[0]: max(dados[1], dados[2]) for dados in zip(pessoas, valor1, valor2)}
print(verificacao)

#  Ultilizando map(), lambda

verificacao = zip(pessoas, map(lambda nota: max(nota), zip(valor1, valor2)))
print(dict(verificacao))
