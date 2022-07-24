"""
     - Podemos ultilizar sorted() com qualquer iterável,
    o comando sorted() server para ordenar um iterável.
"""
numeros = [77, 44, 3, 1111, 5, 4, 3, 0.12]

print(numeros)

print(sorted(numeros))

print(sorted(numeros, reverse=True))  # Reverte a a ordenacão do maior para o menor

usuarios = [
    {"username": "ana", "tweet": ['tomei banho', 'passeio com o gato'], "cor": "rosa", "musica": "axé", "profissão": "doméstica"},
    {"username": "sofia", "tweet": [], "hobbie": "livros", "profissão": "manicure"},
    {"username": "miguel", "tweet": [], "esporte": "futebol", "hobbie": "carros", "cor": "vermelho"},
    {"username": "carlos", "tweet": ['Bom dia', 'Bom trabalho', 'Almoco estava ótimo'], "post": [], "esporte": "formula1", "música": "rock", "cor": "azul",
     "data": "16/07/1993"}
]
print(usuarios)

print(sorted(usuarios, key=lambda usuario: usuario["username"]))  # Ordenando lista

print(sorted(usuarios, key=lambda usuario: len(usuario['tweet'])))

musicas = [
    {"titulo": "OldBand", "tocou": 2},
    {"titulo": "schollBand", "tocou": 1},
    {"titulo": "OmegaAlfa", "tocou": 6},
    {"titulo": "SerieMusic", "tocou": 5}
]
# Da menos tocada para a mais tocada
print(sorted(musicas, key=lambda musica: musica["tocou"]))

#  Da mais tocada a menos tocada
print(sorted(musicas, key=lambda musica: musica["tocou"], reverse=True))