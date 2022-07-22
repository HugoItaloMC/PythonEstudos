# Criando uma funcão semelhante a um for:
def meu_for(iteravel):
    it = iter(iteravel)  # Aqui tornando o iterável em um iterador;
    while True:
        try:
            print(next(it))
        except StopIteration:  # Tratando StopIteration
            break


if __name__ == '__main__':
    meu_for("Geek")
    c = (['x' if a % 2 == 0 else 'o' for a in range(1, 101)] for b in range(1, 1001))

    iterable = (x * 10 for x in range(1000))
    meu_for(iterable)
    meu_for(c)

