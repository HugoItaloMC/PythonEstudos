"""
 Teste de Velocidade com Expressões Geradoras;

#  - Generator
def nums():
    for num in range(1, 10):
        yield num

g1 = nums()
print(g1)
print(next(g1))
# Generator Expression

g2 = (num for num in range(1, 10))
print(g2)
print(next(g2))
"""


# Realizando Teste de velocidade
import time

# Generator Expression

gen_inicio = time.time()
print(sum(n for n in range(1, 100000000)))
gen_time = time.time() - gen_inicio

list_inicio = time.time()
print(sum([n for n in range(1, 100000000)]))
list_time = time.time() - list_inicio

print(f"Tempo de execucão do generator expression {gen_time}")
print(f"Tempo de execucão da list-comprehensions {list_time}")