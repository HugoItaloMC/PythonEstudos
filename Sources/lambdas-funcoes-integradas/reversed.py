"""
reversed()

inverte um iterável e retorna um objeto "list reverse iterator"
"""
lista = [1, 33, 4, 5, 66]
res = reversed(lista)
print(res)

print(list(reversed(lista)))

print(tuple(reversed(lista)))

print(set(reversed(lista)))

# Podemos também reverter uma string ultilizando slice de string

# Recapitulando :

print("Hugo Italo"[::-1])


for letra in reversed("\nHugo Italo"):
    print(letra, end='')

print(''.join(list(reversed("Hugo Italo"))))

# Podemos ultizar o reversed para reverter um range em um for

for n in reversed(range(1, 1000)):
    print(n, end='\n')