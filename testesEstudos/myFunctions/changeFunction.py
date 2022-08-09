"""
  Funcões para alteracões de ocorrências, podendo ser elas:
    String
    integer
    Boolean
    float
    tuple()
    list()
    dict()
    set()
  Entre diversos built'in de Python
"""
# Bloco criacão de funcões


def change_string(itr, put, change):
    """
    :param itr: Parametro de entrada de iterável passado pelo usuário
    :param put: Parametro de busca de ocorrência dentro do iterável
    :param change: Parametro de substituicão de ocorrência feita pelo usuário
    :return: Um iterável local após processamentos da funcão
    """
    after = []
    for line in itr:
        after.append(line.replace(f"{put}", f"{change}"))
    print(after)


def upper_string(iteravel):
    return iteravel.upper()

# bloco de execucão do main para testes das funcões do módulo Python


if __name__ == '__main__':
    iteravel = ["Tweet's", 'Chat', 'Tchau', 'OLA']
    change_string(iteravel, f"{input('Digite Ocorrência : ').lower()}",
                            f"{input('Digite Substituicão da ocorrência : ').lower()}")
