"""
Any e All

 All -> Retorna true se todos os elementos do iterável for verdadeiro ou se o iterável
se encontra vázio
 Any -> Retorna true se pelo menos 1 elemtento do iterável for verdadeiro e False se o iterável
estiver vázio
"""

# Exemplos com  all():

letras = 'abcde'
print(all([n for n in letras if n in 'abcde']))

nomes = ['Camila', 'Carlos,', 'Caique', 'Geovana', 'Carol']
print(all(n[0] == 'C' for n in nomes))  # A execucão para no primeiro False

print(f'{all(n for n in [1, 3, 4, 5, 6, 8, 9] if n % 2 == 0)}\n')

#  Exemplos com any():

print(any(n for n in letras if n in 'abcde'))

print(any(n[0] == 'C' for n in nomes))  # No primeiro True a execucão finaliza

print(any(n for n in [1, 2, 3, 44, 5, 6, 44] if n % 2 == 1))




