# Funcão para mostrar saída da entrada no console


def saida(n):
    cont = []

    def ensaida():
        nonlocal cont

        cont += n
        return ''.join(cont)
    return ensaida()


if __name__ == '__main__':
    print(saida(input(" : ")))
