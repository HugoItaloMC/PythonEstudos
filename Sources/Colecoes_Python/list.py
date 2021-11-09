"""
  Listas(list) em Python é o mesmo que Vetores/Matrizes(arrays) em outras linguagens com a diferenca de serem *dinamicos*
e também podemos colocar *qualquer* tipo de dados.

 Arrays em C e ou Java:
Possuem tamanho e tipo de dado fixos, ou seja, nestas liguagens um array do tipo int e com tamanho 5, este array
será    SEMPRE  do tipo int SEMPRE  no máximo 5 valores.
  Arrays em Python:
- Dinamico: não possui tamanho fixo, ou seja, podemos criar  a lista e simplesmente ir adicionando elementos.
- Qualquer tipo de dados:  Não possuem tipo de dados fixo, ou seja, podemos colocar qualquer tipo de dados.
 As listas em Python são representadas por colchetes:    '[]'
"""
type([]) # Definicão de uma lista
list1 = [1, 2, 3, 4, 54, 55, 63, 66, 77, 72, 88, 81, 99, 90, 100, 101]
list2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
list3 = []
list4 = list(range(11))
list5 = ['Geek University']

print(f"\nlist1=\t{list1}\n", f"variável list1 é do tipo de dado {type(list1)}\n\n",
      f"\nlist2=\t{list2}", f"variável lis12 é do tipo de dado {type(list)}\n\n",
      f"list3=\t{list3}\n", f"variável list3 é do tipo de dado {type(list3)}\n\n",
      f"list4= range(11)\t{list4}\n", f"a variável list4 é do tipo de dado {type(list4)}\n\n",
      f"list5=\t{list5}\n", f"a variável list5 é do tipo de dado {type(list5)}\n\n")

# Verificando dados de uma lista:
    #   Ultilizando estrutura if:
a = True if 88 in list1 else False
print(f"{a}\n")

# Conhecendo módulos para se ultilizar com tipo de dado list[]
    # .sort() : Ordena uma lista;
        # Exemplos:
list1.sort()
list2.sort()
print(f" {list1}\n", f"{list2}\n")

    # .count() : Conta o número de occorenci   as de um valor;
        # Exemplos:
print(f" {list1.count(55)}\n",f"{list2.count('e')}\n")
    # .append() : Adiciona elementos em uma lista;
        # Módulo aceita uma insercão por vez (sublista), erro TypeError caso passe mais de um elemento
        # ** list1.append(11, 55, True, False) # TypeError **
        # Exemplos:
print(list1)
list1.append([11,22,33])
print(list1)
    # .extend() : Adiciona elementos em uma lista;
        # Módulo adiciona elemento um a um como nova ocorrencia com novo valor
        # Exemplos:
list1.extend([10111,10100,11111,'10111','10100','11111'])
list1.extend(['Geek'])
print(list1)

# ## append() && extend() inserem ocorrencias sempre ao final da list ##
    # Podemos inserir uma nova ocorrencia informando a posicão em qual iremos atribuir o valor
    # .insert(posicão, valor) : Atribui novo valor informando posicão de ocorrencia;
        # Exemplos
list1.insert(2, 'New')
print(list1)
"""
# OBS: No caso da insercão de um valor em uma posicão já preenchida, todas as ocorrencias 
já existentes, a partir da posicão declarada, serão alocadas uma casa a direita, não perdendo nem um dado.
"""
    # Juntando duas list em uma
        # Exemplos:
print(f"\n{list1+list2}")

list6 = list1 + list2
print(f"\n{list6}")

list1.extend(list2)
print(f"\n{list1}")

list2 = list2 + list1
print(f"\n{list2}")

    # Revertendo uma list;
        # Exemplos:
            # Ultilizando .reverse()
list1.reverse()
list2.reverse()
print(f"\n{list1}",
      f"\n{list2}")

        # Ultilizando slice:
print(f"\n{list1[::-1]}",
      f"\n{list2[::-1]}")

      # Copiando uma list
            # Ultilizando .copy():
                  # Exemplo:
list6 = list1.copy()
list6 = list2.copy()
print(f"\n{list6}")

      # Contando elementos de uma lista:
            # Ultilizando len()
print(f"\n {len(list6)} ocorrencias da 'list6'")

      # Removendo elementos de uma list
            # .pop() : este módulo retorna e remove o elemento passado
                  # Exemplo:
print( f"\n{list6}", f"\nelemento: '{list6.pop()}' removido", f"\n{list6}",
       f"\nelemento: '{list6.pop(2)}' removido", f"\n{list6}") # -- Removendo elemento pelo indice

      # Removendo todos elementos de uma lista
            # .clear() : limpa uma list
                  # Exemplo:
print(f"\nlist6 = {list6}")
list6.clear()
print(f"list6 = {list6} após ultilizar o método .clear()")

      # Repetindo elementos de uma lista
            # Exemplo
list6 = [1, 2, 3]
print(f"\nlist6 = [1,2,3] *3 = {list6*3}") # -- O mesmo serve para strings, fazendo concatenacão.
      # Convertendo uma string em uma lit
            # .split() : converte uma string a uma list
            # OBS : por padrão o este método separa as palavras por ' ' espacos vázios, separador pode ser declarado
            # ExemploOBS: .split('/') -- aqui o separador é a barra-invertida.
                  # Exemplo:
testestring = "String de Teste"

