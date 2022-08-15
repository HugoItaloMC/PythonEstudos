import re as rgx



def rgx_put_dec(arg):
    """
    Recebe arg como argumento obrigatório
    :param arg: Tratado para retornar somente decimais
    :return: Retorna um iterável
    """
    rg_putWords = rgx.compile(r"[^0-9 \n]?", flags=rgx.IGNORECASE)
    arg = rgx.split(rg_putWords, arg)
    return ''.join(arg)


def rgx_put_char(arg):
    """
    :param arg: Recebe arg como argumento obrigatório, arg é tratado para retornar char's (literais)
    :return: retorna um iterável
    """
    rg_putChar = rgx.compile(r"\d|[\t\n ]", flags=rgx.IGNORECASE)
    arg = rgx.split(rg_putChar, arg)
    return ''.join(arg)


def rgx_put_word(arg):
    """
    :param arg: Recebe um arg como argumento obrigatório, arg é tratado para retornar palavras separadas por espaco
    :return:
    """
    rg_putWords = rgx.compile(r"[^0-9\t\n]", flags=rgx.IGNORECASE)
    arg = rgx.split(rg_putWords, arg)
    return arg

if __name__ == '__main__':
    from typing import List
    arq = open('dataCitys.txt', "r+")
    arq = arq.read()
    #print(rgx_put_word(arq))
    #print(rgx_put_char(arq))
    #print(rgx_put_dec(arq))
    arq_word = rgx_put_word(arq)
    arq_dec = rgx_put_dec(arq)

