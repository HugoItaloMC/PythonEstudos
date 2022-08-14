import re as rgx


def rgx_put_dec(arg):
    """
    :param arg: Recebe arg como argumento obrigatório, arg é tratado para retornar somente decimais
    :return: Retorna um iterável
    """
    rg_putWords = rgx.compile(r"[^0-9 ]", flags=rgx.IGNORECASE)
    arg= [rgx.sub(rg_putWords, '', line) for line in arg if not line == '']
    return ''.join(arg)


def rgx_put_char(arg):
    """
    :param arg: Recebe arg como argumento obrigatório, arg é tratado para retornar char's (literais)
    :return: retorna um iterável
    """
    rg_putChar = rgx.compile(r"\d|[\t\n ]", flags=rgx.IGNORECASE)
    arg = [rgx.sub(rg_putChar, '', line) for line in arg if not line == '']
    return ''.join(arg)


def rgx_put_word(arg):
    """
    :param arg: Recebe um arg como argumento obrigatório, arg é tratado para retornar palavras separadas por
    :return:
    """
    rg_putWords = rgx.compile(r"\d|[\t]", flags=rgx.IGNORECASE)
    arg = [rgx.sub(rg_putWords, '', line) for line in arg if not line == '']
    return ''.join(arg)

if __name__ == '__main__':
    arq = open('dataCitys.txt', "r+")
    arq = arq.read()
    print(rgx_put_word(arq))
    print(rgx_put_char(arq))
    print(rgx_put_dec(arq))