print(f"{type(testestring)}\t{testestring}")
testestring = testestring.split()
print(f"\n{type(testestring)}\t{testestring}")

      # Convertendo uma list em uma string
            # ' '.join() : altera uma list em uma string ultilizando ' ' como separador das strings
                  # Exemplo
testestring = ' '.join(testestring)
print(f"\n{type(testestring)}\t{testestring}\n")

"""
_________________________
||:ITERANDO SOBRE list:||
-------------------------
"""

      # Ultilizando estrutura for:
            # Exemplos:
list1 = [1, 2, 3, 4, 54, 55, 63, 66, 77, 72, 88, 81, 99, 90, 100, 101]
list2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
print(f"\nlist1 =\t{list1}\nvariável list1 é do tipo de dado {type(list1)}\n\n",
      f"\nlist2 =\t{list2}\nvariável list2 é do tipo de dado {type(list2)}\n\n")

soma = 0
for elemento in list1:
      print(f"{elemento}")
      soma += elemento
print(f"\n{soma} é a soma dos elementos de list1")

      # Ultilizando estrutura while:
            # Exemplo:
carrinho = []
produto = ''
while produto != 'sair':
     print(f"\n Digite 'sair' para sair")
     produto = input(": ")
     if produto != 'sair':
           carrinho.append(produto)
produto = ''
produto += ', \n'.join(carrinho)
print(f"\nProdutos :\n{produto}")

    # -- Fazemos Acesso aos indices de forma indexada
    #      0         1         2         3
cores = ['azul', 'amarelo', 'verde', 'branco', 'roxo']

print(f"\n {cores[0]}",    # azul
      f"\n {cores[1]}",    # amarelo
      f"\n {cores[2]}",    # verde
      f"\n {cores[3]}",    # branco
      f"\n {cores[4]}")    # roxo
    # Para entender os indices negfativos, pense na list como um circulo onde o final se encontra com o comeco.
        # Exemplo :
print(f"\n\n{cores[0]}",    # azul
      f"\n {cores[-1]}",    # roxo
      f"\n {cores[-2]}",    # branco
      f"\n {cores[-3]}",    # verde
      f"\n {cores[-4]}\n")    # amarelo

       # Gerando um indice com estrutura for
            # Exemplo:
for i, c in enumerate(cores):
      print(f"| indice : [{i}] \t| valor : \t'{c}'  \t|")

      # Gerando um indice:
            # Exemplo:
cores = list(enumerate(cores))
print(f"\n{cores}")

"""
_________________________________________
||:Ultilizando outros métodos com list:||
-----------------------------------------
"""
list1 = [1, 2, 3, 4, 54, 55, 63, 66, 77, 72, 88, 81, 99, 90, 100, 101]
list2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
print(f"\nlist1 =\t{list1}\nvariável list1 é do tipo de dado {type(list1)}\n",
      f"\nlist2 =\t{list2}\nvariável list2 é do tipo de dado {type(list2)}\n\n")

      # Encontrando indice de um elemento da lista
            # Exemplo:
print(f"\nindice : [{list1.index(4)}] onde se encontra o valor list1.index(4)",  # -- em qual indice está o valor '4'
      f"\nindice : [{list2.index('y')}] onde se encontra o valor list2.index('y')", # --  em qual indice está o valor 'y'
      f"\n{list2.index('e', 8)}",         # -- fazendo a busca dentro de um range, qual indice iniciar e qual parar, no exemplo, procure valor 'e' a partir do indice 8
      f"\n{list2.index('e', 1, 14)}")     # -- busque o valor 'e' entra o indice 1 até o 14
# OBS :  Passado valor inexistente no método .index() será gerado 'ValueError' e em valores repetidos e retornado o primeiro indice

      # Revisando slicing:
# list[inicio:fim:passo] : list[1:100:2] -- inicie no indice 1 até o 100 de 2 em 2 passos.
# range(inicio:fim:passo) : range(1, 101, 2) -- inicie um range em 1 até 100 de 2 em 2 passos
            # Exemplos 'inicio' :
print(f"\n{list1[1:]}") # Iniciando no indice 1 e retornando todos restantes

            # Exemplos 'fim' :
print(f"\n{list1[:2]}",     # Comeca em 0 e vai até o indice 2 -1
      f"\n{list1[:10]}",    # Comeca em 0 e vai até o indice 10 -1
      f"\n{list1[:15]}",    # Comeca em 0 e vai até o indice 15 -1
      f"\n{list1[:5]}")     # Comeca em 0 e vai até o indice 5 -1

            # Exemplos 'passo' :
print(f"\n{list1[1::2]}",     # Comeca em 1 vai até o final de 2 passos
      f"\n{list1[::2]}\n")      # Comeca em 0 vai até o final de 2 passos

      # Invertendo valores de uma list
            # Exemplo :
stringteste = ['Teste', 'String']

print(stringteste)
stringteste[0], stringteste[1] = stringteste[1], stringteste[0]
print(stringteste)

stringteste.reverse()
print(stringteste)

      # Soma, Max valor, Min valor
            # sum() : soma valores de uma list
            # max() : retorna valor maximo da list
            # min() : retorna o valor minimo da list
                  # Exemplos :
print(f"\nsum(list1) = {sum(list1)}",
      f"\nmax(list1) = {max(list1)}",
      f"\nmin(list1) = {min(list1)}")