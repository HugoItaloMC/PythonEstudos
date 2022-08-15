"""
 Faca um programa que receba o nome de um arquivo de entrada e outro de saída. O arquivo de entrada contém cada
linha do nome de uma cidade e o seu número de habitantes (ocupando 40 caracteres). O programa devera ler o arquivo
gerar o arquivo de saída o onde aparece o nome da cidade mais populosa.

"""

import re as rgx


def clear_path_file(arg):
    """
    Recebe arg como argumento obrigatório
    :param arg: É tratado para limpar caminhos (path) de arquivos (files)
    :return: retorna um iterável
    """

    clear = rgx.compile(r'.*svg|.*png|.*gif|.*jpg', flags=rgx.IGNORECASE)
    arg = rgx.sub(clear, '', arg)
    return arg


if __name__ == '__main__':

    import MyFolder.MySources.myFunctions.regexFunction as rgxF

    try:
        # Arquivo de Entrada
        with open(f"dataCitys.txt", "r+") as dataCitys:
            dataCitys = dataCitys.read()
            if not len(dataCitys) == 0:
                #  Implementando padrões, descartando caracteres que ñ são padrões no arquivo
                # Tratamentos específicos levantado no arquivo de saída para alfanúmericos e literais

                # Tratamento com Regex no arquivo
                dataCitysNameList = clear_path_file(dataCitys)

                dataCitysNameList = rgxF.rgx_put_word(dataCitysNameList)
                dataCitysNameList = [line for line in dataCitysNameList.split('\n')]
                dataCityPeopleList = rgxF.rgx_put_dec(dataCitys)
                dataCityPeopleList = ''.join([rgx.sub(r'^[0-9]..\t?| ', '', line)
                                               for line in dataCityPeopleList.split('\n') if not line == ''])
                print(dataCitys, dataCityPeopleList, dataCitysNameList)
                dataCityPeopleList = list(map(int, dataCityPeopleList))
                dataCityObj = {dataCitysNameList[line]: dataCityPeopleList[line]
                               for line in range(0, len(dataCityPeopleList))
                               if len(dataCitysNameList[line]) < 40
                               }
                print(dataCityObj)
                dataCityExit = dataCityObj[max(dataCityObj, key=dataCityObj.get)]
                print(dataCityExit)
                for key, value in dataCityObj.items():
                    if dataCityExit == value:
                        try:
                            with open(f"{input('Digite nome do arquivo de saído : ')}.txt", "w+") as dataCityAfter:
                                if len(dataCityAfter.read()) == 0:
                                    dataCityAfter.write(f" Há Cidade de{key[:11:1]}"
                                                        f"é a cidade com maior numero de hábitantes"
                                                        f"\ncom {dataCityExit} de habitantes")
                                    break
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

" 
  - Arquivos de entrada e saída 
  - Tornalo-os iteráveis:(entrada)
  - Filtrar literais e alfanúmericos:(entrada) para um objeto:(saída)
  - Retornar chave com maior valor do objeto:(saída)
"

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
