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


def change_string(iteravel):
    """
      Mudando strings

    :param iteravel: Recebe um iterável do usuário, usuário passa ocorrência e o substituto da ocorrência
    também é passado pelo usuário.

    """
    iteravel = iteravel.read()
    iteravel = iteravel.upper()
    after = open('arq2.txt', 'w+')
    put = input('Digite ocorrência : ')
    change = input('Digite substituicão da ocorrência : ')
    for line in iteravel:
        after.write(line.replace(f"{put}", f"{change}"))


def upper_string(iteravel):
    iteravel
# bloco de execucão do main para testes das funcões do módulo Python


if __name__ == '__main__':
    upper_string()
