"""
  - Escrevendo em arquivos CSV
  : writer() , cria o objeto para escrita a partir do arquivo aberto
     - writerow() , escreve uma linha no arquivo CSV, este método recebe uma lista;
  : DictWriter, cria um objeto para escrita a partir de um arquivo aberto, o método
  writenow() do módulo DictWriter recebe um dict como entrada e as chaves dos dicio-
  nários devem ser as mesmas declaradas no cabecalho
"""

from csv import writer, DictWriter

# Utilizando writer

with open('material_apoio/filmes.csv', 'w+') as arq:
    arquivo = writer(arq)  # Criando objeto para escrita a partir do arquivo criado
    filme = None
    arquivo.writerow(['Titulo', 'Gênero', 'Duracão'])  # Escrevendo Cabecalho do arquivo
    while filme != 'sair':
        filme = input('Digite Filme : ')
        if filme != 'sair':
            genero = input("Gênero do Filme : ")
            duracao = int(input("Duracão do Filme (em minutos) : "))
            arquivo.writerow([filme, genero, duracao])


# Utilizando DictWriter

with open('material_apoio/filmes_dict.csv', 'w') as arq:
    cabecalho = ['Título', 'Gênero', 'Duracão']
    arquivo = DictWriter(arq, fieldnames=cabecalho)
    arquivo.writeheader()
    filme = None
    while filme != 'sair':
        filme = input('Informe o nome do filme : ')
        if filme != 'sair':
            genero = input('Informe Gênero do Filme : ')
            duracao = input('Informe duracão do filme (em minutos) : ')
            arquivo.writerow({'Título': filme, 'Gênero': genero, 'Duracão': duracao})