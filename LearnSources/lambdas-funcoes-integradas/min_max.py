lista = [22, 33, 4, 1, 22, 44434, 12]

tupla = (22, 33, 4, 1, 22, 44434, 12)

conjunto = {22, 33, 4, 1, 22, 44434, 12}

dicionario = { "a": 22, "b": 33, "c": 4, "d": 1, "e": 22, "f": 44434, "g":12}

print(max(lista))
print(min(lista))

print(max(tupla))
print(min(tupla))

print(max(conjunto))
print(min(conjunto))

print(max(dicionario))
print(min(dicionario.values()))

n1 = int(input("Digite valor: "))
n2 = int(input("Digite Valor: "))

print(max(n1, n2))
print(min(n1, n2))


print(max(11, 2, 33, 4, 12311, 0))
print(min(11, 2, 33, 4, 12311, 0))

musicas = [
    {"titulo": "OldBand", "tocou": 2},
    {"titulo": "schollBand", "tocou": 1},
    {"titulo": "OmegaAlfa", "tocou": 6},
    {"titulo": "SerieMusic", "tocou": 5}
]

print(max(musicas, key=lambda musica: musica["tocou"])["titulo"])
print(min(musicas, key=lambda musica: musica["tocou"])["titulo"])