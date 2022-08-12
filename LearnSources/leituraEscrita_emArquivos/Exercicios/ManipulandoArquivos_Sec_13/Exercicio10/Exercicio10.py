"""
 Faca um programa que receba o nome de um arquivo de entrada e outro de saída. O arquivo de entrada contém cada
linha do nome de uma cidade e o seu número de habitantes (ocupando 40 caracteres). O programa devera ler o arquivo
gerar o arquivo de saída o onde aparece o nome da cidade mais populosa.



"""


import re as rgx
# import copy as cp

if __name__ == '__main__':
    try:
        with open(f"dataCitys.txt", "r+") as dataCitys:  # Arquivo de Entrada
            dataCitys = dataCitys.read()
            if not len(dataCitys) == 0:

                #  Implementando padrões, descartando caracteres que ñ são padrões no arquivo

                reg_subLit = rgx.compile(r'[0-9\t]+|.*svg|.*png|.*gif|.*jpg',
                    rgx.IGNORECASE)  # Retorna Alfanumericos, extensões de img, '\t' tablatura e ignorar cases
                reg_subAlf = rgx.compile(
                    r'[^0-9 \n]+|^[0-9]\t?')  # Retorna tudo que ñ for alfanúmerico e os caracter vazio '\n' (quebra-linha)

                # Tratamento com Regex no arquivo
                dataCitysNames = rgx.sub(reg_subLit, '', dataCitys)  # Armazenando somente literais padrões
                dataCitysPeople = rgx.sub(reg_subAlf, '', dataCitys)  # Armazenando somente alfanúmericos

                print(dataCitysPeople)
                print(dataCitysNames)
            else:
                print(f"Err ### Arquivo vázio")
    except (TypeError, ValueError, OSError, FileExistsError, FileNotFoundError, SyntaxError) as err:
        print(f"Erro ## {err}")

"""
arq = open("cidadesNomes.txt")
arq = arq.read()
arq2 = open("cidadesPopulacao.txt")
arq2 = arq2.read()

cidadesNomes = [line for line in arq]
cidadesNomes = filter(lambda size: len(size) < 10 and len(size) > 0, cidadesNomes)
cidadesNomes = ''.join(cidadesNomes)
print(cidadesNomes)

cidadesPopulacao = [line for line in arq2.split()]
cidadesPopulacao = list(filter(lambda size: len(size) > 0, cidadesPopulacao))
#  cidadesPopulacao = ' '.join(cidadesPopulacao)


c = {cidadesNomes.split('\n')[d]: cidadesPopulacao[d] for d in range(0, len(cidadesPopulacao))}
print(c)
"""