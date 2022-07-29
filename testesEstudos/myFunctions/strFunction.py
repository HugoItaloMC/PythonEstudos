"""
Funcões para espeficiar caracteres dentro de um arquivo

"""

# Retornando vogais em ocorrências:


def it_vogais(iteravel):
    iteravel = iteravel.lower()  # Lower case nas strings
    result = 0  # Alocando ocorrência
    vogais = 'aeiou'  # condicão da ocorrência
    for i in vogais:  # Indexando condicão de ocorrência
        if i in iteravel:  # Criando caso recursivo
            result += iteravel.count(i)  # recursividade no iterador
    return result  # retornando ocorrências alocadas


#  # Retornando consoantes em ocorrência


def it_consoantes(iteravel):
    iteravel = iteravel.lower()  # Lower case nas strings
    result = 0  # Alocando ocorrência
    vogais = 'bcdfghkjlmnpqrstvwxyz'  # condicão da ocorrência
    for i in vogais:  # Indexando condicão de ocorrência
        if i in iteravel:  # Criando caso recursivo
            result += iteravel.count(i)  # recursividade no iterador
    return result  # retornando ocorrências alocadas


# Retornando vogal especificando caractere e número de ocorrência do mesmo.


def scan_vogais(iteravel):
    iteravel = iteravel.lower()  # Lower case nas strings
    result = {}  # Alocando ocorrência
    vogais = 'aeiou'  # condicão da ocorrência
    for i in vogais:  # Indexando condicão de ocorrência
        if i in iteravel:  # Criando caso recursivo
            result[i] = iteravel.count(i)  # recursividade no iterador
    return result  # retornando ocorrências alocadas


# Retornando consoante especificando caractere e número de ocorrência do mesmo.


def scan_not_vogais(iteravel):
    iteravel = iteravel.lower()  # Lower case nas strings
    result = {}  # Alocando ocorrência
    vogais = 'bcdfghkjlmnpqrstvwxyz'  # condicão da ocorrência
    for i in vogais:  # Indexando condicão de ocorrência
        if i in iteravel:  # Criando caso recursivo
            result[i] = iteravel.count(i)  # recursividade no iterador
    return result  # retornando ocorrências alocadas


# Retornando ocorrência informada pelo usuário


def put_case(iteravel):
    iteravel = iteravel.lower()
    entrada = input('Digite Ocorrência a pesquisar : ').lower()
    result = 0
    for i in entrada:
        if i in iteravel:
            result += iteravel.count(i)
    return result


# Funcão para alterar caractere solicitado:


# Bloco de execucão dentro de main:


if __name__ == '__main__':
    # Textando funcões:
    print(it_vogais('olaaaaqrtiplkj'))
    a = f"{input('Digite Path do Arquivo: ')}"
    print(put_case(f"{a}"))
