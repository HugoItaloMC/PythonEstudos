import pandas as pd

with open("materiais_apoio/cities_w_more_1m_p.csv") as arq:
   #  Paises com cidades contendo mais de 1 milhão de pessoas

   df = pd.read_csv(arq)
   print(df.shape)  # Verificando quantidade de linhas e colunas
   print(df.columns)  # Verificando  Colunas

   # Renomeando Nome de Colunas
   df = df.rename(columns={'country': 'Pais'})
   print(df.columns)  # Verificando  Colunas
   print(df.dtypes)   # Tipo de dados no arquivo
   print(df.tail())   # Retornando últimas linhas do arquivo
   print(df.describe())  #  Retornando Informacões estatísticas de arquivo

   #  Filtrando Pesquisas

   print(df["1989"].unique())
   print(f"{df.loc(df['Pais'] == 'Brazil')}")
