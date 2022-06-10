"""
Len, Abs, Sum, Round;

# len()
Retorna o número de itens de um iterável

# abs()
Retorna um valor absoluto de um inteiro ou um número real

# sum()
Soma valores inteiros ou reais de um iterável


# round()
Arredonda um número, podendo informar quantidade de casas decimais a serem exibidas
"""
# Exemplos len()

print(len("HUgo Italo"))

print(len([1, 2, 3, 4, 5, 66]))

print(len((1, 2, 3, 4, 5, 66)))

print(len({1, 2, 3, 4, 5, 66}))

print(len({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 66}))


# Exemplos abs()

print(abs(4.15))
print(abs(-4.15))
print(abs(5))
print(abs(-5))

# OBS : Se o número for negativo ele o retorna positivo

# Exemplos sum()


print(sum([1, 2, 3, 4, 5, 66]))

print(sum([1, 2, 3, 4, 5, 66], 6))

print(sum([1, 2, 3, 4, 5, 66], -1))

print(sum((1, 2, 3, 4, 5, 66)))

print(sum({1, 2, 3, 4, 5, 66}))


print(sum({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 66}.values()))

# Exemplos round()

print(round(3.14))

print(round(2.2345356, 2))  # Informando para exibir 2 casas decimais após o ponto

print(round(2.2345356, 4))  # Informando para exibir 4 casas decimais após o ponto

print(round(1.33 + 3.79, 3))