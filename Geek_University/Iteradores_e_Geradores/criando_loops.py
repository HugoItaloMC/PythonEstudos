"""
Criando sua própria versão de loop

"""

# Entendendo mais a fundo o for
import six
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

