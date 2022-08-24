import re as rgx


def rgx_put_dec(arg):
    """
    Recebe um parametro obrigatório
    :param arg: Tratado para retornar somente decimais separados por
    espacos, quebras de linhas e tablaturas
    :return: Retorna um iterável
    """
    put_decimal = rgx.compile(r"[^0-9 \n]?", flags=rgx.IGNORECASE)
    arg = rgx.sub(put_decimal, '', arg)
    return arg


def rgx_put_char(arg):
    """
    Recebe um parametro obrigatório
    :param arg: Tratado para retornar char's literais e alfanuméricos
    sem espacamentos
    :return: retorna um iterável
    """
    put_char = rgx.compile(r"[\t \n]", flags=rgx.IGNORECASE)
    arg = rgx.sub(put_char, '', arg)
    return arg


def rgx_put_word(arg):
    """
    Recebe um parametro de entrada obrigatório
    :param arg: Tratado para retornar palavras separadas por espaco
    :return: retorna um iterável
    """
    put_word = rgx.compile(r"""[0-9\t\n.,)!@#$%^&*(+></?=|~`'"]""", flags=rgx.IGNORECASE)
    arg = rgx.sub(put_word, '', arg)
    return arg


def obj_dict(foo):
    """
     - Recebe um parametro obrigatório.

    :param arg: Tratado com regex para retornar padrões, o texto deve ser
    de padrões de escrita tradicionais, excecões devem ser tratadas com outras
    funcões deste módulo ou não.

    :return: Um objeto, kwarg(key) como chave e karg(value) como valor inteiro
    de {kwarg:karg}
    """
    put_word = [rgx.sub(r"[0-9 º/\t-]*", '', line, flags=rgx.IGNORECASE) for line in foo.split('\n')]
    put_dec = [rgx.sub(r"[^0-9 /\n-]+", '', line) for line in foo.split('\n') if not line == '']
    obj = {put_word[line]: put_dec[line] for line in range(0, len(put_dec))}
    return obj


if __name__ == '__main__':
    arq = open('dataCitys.txt', "r+")
    arq = arq.read()
    print(obj_dict(arq))
