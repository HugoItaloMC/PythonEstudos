"""
 - Lendo Arquivos CSV
  O a palavra CSV vem de Comma Separeted Values que em português é - Valores Separados Por Vírgulas

 : A linguagem python possue 2 formas para ler dados em arquivos csv
   - reader -> Permite iterarmos sobre a linha de arquivo CSV com listas;
   - DictReader -> Permite itterarmos sobre as linhas do arquivos CSV como OrderedDicts;
"""

# Sem utilizar o módulo Python para manipular CSV

with open('material_apoio/lutadores.csv') as arq:
    arq = arq.read()
    print(type(arq))
    print(arq)


# Utilizando Módulo Python para trabalhar com CSV
from csv import reader, DictReader

#  - reader

with open('material_apoio/lutadores.csv') as arq:
    arquivo = reader(arq)
    next(arquivo)  # Pulando Cabecalho do Arquivo
    for line in arquivo:
        # Cada linha é uma lista
        print(f"\n...{line[0]} Nasceu em {line[1]} \n\t...Altura {line[2]}")


#  - DictReader
with open('material_apoio/lutadores.csv') as arq:
    arquivo = DictReader(arq)
    for line in arquivo:
        #  Cada linha é um OrderedDict
        #  Lembrando que acessamos valores em dicionários pela chave
        print(f"\n...{line['Nome']} Nasceu em {line['País']} \n\t...Altura {line['Altura (em cm)']}")

#  Aplicando outros separadores/delimitadores
with open('material_apoio/lutadores.csv') as arq:
    arquivo = DictReader(arq, delimiter=',')
    for line in arquivo:
        #  Cada linha é um OrderedDict
        #  Lembrando que acessamos valores em dicionários pela chave
        print(f"\n...{line['Nome']} Nasceu em {line['País']} \n\t...Altura {line['Altura (em cm)']}")
