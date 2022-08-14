"""
  Faca um programa que que abra um arquivo, calcule e escreva  o número de linhas,  caracteres, palavras,
neste arquivo. Escreva também quantas vezes cada letra ocorre no arquivo (ignorando letras com acento). OBS:
palavras são separadas por um espaco ou mais, tabulacão '\t' nova linha '\n'.:arg.f"{}"

"""

import re as rgx

if __name__ == '__main__':
    try:
        with open(f"Exercicio10/dataCitys.txt", "r+") as dataCity:
            if not len((dataCity.read())) == 0:
                dataCity.seek(0)
                dataCity = dataCity.read()
                # Criando padrões:

                # Armazenando linhas
                rgx_putLine = rgx.compile(r"[^\n]")

                # Armazenando palavras
                rgx_putWord = rgx.compile(r"[^a-z ]", flags=rgx.IGNORECASE)

                # Armazenando caracteres
                rgx_putChar = rgx.compile(r"[^a-z]", flags=rgx.IGNORECASE)

                # Contador de letras : ultilizando counter();
                for chars in dataCity:
                    for words in chars:
                        words = rgx.split(rgx_putWord, dataCity)
                        print(words)


            else:
                print(f"Erro ## O Arquivo está vázio ## ")
    except (TypeError, ValueError, FileExistsError, FileNotFoundError, SyntaxError, AttributeError, OSError) as err:
        print(f"Erro ## {err}")