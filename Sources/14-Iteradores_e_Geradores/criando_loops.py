"""
Criando sua própria versão de loop

"""

# Entendendo mais a fundo o for

for n in [1, 2, 3, 4, 5]:
    print(n)

for letras in "Geek University":
    print(letras)

# Internamente o Python aplicou a funcão iter() ao iretável
# E aplica o next() em cada elemento e finaliza antes do StopIteration

iter([1, 2, 3, 4, 5])

iter("Geek University")

# Criando loop :


def meu_for(iteravel):
    it = iter(iteravel)
    while True:
        try:
            print(next(it))
        except StopIteration:  # Tratando StopIteration
            break


meu_for("Geek")
c = (['x' if a % 2 == 0 else 'o' for a in range(1, 101)] for b in range(1, 1001))

iterable = (x * 10 for x in range(1000) )
for event in iterable:
    print(event)

meu_for(c)
meu_for(iterable)
