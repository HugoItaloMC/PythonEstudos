"""
Módulo Collections -> Counter

Collections é conhecido como: High-Perfomance Container Datatype

Counter: Recebe um interável como parametro e cria um objeto do tipo Collections Counter que é parecido com um dict,
contendo como chave o elemento da lista e como valor o número de ocorrencias deste elemento.
"""


# Exemplo1:
# Realizando o import
from collections import Counter

# Podemos ultilizar qualquer interável, aqui ultilizamos uma lista
lista = [1,1,2,2,3,3,3,4,4,66,55,77,77,77,88,88,11,11,100,222,444,1001]

# Ultilizando o Counter
res = Counter(lista)
print(f"{res}", '\n' f"{type(res)}")
# Counter({3: 3, 77: 3, 1: 2, 2: 2, 4: 2, 88: 2, 11: 2, 66: 1, 55: 1, 100: 1, 222: 1, 444: 1, 1001: 1})
# <class 'collections.Counter'>

# Exemplo 2 :
# Ultilizando Counter com string
print(Counter('Teste de Estudo Módulo Counter'))
# Counter({'e': 4, ' ': 4, 't': 3, 'd': 3, 'u': 3, 'o': 3, 's': 2, 'T': 1, 'E': 1, 'M': 1, 'ó': 1, 'l': 1, 'C': 1, 'n': 1, 'r': 1})

# Exemplo3:

# Ultilizando Counter com textos grandes

texto= """
A Wikipédia em língua portuguesa começou em junho de 2001, criada pela Fundação Wikimedia. 
Como todo o projeto da fundação, busca um mundo em que cada ser humano tenha livre acesso à soma de todos os conhecimentos. 
Assim, incentiva que todos editem e tenham acesso a esse conteúdo, na medida em que disponibiliza todo seu acervo sob 
licenças livres. 
Para manter-se transparente, todas as alterações ficam gravadas nos históricos de edição. 
Parte do Movimento Wikimedia, a comunidade vem crescendo diariamente. Porém, precisamos de mais colaboradores para podermos 
ampliar o número de artigos em língua portuguesa e expandir, melhorar e consolidar os que já existem.
"""
palavras = texto.split()
print(f"{Counter(palavras)}" '\n' , f"{type(palavras)}")