"""
 Faca um programa que receba o nome de um arquivo de entrada e outro de saída. O arquivo de entrada contém cada
linha do nome de uma cidade e o seu número de habitantes (ocupando 40 caracteres). O programa devera ler o arquivo
gerar o arquivo de saída o onde aparece o nome da cidade mais populosa.

"""
import re
import re as rgx

if __name__ == '__main__':
    try:
        # Arquivo de Entrada
        with open(f"dataCitys.txt", "r+") as dataCitys:
            dataCitys = dataCitys.read()
            if not len(dataCitys) == 0:

                #  Implementando padrões, descartando caracteres que ñ são padrões no arquivo

                # Retorna Alfanumericos, extensões de img, '\t' (tablatura) e ignora cases:
                reg_putLit = rgx.compile(r'[0-9\t]+|.*svg|.*png|.*gif|.*jpg', flags=rgx.IGNORECASE)

                # Retorna tudo que ñ for alfanúmerico e os caracter vazio '\n' (quebra-linha):
                reg_putAlf = rgx.compile(r'[^0-9 \n]?')

                # Tratamento com Regex no arquivo
                dataCitysNames = rgx.sub(reg_putLit, '', dataCitys)  # Armazenando somente literais padrões
                dataCitysPeople = rgx.sub(reg_putAlf, '', dataCitys)  # Armazenando somente alfanúmericos padrões

                # Tratamentos específicos levantado no arquivo de saída para alfanúmericos e literais
                dataCitysNamesList = [line for line in dataCitysNames.split('\n')]

                dataCityPeopleList = [rgx.sub(r'^[0-9]..\t?| ', '', line, (re.ASCII | re.IGNORECASE | re.DOTALL))
                                      for line in dataCitysPeople.split('\n') if not line == ''
                                      ]
                dataCityPeopleList = list(map(int, dataCityPeopleList))
                dataCityObj = {dataCitysNamesList[line]: dataCityPeopleList[line]
                               for line in range(0, len(dataCityPeopleList))
                               if len(dataCitysNamesList[line]) < 40 and len != ''
                               }
                dataCityExit = dataCityObj[max(dataCityObj, key=dataCityObj.get)]
                for key, value in dataCityObj.items():
                    if dataCityExit == value:
                        try:
                            with open(f"{input('Digite nome do arquivo de saído : ')}.txt", "w+") as dataCityAfter:
                                if len(dataCityAfter.read()) == 0:
                                    dataCityAfter.write(f" Há Cidade de{key[:11:1]}"
                                                        f"é a cidade com maior numero de hábitantes"
                                                        f"\ncom {dataCityExit} de habitantes")
                                else:
                                    print(f"Error ## O arquivo não está vázio")
                        except (TypeError, ValueError, OSError, FileExistsError, FileNotFoundError, SyntaxError,
                                IndentationError, AttributeError) as err:
                            print(f"Erro ## {err}")
            else:
                print(f"Err ### Arquivo vázio")
    except (TypeError, ValueError, OSError, FileExistsError, FileNotFoundError, SyntaxError, AttributeError) as err:
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
